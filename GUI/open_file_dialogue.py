from tkinter import *
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfilename(initialdir='C:\\Users\\Josue\\Downloads',
                                        title='Opening file . . .',
                                        filetypes=(('text files','*.txt'),
                                        ('all files','*.*'))
                                        )
    f = open(file, 'r')
    print(f.read())
    f.close()
    

window = Tk()
button = Button(window, text='Open', command=open_file)
button.pack()
window.mainloop()