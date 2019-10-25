import tkinter
from tkinter import *
from tkinter import messagebox



import sys
import os



def loadVideos():
    os.system('python understand_site.py')
    
def makeData():
    os.system('python create_data.py')

def edgeDetection():
    os.system('python edge_detection.py')   

def trainModel():
    messagebox.showwarning("TRAINING", "Only use if location of CCTV is changed. It will take a lot of time to be completed")
    os.system('python cnn_model.py')   



def prediction():
    os.system('python prediction.py')

def book():
    os.system('python GuiForBooking.py')    








k=tkinter.Tk()
k.title("Parking system")
k["bg"] = "black"

label=Label(k,text="Options Available",bg="black",fg="red")
label.grid(row=2)

button=tkinter.Button(k,text="Load Video(1)",width=20,height=2,font="Helvetica 10 italic bold",bg="black",fg="red",command=loadVideos)
button.grid(row=6,sticky=W,column=0)

button=tkinter.Button(k,text="Make Data(2)",width=20,height=2,font="Helvetica 10 italic bold",bg="black",fg="red",command=makeData)
button.grid(row=6,sticky=W,column=3)

button=tkinter.Button(k,text="Edge Detection(3)",width=20,height=2,font="Helvetica 10 italic bold",bg="black",fg="red",command=edgeDetection)
button.grid(row=8,sticky=W,column=0)

button=tkinter.Button(k,text="Train Model(!!)",width=20,height=2,font="Helvetica 10 italic bold",bg="black",fg="red",command=trainModel)
button.grid(row=8,sticky=W,column=3)

button=tkinter.Button(k,text="Prediction(4)",width=20,height=2,font="Helvetica 10 italic bold",bg="black",fg="red",command=prediction)
button.grid(row=10,sticky=W,column=0)

button=tkinter.Button(k,text="Booking(5)",width=20,height=2,font="Helvetica 10 italic bold",bg="black",fg="red",command=book)
button.grid(row=10,sticky=W,column=3)





button.mainloop()

