from tkinter import *

classes = ["Wizard","Warrior","Archer"]

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    
    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

window =Tk()

listbox = Listbox(window,
                    bg='Black',
                    fg='White',
                    font=('Constantia', 15),
                    activestyle='underline',
                    width=12,
                    selectbackground='Black',
                    selectmode=MULTIPLE)

for i in range(len(classes)):
    listbox.insert(i, classes[i])

listbox.config(height=listbox.size())

submit_button = Button(window, text='Submit', command=submit)
add_button = Button(window, text='Add', command=add)
delete_button = Button(window, text='Delete', command=delete)
entrybox = Entry(window)

listbox.pack()
entrybox.pack()
submit_button.pack()
add_button.pack()
delete_button.pack()

window.mainloop()


