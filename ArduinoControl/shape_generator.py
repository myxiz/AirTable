import numpy as np
from ArduinoControl.single_valve import pin11


def creat_dynamic_shape(coor_list, duration=0.15, interval=0.1, pause = 0.3):
    jets = []
    start_times = np.arange(0, 20, round(interval, 2
                                         ))
    i = 0
    for point in coor_list:
        if point == (0,0):
            stop_time = start_times[i-1] + pause
            jet = dict(pin=pin11, point=point, start_time=start_times[i], stop_time=stop_time, on=0)
            start_times = np.arange(stop_time, stop_time+10, round(interval, 2
                                                 ))
            i = 0
        jet = dict(pin=pin11, point=point, start_time=start_times[i], stop_time=duration, on=0)
        jets.append(jet)
        i += 1
    #
    print(jets)
    return jets


def creat_static_shape(coor_list, on_time=3):
    jets = []
    start_time = 0.01
    for point in coor_list:
        jet = dict(pin=pin11, point=point, start_time=start_time, stop_time=on_time, cycle=on_time + off_time, on=0,
                   on_time=on_time, off_time=0)
        jets.append(jet)
    return jets


#
# start_times = np.arange(1, 100, 0.07)
# # stop_times = np.arange(1,100,0.07)
# stop_times = [0.1, 0.1, 0.1, 0.1]
# on_times = [0.1, 0.1, 0.1, 0.1]
# off_times = [0.07, 0.07, 0.07, 0.07]
# moving_line = [dict(pin=pin11, on=0, point=(4, 2), start_time=start_times[0] - 0.07, stop_time=stop_times[0],
#                     on_time=on_times[0], off_time=off_times[0]),
#                dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_time=stop_times[0],
#                     on_time=on_times[0], off_time=off_times[0])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[1], stop_time=stop_times[1],
#                     on_time=on_times[1], off_time=off_times[1])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[2], stop_time=stop_times[2],
#                     on_time=on_times[2], off_time=off_times[2])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_time=stop_times[3],
#                     on_time=on_times[3], off_time=off_times[3])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[0], stop_time=stop_times[0],
#                     on_time=on_times[0], off_time=off_times[0])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_time=stop_times[1],
#                     on_time=on_times[1], off_time=off_times[1])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_time=stop_times[2],
#                     on_time=on_times[2], off_time=off_times[2])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=stop_times[3],
#                     on_time=on_times[3], off_time=off_times[3])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_time=stop_times[0],
#                     on_time=on_times[0], off_time=off_times[0])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[1], stop_time=stop_times[1],
#                     on_time=on_times[1], off_time=off_times[1])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_time=stop_times[2],
#                     on_time=on_times[2], off_time=off_times[2])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[3], stop_time=stop_times[3],
#                     on_time=on_times[3], off_time=off_times[3])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(7, 2), start_time=start_times[0], stop_time=stop_times[0],
#                     on_time=on_times[0],
#                     off_time=off_times[0])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(7, 3), start_time=start_times[1], stop_time=stop_times[1],
#                     on_time=on_times[1], off_time=off_times[1])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[2], stop_time=stop_times[2],
#                     on_time=on_times[2], off_time=off_times[2])
#     ,
#                dict(pin=pin11, on=0, started=0, point=(7, 5), start_time=start_times[3], stop_time=stop_times[3],
#                     on_time=on_times[3], off_time=off_times[3])
#                ]
#
# start_times = np.arange(1, 100, 0.1)
# on_times = [100, 100, 100, 100]
# off_times = [0.04, 0.03, 0.008, 0.003]
# growing_square = [
#     dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_time=10000,
#          on_time=on_times[0], off_time=off_times[0])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_time=1000,
#          on_time=on_times[1], off_time=off_times[1])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[0], stop_time=1000,
#          on_time=on_times[2], off_time=off_times[2])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[0], stop_time=100,
#          on_time=on_times[3], off_time=off_times[3])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[1], stop_time=1000,
#          on_time=on_times[0], off_time=off_times[0])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_time=1000,
#          on_time=on_times[1], off_time=off_times[1])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[1], stop_time=1000,
#          on_time=on_times[2], off_time=off_times[2])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[1], stop_time=1000,
#          on_time=on_times[3], off_time=off_times[3])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[2], stop_time=1000,
#          on_time=on_times[0], off_time=off_times[0])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[2], stop_time=1000,
#          on_time=on_times[1], off_time=off_times[1])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_time=1000,
#          on_time=on_times[2], off_time=off_times[2])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_time=1000,
#          on_time=on_times[3], off_time=off_times[3])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(7, 2), start_time=start_times[3], stop_time=1000,
#          on_time=on_times[0],
#          off_time=off_times[0])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(7, 3), start_time=start_times[3], stop_time=1000,
#          on_time=on_times[1], off_time=off_times[1])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[3], stop_time=1000,
#          on_time=on_times[2], off_time=off_times[2])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(7, 5), start_time=start_times[3], stop_time=1000,
#          on_time=on_times[3], off_time=off_times[3]),
#     dict(pin=pin11, on=0, started=0, point=(8, 2), start_time=start_times[4], stop_time=1000,
#          on_time=on_times[0],
#          off_time=off_times[0])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(8, 3), start_time=start_times[4], stop_time=1000,
#          on_time=on_times[1], off_time=off_times[1])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(8, 4), start_time=start_times[4], stop_time=1000,
#          on_time=on_times[2], off_time=off_times[2])
#     ,
#     dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[4], stop_time=1000,
#          on_time=on_times[3], off_time=off_times[3])
# ]

