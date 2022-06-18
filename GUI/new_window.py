from tkinter import *

def new_window():
    new_window = Tk()   # Creates a new and independent window
    old_window.destroy()

    # new_window = Toplevel()   # Creates a new window of top level making the old_window be a bottom level,
                                # this way, if the bottom window is closed out, the top level will do too

old_window = Tk()

Button(old_window, text='Click here', command=new_window).pack()

old_window.mainloop()
