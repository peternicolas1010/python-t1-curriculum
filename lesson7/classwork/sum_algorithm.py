numbers = [5, -8, 35, -3, 6, 2]

total = sum(numbers) # a short cut to find sum
print("The sum is:", total)

print("Our algorithm:")

total2 = 0
for i in range(len(numbers)): # Go through each index in the list
    item = numbers[i] # Get the numbers at the current index
    total2 = total2 + item # add the current number to the running total
print("The sum is:", total2)

# Find te sum of only the positive numbers.
positive_total = 0
total3 = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 0:  # Check if the current number is positive
        total3 = total3 + item # add the current number to the running total if it is positive
print("The sum of only the positive numbers its:", total3)