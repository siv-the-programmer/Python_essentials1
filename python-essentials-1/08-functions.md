# Python Essentials 1 – Functions
## PCEP Study Guide

---

## Purpose of This Module
Functions allow you to **group reusable logic** and give it a name.

PCEP tests whether you understand:
- how functions are defined and called
- how arguments and parameters work
- return values vs printing
- variable scope
- default parameters

Many beginners fail PCEP here by confusing **what a function returns** with **what it prints**.

---

## What Is a Function
A function is a **named block of code** that performs a specific task.

Functions help you:
- avoid repetition
- organize logic
- make code easier to understand and test

---

## Defining a Function

Functions are defined using the `def` keyword.

    def greet():
        print("Hello")

Key points:
- `def` starts the definition
- the name follows
- parentheses may contain parameters
- a colon starts the function body
- indentation defines the body

---

## Calling a Function

A function does nothing until it is called.

    greet()

### Mental Model
Defining a function is like **writing instructions**.
Calling it is like **executing those instructions**.

---

## Parameters and Arguments

### Parameters
Parameters are variables listed in the function definition.

    def greet(name):
        print("Hello", name)

### Arguments
Arguments are values passed when calling the function.

    greet("Siv")

### PCEP Insight
- Parameter → name inside the function
- Argument → value passed to the function

---

## Multiple Parameters

    def add(a, b):
        print(a + b)

    add(3, 4)

Order matters unless keywords are used.

---

## Return Values (CRITICAL FOR PCEP)

### What `return` Does
`return` sends a value back to the caller and **ends the function**.

    def add(a, b):
        return a + b

    result = add(2, 3)
    print(result)

### Print vs Return (PCEP FAVORITE)

    def add(a, b):
        print(a + b)

This function:
- prints a value
- returns `None`

    x = add(2, 3)
    print(x)   # None

### Exam Trap
Printing is **not** returning.

---

## Functions Without `return`

If no `return` is used, Python returns `None`.

    def demo():
        pass

    print(demo())   # None

---

## Default Parameters

Default parameters allow arguments to be optional.

    def greet(name="World"):
        print("Hello", name)

    greet()
    greet("Siv")

### Rule
Default parameters must come **after** non-default parameters.

Invalid:

    def f(a=1, b):
        pass

---

## Keyword Arguments

Arguments can be passed by name.

    def info(name, age):
        print(name, age)

    info(age=25, name="Siv")

Order does not matter with keyword arguments.

---

## Variable Scope (PCEP CRITICAL)

### Local Scope
Variables created inside a function are local.

    def demo():
        x = 10
        print(x)

    demo()
    print(x)   # NameError

### Global Scope
Variables created outside functions are global.

    x = 5
    def demo():
        print(x)

---

## Shadowing Variables

A local variable can have the same name as a global variable.

    x = 5
    def demo():
        x = 10
        print(x)

    demo()
    print(x)

Output:
- 10
- 5

### PCEP Trap
The global variable is **not changed**.

---

## The `global` Keyword (Awareness Only)

    x = 5
    def demo():
        global x
        x = 10

Use with caution. PCEP expects recognition, not heavy use.

---

## Function Execution Flow

When a function is called:
1. Arguments are passed
2. Function body executes
3. `return` sends value back
4. Control returns to caller

---

## Common PCEP Mistakes

- Forgetting to call the function
- Confusing print with return
- Using variables outside their scope
- Expecting functions to run automatically
- Incorrect default parameter order

---

## Summary (Mental Model)
- Functions group reusable logic
- `def` defines, calling executes
- Parameters receive values
- Arguments pass values
- `return` sends data back
- Printing is not returning
- Scope controls variable visibility

---

## Self-Test (Must Be Solid)

1. What does a function return if there is no `return`?
2. What is the difference between a parameter and an argument?
3. Why does `print(add(2,3))` sometimes print `None`?
4. Why does changing a variable inside a function not affect the global one?
5. When should default parameters be used?

If any answer is unclear, rewrite the examples and test variations.
