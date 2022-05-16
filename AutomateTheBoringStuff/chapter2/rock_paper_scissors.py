import random

def main():
    while True:
        computerChoice = getComputerChoice()
        userChoice = getUserChoice()
        roundResult = doesUserWin(userChoice, computerChoice)
        print(f"The computer picked {computerChoice} so you {roundResult}")

def getComputerChoice():
    return (["rock", "paper", "scissors"])[random.randint(0,2)]

def getUserChoice():
    while True:
        userChoice = input("rock, paper or scissors?: ").lower()
        
        if userChoice in ["rock", "paper", "scissors"]:
            return userChoice

def doesUserWin(userChoice, computerChoice):
    choices = ["rock", "paper", "scissors"]
    
    userChoiceIndex = choices.index(userChoice)
    computerChoiceIndex = choices.index(computerChoice)
    
    if computerChoiceIndex == userChoiceIndex:
        return "tie"
    #Because of the cyclical way rock paper scissors is designed
    #the winner is the word adjacent to the right of the losing word:
    #i.e. +1
    #And so if the winner is at the start of the array 0 - 2 --> -2
    #That's what [1, -2] means.
    elif userChoiceIndex - computerChoiceIndex in [1,-2]:
        return "win"
    return "lose"
    

if __name__ == "__main__":
    main()