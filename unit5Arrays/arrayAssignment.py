from tkinter import *
from random import randint

screen = Canvas(Tk(), height=600, width=900, background="darkslategray")
screen.pack()

# Creating the ground
screen.create_rectangle(0, 580, 900, 600, fill="black")

# Making the stars in the background
for i in range(300):
    x = randint(0, 900)
    y = randint(0, 200)
    screen.create_oval(x - 2, y - 2, x + 2, y + 2, fill="white")

# Randomly generating buildings

for i in range(10):
    bSizeX = randint(100, 150)
    bSizeY = randint(200, 250)

    x = randint(-90, 780)
    y = 580

    screen.create_rectangle(x, y, x + bSizeX, y - bSizeY, fill="darkgray")

screen.mainloop()
