# Source - https://stackoverflow.com/a/43008165
# Posted by Skarga, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-08, License - CC BY-SA 3.0

from tkinter import *
root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

textBox=Text(root, height=2, width=10)
textBox.pack()
inputValue=textBox.get("1.0","end-1c")
print(inputValue)
# Button(root, height=1, width=10, text="Commit", 
#                     command=retrieve_input).pack()
#command=lambda: retrieve_input() >>> just means do this when i press the button


mainloop()
