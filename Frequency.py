from ArduinoControl.jets_controller import  *

if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs

    file = 'result_.txt'
    """Demonstrate communicating with an attached Arduino for shifting
    one level at a time."""
    port_u = '/dev/ttyACM1'
    def crap():
        ser = serial.Serial(port_u, baudrate=250000)
        ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
        on_times =  [ 0.004, 0.005, 0.008, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
        # on_times = [0.004, 0.005, 0.008, 0.01, 0.05, 0.1, 0.2, 0.3]
        off_times = [  0.004, 0.008, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.040]

        combinations = []
        for on_time in on_times:
            for off_time in off_times:
                combinations.append((on_time, off_time))
        random.shuffle(combinations)

        # frequency_pilot(ser,combinations)

        run_frequency_pilot(ser,file ,combinations)





        # on_times = [0.003, 0.004, 0.006, 0.008, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2,
        #             0.22, 0.24, 0.26, 0.28, 0.3, 0.35, 0.4, 0.45, 0.5]
        # v_start = [0.003, 0.004, 0.005, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022, 0.024, 0.026, 0.028,
        #              0.03, 0.034, 0.038, 0.042, 0.046, 0.05, 0.05, 0.055, 0.06, 0.07]

        #
        # for n in range(100000000):
        #     t = time.time() - start
        #     controller.switch(t)
        #     ser.write(pin11.shift_str())


    crap()