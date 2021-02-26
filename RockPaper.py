""" Rock Paper Scissors """

import random
from namequestion import askname
from namequestion import alwaysloses

#list of numbers played and won
plays=0
win=0

global name
name = askname()

def score():
    if plays <= 0:
        print("\n%s Lets play the game. Rock! paper! scissors!!!"%name)
    else:
        print("You have played %d many times and won %d times"%(int(plays), int(win)))

score()

while True:
    userChoice = input("\nPlease choose one! [R]ock, [P]aper, or [S]cissors: ")
    inputlist = ["S", "s", "R", "r", "P", "p"]

    #if you did not choose one of the three letters
    if userChoice not in inputlist:
        print("Please choose one of three letter in [ ]")
        continue

    print("You chose: " + str.upper(userChoice))
    choices = ['R', 'P', 'S']
    myChoice = random.choice(choices)
    print("I chose: " + myChoice)

    #automatically lose if you are name is remotly similar to AshleyWong
    alwaysloses(name)

    if myChoice == str.upper(userChoice):
        print("Tie!")
        plays += 1
        score()
    elif myChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win! ")
        plays += 1
        score()
        continue
    elif myChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        plays += 1
        score()
        continue
    elif myChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        plays += 1
        score()
        continue
    else:
        print("You win!")
        plays += 1
        win += 1
        score()