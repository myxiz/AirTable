from ArduinoControl.single_valve import *
# import csv
# import multiprocessing
# from ArduinoControl.single_valve import Level,Coord, Board
class Controller(object):
    val = 0
    def __init__(self,X,Y,Level):
        self.level  = Level
        self.interval = {}
        self.duration ={}
        self.startTime = {}
        self.start = time.time()
        for x in range(X):
            for y in range(Y):
                self.interval[(x,y)] = None
                self.duration[(x, y)] = None
                self.startTime[(x,y)] = float('inf')

    def set_parameters(self,x,y,time,interval,duration):
        self.duration[(x,y)] = int(duration)
        self.interval [(x,y)] = int(interval)
        self.startTime[(x,y)] = int(time)
        f = open("duration.txt", "w")
        f.write(str(self.duration))
        f.close()
        f = open("interval.txt", "w")
        f.write(str(self.interval))
        f.close()
        f = open("startTime.txt", "w")
        f.write(str(self.startTime))
        f.close()


    def reset_time (self):
        self.start = time.time()
    def status_controller(self):
        # print('call')
        t = (time.time() - self.start)*1000
        start = time.time()
        flag = 0
        for (x,y),startTime in self.startTime.items():
            # print('start', startTime)
            if  t > startTime :
                flag = 1
                # print('start',startTime)
                duration = self.duration[(x,y)]
                interval = self.interval[(x,y)]
                residual_time = (t - float(startTime))% (duration + interval)

                # print(duration,interval)
                if  duration <= residual_time <= duration + update_rate*2:
                    # print(t)
                    root.grid_slaves(y,13-x)[0]['image'] = off_img
                    self.level.set((x,y),0)
                    # print('off')
                if residual_time  <= update_rate*2:
                    # print(t)
                    self.level.set((x,y),1)
                    root.grid_slaves(y, 13 - x)[0]['image'] = on_img
                    # print('on')
        if  flag : ser.write(self.level.shift_str())
        # print('need',(time.time()-start)*1000000)
        root.after(update_rate, self.status_controller)

    def switch_status(self):
        self.val = not self.val
        self.level.set((1, 0), self.val)
        ser.write(self.level.shift_str())
        print(time.time()*1000)
        root.after(1,self.switch_status)
# --- valve actions ---




def set_valve_on(widget,level,x,y):
    level.set((x,y),1)
    print(x,y)
    widget['image'] = on_img
    ser.write(level.shift_str())

def set_valve_off(widget,level,x,y):
    level.set((x, y), 0)
    widget['image'] = off_img
    ser.write(level.shift_str())



# --- click handlers ---

def on_click(args):
    widget, level, x,y, _off_img_name = args[0],args[1],args[2],args[3],args[4]
    if widget['image'] ==_off_img_name:
        set_valve_on(widget,level,x,y)
        print(widget['image'])

    else:
        set_valve_off(widget,level,x,y)
        print(widget['image'])
        pin11.set((x, y), 0)
        ser.write(pin11.shift_str())
def double_click_handler(e, args,controller):
    def confirm_freq(win,para):
        win.destroy()
        controller.set_parameters(x,y,para[0].get(),para[1].get(),para[2].get())

        controller.reset_time()
    widget, level, x, y = args[0], args[1], args[2],args[3]
    win_define_freq = tk.Toplevel(root)
    win_define_freq.geometry('300x200')
    win_define_freq.title('define interval and duration')
    var_interval = tk.StringVar()
    var_interval.set('interval')
    var_duration = tk.StringVar()
    var_duration.set('duration')
    var_starTime = tk.StringVar()
    var_starTime.set('start time')
    l1 = tk.Entry(win_define_freq, bg='white', fg='black', width=20, textvariable=var_interval)
    l2 = tk.Entry(win_define_freq, bg='white', fg='black', width=20, textvariable=var_duration)
    l3 = tk.Entry(win_define_freq, bg='white', fg='black', width=20, textvariable=var_starTime)
    button = tk.Button(win_define_freq, text="Confirm",
                       command=lambda  win=win_define_freq, para  = [var_starTime ,var_interval,  var_duration]
                       : confirm_freq(win,para))
    button.pack()
    l1.pack()
    l2.pack()
    l3.pack()

    # show the frequence


# --- main ---

