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

def delScreen():
    screen.delete("all")    

def startScreenClick(event):
    global platformLength, xBallSpeed, platformSpeed
    global difficulty
    
    xMouse = event.x
    yMouse = event.y

    # -- DIFFICULTY BUTTONS -- #

    # Easy
    if xMouse > 600 and xMouse < 900 and yMouse > 200 and yMouse < 300:
        platformLength = 150
        platformSpeed = 20
        difficulty = "Easy"
        xBallSpeed = 10
        delScreen()
        runGame()

    # Medium
    elif xMouse > 600 and xMouse < 900 and yMouse > 350 and yMouse < 450:
        platformLength = 120
        platformSpeed = 17
        difficulty =  "Medium"
        xBallSpeed = 13
        delScreen()
        runGame()

    # Hard
    elif xMouse > 600 and xMouse < 900 and yMouse > 500 and yMouse < 600:
        platformLength = 90
        platformSpeed = 14
        difficulty = "Hard"
        xBallSpeed = 16
        delScreen()
        runGame()

    # -- HOW TO PLAY BUTTON -- #
        
    elif xMouse > 10 and xMouse < 50 and yMouse > 650 and yMouse < 690:
        delStartScreen()

        for i in range(0, 1000):
            xStar = randint(0, 1000)
            yStar = randint(0, 700)
            screen.create_oval(xStar - 1, yStar - 1, xStar + 1, yStar + 1, fill = "white")

        screen.create_rectangle(50, 50, 950, 150, fill = "yellow")
        screen.create_text(500, 100, text = "Space Ball Instructions", font = "Impact 50", fill = "black")

        screen.create_rectangle(50, 200, 950, 500, fill = "yellow")
        screen.create_text(500, 250, text = "The goal of the game is to keep the ball from falling off the platform.", font = "Impact 20", fill = "black")
        screen.create_text(500, 300, text = "Use the left and right arrow keys to keep the ball on the platform.", font = "Impact 20", fill = "black")
        screen.create_text(500, 400, text = "Good Luck!", font = "Impact 30", fill = "black")

        screen.create_rectangle(10, 650, 50, 690, fill = "yellow")
        screen.create_text(30, 670, text = "<-", font = "Impact 20", fill = "black")
        
        root.bind("<Button-1>", helpClick)

def helpClick(event):
    xMouse = event.x
    yMouse = event.y

    if xMouse > 10 and xMouse < 50 and yMouse > 650 and yMouse < 690:
        delScreen()
        startScreen()

# ********** INITIALIZING VALUES ********** #

def setInitialValues():
    #List global variables
    global xPlatform, yPlatform, platformHeight, moveLeft, moveRight
    global score, lost, won
    global yBallSpeed, xBall, yBall, ballRadius, gravity, ballMovement, upSpeedAfterImpact, xStart, yStart
	
    #Platform Values
    xPlatform = 500
    yPlatform = 600
    platformHeight = 10
    moveLeft = False
    moveRight = False
    
    #Ball Values
    xBall = 500
    yBall = 500
    ballRadius = 10
    yBallSpeed = -25  # Increase the initial vertical speed for a higher parabola
    gravity = 1
    ballMovement = []
    for i in range(1000):
        ballMovement.append(randint(0, 1))

    #Game Values
    score = 0
    lost = False
    won = False

    #Drawing the background
    for i in range(0, 1000):
        xStar = randint(0, 1000)
        yStar = randint(0, 700)
        screen.create_oval(xStar - 1, yStar - 1, xStar + 1, yStar + 1, fill = "white")

# ********** DRAWING AND UPDATING OBJECTS (including stats) ********** #

def drawObjects():
    global xPlatform, yPlatform, platformHeight, platformLength, platform
    global xBallSpeed, yBallSpeed, xBall, yBall, ballRadius, ball
    
    ball = screen.create_rectangle(xPlatform - platformLength, yPlatform - platformHeight, xPlatform + platformLength, yPlatform + platformHeight, fill = "green")
    platform = screen.create_oval(xBall - ballRadius, yBall - ballRadius, xBall + ballRadius, yBall + ballRadius, fill = "yellow")

