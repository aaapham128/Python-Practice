aRandomNumber = input("Set a number. ")
aRandomNumber = int(aRandomNumber)

numberOfGuesses = 4

while numberOfGuesses > 0:
        numberOfGuesses -= 1
        guess = input("Guess a number between 1 to 20! ")

        if not guess.isnumeric():
            print("This is not a postive whole number.")

        else:
            guess = int(guess)

            if guess == aRandomNumber:
                print("You are correct!")
                break

            elif guess < aRandomNumber:
                    print("Guess a higher number.")
            else:
                print("Guess a lower number.")
                
