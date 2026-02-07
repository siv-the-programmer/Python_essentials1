"""----------Conditionals with Python---------

# What are conditionals?
# Conditionals in Python are statements that allow a program to make decisions and execute different blocks of code based on whether a specified condition is True or False.
# They are fundamental for controlling the flow of a program and enabling it to respond dynamically to various inputs or situations.
# if 
# elif
# else
"""
"""
---------------------------
    How they work Example
---------------------------
"""
# We store the users input in the variable called <name>
name = input("What is your name: ")
if name == "John": # if the user name is equal to john we will print a message "Hello john" 
    print(f"Hello {name}")
else: # If the users name is not john we will print a message letting the program know john is not present
    print(f"I only say hello if john is present")
"""
---------------------------
    Example 2
---------------------------
"""
age = input("Enter your age ")
if age >= "18":
    print("You are allowed to vote")
else:
    print("Please come back when you are 18 or over") 
"""
---------------------------
    elif : if else
---------------------------
# The elif conditional basically means (else if) , for example: if name is John or Mary or Sam, then do this. If not, do something else
# We would say (if) your name is John (elif) Mary (elif) Sam then do this or (else) do something else
# We will also use the statement (or) to make sure it doesnt matter if the first letter is uppercase or lowercase
"""
"""
---------------------------
    elif Example
---------------------------
"""
"""
# In this example is will be using:
# Variables
# Print 
# if 
# elif 
# else
# or
# f string
"""
print("The only people allowed to Access are:\n")
print("John, Mary, Sam") # We print out the names on the screen for those who are allowed to enter
j = "John" # We store all the user names in variables so we can use them later
m = "Mary"
s = "Sam"
names = input("Enter your name to Access: ") # Ask the user to input their name
if names == "john" or names == "John": # if the name is john or John
    print(f"You have Access {j}") # We will print you have Access john 
elif names == "sam" or names == "Sam": # if the name is sam or Sam
    print(f"You have Access {s}") # We will print you have Access Sam
elif names == "mary" or names == "Mary": # if the name is mary or Mary
    print(f"You have Access {m}") # We will print you have Access Mary
else:
    print("Access Denied") # If none of the names match the names shown above we will then print out Access Denied
"""
---------------------------
    Example using Boolean
---------------------------
"""
print("light on or off?") # print light on or off on the screen for the user to see
light_on = input("> ") # variable called light_on stores the value or data the user inputs
if light_on == "on": # if the user types "on" meaning the light is on we will print the bool True
    print(True)
elif light_on == "off": # if the user types "off" meaning the light is off we will print the Bool False
    print(False)
"""
---------------------------
    Nested if statement Example
---------------------------
Nested if statements are Conditional statements can be nested within other conditional statements to handle more complex logic
"""
age = 25 # This is the age that we gave ourself or it can be the age of the user
has_license = True # The user has a license therefore we put the Bool True. If the user has no license we can change this to the Bool False
if age >= 18: # If the user age is greater than or equals to 18
    if has_license: # Nested if statement meaning if the user has a license even if under 18 or over then it will print/do the following: 
        print("You are old enough to drive and have a license.") # This is if we set the age over 18 and the has license set to the Bool True
    else:
        print("You are old enough to drive but need a license.") # This is if the user is over 18 but has the License set to False
else:
    print("You are not old enough to drive.") # If the user is under 18 it will print this and not ask if the user has license
    
