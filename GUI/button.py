from os import system
from tkinter import *

count = 0

def click():
    system('cls')
    global count
    count += 1
    print(count)

window = Tk()
photo = PhotoImage(file='.\\images\\logo.png')
button = Button(window,
            text="Click Here",
            command=click,
            font=('Somic Sans', 30),
            fg='#000000',
            bg='#a30707',
            activebackground='#a30707',
            activeforeground='#000000',
            state=ACTIVE,
            image=photo,
            compound='bottom')
button.pack()
window.mainloop()
