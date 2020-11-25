from ArduinoControl.single_valve import *
import serial, sys, time
import numpy as np
import random

port_u = '/dev/ttyACM2'
port_w = 'com6'
pin11 = DataPin(11)

def creat_dynamic_shape(coor_list, on_time = 0.2, ISO = 0.1):
    jets = []
    start_times = np.arange(1, 100, ISO)
    i = 0
    for point in coor_list:
        jet = dict(pin=pin11, point=point, startTime=start_times[i], stoptime=on_time, on_time=on_time, off_time=100)
        jets.append(jet)
        i+=1
    return  jets
def creat_static_shape(coor_list, on_time = 0.2):
    jets = []
    start_time = 0.1
    for point in coor_list:
        jet = dict(pin=pin11, point=point, startTime=start_time, stoptime=on_time, on_time=on_time, off_time=100)
        jets.append(jet)
    return  jets


def multi_switch(parameters):
    pin, point, start_time, on_time, off_time = parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]
    on_times = []
    off_times = []
    time.sleep(start_time)
    pin.set(point, 1)
    ser.write(pin.shift_str())
    p_start = time.time()
    on_time = time.time()
    print('point',point, 'start at', on_time )
    for n in range(1000):
        time.sleep(on_time)  # on_time

        pin.set(point, 0)
        ser.write(pin.shift_str())
        off_time = time.time()
        on_times.append(off_time - on_time)

        time.sleep(off_time)  # off_time

        pin.set(point, 1)
        ser.write(pin.shift_str())
        on_time = time.time()
        off_times.append(on_time - off_time)

    print('point', point, 'on_time', sum(on_times), 'ms')
    print('point', point, 'off_time', sum(off_times), 'ms')
    print('point', point, (time.time() - p_start), 's')
    return (off_times,on_times)


start_times = np.arange(1, 100, 0.07)
# stop_afters = np.arange(1,100,0.07)
stop_afters = [0.1, 0.1, 0.1, 0.1]
on_times = [0.1, 0.1, 0.1, 0.1]
off_times = [0.07, 0.07, 0.07, 0.07]
moving_line = [dict(pin=pin11, on=0, point=(4, 2), start_time=start_times[0] - 0.07, stop_after=stop_afters[0],
                    on_time=on_times[0], off_time=off_times[0]),
               dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_after=stop_afters[0],
                    on_time=on_times[0], off_time=off_times[0])
    ,
               dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[1], stop_after=stop_afters[1],
                    on_time=on_times[1], off_time=off_times[1])
    ,
               dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[2], stop_after=stop_afters[2],
                    on_time=on_times[2], off_time=off_times[2])
    ,
               dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_after=stop_afters[3],
                    on_time=on_times[3], off_time=off_times[3])
    ,
               dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[0], stop_after=stop_afters[0],
                    on_time=on_times[0], off_time=off_times[0])
    ,
               dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_after=stop_afters[1],
                    on_time=on_times[1], off_time=off_times[1])
    ,
               dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_after=stop_afters[2],
                    on_time=on_times[2], off_time=off_times[2])
    ,
               dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_after=stop_afters[3],
                    on_time=on_times[3], off_time=off_times[3])
    ,
               dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_after=stop_afters[0],
                    on_time=on_times[0], off_time=off_times[0])
    ,
               dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[1], stop_after=stop_afters[1],
                    on_time=on_times[1], off_time=off_times[1])
    ,
               dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_after=stop_afters[2],
                    on_time=on_times[2], off_time=off_times[2])
    ,
               dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[3], stop_after=stop_afters[3],
                    on_time=on_times[3], off_time=off_times[3])
    ,
               dict(pin=pin11, on=0, started=0, point=(7, 2), start_time=start_times[0], stop_after=stop_afters[0],
                    on_time=on_times[0],
                    off_time=off_times[0])
    ,
               dict(pin=pin11, on=0, started=0, point=(7, 3), start_time=start_times[1], stop_after=stop_afters[1],
                    on_time=on_times[1], off_time=off_times[1])
    ,
               dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[2], stop_after=stop_afters[2],
                    on_time=on_times[2], off_time=off_times[2])
    ,
               dict(pin=pin11, on=0, started=0, point=(7, 5), start_time=start_times[3], stop_after=stop_afters[3],
                    on_time=on_times[3], off_time=off_times[3])
               ]

