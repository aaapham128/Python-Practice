# #level 1: create a function that:
#
# #1. Adds 3 numbers together
# def addfcn(value1, value2, value3):
#     print(value1 + value2 + value3)
# addfcn(12, 54, 20)
#
# # 2. Subtracts one number from another
# def subfcn(number1, number2):
#     print(number1 - number2)
# subfcn(10, 3)
#
# #3. Multiplies two numbers
# def mulfcn(val1, val2):
#     print(val1 * val2)
# mulfcn(3, 20)
#
# #4. Divides two numbers
# def divfcn(divi1, divi2):
#     print(divi1 / divi2)
# divfcn(40, 5)
# #5. Adds 2 numbers and then divides them
# def paranfcn(no1, no2, no3):
#     print((no1 + no2)/ no3)
# paranfcn(100, 5, 10)

#Level 2: Create a function that:
#1. Takes in 4 numbers. Adds the first two numbers to get a sum.
def addFour(no1, no2, no3, no4):
    if ((no1 + no2) > (no3 + no4)):
        print(no1 + no2)
    elif((no3 + no4) > (no1 + no2)):
        print(no3 + no4)
    else:
        print("Values are equal")
addFour(1, 2, 3, 4)

#2. Then adds the second two numbers to get a sum.
#Compares the two new sums and prints the smaller sum.

#Level 3: Create a function that:
#1.Takes in a string. Checks that string for the letter bselfself.
#If it contains the letter b or c, print it. Otherwise, print "Can't print word"
