# Python Essentials 1 – Operators and Expressions
## PCEP Study Guide

---

## Purpose of This Module
Operators and expressions are heavily tested in PCEP because they reveal whether you
understand **how Python evaluates code**, not just how to write it.

Most PCEP mistakes come from:
- operator precedence
- type interactions
- misunderstanding comparison vs assignment

---

## What Is an Operator
An **operator** tells Python to perform an operation on one or more values.

    2 + 3

- `+` is the operator
- `2` and `3` are operands

Operators do not store values — they **produce results**.

---

## What Is an Expression
An **expression** is any piece of code that evaluates to a value.

Examples of expressions:

    2 + 3
    x > 10
    a and b

Expressions can be:
- numeric
- Boolean
- combined into larger expressions

---

## Arithmetic Operators

### Supported Operators
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` integer (floor) division
- `%` modulus (remainder)
- `**` exponentiation

Examples:

    print(10 + 3)     # 13
    print(10 - 3)     # 7
    print(10 * 3)     # 30
    print(10 / 3)     # 3.333...
    print(10 // 3)    # 3
    print(10 % 3)     # 1
    print(2 ** 3)     # 8

---

## Division Behavior (PCEP CRITICAL)

### True Division `/`
Always returns a **float**, even if numbers divide evenly.

    print(6 / 3)      # 2.0

### Floor Division `//`
Returns an integer result **rounded down**.

    print(7 // 3)     # 2
    print(-7 // 3)    # -3

### PCEP Trap
Floor division rounds **toward negative infinity**, not toward zero.

---

## Modulus Operator `%`
Returns the remainder after division.

    print(10 % 3)     # 1
    print(9 % 3)      # 0

### Why Modulus Matters
Often used to test even/odd numbers:

    n = 4
    print(n % 2 == 0)   # True

---

## Operator Precedence (Very Important)

Python evaluates operators in a fixed order.

### Simplified Precedence Order
1. `**`
2. `* / // %`
3. `+ -`
4. Comparisons
5. Logical operators

Example:

    print(2 + 3 * 4)      # 14
    print((2 + 3) * 4)    # 20

### PCEP Trap
If parentheses are missing, Python will **not guess your intention**.

---

## Comparison Operators

### Operators
- `==` equal
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater or equal
- `<=` less or equal

Examples:

    print(5 == 5)     # True
    print(5 != 3)     # True
    print(5 > 10)     # False

### Important Rule
Comparison operators **always return Boolean values**.

---

## Assignment vs Comparison (PCEP FAVORITE)

### Assignment
    x = 5

### Comparison
    x == 5

### Common Error
Using `=` inside a condition is **invalid**:

    if x = 5:   # SyntaxError

Python prevents this mistake deliberately.

---

## Logical Operators

### Operators
- `and`
- `or`
- `not`

Examples:

    print(True and False)   # False
    print(True or False)    # True
    print(not True)         # False

---

## Short-Circuit Evaluation

Python stops evaluating a logical expression as soon as the result is known.

    False and (10 / 0)   # safe, second part never runs
    True or (10 / 0)     # safe, second part never runs

### Why This Matters
Short-circuiting prevents errors and improves performance.

---

## Mixing Types in Expressions (Exam Traps)

### Valid
    print("A" + "B")     # "AB"
    print("A" * 3)       # "AAA"

### Invalid
    print("A" + 3)       # TypeError

### Numeric vs String Confusion
    print("3" * 2)       # "33"
    print(3 * 2)         # 6

---

## Boolean Expressions in Conditions

Conditions must evaluate to `True` or `False`.

    x = 5
    if x > 3:
        print("Runs")

But Python allows **truthy values**:

    if 1:
        print("Runs")

---

## Common PCEP Mistakes
- Forgetting precedence
- Confusing `=` with `==`
- Assuming `/` returns int
- Mixing strings and numbers
- Ignoring short-circuit behavior

---

## Summary (Mental Model)
- Operators produce values
- Expressions are evaluated left-to-right with precedence
- Division always returns float
- Comparisons return booleans
- Logical operators short-circuit
- Python never guesses intent

---

## Self-Test (Must Be Comfortable)
1. Why does `10 / 5` return `2.0`?
2. What is the result of `-7 // 3`?
3. Why does `"3" * 2` not equal `6`?
4. What happens first in `2 + 3 * 4`?
5. Why does `False and error()` not crash?

If any answer feels unclear, reread and retype the examples.
