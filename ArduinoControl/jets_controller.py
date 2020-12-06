from ArduinoControl.single_valve import *
from ArduinoControl.shape_generator import shading_square
import time
import numpy as np

port_w = 'com6'

class Controller(object):
    def __init__(self, ser, jets_list=None):
        self.ser =ser
        if not jets_list:
            self.jets = shading_square

        else: self.jets = jets_list

        stop_times = [i['stop_time']+i['start_time'] for i in self.jets]
        print(stop_times)
        # for jet in self.jets:
        #     stop_times.append(jet['stop_time'])
        self.loop_period = max(stop_times)

    def periodical_switch(self, time_now):  # jet will start at start_time, on/off duty according to on_time, off_time
        for jet in self.jets:
            t = time_now - jet['start_time']
            if t >= 0:
                res_time = t % (jet['cycle'])
                if  (res_time ==0)& (t<= jet['stop_time']):
                    jet['pin'].set(jet['point'], 1)
                    jet['on'] = 1

                if jet['on_time'] == res_time :
                    jet['pin'].set(jet['point'], 0)
                    jet['on'] = 0


    def sequencial_motion_switch(self,time_now,inter_cycle):
        res_time = time_now % (self.loop_period + inter_cycle)
        for jet in self.jets:
            t = res_time - jet['start_time']
            if t >= 0:
                # res_time = t % (jet['cycle'])
                if  (not jet['on']) & (t<= jet['stop_time']):
                    jet['pin'].set(jet['point'], 1)
                    jet['on'] = 1

                if jet['on']& (t >= jet['stop_time']):
                    jet['pin'].set(jet['point'], 0)
                    jet['on'] = 0

    def get_jets_status(self):
        jets_status = [{jet['point']:jet['on']} for jet in  self.jets]
        return jets_status


    def loop(self,times):
        start = time.time()
        t = start
        for n in range(times):
            if (time.time() - start - t) * 1000 > 2:
                print((time.time() - start - t)*1000)
            t = time.time() - start
            self.periodical_switch(t)

            # print(t*1000)
            self.ser.write(pin11.shift_str())


def compile_frequency(ser, jets,times):   # return (str, time, jets_status)
    serial_strs = [(cobs.encode(bytes([11]) + b'\x00') + b'\x00',-1,[])]
    last = cobs.encode(bytes([11]) + b'\x00') + b'\x00'
    jets_contro = Controller(ser, jets)
    for n in range(times):
        jets_contro.periodical_switch(n / 1000)
        jets_status = jets_contro.get_jets_status()
        if not (last == pin11.shift_str()):
            last =  pin11.shift_str()
            serial_strs.insert(0, (pin11.shift_str(), n, jets_status))
    serial_strs.insert(0, (pin11.shift_str(), float('inf'), jets_contro.get_jets_status()))
    return serial_strs


def compile_motion(ser, jets,times,inter_cycle):
    # serial_strs = [(cobs.encode(bytes([11]) + b'\x00') + b'\x00',-0.001,[0])]
    last = cobs.encode(bytes([11]) + b'\x00') + b'\x00'
    serial_strs = []
    jets_contro = Controller(ser, jets)
    for n in range(times):
        jets_contro.sequencial_motion_switch(n / 1000,0.001)
        jets_status = str([i for i in jets_contro.get_jets_status()[0].values()])
        if not (last == pin11.shift_str()):
            last =  pin11.shift_str()
            serial_strs.insert(0,(pin11.shift_str(),n/1000, jets_status))

    serial_strs.insert(0, (pin11.shift_str(), float('inf'),str([i for i in jets_contro.get_jets_status()[0].values()])))
    return serial_strs


