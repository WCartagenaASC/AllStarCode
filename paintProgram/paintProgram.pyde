from random import *

colorMode = 1


xCoordinate = 0
yCoordinate = 0

def setup():
    size(1000, 1000)
    background(255, 255, 255)    
    fill(255, 0, 0) 
    rect(0, 0, 200, 100)
    fill(0, 255, 0)
    rect(200, 0, 200, 100)
    fill(0, 0, 255)
    rect(400, 0, 200, 100)
    fill(0, 0, 0)
    rect(600, 0, 200, 100)
    fill(255, 255, 255)
    rect(800, 0, 200, 100)


def draw():
    global colorMode
    if mousePressed:
        if mouseX < 200 and mouseY < 100:
            fill(255, 0, 0)
        elif mouseX < 400 and mouseY < 100:
            fill(0, 255, 0)
        elif mouseX < 600 and mouseY < 100:
            fill(0, 0, 255)
        elif mouseX < 800 and mouseY < 100:
            fill(0, 0, 0)
        elif mouseX < 1000 and mouseY < 100:
            fill(255, 255, 255)
        if mouseY > 100:
            noStroke()
            ellipse(mouseX, mouseY, 15, 15)
    