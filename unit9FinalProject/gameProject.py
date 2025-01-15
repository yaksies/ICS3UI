from tkinter import *
from time import *
from random import *

root = Tk()

screen = Canvas(root, width=1000, height=700, background="black")

# ********** START SCREEN ********** #

def startScreen():
    for i in range(0, 1000):
        xStar = randint(0, 1000)
        yStar = randint(0, 700)
        screen.create_oval(xStar - 1, yStar - 1, xStar + 1, yStar + 1, fill = "white")
    
    # -- Create the ball and the rectangle for the intro screen -- #
    screen.create_rectangle(100, 440, 400, 460, fill = "green")
    screen.create_oval(230, 400, 270, 440, fill = "yellow")

    # -- Create the text for the intro screen -- #

    # Title of the Game
    screen.create_rectangle(100, 50, 900, 150, fill = "yellow")
    screen.create_text(500, 100, text = "Space Ball", font = "Impact 50", fill = "black")

    # Difficulties
    screen.create_rectangle(600, 200, 900, 300, fill = "yellow")
    screen.create_text(750, 250, text = "Easy", font = "Impact 40", fill = "black")

    screen.create_rectangle(600, 350, 900, 450, fill = "yellow")
    screen.create_text(750, 400, text = "Medium", font = "Impact 40", fill = "black")

    screen.create_rectangle(600, 500, 900, 600, fill = "yellow")
    screen.create_text(750, 550, text = "Hard", font = "Impact 40", fill = "black")


#THE JOB OF THIS PROCEDURE IS TO CREATE ALL THE VARIABLES THE GAME WILL NEED
#AND GIVE THEM STARTING VALUES
def setInitialValues():
    #List global variables
    global xPlatform, yPlatform, platformSpeed, platformLength, platformHeight
    global score
    global xBallSpeed, yBallSpeed, xBall, yBall, ballRadius
	
    #Platform Values
    xPlatform = 500
    platformLength = 150
    yPlatform = 600
    platformHeight = 10
    platformSpeed = 0
    
    #Ball Values
    xBall = 500
    yBall = 580
    ballRadius = 10
    xBallSpeed = []
    yBallSpeed = 0

    for i in range(0, 100):
        xBallSpeed.append(uniform(20, 40))

    #Game Values
    score = 0


def drawObjects():
    global xPlatform, yPlatform, platformHeight, platformLength
    global xBallSpeed, yBallSpeed, xBall, yBall, ballRadius

    for i in range(0, 1000):
        xStar = randint(0, 1000)
        yStar = randint(0, 700)
        screen.create_oval(xStar - 1, yStar - 1, xStar + 1, yStar + 1, fill = "white")

    
    ball = screen.create_rectangle(xPlatform - platformLength, yPlatform - platformHeight, xPlatform + platformLength, yPlatform + platformHeight, fill = "green")
    platform = screen.create_oval(xBall - ballRadius, yBall - ballRadius, xBall + ballRadius, yBall + ballRadius, fill = "yellow")

def drawStats():
	global livesDisplay, scoreDisplay
	
	
#THIS PROCEDURE GETS CALLED EVERY TIME THE USER CLICKS THE MOUSE...AND ONLY WHEN THEY CLICK THE MOUSE
def mouseClickHandler( event ):
    global xMouse, yMouse
    
 
#THIS PROCEDURE GETS CALLED EVERY TIME THE USER LETS GO OF THE MOUSE.
#THIS IS WHAT MAKES THE ROCKET FLAME DISAPPEAR AFTER EACH MOUSE CLICK
def mouseReleaseHandler( event ):
	global xMouse, yMouse

   
#THIS PROCEDURE GETS CALLED EVERY TIME THE USER PRESSES A KEY
def keyDownHandler( event ):
    pass

#THIS PROCEDURE GETS CALLED EVERY TIME THE USER LETS GO OF A KEY
def keyUpHandler( event ):
    pass


#UPDATES THE POSITIONS AND SPEEDS OF ALL OBJECTS IN THE CURRENT FRAME OF THE ANIMATION
def updateObjectPositions():
	global xBall, yBall, xBallSpeed, yBallSpeed
	  


#THIS IS THE MAIN PROCEDURE THAT RUNS THE GAME. IT GETS CALLED ONCE WHEN THE PROGRAM STARTS  
def runGame():

    #Creates all the variables the program will need, and gives them starting values
    setInitialValues()

    #Keeps the game running for as long as the character is still alive
    while True: #or some other condition 
        drawObjects()
        drawStats()
        #updateObjects() 
        
        screen.update()
        sleep(0.03)
        screen.delete( ball, platform ) #Or only the characters

    #WHEN THE WHILE-LOOP ABOVE STOPS, THE GAME ENDS
    gameOverMessage()
    askToRestart()

#THESE 5 COMMANDS WILL BE NEW TO YOU. ALL GAMES MUST INCLUDE THEM.

root.after( 500, startScreen) #makes the program call the runGame() procedure 500 milliseconds after the program starts

screen.bind("<Button-1>", mouseClickHandler) #makes the program call the procedure mouseClickHandler() every time the user clicks the left mouse button (what Python called "Button-1")

screen.bind("<ButtonRelease-1>", mouseReleaseHandler) #makes the program call the procedure mouseReleaseHandler() every time the user lets go of the mouse

screen.bind("<Key>", keyDownHandler) # Makes the program call the keyDownHandle() function whenever the user presses a key

screen.bind("<KeyRelease>", keyUpHandler) # Calls the function keyUpHandler() when the user releases a key

screen.pack() #sets up the drawing screen (same as in any Tkinter program)

screen.focus_set() #makes Python pay attention to mouse clicks and button pushes
 
screen.mainloop()