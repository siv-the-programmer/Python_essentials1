# Python Essentials 1 – Control Flow
## PCEP Study Guide

---

## Purpose of This Module
Control flow determines **which code runs**, **when it runs**, and **whether it runs at all**.

PCEP focuses on:
- Boolean logic in conditions
- Correct branching
- Understanding how Python chooses a path

Most errors here are **logic errors**, not syntax errors.

---

## What Is Control Flow
Control flow is the order in which Python executes statements.

By default, Python executes code **top to bottom**.
Control flow statements change this order.

---

## Boolean Conditions

Every control-flow decision depends on a Boolean value:
- `True`
- `False`

Example:

    x = 5
    x > 3      # True
    x == 10    # False

Only Boolean results control execution paths.

---

## The `if` Statement

The `if` statement executes a block **only if** its condition is True.

    x = 10
    if x > 5:
        print("Greater than 5")

### Mental Model
Read it as:
“If this condition is true, execute the indented block.”

If the condition is False, Python **skips the block entirely**.

---

## Importance of Indentation

Indentation defines **what belongs to the condition**.

    if x > 5:
        print("Inside")
        print("Still inside")
    print("Outside")

Incorrect indentation changes logic, not just appearance.

---

## The `else` Clause

The `else` block runs **only if the `if` condition is False**.

    x = 3
    if x > 5:
        print("Greater")
    else:
        print("Not greater")

Exactly **one** branch executes.

---

## The `elif` Clause

`elif` means “else if”.

Used to test **multiple mutually exclusive conditions**.

    x = 10
    if x > 10:
        print("Greater")
    elif x == 10:
        print("Equal")
    else:
        print("Smaller")

### Execution Rule
Python checks conditions **top to bottom**.
The first True condition wins.
Remaining branches are ignored.

---

## Why Order Matters (PCEP Favorite)

    x = 10
    if x > 5:
        print("Greater than 5")
    elif x > 8:
        print("Greater than 8")

Output:
- `"Greater than 5"`

Why?
Because Python never reaches the `elif`.

---

## Nested `if` Statements

An `if` statement can exist inside another.

    x = 7
    if x > 0:
        if x < 10:
            print("Single-digit positive")

### Mental Model
Each `if` is evaluated independently.
Indentation defines hierarchy.

---

## Combining Conditions with Logical Operators

Conditions can be combined using `and`, `or`, `not`.

    age = 20
    if age >= 18 and age <= 65:
        print("Working age")

Equivalent (cleaner):

    if 18 <= age <= 65:
        print("Working age")

---

## Truthy and Falsey Conditions (PCEP Critical)

Conditions do not require explicit `True` or `False`.

### Falsey Values
These evaluate to False:
- `0`
- `0.0`
- `""`
- `None`
- `[]`
- `{}`

Example:

    if "":
        print("Runs")
    else:
        print("Does not run")

### Truthy Values
Almost everything else is truthy:
- `"0"`
- `1`
- `-1`
- `[0]`

---

## Common PCEP Traps

### Using Assignment Instead of Comparison
Invalid:

    if x = 5:

Python raises a SyntaxError.

### Forgetting Colon
Invalid:

    if x > 5
        print(x)

### Comparing Different Types
Valid but dangerous:

    print("5" == 5)   # False

### Assuming Else Is Optional
If no `else` exists and condition is False, nothing happens.

---

## Multiple Independent `if` Statements

Each `if` is evaluated separately.

    x = 10
    if x > 5:
        print("A")
    if x > 8:
        print("B")

Output:
- A
- B

This is **not** the same as `if / elif`.

---

## Control Flow vs Loops
Control flow decides **which block runs**.
Loops decide **how many times a block runs**.

They are related but distinct concepts.

---

## Summary (Mental Model)
- Control flow selects execution paths
- Conditions must evaluate to Boolean
- Only one branch of if/elif/else executes
- Order of conditions matters
- Indentation defines logic
- Truthiness affects conditions

---

## Self-Test (Must Be Solid)

1. Why does only one branch of `if/elif/else` run?
2. What happens if all conditions are False and there is no `else`?
3. Why is order important in `elif` chains?
4. Name five falsey values.
5. What is the difference between nested `if` and combined conditions?

If any answer feels shaky, retype the examples and test variations.
