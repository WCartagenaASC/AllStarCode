
aliens = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1] , [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
alienY = 50
alienX = 110
bulletX = 50
bulletY = 565
playerX = 250
bulletFired = False
alienSpeedX = 1
alienXR = 610
alienXL = alienX 
counter 



def setup():
    size(700, 600)
    background(0)
def intersect(bulletX, bulletY, alienX, alienY):
    if (bulletX > alienX - 20) and (bulletX < alienX + 20) and (bulletY > alienY - 20) and (bulletY < alienY + 20):
        return 1
    else: 
        return 0
    
    
def draw():
    global alienX, alienY, aliens, playerX, bulletY, bulletX, bulletFired, alienSpeedX, alienXR, alienXL
    background(0)
    rect(playerX, 565, 30, 30)
    alienX = alienX + alienSpeedX
    alienXL = alienXL + alienSpeedX
    alienXR = alienXR + alienSpeedX
    
    if alienXR > 700 - 15 or alienXL < 0 + 15: 
        alienSpeedX = alienSpeedX * -1
    
    
    # Draws the aliens
    for i in range(len(aliens)): 
        for j in range(len(aliens[i])):
            
            if aliens[i][j] == 1:
                ellipse(alienX + i * 50, alienY + j * 60, 30, 30)
                
            if aliens[i][j] == 1 and intersect(bulletX,bulletY, alienX + i * 50, alienY + j * 60):
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
                bulletX = playerX + 15
                bulletFired = True

    if bulletFired == True:
        rect(bulletX - 5, bulletY, 10, 10)
        bulletY = bulletY - 10
        if bulletY < 0:
            bulletFired = False 
            bulletY = 565
            
    # if bullet hits the Alien
    
    