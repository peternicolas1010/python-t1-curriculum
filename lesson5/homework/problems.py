import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.

operating = ["print", "if", "random"]

print(operating [len(operating) - 1 ])
operating.reverse()
print(operating)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.

subjects = ["math", "write", "read", "lunch",]

print(subjects[2])

# Sort them alphabetically
subjects.sort()
print(subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
errors = ["300", "230", "403", "843", "500",]

print(len(errors))
print(errors.index("403"))

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random

languages = ["french","english",]
languages2 = ["french","english", "spanish",]
language = random.choice(languages)  # Picks a randome language
print(language)
print(languages2)



# or Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
list = ["chevaux", "bateaux", "fromage", "chat", "police", "code",]

print(list [len(list) - 4 ])

if not print(list[len(list) - 6])