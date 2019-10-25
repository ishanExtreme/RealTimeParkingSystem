import tkinter
from tkinter import *
import sys


root = tkinter.Tk()
root.geometry("400x200")
root.title("FRAME COUNTER")
frame_1 = Frame(root) 
frame_1.pack(side = LEFT,expand = True, fill = BOTH ) 
counter = tkinter.IntVar()
counter.set(400)
def increase(event=None):
    counter.set(counter.get() + 1)

def decrease(event=None):
    counter.set(counter.get() - 1)
    if counter.get()<0:
        counter.set(0)
    

var =tkinter.StringVar()
var.set("FRAME 1")
tkinter.Label(frame_1, textvariable=var).pack()
tkinter.Label(frame_1, textvariable=counter).pack()


tkinter.Button(frame_1, text="+", command=increase, fg="dark green", bg = "white").pack(side = RIGHT, expand = True, fill = BOTH)

tkinter.Button(frame_1, text="-", command=decrease, fg="dark green", bg = "white").pack(side = LEFT, expand = True, fill = BOTH)


########################################################################################
frame_3 = Frame(root) 
frame_3.pack(side = LEFT,expand = True, fill = BOTH) 
frame_3.config(bg="green")
#######################################################################################
frame_2 = Frame(root) 
frame_2.pack(side = RIGHT,expand = True,fill = BOTH) 
counter_2 = tkinter.IntVar()
counter_2.set(800)



def increaseFor2(event=None):
    counter_2.set(counter_2.get() + 1)

def decreaseFor2(event=None):
    counter_2.set(counter_2.get() - 1)
    if counter_2.get()<0:
        counter_2.set(0)
    

var_2 =tkinter.StringVar()
var_2.set("FRAME 2")
tkinter.Label(frame_2, textvariable=var_2).pack()
tkinter.Label(frame_2, textvariable=counter_2).pack()


tkinter.Button(frame_2, text="+", command=increaseFor2, fg="dark green", bg = "white").pack(side = RIGHT, expand = True, fill = BOTH)

tkinter.Button(frame_2, text="-", command=decreaseFor2, fg="dark green", bg = "white").pack(side = LEFT, expand = True, fill = BOTH)
root.mainloop()