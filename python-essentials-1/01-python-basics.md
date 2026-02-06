# Python Essentials 1 – Python Basics
## PCEP Study Guide

---

## Purpose of This Module
This module builds the mental foundation for Python programming.
PCEP questions here test **understanding**, not memorization.

If you misunderstand this section, everything later becomes fragile.

---

## What Is Programming

Programming is the process of creating **step-by-step instructions** that a computer can execute to solve a problem.

A program must be:
- Precise
- Unambiguous
- Executable

Computers do exactly what you tell them — not what you mean.

---

## What Is Python

Python is a programming language designed for:
- Readability
- Simplicity
- Rapid development

Python is:
- **High-level**: close to human language
- **Interpreted**: executed line by line
- **Dynamically typed**: variable types decided at runtime

### PCEP Exam Insight
Expect questions comparing Python to compiled languages (like C).
Python does **not** require compilation before execution.

---

## The Python Interpreter

### How Python Executes Code
Python code is executed **top to bottom**, **line by line** by the interpreter.

    print("Hello")
    print("World")

If Python encounters an error, execution **stops immediately**.

### Interpreter Mental Model
Think of Python as a strict reader:
- Reads one line
- Executes it
- Moves to the next line
- Stops on error

---

## Syntax vs Semantics

### Syntax
Syntax defines **how code must be written**.

Incorrect syntax causes a **SyntaxError**.

    if True
        print("Hello")

### Semantics
Semantics defines **what the code means**.

This code is syntactically valid but semantically wrong:

    print(10 / 0)

### PCEP Trap
Syntax errors stop the program before execution.
Semantic errors happen during execution.

---

## Indentation (Critical for PCEP)

Python uses indentation to define **code blocks**.

    if True:
        print("Valid")

This is **mandatory**, not stylistic.

Incorrect indentation:

    if True:
    print("Invalid")

### Why Python Uses Indentation
- Forces readable code
- Eliminates ambiguity
- Prevents hidden logic errors

### Exam Trap
Mixing tabs and spaces may appear correct but causes errors.
Use **consistent indentation**.

---

## Code Blocks

A code block is a group of instructions executed together.

Examples that create blocks:
- if
- elif
- else
- while
- for
- def

    if x > 0:
        print("Positive")
        print("Still inside block")

---

## Comments

Comments are ignored by the interpreter.
They exist only for humans.

    # This is a comment

### Why Comments Matter
- Explain intent
- Clarify logic
- Help future readers (including you)

### PCEP Insight
Comments do **not** affect program output.

---

## Python Keywords

Keywords are **reserved words** with special meaning.
They cannot be used as variable names.

Examples:
- if
- else
- while
- for
- def
- return
- True
- False
- None

Invalid usage:

    if = 10

### Exam Trap
`True`, `False`, and `None` are keywords — case-sensitive.

---

## Statements vs Expressions

### Statement
A statement performs an action.

    print("Hello")

### Expression
An expression evaluates to a value.

    2 + 3

Expressions can exist inside statements.

    print(2 + 3)

---

## Execution Order

Python executes code in the order it appears, unless control flow changes it.

    print("A")
    print("B")
    print("C")

Output is predictable and linear.

---

## Common Beginner Mistakes (PCEP Favorites)

### Forgetting Colon
    if x > 5
        print(x)

### Incorrect Indentation
    if x > 5:
    print(x)

### Using Undefined Variables
    print(y)

### Assuming Python “guesses”
Python does **not** guess intent.
It executes rules strictly.

---

## Summary (Mental Model)

By the end of this module, you must understand:
- Python reads code top to bottom
- Indentation defines logic
- Syntax errors stop execution
- Comments are ignored
- Keywords are reserved
- Code structure matters more than appearance

This is not optional knowledge.
It is the foundation for passing PCEP.

---

## Self-Test (You Should Answer These)

1. Why does Python stop execution on the first error?
2. What is the difference between syntax and semantics?
3. Why is indentation mandatory in Python?
4. Can comments change program behavior?
5. Why is `True` not the same as `"True"`?

If you cannot answer these cleanly, reread this file.
