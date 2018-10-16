#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
firstName = ["Andrea", "Hashtag", "Patrick", "Liz", "Abby", "Mark", "N", "Candy"]
lastName = ["James", "Mat", "Ro", "Hashtag", "Bo", "Dan"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
print(firstName[aRandomIndex] )
