from ArduinoControl.jets_controller import *
from ArduinoControl.shape_generator import *

# shading square
if __name__ == '__main__':
    import serial, sys, time
    from cobs import cobs

    ser = serial.Serial(port_u, baudrate=250000)
    ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')
    shading = 'shading'
    file = f'/home/molly/PycharmProjects/AirTable/result/result_shading.txt'
    induce_shading(ser,file,no_shading_square,shading,10) # render a no shading square
    induce_shading(ser,file,shading_square,shading,10) # render a shading square
    induce_shading(ser,file,no_shading_square,shading,10) # render a no shading square