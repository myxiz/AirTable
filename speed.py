from ArduinoControl.shape_generator import *
from ArduinoControl.jets_controller import *
from ArduinoControl.single_valve import *

if __name__ == '__main__':
    import  serial,random
    ser = serial.Serial(port_u, baudrate=250000)
    # jets_square4x4 = creat_dynamic_shape(square4x4_corner)
    # print(jets_square4x4)
    file = 'result/result_shapes.txt'
    # shape_name = 'square'
    # times = 100000
    #
    # induce_static_shape(ser,file,jets_square4x4,shape_name,times)

    #randering speed

    # jets_triangle4x4 = creat_static_shape(triangle4x4)
    # file = 'result/result_shapes.txt'
    # shape_name = 'triangle'
    # times = 100000
    # induce_static_shape(ser,file,jets_triangle4x4,shape_name,times)


    # jets_circle4x4 = creat_static_shape(hexagon4x4)
    # file = 'result/result_shapes.txt'
    # shape_name = 'circle'
    # times = 100000
    # induce_static_shape(ser, file, jets_circle4x4, shape_name, times)

    speed_combinations  =[ (0.07 , 0.1 ), (0.07, 0.150), (0.07, 0.2), (0.1, 0.15), (0.1, 0.2), (0.1,0.25), (0.15, 0.2), (0.15, 0.25), (0.2, 0.25) ]
    file = 'result/result_motion.txt'

    # for speed_combination in speed_combinations:
    #     interval, duration = speed_combination
    #     jets_hexagon4x4 = creat_dynamic_shape(hexagon4x4, duration, interval)
    #     run_exp_motion_speed(ser, file, jets_hexagon4x4, speed_combination, 5, 0.0001)
    #     ser.write(empty_str)
    random.shuffle(speed_combinations)
    for speed_combination in  speed_combinations:
        interval, duration = speed_combination
        jets_hexagon4x4 = creat_dynamic_shape(hexagon4x4, duration, interval)
        run_exp_motion_speed(ser, file, jets_hexagon4x4, speed_combination, 3, 0.0001)
        ser.write(empty_str)
    with open(file, "a") as myfile:
        myfile.write(str(time.time()))