start_times = np.arange(1, 100, 0.1)
on_times = [100, 100, 100, 100]
off_times = [0.04, 0.03, 0.008, 0.003]
growing_square = [
    dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_after=10000,
         on_time=on_times[0], off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_after=1000,
         on_time=on_times[1], off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[0], stop_after=1000,
         on_time=on_times[2], off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[0], stop_after=100,
         on_time=on_times[3], off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[1], stop_after=1000,
         on_time=on_times[0], off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_after=1000,
         on_time=on_times[1], off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[1], stop_after=1000,
         on_time=on_times[2], off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[1], stop_after=1000,
         on_time=on_times[3], off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[2], stop_after=1000,
         on_time=on_times[0], off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[2], stop_after=1000,
         on_time=on_times[1], off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_after=1000,
         on_time=on_times[2], off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_after=1000,
         on_time=on_times[3], off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 2), start_time=start_times[3], stop_after=1000,
         on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 3), start_time=start_times[3], stop_after=1000,
         on_time=on_times[1], off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[3], stop_after=1000,
         on_time=on_times[2], off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 5), start_time=start_times[3], stop_after=1000,
         on_time=on_times[3], off_time=off_times[3]),
    dict(pin=pin11, on=0, started=0, point=(8, 2), start_time=start_times[4], stop_after=1000,
         on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 3), start_time=start_times[4], stop_after=1000,
         on_time=on_times[1], off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 4), start_time=start_times[4], stop_after=1000,
         on_time=on_times[2], off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[4], stop_after=1000,
         on_time=on_times[3], off_time=off_times[3])
]

ISOI = 0.07
start_times = np.arange(1, 100, 0.1)
on_times = [0.1, 0.1, 0.1, 1000]
off_times = [0.08, 0.05, 0.01, 0.005]
shading_square = [
    dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_after=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_after=10000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[2], stop_after=10000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_after=10000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_after=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_after=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_after=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[1], stop_after=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_after=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[3], stop_after=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 3), start_time=start_times[1], stop_after=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[2], stop_after=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 5), start_time=start_times[3], stop_after=1000, on_time=on_times[3],
         off_time=off_times[3])
]

start_times = np.arange(1, 100, 0.07)

start_times = np.arange(1, 100, 0.07)
on_times = [0.004, 0.004, 0.004, 0.004]
off_times = [0.004, 0.004, 0.004, 0.004]
two_square = [
    dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_after=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_after=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[1], stop_after=100, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[3], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[2], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[0], stop_after=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 3), start_time=start_times[0], stop_after=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 4), start_time=start_times[0], stop_after=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(9, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(9, 3), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(9, 4), start_time=start_times[0], stop_after=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(10, 2), start_time=start_times[0], stop_after=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(10, 3), start_time=start_times[0], stop_after=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(10, 4), start_time=start_times[0], stop_after=1000, on_time=on_times[3],
         off_time=off_times[3])
]
phantom = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=0, stop_after=0.01, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, point=(4, 4), start_time=0, stop_after=0.01, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, point=(4, 7), start_time=0, stop_after=0.01, on_time=0.003,
         off_time=0.003)
    ,
]

# moving_point = [
#     dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[8], stop_after=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[7], stop_after=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[6], stop_after=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[5], stop_after=0.1, on_time=0.003, off_time=0.003),
#     dict(pin=pin11, on=0, started=0, point=(4, 6), start_time=start_times[4], stop_after=0.1, on_time=0.003,
#          off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_after=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_after=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(7, 5), start_time=start_times[1], stop_after=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[0], stop_after=0.1, on_time=0.003, off_time=0.003),  dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[0]-0.07, stop_after=0.1, on_time=0.003, off_time=0.003)]
#
moving_point = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[6], stop_after=0.1, on_time=0.1, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[5], stop_after=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_after=0.1, on_time=0.1,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_after=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_after=0.1, on_time=0.1,
         off_time=0.003)

]
moving_point_dulconer = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[7], stop_after=0.1, on_time=0.1, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[6], stop_after=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[5], stop_after=0.1, on_time=0.1,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_after=0.1, on_time=0.1,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_after=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_after=0.1, on_time=0.1,
         off_time=0.003)

]

