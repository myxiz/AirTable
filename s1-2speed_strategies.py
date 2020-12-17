from ArduinoControl.shape_generator import *
from ArduinoControl.jets_controller import *
from ArduinoControl.single_valve import *


def get_balanced_order(no_p):
    # l_m = [[0, 1, 2],
    #        [0, 2, 1],
    #        [2, 0, 1],
    #        [2, 1, 0],
    #        [1, 2, 0],
    #        [1, 0, 2]]

    l_m = [[0, 1, 3, 2],
           [1, 2, 0, 3],
           [2, 3, 1, 0],
           [3, 0, 2, 1]
           ]
    n = no_p % 4
    return l_m[n]


def get_jets_lists(speed):
    interval, duration = speed[0], speed[1]
    jets_n = dict(
        triangle_n=creat_dynamic_shape(triangle4x4, interval=interval, duration=duration),
        square_n=creat_dynamic_shape(square3x3, interval=interval, duration=duration),
        circle_n=creat_dynamic_shape(hexagon4x4, interval=interval, duration=duration),
    )

    jets_o = dict(
        triangle_o=creat_dynamic_shape(triangle4x4_over, interval=round(interval * 0.8 / 1.2, 2),
                                       duration=round(duration * 0.8 / 1.2, 2)),
        square_o=creat_dynamic_shape(square3x3_over, interval=round(interval * 0.8 / 1.3, 2),
                                     duration=round(duration * 0.8 / 1.3, 2)),
        circle_o=creat_dynamic_shape(hexagon4x4, interval=round(interval, 2), duration=round(duration, 2))
    )

    jets_p = dict(
        triangle_p=creat_dynamic_shape(triangle4x4_pause, interval=round(interval * 0.8 / 1.3, 2),
                                       duration=round(duration * 0.8 / 1.3, 2)),
        square_p=creat_dynamic_shape(square3x3_pause, interval=round(interval * 0.8 / 1.5, 2),
                                     duration=round(duration * 0.8 / 1.5, 2)),
        circle_p=creat_dynamic_shape(hexagon4x4, interval=round(interval, 2),
                                     duration=round(duration / 1.1, 2))
    )
    return [jets_n, jets_o, jets_p]


def run_practice(ser, jets, speed):
    interval, duration = speed[0], speed[1]
    shapes = list(jets.keys())
    random.shuffle(shapes)
    for shape in shapes:
        run_exp_rendering_practice(ser, shape, jets[shape], rnd=4, inter_cycle=0.5)
        ser.write(empty_str)


def run_exp2_speed_strategies(ser, file, no_p):
    speeds = ((0.07, 0.1), (0.12, 0.15), (0.17, 0.2))
    # speeds = ((0.07, 0.1), (0.12, 0.15), (0.17, 0.2))
    order_1 = get_balanced_order(no_p + 1)
    for n in order_1:
        speed = speeds[0]
        print(speed)
        jet_list = get_jets_lists(speed)
        order = get_balanced_order(no_p)
        for i in order:
            jets = jet_list[i]
            run_practice(ser, jets, speed)
            k = input('practice finished, do you want to start? y/n')
            practice_number = 1
            while (k != 'n') & (k != 'y'):
                k = input('practice finished, do you want to start? y/n')
            while k == 'n':
                practice_number += 1
                run_practice(ser, jets, speed)
                k = input('practice finished, do you want to start? y/n')
            shapes = list(jets.keys())
            shapes += (list(shapes) + list(shapes))
            random.shuffle(shapes)
            with open(file, "a") as myfile:
                myfile.write(str(shapes) + '\n')
            for shape in shapes:
                run_exp_rendering(ser, shape, jets[shape], rnd=4, inter_cycle=0.5)
                ser.write(empty_str)
            print('Break')


if __name__ == '__main__':
    import serial, random

    ser = serial.Serial(port_u, baudrate=250000)
    no_p = 0
    file = f'result/result_rendering_{str(no_p)}.txt'
    with open(file, "a") as myfile:
        myfile.write(f'{str(no_p)} ' + str(time.time()) + '\n')
    run_exp2_speed_strategies(ser, file, no_p)
