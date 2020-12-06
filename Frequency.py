from ArduinoControl.jets_controller import *
import var


point = (4, 6)
def experiment1_frequency():
    ser = serial.Serial(port_u, baudrate=115200)
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    on_times = [0.004, 0.005, 0.008, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]  #
    # on_times = [0.004, 0.005, 0.008, 0.01, 0.05, 0.1, 0.2, 0.3]
    off_times = [0.004, 0.008, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.040]
    combinations = []
    for on_time in on_times:
        for off_time in off_times:
            combinations.append((on_time, off_time))
    # random.shuffle(combinations)

    # frequency_pilot(ser,combinations)

    run_frequency_experiment(ser, file, combinations)
    # characterization


def characterization_frequency():
    ser = serial.Serial(port_u, baudrate=250000)
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')

    point = (4,6)
    # for t in [0.004,0.005,0.05,0.5]:
    for t in [0.004, 0.005, 0.05, 0.5]:
        var.on_time = t
        combinations = [(var.on_time, var.on_time)]
        for i in range (10):
            file = '/home/molly/PycharmProjects/AirTable/result/signal/' + str(point)+'_'+str(t)+'_signal_'+str(i) + '.txt'
            f = open(file,'w+')
            f.close()
            run_frequency_characterization(ser, point, file, combinations)
            time.sleep(2)
        time.sleep(2)


if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs
    import  random

    file = '/home/molly/PycharmProjects/AirTable/result/result_'+str(int(time.time()))+'.txt'
    """Demonstrate communicating with an attached Arduino for shifting
    one level at a time."""
    port_u = '/dev/ttyACM0'

    # experiment1_frequency()
    characterization_frequency()
