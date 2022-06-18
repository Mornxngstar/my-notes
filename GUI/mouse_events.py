from tkinter import *

def do_something(event):
    print(str(event.x) + "," + str(event.y) + ". " + str(event.num))
    print(event)

window = Tk()

# window.bind("<Button-1>", do_something)
# window.bind("<Button-2>", do_something)
# window.bind("<Button-3>", do_something)
# window.bind("<ButtonRelease>", do_something)
# window.bind("<Enter>", do_something)
# window.bind("<Leave>", do_something)
# window.bind("<Motion>", do_something)
window.bind("<B1-Motion>", do_something)



window.mainloop()
