from ArduinoControl.single_valve import *
import  multiprocessing

if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs
    """Demonstrate communicating with an attached Arduino for shifting
    one level at a time."""

    point1 = (3,6)
    point2 = (9,6)

    l0 = Level(11)
    # ser = serial.Serial(sys.argv[1], baudrate=115200)
    ser = serial.Serial('com6', baudrate=115200)

    print(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')

    val = True
    l0.set(point2, val)
    start = time.time()
    n = 0
    lis = [(point2,0),(point2,1)]*10000

    def switch(point,val):
        l0.set(point, val)
        time.sleep(0.001)
        ser.write(l0.shift_str())
    map(switch,lis)
    print(0.1 * (time.time() - start))
    start = time.time()
    off_time = time.time()
    interval = 0
    duration = 0
    for n in range(1000):
        on_time = time.time()
        l0.set(point1, 0)
        # l0.set(point2, 1)
        ser.write(l0.shift_str())
        # time.sleep(0.000001/1000)
        # time.sleep(0.000000001)
        val = not val
        # print(" ")
        time.sleep(0.00001)
        interval +=  (on_time - off_time)
        off_time = time.time()
        l0.set(point1, 1)
        # l0.set(point2, 0)
        ser.write(l0.shift_str())
        duration+=  (off_time - on_time)
        # time.sleep(0.05)


    print('duration',duration )
    print('interval',interval)
    print(0.1*(time.time() -  start))