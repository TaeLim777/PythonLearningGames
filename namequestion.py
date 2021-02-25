import re

def askname():
    name = input("What is your name?:  ")
    return name

def alwaysloses(name):
    result = re.search("as*h|won*g", name, re.IGNORECASE)
    while result:
        print("Sorry! You have lost!!")
        exit()
