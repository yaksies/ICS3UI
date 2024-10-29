from tkinter import*
from random import randint, choice
from time import sleep

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

#x1, x2, x3, y1, y2, y3 = 200, 400, 600, 500, 200, 500 # testing purposes only

screen.create_polygon( x1, y1, x2, y2, x3, y3, outline="white", width=4)

#RIGHT HALF       
for _ in range(1000):
    x = randint(x2, x3)
    y = randint(min(y2, y3), max(y2, y3))

    m = (y3 - y2) / (x3 - x2)

    b = y3 - m*x3
    #print(m1)
   
    yLine = m*x + b
    for i in range(1000):
        xa = randint(x1, x3)
        ya = randint(min(y1, y3), max(y1, y3))

        ma = (y3 - y1) / (x3 - x1)

        b = y3 - ma * x3

        yLine1 = ma*xa + b
        
        if ya > yLine1 and y > yLine and x == xa:
            screen.create_line(x, yLine, xa, yLine1, width = 2, fill = choice(colors))

#LEFT HALF
for _ in range(1000):
    x = randint(x1, x2)
    y = randint(min(y1, y2), max(y1, y2))

    m = (y1 - y2) / (x1 - x2)

    b = y1 - m*x1
    #print(m1)
   
    yLine = m*x + b

    for i in range(1000):
        xa = randint(x1, x3)
        ya = randint(min(y1, y3), max(y1, y3))

        ma = (y3 - y1) / (x3 - x1)

        yLine1 = ma*xa + b
        
        if ya > yLine1 and y > yLine and x == xa:
            screen.create_line(x, yLine, xa, yLine1, width = 2, fill = choice(colors))

screen.mainloop()
