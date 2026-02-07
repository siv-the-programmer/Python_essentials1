"""
Loops in Python
---------------

What is loops?
--------------
Loops in Python are used to repeat actions
They let your program do something over and over again without writing the same code many times

They are basically saying, “keep doing this until I tell you to stop” 
or “do this for every item in a list.”
"""

"""
There are two main types of loops in Python:
---------------------------------------------

1. while loop, used to keep repeating something as long as a certain condition is true.
2. for loop used to repeat something a set number of times or go through items in a sequence (like a list or string).
-Even tho <Range> is not a type of loop we will cover it as a number generator for the for loops in this file
"""
"""
------------------------
    WHILE LOOP EXAMPLE 1
------------------------
"""
counter = 0 # The number you would like to start with gets stored in the variable counter
while counter < 10: # keep repeating the code below as long as the counter is less than 10 or else it will stop when it reaches 9
    print(counter) # Print the starting number
    counter += 1 # Increment by 1 each time 
    
"""
Output example:

0
1
2
3
4
5
6
7
8
9

"""
"""
--------------
    EXAMPLE 2
--------------
"""
exit_program = " " # Tells the program to loop no matter what the user types
while exit_program != "yes": # If the Var exit_program is not equal to "yes"
    print("keep looping") # The program will keep looping no matter what the user types
    exit_program = input("exit? ") # Once the user types the keyword "yes" the program will exit
if exit_program == "yes": # Added an if statement so once the program exits it will greet the user goodbye
    print("goodbye") # Greets the user goodbye after typing yes and exiting the program

""" 
Output example:

keep looping
exit? no
keep looping
exit? nope
keep looping
exit? never
keep looping
exit? yes
goodbye
"""
""" 
---------------
    EXAMPLE 3
---------------
"""
while True: # This wraps the code in a loop
    print("Press a 1 to loop and 2 to exit") # Print the question on the screen for the user
    press = input("> ") # Input the user or ask the user to type the number of the above screen
    if press == "1": # if the user types 1
        print("This is a loop") # The program will print this is a loop and loop again 
    elif press == "2": # If the user types 2 then break or exit the loop
        break # This breaks the loop
    else: # if the user types anything else other than 1 or 2 it will say Incorrect option selected and loop again until the until the user presses 2 to exit
        print("Incorrect option selected")
        
"""
--------------
    EXAMPLE 4
--------------
"""