def drawStats():
    global score, scoreDisp
    scoreDisp = screen.create_text(50, 20, text=f"Score: {score}", font="Impact 20", fill="white")

def updateObjects():
    global xBall, yBall, xBallSpeed, yBallSpeed, ballRadius, ball, timesRun, gravity
    global score
    global xPlatform, yPlatform, platformSpeed, platformHeight, platform

    if moveRight:
        xPlatform += platformSpeed
    if moveLeft:
        xPlatform -= platformSpeed

    moveBall()

    platform = screen.create_rectangle(xPlatform - platformLength, yPlatform - platformHeight, xPlatform + platformLength, yPlatform + platformHeight, fill = "green")
    ball = screen.create_oval(xBall - ballRadius, yBall - ballRadius, xBall + ballRadius, yBall + ballRadius, fill = "yellow")


def moveBall():
    global xBall, yBall, xBallSpeed, yBallSpeed, yPlatform, gravity
    global ballRadius, platformLength, lost, won, score

    # Update horizontal position
    xBall += xBallSpeed

    # Update vertical position with gravity
    yBallSpeed += gravity
    yBall += yBallSpeed

    # Bounce off the platform
    if yBall + ballRadius >= yPlatform and xBall >= xPlatform - platformLength and xBall <= xPlatform + platformLength:
        yBallSpeed = -25  # Reset the vertical speed to its initial value
        platformLength -= 3  # Decrease platform length
        score += 1

        # Add a small random variation to xBallSpeed
        xBallSpeed += randint(-2, 3)

        # Check if the platform length is below the threshold
        if score == 30:
            won = True

    # Bounce off the screen edges
    if xBall - ballRadius <= 0 or xBall + ballRadius >= 1000:
        xBallSpeed = -xBallSpeed

    # Check if the ball falls off the screen
    if yBall - ballRadius > 700:
        lost = True

# ********** KEY PROCEDURES ********** #

# This procedure gets called every time the user presses a key
def keyDownHandler(event):
    global moveLeft, moveRight

    if event.keysym == "Right":
        moveRight = True
    elif event.keysym == "Left":
        moveLeft = True

# This procedure gets called every time the user lets go of a key
def keyUpHandler(event):
    global moveLeft, moveRight

    if event.keysym == "Right":
        moveRight = False
    elif event.keysym == "Left":
        moveLeft = False

# ********** GAME PROCEDURES ********** #

def gameOver():
    global runGame, delScreen, won, lost, difficulty

    if won:
        if difficulty == "Easy":
            screen.create_text(500, 350, text="Congratulations! You won the game!", font="Impact 40", fill="white")
        elif difficulty == "Medium":
            screen.create_text(500, 350, text="Congratulations! You won the game!", font="Impact 40", fill="white")
    


# This is the main procedure that runs the game. It gets called once the user chooses a difficulty  
def runGame():
    global ball, platform, scoreDisp
    
    root.bind("<Button-1>", "")

    #Creates all the variables the program will need, and gives them starting values
    setInitialValues()

    drawObjects()


    screen.delete( ball, platform )
    #Keeps the game running for as long as the player has not lost or won
    while not lost and not won:
        drawStats()
        updateObjects()

        screen.update()
        sleep(0.01)
        screen.delete( ball, platform, scoreDisp )

    #WHEN THE WHILE-LOOP ABOVE STOPS, THE GAME ENDS
    gameOver()
    askToRestart()

root.after( 500, startScreen) #makes the program call the runGame() procedure 500 milliseconds after the program starts

screen.bind("<KeyPress>", keyDownHandler) # Makes the program call the keyDownHandler() function whenever the user presses a key

screen.bind("<KeyRelease>", keyUpHandler) # Calls the function keyUpHandler() when the user releases a key

screen.pack() #sets up the drawing screen (same as in any Tkinter program)

screen.focus_set() #makes Python pay attention to mouse clicks and button pushes
 
screen.mainloop()