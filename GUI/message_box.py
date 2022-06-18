from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is a message', message='You are a person.')

    # while True:
    #     messagebox.showwarning(title='WARNING', message='YOU HAVE A VIRUS!!!!')

    # messagebox.showerror(title='ERROR', message='Something has gone wrong.')

    # if messagebox.askokcancel(title='Question', message='Would you?'):
    #     print('You would.')
    # else:
    #     print("You wouldn't.")

    # if messagebox.askretrycancel(title='Question', message='Would you retry?'):
    #     print('You would retry.')
    # else:
    #     print("You wouldn't retry.")

    # if messagebox.askyesno(title='Question', message='Would you?'):
    #     print('You would.')
    # else:
    #     print("You wouldn't.")

    # answer = messagebox.askquestion(title='Question', message='Would you or not?')

    # if answer == "yes":
    #     print("Good")
    # else:
    #     print("Damn")

    answer = messagebox.askyesnocancel(title='Question', message='Do you like to code?')

    if answer is True:
        print("So do I.")
    elif answer is False:
        print("Why not?")
    else:                      # If 'Cancel' is clicked, the message box will return 'None'
        print("Goodbye.")
        

window = Tk()

button = Button(window, text='Click Here', command=click)
button.pack()

window.mainloop()
