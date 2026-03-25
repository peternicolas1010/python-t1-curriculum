# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names.count("Alex"))



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals.count("elephant"))
if "elephant" in animals:
    print ("elephant is found!")
else:
    print ("no elephant is in the list")



# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores.count(100))



# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors.count("blue"))
if "blue" in colors:
    print("It is in the list")

else:
    print("the color blue is not found")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]

count = 0

for temp in temperatures:
    if temp <= count:
        count += 1

print(count)