# This is a comment
print("Hello World")
print(14 + 1)
print("apple" + "banana")
print("apple" + " " + "banana")
print(6 / 3)
print(5 / 3)
print(5 // 3)
print(9 % 3)
print(8 % 3)
print(7 % 3)
print(6 % 3)
print(10 * 4)
print(10 ** 4)
print(5 == 5)
answer = input("Who inspires you? ")
print(answer, "inspires you!")
i = 0
for i in range(5):
    print(i)
i = -1
while True:
    i += 1

    if(i > 20):
        break

    if(i % 2 != 0): # i is odd
        continue
    print(i)
#from random import *
aRandomNumber = input("Set a number: ")
aRandomNumber = int(aRandomNumber) #integer type variable

numGuesses = 3
while numGuesses >0:
    numGuesses -= 1
#guess is going to be a string type when it is captured as input
    guess = input("Guess a number between 1 and 20:")
    if not guess.isnumeric(): #checks that guess is a number
        print("That is not a whole postive number!")
    else:
        guess = int(guess) #turns guess into a integer type
        if (guess == aRandomNumber):
            print("Yay! You got it!")
            break
        elif (guess > aRandomNumber):
            print("Try a lower number.")
        else:
            print("Try a higher number.")
