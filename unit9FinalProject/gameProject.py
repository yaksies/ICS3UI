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

    # How to Play
    screen.create_rectangle(10, 650, 50, 690, fill = "yellow")
    screen.create_text(30, 670, text = "?", font = "Impact 20", fill = "black")

    root.bind("<Button-1>", startScreenClick)

def delStartScreen():
    screen.delete("all")
     

def startScreenClick(event):
    global platformLength, xBallSpeed, platformSpeed
    
    xMouse = event.x
    yMouse = event.y

    # -- DIFFICULTY BUTTONS -- #

    # Easy
    if xMouse > 600 and xMouse < 900 and yMouse > 200 and yMouse < 300:
        platformLength = 150
        platformSpeed = 40
        xBallSpeed = []
        for i in range(0, 1000):
            xBallSpeed.append(uniform(10, 30))
        delStartScreen()
        runGame()

    # Medium
    elif xMouse > 600 and xMouse < 900 and yMouse > 350 and yMouse < 450:
        platformLength = 120
        platformSpeed = 35
        xBallSpeed = []
        for i in range(0, 1000):
            xBallSpeed.append(uniform(20, 40))
        delStartScreen()
        runGame()

    # Hard
    elif xMouse > 600 and xMouse < 900 and yMouse > 500 and yMouse < 600:
        platformLength = 90
        platformSpeed = 30
        xBallSpeed = []
        for i in range(0, 1000):
            xBallSpeed.append(uniform(30, 50))
        delStartScreen()
        runGame()
    elif xMouse > 10 and xMouse < 50 and yMouse > 650 and yMouse < 690:
        delStartScreen()

        for i in range(0, 1000):
            xStar = randint(0, 1000)
            yStar = randint(0, 700)
            screen.create_oval(xStar - 1, yStar - 1, xStar + 1, yStar + 1, fill = "white")

        screen.create_rectangle(100, 50, 900, 150, fill = "yellow")
        screen.create_text(500, 100, text = "Space Ball Instructions", font = "Impact 50", fill = "black")

        screen.create_rectangle(100, 200, 900, 500, fill = "yellow")
        screen.create_text(500, 350, text = "The goal of the game is to keep the ball from falling off the platform. \nYou can move the platform left and right by using the right and left arrow keys.\nEasy is slow, Medium is medium, and Hard is fast. \nGood luck!", font = "Impact 20", fill = "black")

        screen.create_rectangle(10, 650, 50, 690, fill = "yellow")
        screen.create_text(30, 670, text = "<-", font = "Impact 20", fill = "black")
        
        root.bind("<Button-1>", helpClick)

def helpClick(event):
    xMouse = event.x
    yMouse = event.y

    if xMouse > 10 and xMouse < 50 and yMouse > 650 and yMouse < 690:
        screen.delete("all")
        startScreen()


#THE JOB OF THIS PROCEDURE IS TO CREATE ALL THE VARIABLES THE GAME WILL NEED
#AND GIVE THEM STARTING VALUES
def setInitialValues():
    #List global variables
    global xPlatform, yPlatform, platformHeight
    global score
    global yBallSpeed, xBall, yBall, ballRadius
	
    #Platform Values
    xPlatform = 500
    yPlatform = 600
    platformHeight = 10
    
    #Ball Values
    xBall = 500
    yBall = 580
    ballRadius = 10
    yBallSpeed = 0

    #Game Values
    score = 0

    #Drawing the background
    for i in range(0, 1000):
        xStar = randint(0, 1000)
        yStar = randint(0, 700)
        screen.create_oval(xStar - 1, yStar - 1, xStar + 1, yStar + 1, fill = "white")


def drawObjects():
    global xPlatform, yPlatform, platformHeight, platformLength, platform
    global xBallSpeed, yBallSpeed, xBall, yBall, ballRadius, ball
    
    ball = screen.create_rectangle(xPlatform - platformLength, yPlatform - platformHeight, xPlatform + platformLength, yPlatform + platformHeight, fill = "green")
    platform = screen.create_oval(xBall - ballRadius, yBall - ballRadius, xBall + ballRadius, yBall + ballRadius, fill = "yellow")

def drawStats():
	global livesDisplay, scoreDisplay

   
#THIS PROCEDURE GETS CALLED EVERY TIME THE USER PRESSES A KEY
def keyDownHandler( event ):
    global xPlatform, platformSpeed

    if event.keysym == "Right":
        xPlatform = xPlatform + platformSpeed
    elif event.keysym == "Left":
        xPlatform = xPlatform - platformSpeed

#THIS PROCEDURE GETS CALLED EVERY TIME THE USER LETS GO OF A KEY
def keyUpHandler( event ):
    pass


#UPDATES THE POSITIONS AND SPEEDS OF ALL OBJECTS IN THE CURRENT FRAME OF THE ANIMATION
def updateObjectPositions():
    global xBall, yBall, xBallSpeed, yBallSpeed, ballRadius, ball
    global xPlatform, yPlatform, platformSpeed, platformHeight

    ball = screen.create_rectangle(xPlatform - platformLength, yPlatform - platformHeight, xPlatform + platformLength, yPlatform + platformHeight, fill = "green")
    platform = screen.create_oval(xBall - ballRadius, yBall - ballRadius, xBall + ballRadius, yBall + ballRadius, fill = "yellow")
	  


#THIS IS THE MAIN PROCEDURE THAT RUNS THE GAME. IT GETS CALLED ONCE WHEN THE PROGRAM STARTS  
def runGame():
    global ball, platform

    #Creates all the variables the program will need, and gives them starting values
    setInitialValues()

    #Keeps the game running for as long as the character is still alive
    while True: #or some other condition 
        drawObjects()
        drawStats()
        #updateObjects() 
        
        screen.update()
        sleep(0.001)
        screen.delete( ball, platform ) #Or only the characters

    #WHEN THE WHILE-LOOP ABOVE STOPS, THE GAME ENDS
    gameOverMessage()
    askToRestart()

#THESE 5 COMMANDS WILL BE NEW TO YOU. ALL GAMES MUST INCLUDE THEM.

root.after( 500, startScreen) #makes the program call the runGame() procedure 500 milliseconds after the program starts

screen.bind("<Key>", keyDownHandler) # Makes the program call the keyDownHandle() function whenever the user presses a key

screen.bind("<KeyRelease>", keyUpHandler) # Calls the function keyUpHandler() when the user releases a key

screen.pack() #sets up the drawing screen (same as in any Tkinter program)

screen.focus_set() #makes Python pay attention to mouse clicks and button pushes
 
screen.mainloop()