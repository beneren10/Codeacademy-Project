#rock paper scissors programme written using Python + testing GIT hub accessibility  

import random
import re

userChoice = "r"

def rps(userChoice):
    
    def computerInput():
        computerChoice = random.randint(0,2)
        match computerChoice: 
            case 0:
                return "r"
            case 1:
                return "p"
            case 2:
                return "s"

    def userInput():
        compChoice = computerInput()

        if compChoice == userChoice:
            return "Draw"
        elif compChoice == "r":
            match userChoice:
                case "p":
                    return "{} v {} - User Wins".format(compChoice,userChoice)
                case "s":
                    return "{} v {} - Computer Wins".format(compChoice,userChoice)
        elif compChoice == "p":
            match userChoice:
                case "r":
                    return "{} v {} - Computer Wins".format(compChoice,userChoice)
                case "s":
                    return "{} v {} - User Wins".format(compChoice,userChoice)
        elif compChoice == "s":
            match userChoice:
                case "p":
                    return "{} v {} - Computer Wins".format(compChoice,userChoice)
                case "r":
                    return "{} v {} - User Wins".format(compChoice,userChoice)
    
    return userInput()

def countresults(num):
    counter = 0 
    for i in range(1,num):
        x = rps(userChoice)
        if ("User" in x):
            counter += 1
    return counter        


    

print(countresults(1000000))