ISOI = 0.07
start_times = np.arange(1, 100, 0.1)
on_times = [0.005, 0.008, 0.01, 0.02]
off_times = [0.09, 0.03, 0.01, 0.005]
shading_square = [
    dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_time=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_time=10000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[2], stop_time=10000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_time=10000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[1], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[3], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 3), start_time=start_times[1], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 4), start_time=start_times[2], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 5), start_time=start_times[3], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
]

start_times = np.arange(1, 100, 0.1)
on_times = [0.01, 0.01, 0.01, 0.01]
off_times = [0.005, 0.005, 0.005, 0.005]

no_shading_square = [
    dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_time=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_time=10000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[2], stop_time=10000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_time=10000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[1], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[1], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[2], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[3], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 3), start_time=start_times[1], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 4), start_time=start_times[2], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(3, 5), start_time=start_times[3], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
]

start_times = np.arange(1, 100, 0.07)
on_times = [0.004, 0.004, 0.004, 0.004]
off_times = [0.004, 0.004, 0.004, 0.004]
two_square = [
    dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[0], stop_time=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[0], stop_time=10000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 2), start_time=start_times[1], stop_time=100, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[3], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[2], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[0], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 3), start_time=start_times[0], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 4), start_time=start_times[0], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(9, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
    ,
    dict(pin=pin11, on=0, started=0, point=(9, 3), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(9, 4), start_time=start_times[0], stop_time=1000, on_time=on_times[0],
         off_time=off_times[0])
    ,
    dict(pin=pin11, on=0, started=0, point=(10, 2), start_time=start_times[0], stop_time=1000, on_time=on_times[1],
         off_time=off_times[1])
    ,
    dict(pin=pin11, on=0, started=0, point=(10, 3), start_time=start_times[0], stop_time=1000, on_time=on_times[2],
         off_time=off_times[2])
    ,
    dict(pin=pin11, on=0, started=0, point=(10, 4), start_time=start_times[0], stop_time=1000, on_time=on_times[3],
         off_time=off_times[3])
]
phantom = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=0, stop_time=0.01, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, point=(4, 4), start_time=0, stop_time=0.01, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, point=(4, 7), start_time=0, stop_time=0.01, on_time=0.003,
         off_time=0.003)
    ,
]

