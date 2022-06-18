
from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("My very first window")
icon = PhotoImage(file='.\\images\\icon.png')
window.iconphoto(True,icon)

window.config(background="#000000")

window.mainloop()
