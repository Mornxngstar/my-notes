from tkinter import *

def do_something(event):
    label.config(text=event.keysym)
    print(event)

window = Tk()

window.bind('<Key>', do_something)
label = Label(window, font=('Constantia',25))
label.pack()

window.mainloop()
