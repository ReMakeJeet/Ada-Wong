import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import Scrollbar
from tkinter import Canvas
import time

from tkinter.scrolledtext import ScrolledText


#Global variables for state-management of input and output  i use _ as starting char the variables which are global.
# wait what if i use a class?
'''
if so then what it's name ? and what are its attributes?(states?) and behaviours.
i think i should go with funtiosn and non-reusable codes first and follow kiss!

'''
#4. style the output produced by gemma which is in text form(string) take it and change fonts, animate, colors etc RGB-kind of gaems feel if possible use resident evil stle!
def style():
    pass

#3. it procceses the data and display it in a new screen use "Message" it shoulb be transpaent in look wise!
def gemma_ko_bhejo(input_screen,input_field):
    leonInput=input_field.get("1.0","end-1c")
    input_screen.destroy()
    # it should create the messagee screen !
    # output = process__leon_input()
    # output = style(ouput)# we have to create this style method
  

    new_screen = tk.Tk()
    new_screen.title("Message screen means Ada response")
    new_screen.geometry("1200x500")

    output_font = tkFont.Font(family="Helvetica", size=24, slant=tkFont.ROMAN)
    output_field = ScrolledText(new_screen,background="black", foreground="white")
    output_field.configure(padx=10,pady=10,font=output_font,state=NORMAL)
    delta=300
    delay=10
        
    for i in range(len(leonInput)):
        s= leonInput[i]
        print(s)
        output_field.insert(f"{i+1.0}",s)

        output_field.pack(expand=True, fill="both")# it's just a widget or compnonet inside the frame so no need to loop here!
        time.sleep(0.01)# i have to print to next line of the last possition!!

        new_screen.update()
        



    # we need a transparent message screnn.
    new_screen.mainloop()
    

#2. when clicked on ada or for now in a button on ada's main screen, this open up a new widget, and it closes as soon as "send" button clicked!
def prompt_input():
    new_screen = Tk()
    new_screen.title("Leon input screen ")
    new_screen.geometry("400x200")

    input_field = ScrolledText(new_screen,height=4, width=30)
    input_field.pack()# it's just a widget or compnonet inside the frame so no need to loop here!

    Button(new_screen, text="Send", command=lambda: gemma_ko_bhejo(new_screen,input_field)).pack()
    new_screen.mainloop()
    pass




#1. main screen which will be on top alwaye, use "toplevel" 
Ada = Tk()
Ada.geometry("200x100")
Ada.title("Ada main screen")
Button(Ada, text="Message", command=prompt_input).pack()
Ada.mainloop()
