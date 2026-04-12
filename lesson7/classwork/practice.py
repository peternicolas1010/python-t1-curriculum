# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
total = sum(numbers) # a short cut to find sum
print("The sum is:", total)


# Problem 2
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
biggest_item = max(numbers)
print(biggest_item)


# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers = [2, -1, 8, 10, -7, 6]

negative_total = 0
total3 = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item < 0:  # Check if the current number is negative
        total3 = total3 + item # add the current number to the running total if it is positive
print("The sum of only the negative numbers its:", total3)

# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item % 2 == 0:
        total = total + item
print(total)


# Problem 5
# Find and print the biggest number that is negative in the list.
numbers = [-1, -30, -5, 7, 12, -2]
 
biggest = -999999
for i in range(len(numbers)):
    item = numbers[i]
    if item < 0 and item > biggest:
        biggest = item
print("The biggest numbers in the negative numbers its:", total3)


