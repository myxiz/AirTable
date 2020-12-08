from ArduinoControl.jets_controller import *
import var

point = (4, 8)


def experiment1_frequency(file):
    ser = serial.Serial(port_u, baudrate=250000)
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    on_times = [0.004, 0.005, 0.008, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]  #
    # on_times = [0.004, 0.005, 0.008, 0.01, 0.05, 0.1, 0.2, 0.3]
    off_times = [0.004, 0.008, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.040]
    combinations = []
    for on_time in on_times:
        for off_time in off_times:
            combinations.append((on_time, off_time))
    random.shuffle(combinations)
    run_frequency_experiment(ser, file, combinations)


def characterization_frequency():
    ser = serial.Serial(port_u, baudrate=250000)
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')

    # for t in [0.004,0.005,0.05,0.5]:
    for t in [0.004, 0.006, 0.010, 0.016, 0.027, 0.044]:
        var.on_time = t
        combinations = [(var.on_time, var.on_time)]
        for i in range(2):
            file = '/home/molly/PycharmProjects/AirTable/result/signal/' + str(point) + '_' + str(t) + '_signal_' + str(
                i) + '.txt'
            f = open(file, 'w+')
            f.close()
            run_frequency_characterization(ser, point, file, combinations, record=True)
            time.sleep(0.5)
        time.sleep(0.5)


if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs
    import random

    participant = 'p1'
    id = str(int(time.time()))[-6:]
    file = f'/home/molly/PycharmProjects/AirTable/result/fre_exp/result_{participant}_{id}.txt'
    f = open(file, 'w+')
    f.close()
    port_u = '/dev/ttyACM1'
    # experiment1_frequency(file)
    characterization_frequency()
