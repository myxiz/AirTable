from cobs import cobs
class Coord(object):
    """A simple coordinate object representing x/y coordinates. Supports
    comparison with other Coords, tuples, and lists; hashing; and
    addition with other Coord objects, tuples, lists, and numbers."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord({}, {})".format(self.x, self.y)


    def __hash__(self):
        return hash((self.x, self.y))


    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)
        elif isinstance(other, (tuple, list)):
            return Coord(self.x + other[0], self.y + other[1])
        else:
            return Coord(self.x + other, self.y + other)


    def __radd__(self, other):
        return self + other


    def __eq__(self, other):
        if isinstance(other, (tuple, list)):
            return self.x == other[0] and self.y == other[1]
        return self.x == other.x and self.y == other.y



class Board(object):
    """Represents a single shift register board with a mapping of
    coordinates to pins. Provide a mapping (see the default_mapping
    variable in the code) or an offset that will be added to each
    coordinate in the mapping. The offset can be a number, a tuple/list,
    or a Coord object."""
    def __init__(self, offset=None, mapping=None, **kwargs):
        """Mapping should map 8 coordinates to the pins 0-7 (A-H) on the
        shift register via a dict. E.g.: {(0,0): 0, (0,1): 1, ...}"""
        self.bits = 0


        # default_mapping = {
        # 	(0, 0): 0, (1, 0): 4,
        # 	(0, 1): 1, (1, 1): 5,
        # 	(0, 2): 2, (1, 2): 6,
        # 	(0, 3): 3, (1, 3): 7,
        # }
        default_mapping = {
            (0, 0): 7, (1, 0): 3,
            (0, 1): 6, (1, 1): 2,
            (0, 2): 5, (1, 2): 1,
            (0, 3): 4, (1, 3): 0,
        }
        if mapping is None:
            mapping = default_mapping

        self.mapping = {Coord(*k): v for k ,v in mapping.items()}

        if offset is not None:
            self.offset_mapping(offset)
        # print(self.mapping)


    def set(self, coord, value):
        try:
            pin = self.mapping[coord]
        except KeyError:
            return False
        if value:
            self.bits |= 1 << pin % 8
        else:
            self.bits &= ~(1 << pin % 8)
        return True


    def offset_mapping(self, other):
        """Offset the mapping by a given amount."""
        self.mapping = {(k + other): v for k ,v in self.mapping.items()}


class Level(object):
    """Represents one level of the display with a bunch of shift
    register boards."""

    # For the one board that spans two lines
    # rotated_mapping = {
    # 	(0, 13): 5, (0, 12): 1,
    # 	(1, 13): 6, (1, 12): 2,
    # 	(2, 13): 7, (2, 12): 3,
    # 	(3, 13): 8, (3, 12): 4,
    # }

    # flipped_mapping = {
    # 	(0, 0): 7, (1, 0): 3,
    # 	(0, 1): 6, (1, 1): 2,
    # 	(0, 2): 5, (1, 2): 1,
    # 	(0, 3): 4, (1, 3): 0,
    # }
    flipped_mapping = {
        (0, 0): 0, (1, 0): 4,
        (0, 1): 1, (1, 1): 5,
        (0, 2): 2, (1, 2): 6,
        (0, 3): 3, (1, 3): 7,
    }
    board19_mapping = {
        (0, 0): 7, (1, 0): 3,
        (0, 1): 6, (1, 1): 1,
        (0, 2): 5, (1, 2): 2,
        (0, 3): 4, (1, 3): 0,
    }

    def __init__(self, data_pin):
        """Set up a Level. Set data_pin to the data line that this level
        is attached to (all shift register boards can share the same
        latch/rck and clock/sck lines.)"""
        # Set up a single level with offsets. The Boards are arranged in
        # the same order as they are connected in.
        self.data_pin = data_pin
        self.layout = [
            # Board(mapping=Level.rotated_mapping),
            Board((12 ,8)),
            Board((12 ,4)),
            Board((12 ,0),mapping=Level.board19_mapping),
            Board((10 ,0) ,mapping=Level.flipped_mapping),
            Board((10 ,4) ,mapping=Level.flipped_mapping),
            Board((10 ,8) ,mapping=Level.flipped_mapping),
            Board((8 ,8)),
            Board((8 ,4)),
            Board((8 ,0)),
            Board((6 ,0) ,mapping = Level.flipped_mapping),
            Board((6 ,4) ,mapping = Level.flipped_mapping),
            Board((6 ,8) ,mapping=Level.flipped_mapping),
            Board((4 ,8)),
            Board((4 ,4)),
            Board((4 ,0)),
            Board((2 ,0) ,mapping = Level.flipped_mapping),
            Board((2 ,4) ,mapping = Level.flipped_mapping),
            Board((2 ,8) ,mapping = Level.flipped_mapping),
            Board((0 ,8)),
            Board((0 ,4)),
            Board((0 ,0))

            # Board((4,4)),
            # Board((4,8)),
            # # Board((4,12),mapping=Level.rotated_mapping),
            # Board((6,8),mapping = Level.flipped_mapping),
            # Board((6,4),mapping = Level.flipped_mapping),
            # Board((6,0),mapping = Level.flipped_mapping),
            # Board((8,0)),
            # # Board((8,4)),
            # Board((8,8)),
        ]

        self.coord_to_board = {}
        for board in self.layout:
            for coord in board.mapping:
                self.coord_to_board[coord] = board


    def set(self, coord, value):
        """Set a single coordinate to a value (1/0 or True/False)."""
        self.coord_to_board[coord].set(coord, value)


    def get_shift_string(self):
        """Return a binary string that represents the entire Level that
        can be shifted into the first board."""
        # print(b''.join([bytes([board.bits]) for board in self.layout]))
        return b''.join([bytes([board.bits]) for board in self.layout])


    def shift_str(self):
        """Return the string to shift out this level on its data pin."""
        return cobs.encode(
            bytes([self.data_pin]) + self.get_shift_string()) + b'\x00'


if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs
    """Demonstrate communicating with an attached Arduino for shifting
    one level at a time."""

    l0 = Level(11)
    # l1 = Level(10)
    ser = serial.Serial(sys.argv[1], baudrate=115200)
    # ser = serial.Serial('comp6', baudrate=115200)

    print(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')

    val = True
    while True:

        # x,y= map(int,input('x,y = ').split(','))  #wait for the Enter key

        # val = bool(input('val = '))
        # l0.set((x,y), val)
        # ser.write(l0.shift_str())

        # for x in range(0 ,10):
        # 	for val in [1,0]:
        # 		for y in range(0,12):
        # 			print('({}, {})'.format(x, y))
        # 			input()  #wait for the Enter key
        # 			l0.set((x,y), val)
        # 			l0.set((x+1,y), val)
        # 			l0.set((x+2,y), val)
        # 			print("shift_str",l0.shift_str())
        # 			ser.write(l0.shift_str())
        # val = not val


        for x in range(10 ,15):
            for val in [1, 0]:
                for y in range(11, 0, -1):
                    print('({}, {})'.format(x, y))
                    input()  # wait for the Enter key
                    l0.set((x, y), val)
                    # l0.set((x+1,y), val)
                    # l0.set((x+2,y), val)
                    # if y < 10:
                    # 	l0.set((x,y+2), not val)
                    # 	l0.set((x+1,y+2),not val)
                    # 	l0.set((x+2,y+2),not val)
                    print("shift_str", l0.shift_str())
                    ser.write(l0.shift_str())