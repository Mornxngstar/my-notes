from tkinter import *

def submit():
    input_ = text.get('1.0', END)
    print(input_)


window = Tk()
window.config(bg='Black')
text = Text(window,
            bg='Black',
            fg='White',
            font=('Constantia', 15),
            height=8,
            width=20,
            padx=10,
            pady=10)
button = Button(window, text="Click Here", command=submit, bg='Black',fg='White')
text.pack()
button.pack()

window.mainloop()