moving_point_square = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[0], stop_after=0.1, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[1], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[2], stop_after=0.1, on_time=0.003,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[4], stop_after=0.1, on_time=0.003,
         off_time=0.003),
    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[5], stop_after=0.1, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[6], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[7], stop_after=0.1, on_time=0.003,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[8], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    ,
    # dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_after=0.1, on_time=0.003,
    #      off_time=0.003)
]
i = 0
moving_point_square_dulcorner = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[0], stop_after=0.1, on_time=0.1, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[1], stop_after=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[2], stop_after=0.1, on_time=0.003,
         off_time=0.003),
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_after=0.1, on_time=0.003,
         off_time=0.003),  # corner

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[4], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, point=(6, 5), start_time=start_times[5], stop_after=0.1, on_time=0.003,
         off_time=0.003),
    dict(pin=pin11, on=0, point=(6, 5), start_time=start_times[6], stop_after=0.1, on_time=0.003,
         off_time=0.003),  # corner

    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[7], stop_after=0.1, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[8], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    , dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[9], stop_after=0.1, on_time=0.003,
           off_time=0.003)  # corner
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[10], stop_after=0.1, on_time=0.003,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[11], stop_after=0.1, on_time=0.003,
         off_time=0.003)
    ,
    # dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_after=0.1, on_time=0.003,
    #      off_time=0.003)
]

# for jet in moving_point_square_dulcorner:
#     jet['point'] =(jet['point'][0]+5, jet['point'][1])

moving_point_two_square = moving_point_square_dulcorner + moving_point_square

off_time = 0.07
on_time = 0.1
triangle_seq = [
    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[7], stop_after=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, point=(5, 5), start_time=start_times[6], stop_after=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 6), start_time=start_times[5], stop_after=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_after=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[3], stop_after=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[3], stop_after=0.1, on_time=on_time,
         off_time=off_time),
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_after=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[1], stop_after=0.1, on_time=on_time,
         off_time=off_time)

]
triangle = [
    dict(pin=pin11, on=0, point=(7, 4), start_time=start_times[0], stop_after=0.1, on_time=0.1,
         off_time=off_time),
    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[1], stop_after=0.1, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, point=(5, 4), start_time=start_times[2], stop_after=0.1, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[3], stop_after=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_after=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 6), start_time=start_times[5], stop_after=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 7), start_time=start_times[6], stop_after=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[7], stop_after=100, on_time=0.1,
         off_time=off_time)
    , dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[8], stop_after=100, on_time=0.1,
           off_time=off_time)
    , dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[9], stop_after=100, on_time=0.1,
           off_time=off_time)

]

off_time = 0.004
on_time = 1
circle = [
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[0], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 6), start_time=start_times[1], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 7), start_time=start_times[2], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 7), start_time=start_times[3], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 6), start_time=start_times[4], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[5], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[6], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[7], stop_after=1000,
         on_time=on_time,
         off_time=off_time),
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[7], stop_after=1000,
         on_time=on_time,
         off_time=off_time)
]

start_times = np.arange(1, 100, 0.1)
i = 0
for jet in shading_square:
    i += 1
    jet['cycle'] = jet['on_time'] + jet['off_time']
    # jet['start_time'] = start_times[i]
    # jet['on_time'] = 0.2
    # jet['off_time'] = 0.2
    # jet['stop_after'] = 0.1

############# experiment 1 dynamic shape ########################
square2x2 = [(4, 3), (4, 4), (5, 4), (5, 3), (4, 3)]
diamond3x3 = [(4, 3), (5, 4), (6, 3), (5, 2), (4, 3)]
square3x3 = [(4, 4), (5, 4), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4)]
square4x4 = [(4, 5), (5, 5), (6, 5), (7, 5), (7, 4), (7, 3), (7, 2), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5)]
triangle4x4 = [(4, 4), (5, 3), (6, 2), (7, 1), (6, 1), (5, 1), (4, 1), (4, 2), (4, 3), (4, 4)]
hexagon4x4 = [[5, 4], (6, 4), (7, 3), (7, 2), (6, 1), (5, 1), (4, 2), (4, 3), (5, 4)]

# square2x2_corner = [(4,3),(4,3),(4,4),(4,4),(5,4),(5,4),(5,3),(5,3),(4,3),(4,3)]
# diamond3x3_corner = [(4,3),(4,3),(5,4),(5,4),(6,3),(6,3),(5,2),(5,2),(4,3),(4,3)]
square3x3_corner = [(4, 4), (4, 4), (5, 4), (6, 4), (6, 4), (6, 3), (6, 2), (6, 2), (5, 2), (4, 2), (4, 2), (4, 3),
                    (4, 4), (4, 4)]
square4x4_corner = [(4, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 5), (7, 4), (7, 3), (7, 2), (7, 2), (6, 2), (5, 2),
                    (4, 2), (4, 2), (4, 3), (4, 4), (4, 5), (4, 5)]
