# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
number = int(input("enter a number:"))
if number % 2==0:
    print ("Even")
else:
    print("Odd")

# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day = input("choose a day of the week:")
if day == "saturday":
    print ("Weekend")
elif day == "sunday":
     print ("Weekend")
else:
    print("Weekday")




# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
dhfgsb ghjsrgh





# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".

# if a number can be divisible by 2 it mean its a even number

positive_integer = int(input("choose a positive integer:"))
if positive_integer % 2 == 0 and positive_integer> 10:
    print("Big even number")
else:
    print("Number does not meet criteria")



# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".