def sending_serial_sequence(ser, lasting_time, serial_strs, record = False,file = None):
    (serial_str, t, jets_status) = serial_strs.pop()
    start = time.time()+0.001
    for i in range(lasting_time*1000):
        time_now = (time.time()-start)
        # print(time_now-t)
        # if time_now-t == -float('inf'):
        #     print(time_now)
        #     break
        if abs(t-time_now) <= 0.5:  # 0.9 works
            if record:
                with open(file, "a") as myfile:
                    myfile.write('time : %s signal: %s \n' %(time.time(), jets_status))
            ser.write(serial_str)
            (serial_str, t, jets_status) = serial_strs.pop()
        elif time_now-t > 5:
            print('loss at', time_now)
            break
        if time_now > lasting_time:
            break

    # for n in range(lasting_time):
    #     if t <= n:
    #         time.sleep(0.00073)
    #         if (record) & (jets_status != []):
    #             with open(file, "a") as myfile:
    #                 myfile.write(
    #                     'time : ' + str(time.time() * 1000) + ' signal: ' + str(jets_status[0].values()) + '\n')
    #         ser.write(serial_str)
    #         (serial_str, t, jets_status) = serial_strs.pop()
    #
    #         # print(int((time.time()-start)*1000))  #save to somewhere
    #     else:
    #         time.sleep(0.00087)

    ser.write(empty_str)
    print(int((time.time() - start) * 1000))


# render a static shape
def induce_static_shape(ser,file,jets,shape_name,times):
    serial_strs = compile_frequency(ser, jets, 5000)
    # print('off time:', off_time, 'on time : ', on_time)
    sending_serial_sequence(ser,times,serial_strs)
    s = input('answer the shape: ')
    print('the shape is ', shape_name+',')
    with open(file, "a") as myfile:
        myfile.write(shape_name + ' recognized as ' + s + ' \n')


# render a shape by motion , expect a input
def induce_dynamic_shape(ser, file, jets, shape_name, lasting_time):
    serial_strs = compile_motion(ser, jets, lasting_time, inter_cycle=0.3)
    # print('off time:', off_time, 'on time : ', on_time)
    sending_serial_sequence(ser, lasting_time, serial_strs)
    s = input('answer the shape: ')
    print('the shape is ', shape_name + ',')
    with open(file, "a") as myfile:
        myfile.write(shape_name + ' recognized as ' + s + ' \n')


#  render motions with different duration interval combinations for motion experiments
def induce_motion(ser, file, jets, combination, lasting_time, inter_cycle):
    serial_strs = compile_motion(ser, jets, lasting_time , inter_cycle)
    # print('off time:', off_time, 'on time : ', on_time)
    sending_serial_sequence(ser, lasting_time, serial_strs)
    s = input('answer the quality of motion: ')
    print('the quality is ', s + ',')
    with open(file, "a") as myfile:
        myfile.write("interval, duration: "+str(combination) + ' grade : ' + s + ' \n')


def run_frequency_experiment(ser, file, combinations):
    for (on_time, off_time) in combinations:
        point = [
            dict(pin=pin11, on=0, point=(4, 7), start_time=0.0, stop_time=1000, on_time=on_time, off_time=off_time,
                 cycle=on_time + off_time)]
        serial_strs = compile_frequency(ser,point,5000)

        print('off time:', off_time, 'on time : ', on_time)
        sending_serial_sequence(ser,5000,serial_strs)
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


def run_frequency_characterization(ser,point,file, combinations):
    for (on_time, off_time) in combinations:
        point = [
            dict(pin=pin11, on=0, point=point, start_time=0.0, stop_time=1000, on_time=on_time, off_time=off_time,
                 cycle=on_time + off_time)]
        serial_strs = compile_frequency(ser,point,5000)
        # file = 'home/molly/PycharmProjects/AirTable/result/freq/'+str(int(time.time()))+'_'+str(point[0]['point'])+'_'+str(on_time)+'signal.txt'
        print('off time:', off_time, 'on time : ', on_time)
        sending_serial_sequence(ser,5000,serial_strs,record=True,file = file)
        point[0]['pin'].set(point[0]['point'], 0)
        ser.write(pin11.shift_str())
        print(' off time:', off_time, 'on time : ', on_time)
