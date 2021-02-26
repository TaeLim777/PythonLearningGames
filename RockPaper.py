""" Rock Paper Scissors """

import random
from namequestion import askname
from namequestion import alwaysloses

lose = True

#list of numbers played (plays[0]) and won (plays[1])
plays=[0, 0]

global name
name = askname() #ask player what their name is

def score():
    if plays[0] <= 0:
        print("\n%s Lets play the game. Rock! paper! scissors!!!"%name)
    else:
        print("You have played " + str(plays[0]) + " many times and won " + str(plays[1]) + " times")

score()

def asking_to_continue():
    plays[0] += 1
    plays[1] += 1
    while True:
        continue_question = input("You win! Do you wish to continue? Y/N:  ")
        questions = ["Y", "y", "n", "N"]
        if continue_question not in questions:
            print("Please type in Y/N")
            continue
        if str.upper(continue_question) == "N":
            score()
            exit()
        else:
            return True


while asking_to_continue:
    userChoice = input("\nPlease choose one! [R]ock, [P]aper, or [S]cissors: ")
    inputlist = ["S", "s", "R", "r", "P", "p"]

    #if you did not choose one of the three letters
    if userChoice not in inputlist:
        print("Please choose one of three letter")
        continue

    print("You chose: " + str.upper(userChoice))
    choices = ['R', 'P', 'S']
    myChoice = random.choice(choices)
    print("I chose: " + myChoice)

    #automatically lose if you are name is remotly similar to AshleyWong
    alwaysloses(name)

    if myChoice == str.upper(userChoice):
        print("Tie!")
        plays[0] += 1
    elif myChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win! ")
        plays[0] += 1
        continue
    elif myChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        plays[0] += 1
        continue
    elif myChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        plays[0] += 1
        continue
    else:
        asking_to_continue()