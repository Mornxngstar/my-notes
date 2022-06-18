from tkinter import *

def dislpay():
    if x.get() == 1:
        print("You agree.")
    else:
        print("You don't agree")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
            text='I agree',
            variable=x,
            onvalue=1,
            offvalue=0,
            command=dislpay)
check_button.pack()

window.mainloop()
