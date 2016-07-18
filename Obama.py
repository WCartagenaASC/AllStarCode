from Myro import *

# this is the function
# def obamafication(pic)
def obamafy(picture):
    
    obamaDarkBlue = makeColor(0,51,76)
    obamaRed = makeColor(217, 26, 33)
    obamaBlue = makeColor(112,150,158)
    obamaYellow = makeColor(252, 227, 166)

    for pixel in getPixels(picture):
        gray = getGray(pixel)
        if gray > 180:
            setColor(pixel, ObamaYellow)
        elif gray > 120:
            setColor(pixel, ObamaBlue)
        elif gray > 60:
            setColor(pixel, ObamaRed)
        else:
            setColor(pixel, ObamaDarkBlue)


pic = makePicture(pickAFile())     

pic = (picture)
show(pic)
