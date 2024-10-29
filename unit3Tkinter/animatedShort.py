'''
                ICS3UI ANIMATED SHORT

Background scenery must be detailed and diverse - /5 Points

        Must Contain Linear Motion - /5 Points
      Must Contain Non-linear motion - /5 Points

Must move object made up of more than 1 shape - /5 Points

  Must have multiple phases (2 or more loops) - /5 Points

     Must be creative and entertaining - /5 Points
'''


from tkinter import *
from time import sleep
from random import *
from math import sin, cos

screen = Canvas(Tk(), height = 600, width = 800, background = "skyblue")
screen.pack()

#Make the grass
screen.create_rectangle(0, 580, 800, 600, fill = "lawngreen")

#Make clouds
x = 50
x2 = 120

xc2 = 600
x2c2 = 670

xc3 = 300
x2c3 = 400

#Make the basket of the hot air balloon
xBasket = 100
xBasket2 = 200
yBasket = 520
yBasket2  = 580

for _ in range(10_000):
    #Cloud 1
    cloud1 = screen.create_oval(x, 100, x2, 160, fill="white", outline="white")
    cloud2 = screen.create_oval(x + 30, 80, x2 + 30, 140, fill="white", outline="white")
    cloud3 = screen.create_oval(x + 70, 90, x2 + 70, 150, fill="white", outline="white")
    cloud4 = screen.create_oval(x + 110, 100, x2 + 110, 160, fill="white", outline="white")
    
    #Cloud 2
    cloud5 = screen.create_oval(xc2, 60, x2c2, 120, fill="white", outline="white")
    cloud6 = screen.create_oval(xc2 + 30, 40, x2c2 + 110, 90, fill="white", outline="white")
    cloud7 = screen.create_oval(xc2 + 80, 50, x2c2 + 150, 110, fill="white", outline="white")
    cloud8 = screen.create_oval(xc2 + 110, 70, x2c2 + 180, 140, fill="white", outline="white")
    
    #Cloud 3
    cloud9 = screen.create_oval(xc3, 100, x2c3, 170, fill="white", outline="white")
    cloud10 = screen.create_oval(xc3 + 20, 130, x2c3 - 10, 190, fill="white", outline="white")
    cloud11 = screen.create_oval(xc3 + 50, 100, x2c3 + 30, 160, fill="white", outline="white")
    cloud12 = screen.create_oval(xc3 + 110, 110, x2c3 + 80, 170, fill="white", outline="white")
            
    x += 2
    x2 += 2
    
    xc2 += 1
    x2c2 += 1
    
    xc3 += 3
    x2c3 += 3
    
    #Draw the hot air balloon
    screen.create_rectangle(xBasket, yBasket, xBasket2, yBasket2, fill = "brown", outline = "saddlebrown", width = 5)
    screen.create_line(xBasket - 20, yBasket - 100, xBasket, yBasket, width = 3, fill = "black")
    screen.create_line(xBasket2 + 20, yBasket - 100, xBasket2, yBasket, width = 3, fill = "black")
    screen.create_oval(xBasket - 30, yBasket - 300, xBasket2 + 30, yBasket - 100, fill = "red", outline = "darkred", width = 3)

    screen.update()
    sleep(0.02)
    screen.delete(cloud1, cloud2, cloud3, cloud4, cloud5, cloud6, cloud7, cloud8, cloud9, cloud10, cloud11, cloud12)

screen.mainloop()