# moving_point = [
#     dict(pin=pin11, on=0, started=0, point=(4, 2), start_time=start_times[8], stop_time=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[7], stop_time=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[6], stop_time=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[5], stop_time=0.1, on_time=0.003, off_time=0.003),
#     dict(pin=pin11, on=0, started=0, point=(4, 6), start_time=start_times[4], stop_time=0.1, on_time=0.003,
#          off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_time=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(3, 5), start_time=start_times[1], stop_time=0.1, on_time=0.003, off_time=0.003)
#     ,
#     dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[0], stop_time=0.1, on_time=0.003, off_time=0.003),  dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[0]-0.07, stop_time=0.1, on_time=0.003, off_time=0.003)]
#
moving_point = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[6], stop_time=0.1, on_time=0.1, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[5], stop_time=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_time=0.1, on_time=0.1,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_time=0.1, on_time=0.1,
         off_time=0.003)

]
moving_point_dulconer = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[7], stop_time=0.1, on_time=0.1, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[6], stop_time=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[5], stop_time=0.1, on_time=0.1,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_time=0.1, on_time=0.1,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_time=0.1, on_time=0.1,
         off_time=0.003)

]

moving_point_square = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[0], stop_time=0.1, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[1], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[2], stop_time=0.1, on_time=0.003,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[3], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[4], stop_time=0.1, on_time=0.003,
         off_time=0.003),
    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[5], stop_time=0.1, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[6], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[7], stop_time=0.1, on_time=0.003,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[8], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    ,
    # dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_time=0.1, on_time=0.003,
    #      off_time=0.003)
]
i = 0
moving_point_square_dulcorner = [
    dict(pin=pin11, on=0, point=(4, 3), start_time=start_times[0], stop_time=0.1, on_time=0.1, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[1], stop_time=0.1, on_time=0.1,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[2], stop_time=0.1, on_time=0.003,
         off_time=0.003),
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[3], stop_time=0.1, on_time=0.003,
         off_time=0.003),  # corner

    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[4], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    ,
    dict(pin=pin11, on=0, point=(6, 5), start_time=start_times[5], stop_time=0.1, on_time=0.003,
         off_time=0.003),
    dict(pin=pin11, on=0, point=(6, 5), start_time=start_times[6], stop_time=0.1, on_time=0.003,
         off_time=0.003),  # corner

    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[7], stop_time=0.1, on_time=0.003, off_time=0.003)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[8], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    , dict(pin=pin11, on=0, started=0, point=(6, 3), start_time=start_times[9], stop_time=0.1, on_time=0.003,
           off_time=0.003)  # corner
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 3), start_time=start_times[10], stop_time=0.1, on_time=0.003,
         off_time=0.003),

    dict(pin=pin11, on=0, started=0, point=(4, 3), start_time=start_times[11], stop_time=0.1, on_time=0.003,
         off_time=0.003)
    ,
    # dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[2], stop_time=0.1, on_time=0.003,
    #      off_time=0.003)
]

# for jet in moving_point_square_dulcorner:
#     jet['point'] =(jet['point'][0]+5, jet['point'][1])

moving_point_two_square = moving_point_square_dulcorner + moving_point_square

off_time = 0.07
on_time = 0.1
triangle_seq = [
    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[7], stop_time=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, point=(5, 5), start_time=start_times[6], stop_time=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 6), start_time=start_times[5], stop_time=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_time=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[3], stop_time=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[3], stop_time=0.1, on_time=on_time,
         off_time=off_time),
    dict(pin=pin11, on=0, started=0, point=(5, 4), start_time=start_times[2], stop_time=0.1, on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[1], stop_time=0.1, on_time=on_time,
         off_time=off_time)

]
triangle = [
    dict(pin=pin11, on=0, point=(7, 4), start_time=start_times[0], stop_time=0.1, on_time=0.1,
         off_time=off_time),
    dict(pin=pin11, on=0, point=(6, 4), start_time=start_times[1], stop_time=0.1, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, point=(5, 4), start_time=start_times[2], stop_time=0.1, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[3], stop_time=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 5), start_time=start_times[4], stop_time=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 6), start_time=start_times[5], stop_time=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 7), start_time=start_times[6], stop_time=100, on_time=0.1,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(4, 4), start_time=start_times[7], stop_time=100, on_time=0.1,
         off_time=off_time)
    , dict(pin=pin11, on=0, started=0, point=(6, 5), start_time=start_times[8], stop_time=100, on_time=0.1,
           off_time=off_time)
    , dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[9], stop_time=100, on_time=0.1,
           off_time=off_time)

]

