
import tkinter
from tkinter import *
import sys
  





master = Tk() 

master.title("SLOT BOOKING")

washing = IntVar()
washing.set = 0
emptySlots = 20
if emptySlots>=400:
    price = "500"

if emptySlots<400 and emptySlots>=300:
    price = "400"

if emptySlots<300 and emptySlots>=200:
    price = "300"

if emptySlots<200 and emptySlots>=100:
    price = "200"

if emptySlots<100:
    price = "150"

totalPrice = int(price)+100
totalPrice = str(totalPrice)

l1 = Label(master, text = "NAME:") 
l2 = Label(master, text = "NUMBER PLATE:") 
  

l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2) 
  

e1 = Entry(master) 
e2 = Entry(master) 
  

e1.grid(row = 0, column = 1, pady = 5) 
e2.grid(row = 1, column = 1, pady = 5) 
  

def fun():
    print(e1.get())
    master.destroy()
c1 = Checkbutton(master, text = "Vehicle Cleaning",variable=washing) 
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 


Button(master,text="BOOK NOW",bg = "yellow",height = 3,width=20,command = fun).grid(row=3,column=1,sticky=S)
 
 

   
 
can = Canvas(master,height = 100,width = 250,bg = "red")


   



can.grid(row = 0, column = 2, 
        columnspan = 2, rowspan = 2, padx = 5, pady = 1) 
        

can.create_text(58,20,fill="black",font="Times 10 italic bold",
                        text="Slot Price=Rs."+price)   

can.create_text(79,40,fill="black",font="Times 10 italic bold",
                        text="ConvenienceFees=Rs.100")  

can.create_text(105,70,fill="darkblue",font="Times 15 italic bold",
                        text="TOTAL=Rs."+totalPrice)

can_2 = Canvas(master,height = 100,width = 250,bg = "blue")

can_2.grid(row = 2, column = 2, 
        columnspan = 2, rowspan = 2, padx = 5, pady = 1) 

can_2.create_text(130,40,fill="white",font="Times 28 italic bold",
                        text="THANK YOU!!")
# b1 = Button(master, text = "Zoom in",command=fun) 
# b2 = Button(master, text = "Zoom out") 

  


# b1.grid(row = 2, column = 2, sticky = E) 
# b2.grid(row = 2, column = 3, sticky = E) 
  

mainloop() 