if __name__ == '__main__':
    import tkinter as tk
    import serial, sys, time
    from cobs import cobs
    port_u = '/dev/ttyACM0'
    port_w = 'com6'
    update_rate = 1 # ms
    sys.path.append(r'E:\study\BoardsControl\lib')

    root = tk.Tk()

    off_img = tk.PhotoImage(data ='iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAFG0lEQVRoQ92aV8gdRRTHf7Fg78aCYBcbWBC7eRAfFEXBEntFxIq9ISo2UJFEwYZijWJDRBNsoOiD/UERFcUodmyxREUlVn5hViYns/fu3rv5vhvP292dOXP+s6fNf+4EupHVgF2BHYBNgQ2BlYDlkvqfgR+AmcB7wMvAc8C3wy4/YQgFGngIcCSw/QB6/gFeBaYB9wM/DqCDQQCsDpwNnAAsO8iihTl+oZuBKcA3bXS2AbAYcCpwSeYabdZqMvYn4GLgBuCvJhOaAlgPeBDYtolS4HfgS+CXNN4vtSawZMP5rwEHAR/3G98EwJ7AfcAKPZR9DzwCPAu8AnwK/B3GLwKsA+wI7AbsmwK9Tq1BfyjwVC8Q/QAcBdwG6D4leQO4CngUmNNvt8L7JRKI84Eta+b+CRwD3FunuxcAjb8TioH+BXAm8FBLo+uGu9MG8BqFAWYrM10RRB0A3eaxmp3X6OMAA65LWRG4HdivoPQPYG/g6fiuBMCA1TVKPu/nvrpLqwu6LgQuLzw3JrYGPsnfRQD6+ks12eZ44NYFbHyl/iTgxsJaJohd8hQbAZwBTC1MHIudj8taDy4t2GItur56ngOwwtqrVP1LNUafNyePhxiH+4SFZwMbVX1UDuCa1CLk4802my2AgG26GfZbNn82i7kYh3rFfynSgRaf2Nu4812lyqZGx3FHpIYvf27vtLYNYPUFSkHzOrDNoKt2OE8b3wI2DzptJm+pABjdsSUehd2vbC59BbPlzgLQv74O6OxtbL7atgcdbvw8qpYCvgKWz55aoScKwJ1+IKxs/2O1HSW5Bzg8GDRZANcCp4cXnrQiqPEGc3TqzXI7pgrAdnX3YJ3tRN9efIwRbZxSar7sEwL4ANgge+phZJlCPz/G9s63nG3Or8Di2ZuZAvgOWDl7+BGw/nhbW7P+58Ba2btZAjDT5KjMuVuMKIB3gU0y2+b8LwAs9C60sASxbm4Q5+fz93WhJ4E9gs8bxAbzKEkpjT5eV8gOS1TKKAGQnbgjGDRFAAcm0ip/58BjR8n6xEq4sbkcUDVzNkr54cYDtBTHqDRzS6dmLj8t2sytWhkt3S01nsso9UNyVHcF+14AJlUATgRuCgPeBLYaATeSknw73Tvk5sxlSSoAkkoeKeOBXsZM7n48pRS8kmoeKWfnfu9B+dxgqQyzh/qBLh86QL0KYPswMei6ErjAZzkAT2bSKvmpxzGyzvt3YExbFdo2A9grTHQzpVVmRQD+Pg24rrDSRcAVbS0YcvxlgOtGOSVn7SIzt2iiFrcrTDy5EOhD2lg7vW4jPchPys8qJXJ33UTuGthRpPtKxGtXQLTHnZfgjSLRYFb8LH9RR6/bG+l/pYsN6T4zg8WuSzFg7y74vGtIr0v5PxMXrAPgOBkAr0BLY6Rhzknl3Yo4jJjnLVRmwZht1Kt+bfGaaz7pBaACYV+Un9hyJe+khR8GfmuJwvZgMnBeoUhVqtx52Yii8Q7qB8AxMhYWM/nTOrGwTE+XfLYlHwLeb+WiO0oe7JQu+WSdY+HMx3vQOrjkNk1iIBrq7aI8UeyX6gC5c15YS8IqGip9X3dZGPWYbTR+noAdxIXyOaZYSWDrQSx2Lb2ndrhFygzkrX28pi1OauJCcaKBdlYC08sF2oDSBb1S8nZoboVtKoMAqHRbJ+RVvQL18rqtLrPLi4Ccp/8C8OaltbRdtG4Bc7h/txGIvI29ikFfuZo7bCHK/27zfCLVWhudT/gXslvv+kxLb20AAAAASUVORK5CYII=')
    on_img = tk.PhotoImage(data ='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')
    pin11 = DataPin(11)
    ser = serial.Serial(port_u, baudrate=115200)
    # ser.write(cobs.encode(bytes([11]) + b'\x00') + b'\x00')

    controller = Controller(2, 2, pin11)
    controller.reset_time()
    for x in range(12):
        for y in range(14):
            valve = tk.Button(root, image=off_img)
            offimg_name = valve['image']
            valve['command'] = lambda args=[valve, pin11, 13 - y, x, offimg_name]: on_click(args)
            valve.bind('<Double-Button-1>', lambda e, args = [valve, pin11 , 13 - y, x], fun =double_click_handler: fun(e, args, controller))
            valve.grid(row=x, column=y)

    root.after(update_rate, controller.status_controller)
    # root.after(update_rate, controller.switch_status)
    root.mainloop()