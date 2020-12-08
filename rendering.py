from ArduinoControl.shape_generator import *
from ArduinoControl.jets_controller import *
from ArduinoControl.single_valve import *

if __name__ == '__main__':
    import serial, random

    ser = serial.Serial(port_u, baudrate=250000)
    file = 'result/result_rendering.txt'

    participant = 'p1'
    interval, duration = (0.4, 0.5)
    jets_dict = dict(
        triangle_l=creat_dynamic_shape(triangle4x4_longer, interval=interval / 1.2, duration=duration / 1.2),
        triangle_o=creat_dynamic_shape(triangle4x4_over, interval=interval / 1.2, duration=duration / 1.2),
        triangle_p=creat_dynamic_shape(triangle4x4_pause, interval=interval / 1.3, duration=duration / 1.3),
        square_l=creat_dynamic_shape(square4x4_longer, interval=interval / 1.7, duration=duration / 1.7),
        square_o=creat_dynamic_shape(square4x4_over, interval=interval / 1.7, duration=duration / 1.7),
        square_p=creat_dynamic_shape(square4x4_pause, interval=interval / 1.9, duration=duration / 1.9),
        circle_1=creat_dynamic_shape(hexagon4x4_longer, interval=interval / 1.1, duration=duration / 1.1),
        circle_2=creat_dynamic_shape(hexagon4x4_longer, interval=interval / 1.1, duration=duration / 1.1),
        circle_3=creat_dynamic_shape(hexagon4x4_longer, interval=interval / 1.1, duration=duration / 1.1))
    shapes = list(jets_dict.keys())
    shapes+=(list(shapes)+list(shapes))


    random.shuffle(shapes)
    print(shapes)
    with open(file, "a") as myfile:
        myfile.write(f'{participant} ' + str(time.time())[-6:])
        myfile.write(str(shapes))
    for shape in shapes:
        run_exp_rendering_practice(ser, file, shape, jets_dict[shape], (interval, duration), rnd=5, inter_cycle=0.0001)
        ser.write(empty_str)
