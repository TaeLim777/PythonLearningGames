""" Rock Paper Scissors """

import random

print("\n")
print("READY?  Rock, Paper, Scissors!!!!")

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
    if myChoice == str.upper(userChoice):
        print("Tie!")
    elif myChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win! ")
        continue
    elif myChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif myChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")