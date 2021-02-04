from ArduinoControl.single_valve import *
from ArduinoControl.jets_controller import induce_comparison
import random

# sensation discrimination
def experiment3_difference(file, lasting_time):
    point_1 = (6, 2) #l
    point_2 = (6, 11) #r
    continuous_list = ['0.004 0.006',
                       '0.007 0.027',
                       '0.004 0.071',
                       '0.007 0.044',
                       '0.004 0.114',
                       '0.004 0.185',
                       '0.005 0.185',
                       '0.004 0.044',
                       '0.005 0.3',
                       '0.007 0.016']
    combinations = [tuple(map(float, c.split(' '))) for c in continuous_list]
    comparisons = []
    for combination_1 in combinations:
        for combination_2 in combinations:
            comparisons.append((combination_1, combination_2))
    random.shuffle(comparisons)
    for comparison in comparisons:
        (off_time_1, on_time_1), (off_time_2, on_time_2) = comparison

        jets = [
            dict(pin=pin11, on=0, started=0, point=point_1, start_time=0.08, stop_time=lasting_time,
                 on_time=on_time_1,
                 off_time=off_time_1)
            ,
            dict(pin=pin11, on=0, started=0, point=point_2, start_time=0.1, stop_time=lasting_time,
                 on_time=on_time_2,
                 off_time=off_time_2)
        ]
        induce_comparison(ser, file, jets, comparison, lasting_time)


if __name__ == '__main__':
    import serial,time

    ser = serial.Serial(port_u, baudrate=250000)

    file = 'result/result_difference.txt'

    participant = 'p3'
    id = str(int(time.time()))[-6:]
    file = f'/home/molly/PycharmProjects/AirTable/result/exp_compare/result_{participant}_{id}.txt'
    f = open(file, 'w+')
    f.close()
    port_u = '/dev/ttyACM0'

    experiment3_difference(file, 3)
    f.close()
