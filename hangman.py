# word = input("Type a word for someone to guess: ")
word = "hat"
# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

print(["_", "_", "_"])

# Some useful variables
guesses = ["h", "a", "t"]
maxfails = 7
Lives = "Lives Remaining: " + str(maxfails)
print(Lives)
wrong = ["b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q" "r", "s", "u", "v", "w", "x", "y", "z"]
while maxfails <= 7 and maxfails > 0:
    guess = input("Guess a letter: ")
    if(word.isalpha() == False):
        print("That's not a word!")
        print("Try again.")
    elif guess == guesses[0] or guess == guesses[1] or guess == guesses[2]:
        print("Right?")

    else:
        print("You lost a life.")
        maxfails = maxfails - 1
        if maxfails == 0:
            print("Game over.")
