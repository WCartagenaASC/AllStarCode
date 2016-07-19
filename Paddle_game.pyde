from time import*
from random import*
from math import*

xCoordinate = 200
yCoordinate = 200
xSpeed = randint(1, 10)
ySpeed = randint(1, 10)
    


def setup():
    size(400, 400)
    background(255)
   
    
    
def draw():
    global xCoordinate
    global yCoordinate
    global xSpeed
    global ySpeed
    
    
    stroke(0, 0, 255)
    background(0)
    fill(255,0,0)
    ellipse(xCoordinate, yCoordinate ,55 ,55)
    fill(255)
    rect(mouseX,385,50,10)
    
    xCoordinate = xCoordinate + xSpeed
    yCoordinate = yCoordinate + ySpeed
    sleep(.01)
        
    
    #if yCoordinate > 372.5:
        #ySpeed = ySpeed * -1
    if yCoordinate < 27.5:
        ySpeed = ySpeed * -1
    if xCoordinate > 372.5:
        xSpeed = xSpeed * -1
    elif xCoordinate < 27.5:
        xSpeed = xSpeed * -1
    if yCoordinate > 385 and xCoordinate > mouseX and xCoordinate < mouseX + 50:
        xSpeed = xSpeed * -1
        ySpeed = ySpeed * -1
        
        