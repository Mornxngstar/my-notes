from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 600
    current_task = 0
    speed = 3
    while current_task < tasks: 
        time.sleep(0.025)
        bar['value'] += ((speed/tasks) * 100)
        current_task += 3
        percent.set(str(int((current_task / tasks) * 100))+ '%')
        if current_task >= tasks:
            progress.set("Completed!")
        else:
            progress.set(str(current_task) + "/" + str(tasks) + " tasks completed.")
        window.update_idletasks()

window = Tk()

percent = StringVar()
progress = StringVar()

bar = Progressbar(window, length=300, orient=HORIZONTAL)
bar.pack(padx=20,pady=20)
percent_label = Label(window, textvariable=percent).pack()
progress_label = Label(window, textvariable=progress).pack()
Button(window,text='Download', command=start).pack(pady=10)

window.mainloop()
