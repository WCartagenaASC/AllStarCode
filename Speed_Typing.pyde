from random import *
from time import *

def setup():
    size(700, 500)
    background(255)

letters = ["q","w","e","r","t","y","u","i","o","p","a","l","k","s","j","h","d","g","f","z","x","c","v","b","n","m"]
scrlst = []

xCoordinates = []
yCoordinates = []



counter = 20

def draw():
    global counter
    global xCoordinates
    global yCoordinates

    if counter == 20:
        ranlet = letters[randint(0, 25)]  
        scrlst.append(ranlet)
        xCoordinates.append(0)
        yCoordinates.append(randrange(30,450))
        counter = 0
    
    counter = counter + 1
    
    background(255)
    for i in range(len(scrlst)):
        textSize(25)
        text(scrlst[i], xCoordinates[i], yCoordinates[i])
        fill(0)
        xCoordinates[i] = xCoordinates[i] + 10
        sleep(0.01)
    
        if xCoordinates[i] > 690:
          scrlst[i] = ''
            

        
        
        