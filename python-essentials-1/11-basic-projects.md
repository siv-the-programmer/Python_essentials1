# Python Essentials 1 – Basic Projects
## PCEP Practice and Consolidation

---

## Purpose of This Module
This module consolidates **all previous topics** into small programs.

PCEP does not test large projects, but it **tests understanding** required to build them.

If you can write and explain these programs, you are PCEP-ready.

---

## Project 1 – Number Guessing Game

### Concepts Used
- variables
- loops
- conditions
- user input
- type casting
- break statement

### Code

    import random

    secret = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number: "))
        if guess == secret:
            print("Correct!")
            break
        else:
            print("Try again")

### Mental Model
- Loop continues until correct guess
- `break` exits the loop
- Input is cast from string to int

---

## Project 2 – Simple Calculator

### Concepts Used
- input
- casting
- arithmetic operators
- functions

### Code

    def add(a, b):
        return a + b

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    result = add(x, y)
    print("Result:", result)

---

## Project 3 – Even or Odd Checker

### Concepts Used
- modulus operator
- conditionals
- Boolean logic

### Code

    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

---

## Project 4 – List Processing

### Concepts Used
- lists
- loops
- accumulation

### Code

    numbers = [1, 2, 3, 4, 5]
    total = 0

    for n in numbers:
        total += n

    print("Sum:", total)

---

## Project 5 – Dictionary Lookup

### Concepts Used
- dictionaries
- key checking
- conditionals

### Code

    user = {"name": "Siv", "age": 25}

    key = input("Enter key: ")

    if key in user:
        print(user[key])
    else:
        print("Key not found")

---

## How This Relates to PCEP

PCEP expects you to:
- trace execution
- predict output
- identify errors
- understand logic flow

These projects test exactly that.

---

## Final PCEP Readiness Checklist

You should be able to:
- explain every line of these programs
- modify them without breaking logic
- predict output without running code
- identify common errors instantly

If you can do this, **you are ready for PCEP**.

---

## Final Advice
Do not memorize.
Understand.
Type everything.
Break things on purpose.
Fix them.

That is how you pass — and how engineers are made.
