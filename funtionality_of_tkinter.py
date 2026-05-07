from tkinter import *
from tkinter import font
#4. style the output produced by gemma which is in text form(string) take it and change fonts, animate, colors etc RGB-kind of gaems feel if possible use resident evil stle!
def style():
    styled_font = font.Font(family="Arial", size=30, weight="bold")
    return styled_font
    pass

#3. it procceses the data and display it in a new screen use "Message" it shoulb be transpaent in look wise!
def gemma_ko_bhejo():
    # it should create the messagee screen !
    # output = process__leon_input()
    output = "Done"
    # output = style(ouput)# we have to create this style method
    styled_font = style()
    new_screen = Tk()
    new_screen.title("Message screen means Ada response")
    message_screen = Message(new_screen,text=output,font = styled_font,width=300,fg="red")
    message_screen.pack()
    # we need a transparent message screnn.
    # message_screen.mainloop()
    pass

#2. when clicked on ada or for now in a button on ada's main screen, this open up a new widget, and it closes as soon as "send" button clicked!
def prompt_input():
    new_screen = Tk()
    new_screen.title("Leon input screen ")
    input_field = Text(new_screen)
    input_field.pack()
    Button(new_screen, text="Send", command=gemma_ko_bhejo).pack()
    input_field.mainloop()
    input_field.close()
    pass

#1. main screen which will be on top alwaye, use "toplevel" 
Ada = Tk()
Ada.title("Ada main screen")
Button(Ada, text="Ada", command=prompt_input).pack()
Ada.mainloop()
