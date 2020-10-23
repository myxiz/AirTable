from ArduinoControl.single_valve import *
from multiprocessing import Pool

port_u = '/dev/ttyACM0'
port_w = 'com6'


#
# def switch(pin,point,duration,interval,starttime):
#     intervals = []
#     durations = []
#     time.sleep(starttime)
#     p_start = time.time()
#     for n in range(1000):
#         on_time = time.time()
#         pin.set(point, 0)
#         ser.write(pin.shift_str())
#         # print(" ")
#         time.sleep(interval) # interval
#         intervals.append(on_time - off_time)
#         off_time = time.time()
#         pin.set(point, 1)
#         ser.write(pin.shift_str())
#         durations.append(off_time - on_time)
#         time.sleep(duration) # duration
#
#     print('duration', sum(durations), "ms")
#     print('interval', sum(intervals), "ms")
#     print((time.time() - p_start),'s')

def multi_switch(parameters):
    pin, point, start_time, duration, interval = parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]
    durations = []
    intervals = []
    time.sleep(start_time)
    pin.set(point, 1)
    ser.write(pin.shift_str())
    p_start = time.time()
    on_time = time.time()
    print('point',point, 'start at', on_time )
    for n in range(1000):
        time.sleep(duration)  # duration

        pin.set(point, 0)
        ser.write(pin.shift_str())
        off_time = time.time()
        durations.append(off_time - on_time)

        time.sleep(interval)  # interval

        pin.set(point, 1)
        ser.write(pin.shift_str())
        on_time = time.time()
        intervals.append(on_time - off_time)

    print('point', point, 'duration', sum(durations), 'ms')
    print('point', point, 'interval', sum(intervals), 'ms')
    print('point', point, (time.time() - p_start), 's')
    return (intervals,durations)


if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs

    """Demonstrate communicating with an attached Arduino for shifting
    one level at a time."""


    pin11 = DataPin(11)
    # ser = serial.Serial(sys.argv[1], baudrate=115200)
    ser = serial.Serial(port_u, baudrate=115200)

    print(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    parameters1 = dict(pin=pin11, point=(3, 6), startTime=0.004, duration=0.1, interval=0.01)
    parameters2 = dict(pin=pin11, point=(6, 9), startTime=0.003, duration=0.1, interval=0.01)
    parameters3 = dict(pin=pin11, point=(6, 3), startTime=0.003, duration=0.1, interval=0.01)
    parameters4 = dict(pin=pin11, point=(9, 6), startTime=0.003, duration=0.1, interval=0.01)

    jets = [[pin11, parameters1['point'], parameters1['startTime'], parameters1['duration'], parameters1['interval']],
            [pin11, parameters2['point'], parameters2['startTime'], parameters2['duration'], parameters2['interval']],
            [pin11, parameters3['point'], parameters3['startTime'], parameters3['duration'], parameters3['interval']],
           [pin11, parameters4['point'], parameters4['startTime'], parameters4['duration'], parameters4['interval']]
            ]
    # with Pool(4) as p:
    #     print(p.map(multi_switch, jets))

    val = True
    # pin11.set(parameters1['point'], val)
    start = time.time()
    on_time = time.time()
    intervals = []
    durations = []

    class Controller(object):
        # jet1 = dict(pin=pin11, point=(3, 6), startTime=0.004, duration=0.1, interval=0.01)
        # jet2 = dict(pin=pin11, point=(6, 9), startTime=0.003, duration=0.1, interval=0.01)
        # jet3 = dict(pin=pin11, point=(6, 3), startTime=0.003, duration=0.1, interval=0.01)
        # jet4 = dict(pin=pin11, point=(9, 6), startTime=0.003, duration=0.1, interval=0.01)

        def __init__(self,jets_list = None):
            if not jets_list:
                self.jets = [ dict(pin=pin11, on = 0,started = 0, point=(4, 6), start_time=0.04, duration=0.0100, interval=0.0028)
                            , dict(pin=pin11, on = 0,started = 0, point=(6, 8), start_time=0.03, duration=0.0100, interval=0.0028)
                            , dict(pin=pin11, on = 0,started = 0, point=(6, 4), start_time=0.02, duration=0.0100, interval=0.0028)
                            , dict(pin=pin11, on = 0,started = 0, point=(8, 6), start_time=0.01, duration=0.0100, interval=0.0028)]
            else: self.jets = jets_list

        def switch(self,time):
            for jet in self.jets:
                t = time - jet['start_time']
                if jet['started']:

                    res_time = t % (jet['duration']+ jet['interval'])

                    if (res_time < 0.002) & (not jet['on']) :
                        jet['pin'].set(jet['point'], 1)
                        # ser.write(pin11.shift_str())
                        jet['on'] = 1
                        print('res', res_time)
                        print('p',jet['point'],'on')
                    if (jet['duration']< res_time < jet['duration']+0.002) & jet['on']:
                        jet['pin'].set(jet['point'], 0)
                        jet['on'] = 0
                        # ser.write(pin11.shift_str())
                        print('res', res_time)

                        print('p', jet['point'], 'off')
                    continue
                if t >= 0 :
                    jet['started'] = 1
                    print(self.jets[1])


    controller = Controller()

    for n in range(1000000):
        time.sleep(0.0001)
        t = time.time() - start
        controller.switch(t)
        ser.write(pin11.shift_str())
        print(t*1000)

    #
    # for n in range(10000):time
    #     time.sleep(0.0250000)  # duration of p1 interval of p2
    #
    #     # pin11.set(parameters1['point'], 0)
    #     # pin11.set(parameters2['point'], 1)
    #     pin11.set(parameters3['point'], 0)
    #     # pin11.set(parameters4['point'], 1)
    #     ser.write(pin11.shift_str())
    #     off_time = time.time()
    #     # print('on')
    #     durations.append(off_time - on_time)
    #
    #     time.sleep(0.0050)  # interval of point1 duration of p2
    #     # pin11.set(parameters1['point'], 1)
    #     # pin11.set(parameters2['point'], 0)
    #     pin11.set(parameters3['point'], 1)
    #     # pin11.set(parameters4['point'], 0)
    #     ser.write(pin11.shift_str())
    #     # print('off')
    #
    #     on_time = time.time()
    #     intervals.append(on_time - off_time)
    #
    # print('duration', sum(durations)*0.1, "ms")
    # print('interval', sum(intervals)*0.1, "ms")
    # print((time.time() -  start),'s')
