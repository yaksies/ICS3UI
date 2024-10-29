from tkinter import*
from random import choice

screen = Canvas(Tk(), width=800, height=800, background="black" )
screen.pack()

colors = ["red", "blue", "green", "pink", "orange", "yellow", "white", "grey", "magenta", "maroon", "lawngreen", "hotpink", "skyblue", "purple", "black", "beige"]

x1 = int(input("Enter the x coordinate of the left corner: "))

x2 = int(input("Enter the x coordinate of the middle corner: "))
while x2 < x1:
    print("Your x2 value may not be greater than the value of x1. Please try again. ")
    x2 = int(input("Enter the x coordinate of the middle corner: "))

x3 = int(input("Enter the x coordinate of the right corner: "))
while x3 < x2:
    print("Your x2 value may not be greater than the value of x1. Please try again. ")
    x3 = int(input("Enter the x coordinate of the right corner: "))

y1 = int(input("Enter the y coordinate of the left corner: "))

y2 = int(input("Enter the y coordinate of the middle corner: "))

y3 = int(input("Enter the y coordinate of the right corner: "))

screen.create_polygon( x1, y1, x2, y2, x3, y3, outline="white", width=4)

m = (y2 - y1) / (x2 - x1)
m2 = (y3 - y2) / (x3 - x2)
m3 = (y3 - y1) / (x3 - x1)

b = y1 - m * x1
b2 = y2 - m2 * x2
b3 = y3 - m3 * x3

while not x1 == x2:
    screen.create_line(x1, m * x1 + b, x1, m3 * x1 + b3, width = 2, fill = choice(colors))
    x1 += 2

while not x2 == x3:
    screen.create_line(x2, m2 * x2 + b2, x2, m3 * x2 + b3, width = 2, fill = choice(colors))
    x2 += 2

screen.mainloop()
