from Myro import * 
init("sim")
penDown()
def initial():
    turnBy(120)
    forward(1, 3)
    backward(1, 3)
    turnBy(300)
    forward (1,1.5)
    turnBy (250)
    forward (1,1.5)
    turnBy(120)
    forward(1,3)
    backward(1,3)
    turnBy(295)
    penUp()
    forward(1, 4)
    penDown()
    turnBy(180)
    motors (1, 0, 10)
    
    
initial()
