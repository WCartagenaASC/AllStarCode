
aliens = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1] , [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
alienY = 50
alienX = 110
bulletX = 50
bulletY = 565
playerX = 250
bulletFired = False



def setup():
    size(700, 600)
    background(0)
def intersect(bulletY, bulletX, alienY, alienX):
    if (bulletX > alienX) and (bulletX < alienX) and (bulletY > alienY) and (bulletY < alienY):
        return 1
    else: 
        return 0
    
    
def draw():
    global alienX, alienY, aliens, playerX, bulletY, bulletX, bulletFired
    background(0)
    rect(playerX, 565, 30, 30)
    
    # Draws the aliens
    for i in range(len(aliens)): 
        for j in range(len(aliens[i])):
            
            if aliens[i][j] == 1:
                ellipse(alienX + i * 45, alienY + j * 60, 30, 30)
                
            if intersect(bulletY,bulletX,alienX,alienY):
                aliens[i][j] = 0 
                bulletFired = False
                bulletY = 565
                
    



    
    # Makes the Player move LEFT                
    if keyPressed == True:
        if keyCode == 37:
            playerX = playerX - 5

    
    # Makes the Player move RIGHT                     
    if keyPressed:
        if keyCode == 39:
            playerX = playerX + 5 
            
    # Makes the Player Shoot A bullet
        if keyCode == 0:
        
            if bulletFired == False:
                bulletX = playerX
                bulletFired = True

    if bulletFired == True:
        rect(bulletX + 10, bulletY, 10, 10)
        bulletY = bulletY - 10
        if bulletY < 0:
            bulletFired = False 
            bulletY = 565
            
    # if bullet hits the Alien
    
    