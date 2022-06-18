from tkinter import *
import time
import random

WIDTH = 1000
HEIGHT = 600
xVelocity = 3
yVelocity = 2

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="Black")
canvas.pack()
dvd1_image = PhotoImage(file='.\\images\\dvd1.png')
dvd2_image = PhotoImage(file='.\\images\\dvd2.png')
dvd3_image = PhotoImage(file='.\\images\\dvd3.png')
dvd4_image = PhotoImage(file='.\\images\\dvd4.png')
dvd5_image = PhotoImage(file='.\\images\\dvd5.png')
dvd6_image = PhotoImage(file='.\\images\\dvd6.png')
dvd7_image = PhotoImage(file='.\\images\\dvd7.png')
images = [dvd1_image,dvd2_image,dvd3_image,dvd4_image,dvd5_image,dvd6_image,dvd7_image]
dvd1 = canvas.create_image(random.randint(0,800),random.randint(0,200), image=dvd1_image, anchor=NW)
i= 0

while i <= len(images) - 1:
    image_width = images[i].width()
    image_height = images[i].height()

    coordinates = canvas.coords(dvd1)
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity
        canvas.delete(dvd1)
        dvd1 = canvas.create_image(coordinates[0], coordinates[1], image=images[i], anchor=NW)
        i += 1
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity
        canvas.delete(dvd1)
        dvd1 = canvas.create_image(coordinates[0], coordinates[1], image=images[i], anchor=NW)
        i += 1
    canvas.move(dvd1, xVelocity, yVelocity)
    if i == len(images) - 1:
        i = 0
    window.update()
    time.sleep(0.0001)

window.mainloop()
