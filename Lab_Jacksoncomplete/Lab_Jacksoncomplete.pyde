from random import *

xCoordinate = 0
yCoordinate = 0


def setup():
    size(500, 500)
    background(255,255,255)
    
def draw():
    global xCoordinate
    global yCoordinate
    
    x = mouseX + randint(-60,60)
    y = mouseY + randint(-60,60)
    w = 30
    l = 30
    
    
    noStroke()
    fill(randint(0,255))#,randint(0,255),randint(0,255))
    ellipse(mouseX, mouseY, 55, 55)
    ellipse(x,y,w,l)
    fill(randint(0,255),randint(0,255),randint(0,255))
    ellipse(x,y,w,l)
    ellipse(x,y,w,l)
    ellipse(x,y,w,l)
    
    
    