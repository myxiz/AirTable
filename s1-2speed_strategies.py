from ArduinoControl.shape_generator import *
from ArduinoControl.jets_controller import *
from ArduinoControl.single_valve import *


def get_balanced_order3(no_p):
    l_m = [[0, 1, 2],
           [0, 2, 1],
           [2, 0, 1],
           [2, 1, 0],
           [1, 2, 0],
           [1, 0, 2]]
    n = no_p % 6
    return l_m[n]


def get_balanced_order(no_p):
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

    jets_s = dict(
        triangle_s=creat_static_shape(triangle4x4, on_time=8 * interval * 4 + 1.5),
        square_s=creat_static_shape(square3x3, on_time=8 * interval * 4 + 1.5),
        circle_s=creat_static_shape(hexagon4x4, on_time=8 * interval * 4 + 1.5)
    )
    return [jets_n, jets_o, jets_p, jets_s]


def run_static_practice(ser, jets):
    shapes = list(jets.keys())
    random.shuffle(shapes)
    for shape in shapes:
        print('the shape is ', shape + '.')
        induce_static_shape(ser, jets[shape])
        ser.write(empty_str)
        s = input('guess next shape')


def run_practice(ser, jets, speed):
    interval, duration = speed[0], speed[1]
    shapes = list(jets.keys())
    random.shuffle(shapes)
    for shape in shapes:
        run_exp_rendering_practice(ser, shape, jets[shape], rnd=4, inter_cycle=0.5)
        ser.write(empty_str)


def run_exp2_speed_strategies(ser, file, no_p): # shape identification experiment
    speeds = ((0.07, 0.1), (0.12, 0.15), (0.17, 0.2)) # speed combination : (ISOI, duration)
    order_1 = get_balanced_order3(no_p)
    for n in order_1:
        speed = speeds[n]
        print(speed)
        jet_list = get_jets_lists(speed)
        order = get_balanced_order(no_p) # get speed and order from balanced latin square
        for i in order:
            jets = jet_list[i]
            if i == 3:
                run_static_practice(ser, jets)
            else:
                run_practice(ser, jets, speed)
            k = input('practice finished, do you want to start? y/n')
            while (k != 'n') & (k != 'y'):
                k = input('practice finished, do you want to start? y/n')
            while k == 'n':
                if i == 3:
                    run_static_practice(ser, jets)
                else:
                    run_practice(ser, jets, speed)
                k = input('practice finished, do you want to start? y/n')
            shapes = list(jets.keys())
            shapes += (list(shapes) + list(shapes))
            random.shuffle(shapes)
            with open(file, "a") as myfile:
                myfile.write(str(shapes) + '\n')
            for shape in shapes:
                if i == 3:
                    run_exp_static(ser, shape, jets[shape])
                else:
                    run_exp_rendering(ser, shape, jets[shape], rnd=4, inter_cycle=0.5)
                ser.write(empty_str) # send the str to Arduino
            input('Break')


if __name__ == '__main__':
    import serial, random

    ser = serial.Serial(port_u, baudrate=250000)
    no_p = 4
    file = f'result/result_rendering_{str(no_p)}.txt'
    with open(file, "a") as myfile:
        myfile.write(f'{str(no_p)} ' + str(time.time()) + '\n')
    run_exp2_speed_strategies(ser, file, no_p)
