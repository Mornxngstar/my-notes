from tkinter import *

window = Tk()
window.title('Tengo el')
photo = PhotoImage(file='.\\images\\logo.png')
icon = PhotoImage(file='.\\images\\icon.png')
window.iconphoto(True,icon)
label = Label(window,
            text="Hello World",
            font=('Arial', 40, 'bold'),
            fg="#ffffff",
            bg="#000000",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=photo,
            compound='bottom')
            
label.pack()
# label.place(x=0,y=0)

window.mainloop()
