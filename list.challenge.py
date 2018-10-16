#imports the ability to get a random number (we will learn more about this later!)
from random import *
#Create the list of words you want to choose from.
randomName = ["Amy", "Pat", "Jo", "Susan", "Steve", "James", "Andrea"]

#Generates a random integer.
aRandomIndex = randint(0, len(randomName)-1)

print(randomName[aRandomIndex])
