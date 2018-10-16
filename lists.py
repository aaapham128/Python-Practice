friends = ["Beyonce", "Jay-Z", "Chrissy Teigen", "Barack Obama", "Stephen Colbert"]
weights = [153.4, 81.2, 1293.4, 432.6]
random_data = ["George", 8, 10.2]

print(friends)
print(weights)
print(random_data)

print(friends + weights)
print(friends + weights + random_data)

aList = [0, 1, 2, 3, 4]
print(aList)
print(len(aList))

#In is used to check if something is in a list
print(3 in aList)

numbers = [1,2, 3, 2, 1]
#looking through the list
for num in numbers:
    print(num)
print()
#looking through the index (I still don't get it)
for i in range(len(numbers)):
    print(numbers[i])
    print(numbers)
    print([i])

name = "Anh"
print(len(name))

print("via" in name)

print(name[0])

for letter in name:
    print(letter)

print(name[0] + name[1])
