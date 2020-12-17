from ArduinoControl.jets_controller import *
import var

points = [(1, 0), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (3, 0), (3, 2), (3, 4), (3, 6), (3, 8), (3, 10), (5, 0),
          (5, 2), (5, 4), (5, 6), (5, 8), (5, 10), (7, 0), (7, 2), (7, 4), (7, 6), (7, 8), (7, 10), (9, 0), (9, 2),
          (9, 4), (9, 6), (9, 8), (9, 10), (11, 0), (11, 2), (11, 4), (11, 6), (11, 8), (11, 10)]
point = (5, 8)


def experiment1_frequency(file, lasting_time):
    ser = serial.Serial(port_u, baudrate=250000)
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    # on_times = [0.004, 0.006, 0.01, 0.016, 0.027, 0.044, 0.071, 0.114, 0.185, 0.300]  # logarithmic interval
    on_times = [0.004, 0.006, 0.01, 0.016, 0.027, 0.044, 0.071, 0.114, 0.185, 0.300]  # logarithmic interval

    off_times = [0.004, 0.005, 0.007, 0.011, 0.015, 0.022, 0.031, 0.044]
    combinations = []
    for on_time in on_times:
        for off_time in off_times:
            combinations.append((on_time, off_time))
    random.shuffle(combinations)
    run_frequency_experiment(ser, file, combinations, lasting_time)


if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs
    import random

    participant = 'p1'
    id = str(int(time.time()))[-6:]
    file = f'/home/molly/PycharmProjects/AirTable/result/fre_exp/result_{participant}_{id}.txt'
    f = open(file, 'w+')
    f.close()
    port_u = '/dev/ttyACM0'
    experiment1_frequency(file,3)
    f.close()