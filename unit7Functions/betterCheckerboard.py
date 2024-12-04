from tkinter import *
screen= Canvas(Tk(), height = 600, width = 800, background = "black")
screen.pack()


def evenOrOddSquare( row, col ):   #Here's a function.
  if (row+col) % 2 == 0:
    return "EVEN"
  else:
    return "ODD"


def drawCheckerboard( lightColour, darkColour, size, xStart, yStart , rows, cols):   #Here's a procedure...
  for row in range (rows):
    y = yStart + row * size

    for col in range(cols):
        x = xStart + col * size

        thisSquare = evenOrOddSquare( row, col )     #...that includes a function-call!

        if thisSquare == "EVEN":
            c = lightColour
 
        else:
            c = darkColour

        screen.create_rectangle( x, y, x+size, y+size, fill = c)

#Function-calls
drawCheckerboard("red", "grey70", 50, 0, 0, 10, 10)
drawCheckerboard("cyan", "blanched almond", 30, 235, 390, 8, 8)
drawCheckerboard("green", "yellow", 20, 400, 500, 8, 8)

screen.mainloop()
