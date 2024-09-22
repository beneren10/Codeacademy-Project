#rock paper scissors programme written using GIT hub 

import random

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
    

        