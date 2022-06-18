from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()
scale = Scale(window,from_=200,to=150, length=500, orient=VERTICAL, font=('Consolas',15),tickinterval=10,showvalue=0,
                troughcolor='#69EAFF',fg='#FF1C00',bg='#111111')
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()
button = Button(window, text='Submit', command=submit)
button.pack()
window.mainloop()
