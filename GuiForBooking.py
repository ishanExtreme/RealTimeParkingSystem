
import tkinter
from tkinter import *
import sys
import os
  
master = Tk() 
master["bg"]="#0f2043"
master.title("SLOT BOOKING")

washing = IntVar()
washing.set = 0
file1 = open("empty_slots.txt","r+")
emptySlots = int(file1.read())
file1.close()
 
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
  

l1.grid(row = 0, column = 0, sticky = W, pady = 2,padx=5) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2,padx=5) 
  

e1 = Entry(master) 
e2 = Entry(master) 
  

e1.grid(row = 0, column = 1, pady = 5) 
e2.grid(row = 1, column = 1, pady = 5) 
  

def book():
    file1 = open("name.txt","w") 
    file1.write(e1.get()) 
    file1.close()
    file2 = open("number_plate.txt","w") 
    file2.write(e2.get()) 
    file2.close()
    os.system('python book_spots.py')
    master.destroy()
c1 = Checkbutton(master, text = "Vehicle Cleaning",variable=washing)
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)


Button(master,text="BOOK NOW",bg = "#D5a458",height = 3,width=20,command = book).grid(row=4,column=1,sticky=S)
 
 

   
 
can = Canvas(master,height = 100,width = 250,bg = "#79CEDC",highlightbackground="#D5a458")


   



can.grid(row = 1, column = 2, 
        columnspan = 2, rowspan = 2, padx= 5,sticky = N) 
        

can.create_text(58,20,fill="#0f2043",font="Times 10 italic bold",
                        text="Slot Price=Rs."+price)   

can.create_text(79,40,fill="#0f2043",font="Times 10 italic bold",
                        text="ConvenienceFees=Rs.100")  

can.create_text(105,70,fill="#0f2043",font="Times 15 italic bold",
                        text="TOTAL=Rs."+totalPrice)




#can_2 = Canvas(master,height = 100,width = 250,bg = "#79CEDC")



#can_2.grid(row = 8, column = 2, 
       # columnspan = 2, rowspan = 2, padx = 5, pady = 1) 

#can_2.create_text(130,40,fill="#0f2043",font="Times 28 italic bold",
                        #text="THANK YOU!!")

label=Label(master,text="THANK YOU!! ",bg="#0f2043",fg="#D5a458")
label.grid(row=8)
# b1 = Button(master, text = "Zoom in",command=fun) 
# b2 = Button(master, text = "Zoom out") 

  


# b1.grid(row = 2, column = 2, sticky = E) 
# b2.grid(row = 2, column = 3, sticky = E) 
  

mainloop() 
