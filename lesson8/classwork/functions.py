print("Hello")  # print() is a function which has a string parameter

def make_greeting():
    greeting = "Hello, world!"
    return greeting 

message = make_greeting()
print(message)

#  Function that builds a face
def build_face():
    return":)"

face = build_face()  # Call the build_function
print(face)

# Function dont have to return anything
def print_poem():
    print("If I were a king,")
    print("I could do anything.")

# You can call functionsas many times you want
print_poem()
print_poem()

# Parameters are local variables that can only be accessed inside the function:
def personalized_greeting(name):  # name is a parameter
    return "Hello, " + name + "!"

personalized_message = personalized_greeting("Alice")
print(personalized_message)

# Function that returns a rectangles area based on legth and width
def rectangle_area(legth, width):
    area = legth * width
    return area

# When you call a function in a print statement, python will print what the function 
print("The area of 5x3 rectangle is:", rectangle_area(5, 3))