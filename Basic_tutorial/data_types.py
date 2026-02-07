"""
# Data Types with Python
#-------------------------------------------------
# Data types in python are a way to classify data items
# They represent the kind of value, which determines what operations can be performed on the data
# Since everything is an object in python programming
# Python data types are classes and variables are instances (objects) of those classes
"""

"""
The following are standard or built in data types in Python:
---------------------------------------------------
    Numeric: int, float, complex
    Sequence Type: string, list, tuple
    Mapping Type: dict
    Boolean: bool
    Set Type: set, frozenset
    Binary Types: bytes, bytearray, memoryview
"""

# Below code assigns variable 'x' different values of a few Python data Types
# int, float, list, tuple and string.
# Each assignment replaces previous value making 'x' take on the data type and value of most recent assignment 

x = 50 # int
x = 60.5 # float
x = "Hello team" # string
x = ["python", "for", "aws"] # list
x = ("python", "for", "aws") # tuple
print(x) # This will print the most recent data type which is the tuple

# Output of this will look like:
"""
('python', 'for', 'aws')
    
Numeric Data Types 
# python numbers represent data that has a numeric value
# A numeric value can be an integer , a floating number or even a complex number
# These values are defined as int, float and complex classes

Integers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). 
There is no limit to how long an integer value can be.

Float: value is represented by float class. 
It is a real number with a floating-point representation. 
It is specified by a decimal point. 

Complex Numbers: It is represented by a complex class. 
It is specified as (real part) + (imaginary part)j.
For example - 2+3j

"""
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 +3j
print(type(c))

# The output will look like: 
"""
<class 'int'>
<class 'float'>
<class 'complex'>
    
"""

wel = "Welcome to Python data types"
print(wel)

# check data type
print(type(wel))

# access string with index (0, 1, 2, 3,)
print(wel[1]) # prints the second index
print(wel[2]) # prints the third index
print(wel[-1]) # -1 would start with the last index from the back

# The output would look like: 
"""
Welcome to Python data types
<class 'str'>
e
l
s

"""
"""
---------------LIST-DATA-TYPE----------------
Lists are similar to arrays found in other languages. 
They are an ordered and mutable collection of items. 
It is very flexible as items in a list do not need to be of the same type.

Creating a List in Python

Lists in Python can be created by just
placing the sequence inside the square brackets[].
"""
#---------------LIST-EXAMPLE------------------

# Empty list 
li_st = []

# List with int values
list_int = [1, 2, 3]
print(list_int)

# list with mixed values int and string
list_val = ["byte", "gb", 1, 4, 5]
print(list_val)

# The output would look like : 
"""
[1, 2, 3]
['byte', 'gb', 1, 4, 5]

"""
"""
#------------- Access List Items-----------------
In order to access the list items refer to index number. 
In Python, negative sequence indexes represent positions from end of the array. 
Negative indexing means beginning from end
-1 refers to last item, -2 refers to second-last item, etc.
"""

a = ["python", 'ubuntu', 'bios']
print("Getting element from the list")
print(a[0]) # This will get the first index in the list
print(a[2]) # This will grab the third index in the list

print("Accessing using negative indexing")
print(a[-1]) # using -1 will grab the last index in the list
print(a[-3]) # This will grab the third index from the back

# The output would look like : 
"""
Getting element from the list
python
bios
Accessing using negative indexing
bios
python
"""

"""
--------------Tuple Data Type-------------------
Tuple is an ordered collection of Python objects. 
The only difference between a tuple and a list is that tuples are immutable. 
Tuples cannot be modified after it is created.

In Python, tuples are created by placing a sequence of values separated by
a comma with or without the use of parentheses for grouping data sequence.

"""

# Create an empty tuple
tup1 = ()

tup2 = ("python", "Html")
print("This is a tuple with the use of a string", tup2)

# This would output: 
"""
This is a tuple with the use of a string ('python', 'Html')

"""

#--------------Access Tuple Items-----------
"""
In order to access tuple items refer to the index number. 
Use the index operator [ ] to access an item in a tuple

"""

tup1 = (1, 2, 3, 4, 5)

# Access the tuple items using the index
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

# The output would look like : 
"""
1
5
3

"""

"""
------------------Boolean Data Type-------------
# Python Boolean Data type is one of the two built-in values, True or False. 
# Boolean objects that are equal to True are truthy (true) and those equal to False are falsy (false). 
# However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by class
"""
print(type(True))
print(type(False))

# The output would look like: 
"""
<class 'bool'>
<class 'bool'>

"""
"""
----------------Truthy and Falsy Values--------
# In Python, truthy and falsy values are values that evaluate to True or False in a Boolean context. 
# Truthy values behave like True, while falsy values behave like False when used in conditions.
# Will look more into this topic as I progress
"""
if 1: 
    print("1 is truthy")
if not 0:
    print("0 is falsy")

# Output would look like : 
"""
1 is truthy
0 is falsy
"""
"""
#--------------Set Data Type-------------------
# In Python Data Types, set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
# The order of the elements in a set is undefined though it may consist of various elements.

#--------------Create a set in Python----------
# Sets can be created by using the built-in set() function
# with an iterable object or sequence by placing the sequence inside curly braces, seperated by a comma.
# The type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.
"""
s1 = set()

s1 = set("setdatatype")
print("set with the use of a string", s1)

s2 = set(["python", "data", "data"])
print("set with the use of a list", s2)

# Access set items

# Set items cannot be accesed by reffering to an index since sets are unordered the items have no index
# But we can loop through the set items using a for loop, 
# Or ask if a specified value is in a present set, by using the keyword in.

set1 = set(["python", "data", "data"])
# Duplicates are removed automaically
print(set1)

# Loop through set

for i in set1:
    print(i, end=" ") # Prints elements 1 by 1
    
    # check if item exists in a set
    print("data" in set1)
    
# Output would look like: 
"""
{'python', 'data'}

data True

"""

"""
-----------------Dictionary type data-------------
# A dictionary in Python is a collection of data values used to store data values like a map,
# Unlike other python data types, a dictionary holds a key: value pair.
# key value is provided in a dictionary to make it more optimized.
# Each key-value pair in a dictionary is seperated by a colon:
# whereas each key is separated by a comma

#---------------Create a Dictionary in Python-------
# Values in a dictionary can be of any datatype and can be duplicated,
# Whereas keys cant be repeated and must be immutable
# The dictionary can also be created by the built-in function dict()
# Dictionary keys are key sensitive
"""
d = {}

d = {1: "Dict", 2:"in", 3:"Python"}
print(d)

# Creating dictionary using dict() constructor

d1 = dict({1: "python", 2: "is", 3:"great"})
print(d1)

"""
------------Accessing Key-value in Dictionary---
# In order to access items from a dictionary, refer to its key name
# key can be used inside the squre breackets using get() method we can access dictionary elements
"""
d = {1: "bash", "name": "Python", 3: "nodejs"}
print(d["name"])

print(d.get(3))




