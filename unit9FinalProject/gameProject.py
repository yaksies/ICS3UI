from tkinter import *
from time import *
from random import *

root = Tk()

screen = Canvas(root, width=800, height=600, background="black")

#THE JOB OF THIS PROCEDURE IS TO CREATE ALL THE VARIABLES THE GAME WILL NEED
#AND GIVE THEM STARTING VALUES
def setInitialValues():
    #List global variables
    global xPLatform, yPLatform, platformSpeed, platformLength
    global score, timeLeft
    global xBallSpeed, yBallSpeed, xBall, yBall
	
    #Platform values
    xPlatform = 400
    platformLength = 
	



def drawObjects():
    global rockethead, rocketbody
	

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
	global yRocket, ySpeed
	yRocket = yRocket + ySpeed  
	  


#THIS IS THE MAIN PROCEDURE THAT RUNS THE GAME. IT GETS CALLED ONCE WHEN THE PROGRAM STARTS  
def runGame():

    #Creates all the variables the program will need, and gives them starting values
    setInitialValues()

    #Keeps the game running for as long as the character is still alive
    while True: #or some other condition 
        drawObjects()
        drawStats()
        updateObjects() 
        
        screen.update()
        sleep(0.03)
        screen.delete( "all" ) #Or only the characters

    #WHEN THE WHILE-LOOP ABOVE STOPS, THE GAME ENDS
    gameOverMessage()
    askToRestart()


#THESE 5 COMMANDS WILL BE NEW TO YOU. ALL GAMES MUST INCLUDE THEM.

root.after( 500, runGame) #makes the program call the runGame() procedure 500 milliseconds after the program starts

screen.bind("<Button-1>", mouseClickHandler) #makes the program call the procedure mouseClickHandler() every time the user clicks the left mouse button (what Python called "Button-1")

screen.bind("<ButtonRelease-1>", mouseReleaseHandler) #makes the program call the procedure mouseReleaseHandler() every time the user lets go of the mouse

screen.bind("<Key>", keyDownHandler) # Makes the program call the keyDownHandle() function whenever the user presses a key

screen.bind("<KeyRelease>", keyUpHandler) # Calls the function keyUpHandler() when the user releases a key

screen.pack() #sets up the drawing screen (same as in any Tkinter program)

screen.focus_set() #makes Python pay attention to mouse clicks and button pushes
 
screen.mainloop()