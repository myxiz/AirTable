from ArduinoControl.shape_generator import *
from ArduinoControl.jets_controller import *
from ArduinoControl.single_valve import *

if __name__ == '__main__':
    import  serial
    ser = serial.Serial(port_u, baudrate=250000)
    jets_square4x4 = creat_static_shape(square4x4)
    print(jets_square4x4)
    # file = 'result/result_shapes.txt'
    # shape_name = 'square'
    # times = 100000
    # # sequence = compile_frequency(ser, jets_square4x4 , )
    # induce_static_shape(ser,file,jets_square4x4,shape_name,times)

    # jets_triangle4x4 = creat_static_shape(triangle4x4)
    # file = 'result/result_shapes.txt'
    # shape_name = 'triangle'
    # times = 100000
    # # sequence = compile_frequency(ser, jets_square4x4 , )
    # induce_static_shape(ser,file,jets_triangle4x4,shape_name,times)


    jets_circle4x4 = creat_static_shape(square3x3_longer)
    file = 'result/result_shapes.txt'
    shape_name = 'circle'
    times = 100000
    # sequence = compile_static(ser, jets_square4x4  ,5)
    induce_static_shape(ser, file, jets_circle4x4, shape_name, 5)