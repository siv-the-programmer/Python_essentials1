# Python Essentials 1 – Loops
## PCEP Study Guide

---

## Purpose of This Module
Loops allow Python to **repeat execution** of a block of code.
PCEP tests whether you understand:
- when loops stop,
- how conditions are evaluated,
- and how loop control statements change behavior.

Most loop errors are **logical**, not syntactic.

---

## What Is a Loop
A loop repeats a block of code **while a condition remains true** or **for each item in a sequence**.

Python has two main loop types:
- `while`
- `for`

---

## The `while` Loop

### What It Does
A `while` loop executes a block **as long as its condition is True**.

    i = 0
    while i < 5:
        print(i)
        i += 1

### Mental Model
Read it as:
“While this condition is true, keep looping.”

Python checks the condition **before each iteration**.

---

## Loop Condition Evaluation

If the condition is False at the start, the loop **never runs**.

    i = 10
    while i < 5:
        print(i)   # never executes

---

## Infinite Loops (PCEP Awareness)

A loop becomes infinite if the condition never becomes False.

    while True:
        print("Runs forever")

### Why This Happens
- Condition never changes
- Update statement is missing or wrong

### Exam Insight
PCEP may ask you to identify infinite loops.

---

## Loop Control Variable
A loop control variable determines when the loop ends.

    count = 0
    while count < 3:
        print(count)
        count += 1

If you forget to update it, the loop never ends.

---

## The `for` Loop

### What It Does
A `for` loop iterates over a **sequence**.

    for i in range(5):
        print(i)

The loop variable `i` takes each value in the sequence, one at a time.

---

## The `range()` Function

### Purpose
`range()` generates a sequence of numbers.

    range(start, stop, step)

- `start` is inclusive
- `stop` is exclusive
- `step` is the increment

Examples:

    for i in range(5):
        print(i)        # 0 to 4

    for i in range(1, 5):
        print(i)        # 1 to 4

    for i in range(1, 10, 2):
        print(i)        # odd numbers

---

## Why `range()` Stops Before `stop`
This design avoids off-by-one errors and aligns with indexing rules.

### PCEP Trap
Many learners expect `range(5)` to include 5.
It does not.

---

## Comparing `while` vs `for`

### Use `while` when:
- Number of iterations is unknown
- Loop depends on a condition

### Use `for` when:
- Iterating a known sequence
- Repeating a fixed number of times

---

## The `break` Statement

### What It Does
`break` immediately exits the loop.

    for i in range(10):
        if i == 5:
            break
        print(i)

Execution continues **after** the loop.

---

## The `continue` Statement

### What It Does
`continue` skips the current iteration and moves to the next one.

    for i in range(5):
        if i == 2:
            continue
        print(i)

Value `2` is skipped.

---

## Difference Between `break` and `continue`

- `break` → exits the loop completely
- `continue` → skips to next iteration

### PCEP Trap
Confusing these two changes program behavior drastically.

---

## The `else` Clause on Loops (Important)

### How It Works
The `else` block runs **only if the loop ends normally** (no `break`).

    for i in range(3):
        print(i)
    else:
        print("Loop finished")

But:

    for i in range(3):
        if i == 1:
            break
    else:
        print("This will NOT run")

### PCEP Insight
The loop `else` is rarely used but frequently tested.

---

## Nested Loops

Loops can exist inside other loops.

    for i in range(3):
        for j in range(2):
            print(i, j)

### Mental Model
The inner loop runs completely for **each iteration** of the outer loop.

---

## Common PCEP Mistakes

### Forgetting to Update the Condition
    i = 0
    while i < 5:
        print(i)

### Using Wrong `range()` Limits
    for i in range(1, 5):
        print(i)   # 1–4, not 1–5

### Misunderstanding Loop `else`
Thinking it runs after every loop.

---

## Summary (Mental Model)
- Loops repeat code
- `while` depends on a condition
- `for` iterates over sequences
- `range()` excludes the stop value
- `break` exits the loop
- `continue` skips iteration
- Loop `else` runs only if no break occurs

---

## Self-Test (Must Be Solid)

1. When does a `while` loop stop?
2. What does `range(3)` produce?
3. What is the difference between `break` and `continue`?
4. When does a loop `else` execute?
5. Why can a loop become infinite?

If unsure, rewrite examples and trace execution step by step.
