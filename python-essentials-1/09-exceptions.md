# Python Essentials 1 – Exceptions
## PCEP Study Guide

---

## Purpose of This Module
Exceptions handle **runtime errors**—errors that occur while a program is running.

PCEP tests whether you understand:
- what exceptions are
- when they occur
- how to handle them safely
- how exception handling affects program flow

Many beginners fail questions here by confusing **syntax errors** with **exceptions**.

---

## What Is an Exception
An exception is an **error detected during execution**, not during parsing.

Example:

    print(10 / 0)

This code is syntactically correct but causes an exception at runtime.

---

## Syntax Errors vs Exceptions

### Syntax Error
Occurs before execution begins.

    if True
        print("Hello")

Python cannot run the program at all.

### Exception
Occurs during execution.

    print(int("abc"))

Python starts the program, then crashes when the error happens.

### PCEP Insight
Syntax errors stop the program **before it runs**.  
Exceptions happen **while it runs**.

---

## Why Exceptions Exist
Without exception handling:
- programs crash
- users see errors
- logic cannot recover

Exceptions allow programs to:
- fail safely
- recover gracefully
- handle unexpected input

---

## The `try / except` Structure

Basic structure:

    try:
        # risky code
    except:
        # recovery code

Example:

    try:
        n = int(input("Enter a number: "))
        print(n)
    except:
        print("Invalid input")

---

## How `try / except` Works (Mental Model)

1. Python enters the `try` block
2. Executes code line by line
3. If an exception occurs:
   - Python stops the `try` block
   - Jumps to `except`
4. Program continues after the exception block

---

## Catching Specific Exceptions (IMPORTANT)

Catching all exceptions is bad practice.

Better:

    try:
        n = int(input())
    except ValueError:
        print("Invalid number")

### Why This Matters
- Prevents hiding real bugs
- Makes behavior predictable
- PCEP expects recognition of specific exceptions

---

## Common Built-in Exceptions (PCEP Scope)

### ValueError
Raised when conversion fails.

    int("abc")

### ZeroDivisionError
Raised when dividing by zero.

    10 / 0

### TypeError
Raised when using incompatible types.

    "5" + 3

### NameError
Raised when using an undefined variable.

    print(x)

---

## Multiple Except Blocks

Different exceptions can be handled differently.

    try:
        x = int(input())
        print(10 / x)
    except ValueError:
        print("Not a number")
    except ZeroDivisionError:
        print("Division by zero")

Python checks except blocks **top to bottom**.

---

## Order of Except Blocks (PCEP Trap)

More specific exceptions must come first.

Correct:

    except ValueError:
    except Exception:

Incorrect:

    except Exception:
    except ValueError:

The second block becomes unreachable.

---

## The `else` Clause in Exception Handling

The `else` block runs **only if no exception occurs**.

    try:
        x = int(input())
    except ValueError:
        print("Error")
    else:
        print("Success")

### PCEP Insight
The `else` block is skipped if an exception occurs.

---

## The `finally` Clause (Awareness Level)

`finally` runs **no matter what**.

    try:
        print("Try")
    finally:
        print("Always runs")

Used for cleanup (files, resources).

PCEP expects recognition, not deep usage.

---

## Exception Flow Control

Once an exception occurs:
- the rest of the `try` block is skipped
- execution resumes after `except` / `else` / `finally`

Example:

    try:
        print("A")
        int("x")
        print("B")
    except ValueError:
        print("C")

Output:
- A
- C

---

## Common PCEP Mistakes

- Confusing syntax errors with exceptions
- Catching all exceptions blindly
- Expecting code after an error to run
- Forgetting that `input()` returns strings
- Misunderstanding exception flow

---

## Summary (Mental Model)
- Exceptions are runtime errors
- Syntax errors stop execution before start
- `try` protects risky code
- `except` handles failure
- Specific exceptions are preferred
- Execution jumps on error
- Program continues after handling

---

## Self-Test (Must Be Solid)

1. What is the difference between a syntax error and an exception?
2. Why should you catch specific exceptions?
3. What happens after an exception is raised?
4. When does the `else` block run?
5. Why does `int("abc")` raise an exception?

If any answer is unclear, retype and trace the examples.
