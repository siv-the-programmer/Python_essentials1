# Python Essentials 1 – Strings
## PCEP Study Guide

---

## Purpose of This Module
Strings represent **text data** in Python.

PCEP tests whether you understand:
- how strings are stored
- indexing and slicing
- immutability
- common string operations
- typical beginner mistakes

---

## What Is a String
A string is an **ordered sequence of characters**.

    text = "Hello"

Strings can be created using:
- double quotes `" "`
- single quotes `' '`

Both behave the same.

---

## String Length

The length of a string is the number of characters it contains.

    text = "Hello"
    print(len(text))   # 5

### PCEP Insight
Spaces count as characters.

---

## String Indexing

Strings use **zero-based indexing**.

    text = "Python"
    print(text[0])     # P
    print(text[1])     # y
    print(text[-1])    # n

### Mental Model
Index numbers point to character positions.

---

## String Slicing

Slicing extracts a portion of a string.

    text = "Python"
    print(text[1:4])   # yth

Rules:
- start index is inclusive
- end index is exclusive

---

## Omitting Slice Values

    print(text[:3])    # Pyt
    print(text[3:])    # hon
    print(text[:])     # entire string

---

## String Immutability (PCEP CRITICAL)

Strings **cannot be modified** after creation.

    text = "Hello"
    text[0] = "h"   # TypeError

### Why This Matters
Any operation that appears to “change” a string actually creates a **new string**.

---

## Reassigning Strings

This is allowed because a new string is created.

    text = "Hello"
    text = text.lower()

---

## String Concatenation

Joining strings together.

    first = "Hello"
    second = "World"
    print(first + " " + second)

### PCEP Trap
Concatenation works only with strings.

    print("Age: " + 25)   # TypeError

Correct way:

    print("Age: " + str(25))

---

## String Repetition

Strings can be repeated using `*`.

    print("Hi" * 3)   # HiHiHi

### Exam Trap
This is **not multiplication**, it is repetition.

---

## String Comparison

Strings can be compared lexicographically.

    print("a" < "b")     # True
    print("abc" == "abc")  # True

### PCEP Insight
Uppercase and lowercase differ.

    print("a" == "A")    # False

---

## Common String Methods

### Changing Case

    text = "Python"
    print(text.upper())
    print(text.lower())

### Replacing Text

    print(text.replace("Py", "My"))

### Checking Content

    print(text.isalpha())
    print(text.isdigit())

---

## Escape Characters

Escape characters represent special characters.

    print("Line1\nLine2")
    print("Tab\tSpace")
    print("Quote: \"Hello\"")

---

## Strings in Conditions (Truthiness)

Empty strings are Falsey.

    if "":
        print("Runs")
    else:
        print("Does not run")

Non-empty strings are Truthy.

    if "0":
        print("Runs")

---

## Common PCEP Mistakes

- Trying to modify a string character
- Forgetting strings are indexed from 0
- Mixing strings and numbers without casting
- Assuming `"3" * 2` equals `6`
- Forgetting slicing excludes end index

---

## Summary (Mental Model)
- Strings are sequences of characters
- Indexing starts at 0
- Slicing excludes the end index
- Strings are immutable
- Concatenation requires strings
- Repetition duplicates text

---

## Self-Test (Must Be Solid)

1. Why does `text[0] = "h"` fail?
2. What does `"abc"[1:3]` return?
3. Why does `"3" * 2` return `"33"`?
4. What is the length of `"Hello World"`?
5. Why is `"a" < "B"` not always obvious?

If unsure, retype the examples and experiment.