off_time = 0.004
on_time = 1
circle = [
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[0], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(5, 6), start_time=start_times[1], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 7), start_time=start_times[2], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 7), start_time=start_times[3], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 6), start_time=start_times[4], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(8, 5), start_time=start_times[5], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(7, 4), start_time=start_times[6], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
    ,
    dict(pin=pin11, on=0, started=0, point=(6, 4), start_time=start_times[7], stop_time=1000,
         on_time=on_time,
         off_time=off_time),
    dict(pin=pin11, on=0, started=0, point=(5, 5), start_time=start_times[7], stop_time=1000,
         on_time=on_time,
         off_time=off_time)
]

start_times = np.arange(1, 100, 0.1)

for jet in shading_square:
    jet['cycle'] = jet['on_time'] + jet['off_time']
    # jet['start_time'] = start_times[i]
    # jet['on_time'] = 0.2
    # jet['off_time'] = 0.2
    # jet['stop_time'] = 0.1

# =============== experiment 1 dynamic shape ======================
square2x2 = [(4, 3), (4, 4), (5, 4), (5, 3), (4, 3)]
diamond3x3 = [(4, 3), (5, 4), (6, 3), (5, 2), (4, 3)]

square4x4 = [(4, 5), (5, 5), (6, 5), (7, 5), (7, 4), (7, 3), (7, 2), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5)]

# square4x4 = [(5,5)]
square3x3 = [(4, 4), (5, 4), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4)]  # 9
triangle4x4 = [(4, 5), (5, 4), (6, 3), (5, 2), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)] #9
hexagon4x4 = [(5, 4), (6, 4), (7, 3), (7, 2), (6, 1), (5, 1), (4, 2), (4, 3), (5, 4)]  # 9

# square2x2_corner = [(4,3),(4,3),(4,4),(4,4),(5,4),(5,4),(5,3),(5,3),(4,3),(4,3)]
# diamond3x3_corner = [(4,3),(4,3),(5,4),(5,4),(6,3),(6,3),(5,2),(5,2),(4,3),(4,3)]
hexagon4x4_longer = [ (5, 4), (6, 4), (7, 3), (7, 2), (6, 1), (5, 1), (4, 2), (4, 3), (5, 4), (5, 4)]  # 11
square3x3_longer = [(4, 4), (4, 4), (5, 4), (6, 4), (6, 4), (6, 3), (6, 2), (6, 2), (5, 2), (4, 2), (4, 2), (4, 3),
                    (4, 4), (4, 4)]
square4x4_longer = [(4, 5), (5, 5), (6, 5), (7, 5), (7, 5), (7, 4), (7, 3), (7, 2), (7, 2), (6, 2), (5, 2),
                    (4, 2), (4, 2), (4, 3), (4, 4), (4, 5)]  # 17
triangle4x4_longer = [(4, 5), (5, 4), (6, 3), (6, 3), (5, 2), (4, 1), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
                      (4, 5)]  # 12

square3x3_over = [(4, 4), (5, 4), (6, 4), (7, 4), (6, 3), (6, 2), (6, 1), (5, 2), (4, 2), (3, 2), (4, 3),
                  (4, 4), (4, 5)] #13
square4x4_over = [(4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 2), (5, 2),
                  (4, 2), (3, 2), (4, 3), (4, 4), (4, 5), (4, 6)]  # 17

triangle4x4_over = [(4, 5), (5, 4), (6, 3), (7, 2), (5, 2), (4, 1), (3, 0), (4, 2), (4, 3), (4, 4), (4, 5),
                    (4, 6)]  # 12

square3x3_pause = [(4, 4), (5, 4), (6, 4), (0, 0), (6, 4), (6, 3), (6, 2), (0, 0), (6, 2), (5, 2), (4, 2),
                   (0, 0), (4, 2), (4, 3), (4, 4)]  # 15

square4x4_pause = [(4, 5), (5, 5), (6, 5), (7, 5), (0, 0), (7, 5), (7, 4), (7, 3), (7, 2), (0, 0), (7, 2),
                   (6, 2), (5, 2), (4, 2), (0, 0), (4, 2), (4, 3), (4, 4), (4, 5)]  # 19

triangle4x4_pause = [(4, 5), (5, 4), (6, 3), (0, 0), (6, 3), (5, 2), (4, 1), (0, 0), (4, 1), (4, 2), (4, 3), (4, 4),
                     (4, 5)]  # 13
