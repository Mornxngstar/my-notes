from tkinter import *

movement = 10

def move_up(event):
    if event.keysym == 'w' and event.keysym == 'a':
        label.place(x=label.winfo_x() - movement, y=label.winfo_y() - movement)
    elif event.keysym == 'w' and  event.keysym == 'd':
        label.place(x=label.winfo_x() + movement, y=label.winfo_y() - movement)
    elif event.keysym == 's' and  event.keysym == 'a':
        label.place(x=label.winfo_x() - movement, y=label.winfo_y() + movement)
    elif event.keysym == 's' and  event.keysym == 'd':
        label.place(x=label.winfo_x() + movement, y=label.winfo_y() + movement)
    elif event.keysym == 'w':
        label.place(x=label.winfo_x(), y=label.winfo_y() - movement)
    elif event.keysym == 'a':
        label.place(x=label.winfo_x() - movement, y=label.winfo_y())
    elif event.keysym == 's':
        label.place(x=label.winfo_x(), y=label.winfo_y() + movement)
    elif event.keysym == 'd':
        label.place(x=label.winfo_x() + movement, y=label.winfo_y())

window = Tk()
window.geometry("500x500")
window.bind("<Key>", move_up)
my_image = PhotoImage(file='.\\images\\logo.png')
label = Label(window, image=my_image, width=75, height=75)
label.place(x=250,y=250)

window.mainloop()
