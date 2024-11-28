from tkinter import *
from random import randint, choice

screen = Canvas(Tk(), width=800, height=600, background="black")
screen.pack()

colours = [
    "white",
    "red",
    "blue",
    "skyblue",
    "turquoise",
    "lightgrey",
    "green",
    "lawngreen",
]


def createPerson(x, y, col):
    screen.create_oval(x - 5, y - 5, x + 5, y + 5, outline=col)
    screen.create_line(x, y + 5, x, y + 25, fill=col)
    screen.create_line(x, y + 5, x - 10, y + 20, fill=col)
    screen.create_line(x, y + 5, x + 10, y + 20, fill=col)
    screen.create_line(x, y + 25, x - 10, y + 40, fill=col)
    screen.create_line(x, y + 25, x + 10, y + 40, fill=col)


for i in range(200):
    createPerson(randint(0, 800), randint(0, 600), choice(colours))


screen.mainloop()
