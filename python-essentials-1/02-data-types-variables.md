# Python Essentials 1 – Data Types and Variables
## PCEP Study Guide

---

## Purpose of This Module
PCEP tests whether you understand:
- what values are,
- how Python stores them,
- how variables reference them,
- and how types affect operations.

This module is core exam territory.

---

## What Is a Value
A **value** is data in memory (like a number or a piece of text).

Examples of values:
- `10`
- `3.14`
- `"hello"`
- `True`

Python code manipulates values constantly.

---

## What Is a Variable
A **variable** is a name that references a value.

    x = 10
    name = "Siv"

### Mental Model
A variable is a **label** stuck onto a value in memory.

- The variable is not the value.
- The variable points to the value.

---

## Assignment Operator `=`
The `=` operator assigns the value on the right to the variable on the left.

    x = 10

Read it as:
- “x gets 10”
Not:
- “x equals 10” (that would be `==`)

### PCEP Trap
Many beginners confuse `=` with `==`.

- `=` assigns
- `==` compares

---

## Naming Rules (Identifiers)
Valid variable names:
- Can contain letters, digits, `_`
- Cannot start with a digit
- Case-sensitive

Valid:
- `age`
- `user_name`
- `x1`

Invalid:
- `1x`
- `user-name`
- `class` (keyword)

### Best Practice (Exam-safe)
Use descriptive snake_case:

    first_name = "Alice"
    total_cost = 99.99

---

## Python Is Dynamically Typed
Python variables do not have fixed types.
The **value** has the type.

    x = 10
    x = "ten"

This is allowed because Python checks types at runtime.

### PCEP Insight
You must understand that type is attached to the value, not the name.

---

## Core Built-in Data Types

### Integer (`int`)
Whole numbers (no decimals).

    a = 10
    b = -7
    c = 0

### Float (`float`)
Numbers with decimals.

    pi = 3.14
    temp = -2.5

### Boolean (`bool`)
Truth values.

    is_admin = True
    is_enabled = False

### String (`str`)
Text data.

    name = "Siv"
    msg = "Hello"

---

## Type Checking with `type()`
To see a value’s type:

    x = 10
    print(type(x))

Expected output (conceptually):
- `<class 'int'>`

### PCEP Trap
`type()` returns a type object, not a string.

---

## Type Casting (Conversion)
Casting converts one type into another.

### String to Integer
    n = int("10")

### Integer to Float
    x = float(5)

### Number to String
    s = str(100)

### PCEP Traps
1) You cannot convert non-numeric strings to int:

    int("ten")   # ValueError

2) `int()` truncates toward zero (does not round):

    int(3.9)     # becomes 3
    int(-3.9)    # becomes -3

3) `float("3.14")` works, but:

    float("3,14")  # ValueError in most locales

---

## Input Always Returns a String
`input()` always returns `str`.

    age = input("Enter age: ")
    print(type(age))

To get a number, cast:

    age = int(input("Enter age: "))

### Exam Trap
If you do not cast, arithmetic will fail:

    age = input()
    print(age + 1)   # TypeError

---

## Numeric Literals and Underscores
Python allows underscores for readability:

    big = 1_000_000

This is still an integer.

---

## Scientific Notation (Floats)
Python supports scientific notation:

    x = 3e2     # 300.0
    y = 5e-1    # 0.5

PCEP may test recognition of this format.

---

## Boolean Truthiness (Important for PCEP)

In Python, many values behave as True/False in conditions.

### Common Falsey Values
These evaluate to False:
- `False`
- `None`
- `0`
- `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)

Example:

    if "":
        print("Won't run")
    else:
        print("Empty string is falsey")

### Common Truthy Values
Almost everything else is truthy:
- `"0"` (string with a character)
- `1`
- `-1`
- `[0]`

---

## Multiple Assignment
Assign multiple variables in one line:

    a, b = 1, 2

Swap values:

    a, b = b, a

### PCEP Insight
This is common Pythonic behavior and frequently tested.

---

## Augmented Assignment Operators
Shortcuts for updating a variable.

    x = 10
    x += 5   # x = x + 5
    x -= 2
    x *= 3

---

## Basic Formatting and Printing Variables

### Print with commas
    name = "Siv"
    age = 25
    print(name, age)

### f-strings (Recommended)
    print(f"Name: {name}, Age: {age}")

### PCEP Note
You should recognize f-strings, but PCEP often focuses on basic print behavior too.

---

## Common Mistakes (Exam Favorites)

### Using Undefined Variables
    print(y)   # NameError

### Using Wrong Type in Operations
    print("10" + 5)  # TypeError

### Forgetting Input Cast
    n = input()
    print(n * 2)     # repeats string, not numeric multiply

Example:

    n = "3"
    print(n * 2)     # "33"

Numeric multiply requires casting:

    n = int(input())
    print(n * 2)     # 6

---

## Summary (Mental Model)
- Variables reference values.
- Values have types.
- Python decides types at runtime.
- `input()` returns strings.
- Casting is required for numeric input.
- Truthiness matters in conditions.

---

## Self-Test (You Should Answer These)

1. What is the difference between `=` and `==`?
2. What type does `input()` return?
3. Why does `"3" * 2` produce `"33"`?
4. Name 5 falsey values in Python.
5. What does `int(-3.9)` return and why?

If you struggle, reread and retype the examples.