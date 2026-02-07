"""
---------------------------------------------------------------------
# VARIABLES WITH PYTHON
#--------------------------------------------------------------------

# In python variables are used to store values that can be refrenced and manipulated during program execution
# A variable is essentially a name that is assigned to a values
"""
name = "David" # This is the word David stored inside the variable <name>
age = 28 # 28 is stored inside of the variable <age>
 
print(name) # We are printing the data stored in the variable <name> Which is David
print(age)  # We are printing the data stored in the variable <age>  Which is 28

# When you run :
# python3 .\variables.py
# Output should look like :
"""
# David
# 28
"""
"""
------------------------------------------------------------------------
# Rules for naming variables
# Variable names can only contain letters, digits and underscores
# A variable name cannot start with a digit
# Variables are case sensitive
# Variables in Python are assigned values using the = operator.
------------------------------------------------------------------------
"""
x = 5
y = 3.14
z = "HI" # The = sign assigns the value to the variable
"""
------------------------------------------------------------
# Dynamic Typing
--------------------------------------------------------------
# Python Variables are dynamically typed
# This means the same variable can hold different types of values during execution
# Example:
x = 10
x = "Ten"
# X no longer holds the value 10 but the string "Ten"
# If we print it out it will look like
print(x)
# The output would be:

Ten instead of 10
"""

"""
# if we want to print out both we need to print the first variable before we assign the new value to the second variable"""
# Example : 
x = 10
print(x)
x = "Ten"
print(x)

"""The output would look like :

10
Ten
"""
"""
-------------------------------------------
# Multiple Assignments
-------------------------------------------
# Python allows multiple variables to be assigned values in a single line
"""

a = b = c = 100
print(a, b, c)

"""# Output would look like:

100 100 100 
"""
"""
--------------------------------------------------------
# Assigning Different Values
--------------------------------------------------------
# We can assigne different values to multiple variables simultaneously 
# This makes the code concise and easier to read
"""

x, y, z = 3, 1.4, "Python" # x, = 3 | y, = 1.4 | z = "Python"
print(x, y, z) # This will then print out all those values

"""# The output would look like this: 

3 1.4 Python
"""
"""
------------------------------------------------------------------
# Type Casting a Variable
------------------------------------------------------------------
# Type casting refers to the process of converting the value of-
# one data type into another

# Basic Castin Functions
# int()
# float()
# str()
"""
# Example: 
str_ing = "10" # This is a string or is initially a string
new_string_to_int = int(str_ing) # This converts the string "10" into an integer 10

in_t = 5 # this is a normal integer in the variable in_t
int_to_float = float(in_t) # This turns the integer 5 into a float 0.5

age = 25 
age_tostring = str(age)
print(str_ing)
print(int_to_float)
print(age_tostring)

"""# The output would look like : 

10
5.0
25
"""
"""
--------------------------------------------------------------------------
# Getting the Type of Variable
-----------------------------------------------------------------------------
# In python we can determine the type of variable using the type() function.
# This returns the type of object passed to it
"""
a = 5
b = "hello"
c = "0.5"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

"""output will look like:

<class 'int'>
<class 'str'>
<class 'str'>
<class 'bool'> 
"""

"""
---------------------User input using variables-----------

# In Order to get user input we have to assign the input() function.
"""
nam = input("\nWhat is your name: ")
print(nam)

fav_food = input("\nWhat is your favourite food ")
print(fav_food)
# You may add your own name and fav food, I just used david and pizza as an example

"""# Output would look like: 

What is your name: david
david

What is your favourite food: pizza
pizza

"""

"""
------------------------Input sentences------------------
# We can also print out sentences like we would with a variable
# We use an f string for cleaner code
"""
nam1 = input("\nWhat is your dogs name?: ")
print(f"I can't believe your dogs name is {nam1}") # We can use an f string for cleaner code

nam2 = input("\nWhere do you live?: ")
print(f"Oh you live in {nam2} I have no idea where that is")

"""# The output would look like this

What is your dogs name?: Linux
I can't believe your dogs name is Linux

Where do you live?: Planet Python
Oh you live in Planet Python I have no idea where that is

"""