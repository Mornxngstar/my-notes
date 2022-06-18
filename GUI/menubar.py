from os import system
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file = filedialog.askopenfilename(initialdir='C:\\Users\\Josue\\Downloads',
                                        title='Opening file . . .',
                                        filetypes=(('text files','*.txt'),
                                        ('all files','*.*'))
                                        )
    f = open(file, 'r')
    print(f.read())
    f.close()

def save_file():
    file_path = filedialog.asksaveasfile(initialdir='C:\\Users\\Josue\\Documents\\Programming\\Back-End\\GUI',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All files', '.*')
                                    ])
    if file_path is None:
        return

    file_text = str(text.get(1.0, END))
    file_path.write(file_text)
    file_path.close()


def exit_program():
    answer = messagebox.askokcancel(title='Exit', message='Do you want to exit?')

    if answer is True:
        exit()
    else:
        return

window = Tk()
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
text = Text(window)
text.pack()
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exit_program)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Paste')



window.mainloop()
