""" NUMBER GUESSING GAME """

import random
from namequestion import askname
from namequestion import alwaysloses

#ask for name
name = askname()
print("\nHello! %s. Let's play a number guessing game." %name)

#generate random number between 1 to 10
randomnumber = random.randrange(1, 10)

#asking for a number
while True:
    choice = input("can you guess a number between 1 and 10? ")
    try:
        val = int(choice)
    except ValueError:
        print("That's not an int! please follow instruction")
        continue

    if int(choice) < 1 or int(choice) > 10:
        print("please follow instruction.")
        continue
    else:
        break

#Check to see if the name is valid
alwaysloses(name)

if choice == randomnumber:
    print("you have won!!")
else:
    print("The the randomly generated number is %s. you have lost" %randomnumber)