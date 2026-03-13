age = int(input("how old are you? "))
has_ticket = input("Do you have a movies ticket? (yes/no)")

if age >= 13 and has_ticket == "yes": #And: both conditions must b true for our code inside the if statement to run
    print("You can enter the PG-13 movie.")
else:
    print("You cannot enter the PG-13 movie.")
print("Movie chek complete.")

has_pass = input("Do you have a pass? (yes/no) ")
has_coins = input("Do you nave coins to pay? (yes/no )")

if has_pass == "yes" or has_coins == "yes":  #Or: at less one condition must be true for our code inside the if statement to run
    print("You can ride the bus!")
else:
    print("you cannot ride the bus")
print("Bus check complete.")
Homework_done = input("Did you do your homework? yes/no ")
if not Homework_done == "yes": # NOT: flip True to false and false to true
    print("Go finish your homework!")
else:
    print("good Job! you're all done.")
print("homework check complete.")

# You can combine multiple logical operators
is_raining = input("Is it raining? yes/no")
has_umbrella = input("do you have an umbrella? (yes/no)")

if is_raining == "yes" and not has_umbrella =="yes":
    print("stay inside. You might get wet!")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside!")
else:
    print("no rain! You can go outside")