triangle4x4_corner = [(4, 4), (4, 4), (5, 3), (6, 2), (7, 1), (7, 1), (6, 1), (5, 1), (4, 1), (4, 1), (4, 2), (4, 3),
                      (4, 4), (4, 4)]


class Controller(object):
    def __init__(self, ser, jets_list=None):
        self.ser =ser
        if not jets_list:
            self.jets = shading_square

            # self.jets = [
            #             dict(pin=pin11, on = 0,started = 0, point=(4, 6), start_time=0.10, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             , dict(pin=pin11, on = 0,started = 0, point=(4, 7), start_time=0.20, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             , dict(pin=pin11, on = 0,started = 0, point=(4, 8), start_time=0.30, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             , dict(pin=pin11, on = 0,started = 0, point=(4,9), start_time=0.40, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             ,dict(pin=pin11, on = 0,started = 0, point=(5, 6), start_time=0.20, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             , dict(pin=pin11, on = 0,started = 0, point=(5, 7), start_time=0.30, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             , dict(pin=pin11, on = 0,started = 0, point=(5, 8), start_time=0.40, stoptime=0.21, on_time=0.2, off_time=0.002)
            #             , dict(pin=pin11, on = 0,started = 0, point=(5,9), start_time=0.50, stoptime=0.21, on_time=0.2, off_time=0.002) ]
        else: self.jets = jets_list

    def switch(self, time_):
        for jet in self.jets:
            t = time_ - jet['start_time']
            if t >= 0:
                res_time = t % (jet['cycle'])
                if  (not jet['on']) & (res_time <= jet['on_time'])& (t<= jet['stop_after']):
                    jet['pin'].set(jet['point'], 1)
                    jet['on'] = 1

                if jet['on']&(jet['on_time']<= res_time )  :
                    jet['pin'].set(jet['point'], 0)
                    jet['on'] = 0
    def loop(self,times):
        start = time.time()
        t = start
        for n in range(times):
            if (time.time() - start - t) * 1000 > 2:
                print((time.time() - start - t)*1000)
            t = time.time() - start
            self.switch(t)

            # print(t*1000)
            self.ser.write(pin11.shift_str())

def compile_frequency(ser, point,times):
    serial_strs = [(cobs.encode(bytes([11]) + b'\x00') + b'\x00',0)]
    last = cobs.encode(bytes([11]) + b'\x00') + b'\x00'
    point_contro = Controller(ser, point)
    for n in range(times):
        point_contro.switch(n/1000)
        # print(serial_strs[0][0], pin11.shift_str())
        # print(n)
        if not (last == pin11.shift_str()):
            last =  pin11.shift_str()
            serial_strs.insert(0,(pin11.shift_str(),n))

    serial_strs.insert(0, (cobs.encode(bytes([11]) + b'\x00') + b'\x00', float('inf')))
    return serial_strs

def run_frequency_pilot(ser,file, combinations):  #worse than last one
    for (on_time, off_time) in combinations:
        point = [
            dict(pin=pin11, on=0, point=(4, 7), start_time=0.10, stop_after=1000, on_time=on_time, off_time=off_time,
                 cycle=on_time + off_time)]
        serial_strs = compile_frequency(ser,point,5000)
        (serial_str,t) = serial_strs.pop()
        print('off time:', off_time, 'on time : ', on_time)
        for n in range(5000):
            time.sleep(0.00085)
            if t<=n:
                ser.write(serial_str)
                (serial_str, t) = serial_strs.pop()
                    # print(t,n)

        point[0]['pin'].set(point[0]['point'], 0)
        ser.write(pin11.shift_str())
        k = input()
        if k == 'p':
            print('feel pulsing  off time:', off_time, 'on time : ', on_time)
            with open(file, "a") as myfile:
                myfile.write('off time : ' + str(off_time) + '; on time :' + str(on_time) + ' p' + '\n')

        if k == 'v':
            print('feel vibration   off time:', off_time, 'on time : ', on_time)
            with open(file, "a") as myfile:
                myfile.write('off time : ' + str(off_time) + '; on time :' + str(on_time) + ' v' + '\n')
            # break
        if k == 'c':
            print('feel continues  off time:', off_time, 'on time : ', on_time)
            with open(file, "a") as myfile:
                myfile.write('off time : ' + str(off_time) + '; on time :' + str(on_time) + ' c' + '\n')
        if k == 'n':
            print('feel continues  off time:', off_time, 'on time : ', on_time)
            with open(file, "a") as myfile:
                myfile.write('off time : ' + str(off_time) + '; on time :' + str(on_time) + ' n' + '\n')
