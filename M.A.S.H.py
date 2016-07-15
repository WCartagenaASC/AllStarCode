from random import *

print ("Lets Play A Fun Game")

name = raw_input("What is your name")

playerInput = raw_input("Whats your dream car")
myBmw = ["a M2"," a M3","a M4","a M5","a M6",
"a useless piece of junk that nobody wants"]
myBmw.append(playerInput)

playerInput = raw_input("Where are you going to live")
myHome = ["as a Hobo", "in a Mansion", "in a Yacht", "in a House", "in a Aparment"]
myHome.append(playerInput)


playerInput = raw_input("What do you think your financial standing will be")
myMoney = ["Billionaire", "Millionaire", "Bankrupt young adult with no friends"]
myMoney.append(playerInput)

if name=="Nice" or name=="nice":
    finalBmw = myBmw[5]
    finalHome = myHome[0]
    finalMoney = myMoney[2]
    
else:


    finalBmw= choice(myBmw)

    finalHome = choice(myHome)

    finalMoney = choice(myMoney)

print("Your car will be", finalBmw, "you will live", finalHome, "you will be a",
 finalMoney)



