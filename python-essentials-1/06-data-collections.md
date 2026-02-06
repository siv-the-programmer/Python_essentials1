# Python Essentials 1 – Data Collections
## PCEP Study Guide

---

## Purpose of This Module
Data collections allow Python to store **multiple values** under one name.

PCEP focuses on:
- understanding differences between collection types
- mutability vs immutability
- indexing and iteration
- common beginner mistakes with collections

---

## What Is a Collection
A collection is a data structure that holds **multiple values**.

Python Essentials 1 focuses on:
- lists
- tuples
- dictionaries

Each exists for a different reason.

---

## Lists

### What Is a List
A list is an **ordered, mutable** collection of values.

    numbers = [1, 2, 3]

- Ordered → position matters
- Mutable → contents can change

---

## Accessing List Elements (Indexing)

Python uses **zero-based indexing**.

    numbers = [10, 20, 30]
    print(numbers[0])    # 10
    print(numbers[1])    # 20
    print(numbers[-1])   # 30

### PCEP Trap
Index `0` is the **first element**, not `1`.

---

## List Slicing

Slicing extracts a portion of a list.

    numbers = [1, 2, 3, 4, 5]
    print(numbers[1:4])   # [2, 3, 4]

Rules:
- start index is inclusive
- end index is exclusive

---

## Modifying Lists (Mutability)

Lists can be changed after creation.

### Adding Elements

    numbers.append(4)
    numbers.insert(1, 99)

### Removing Elements

    numbers.remove(99)
    last = numbers.pop()

### PCEP Insight
Mutability means **the same list object changes**, not a new one.

---

## Iterating Over Lists

Lists are commonly processed using loops.

    for n in numbers:
        print(n)

### Mental Model
The loop variable takes **each element**, not each index.

---

## Nested Lists

Lists can contain other lists.

    matrix = [
        [1, 2],
        [3, 4]
    ]

Accessing elements:

    print(matrix[0][1])   # 2

---

## Tuples

### What Is a Tuple
A tuple is an **ordered, immutable** collection.

    coords = (10, 20)

### Why Tuples Exist
- Protect data from modification
- Slightly faster than lists
- Used for fixed data

---

## Tuple Immutability (PCEP Critical)

You **cannot** modify a tuple.

    coords[0] = 5   # TypeError

This is a common exam trap.

---

## Tuple Unpacking

Tuples support unpacking.

    x, y = coords

### PCEP Insight
Unpacking works only if counts match.

---

## Dictionaries

### What Is a Dictionary
A dictionary stores **key–value pairs**.

    user = {"name": "Siv", "age": 25}

- Keys must be unique
- Values can repeat
- Dictionaries are unordered (conceptually)

---

## Accessing Dictionary Values

    print(user["name"])

### PCEP Trap
Accessing a missing key raises an error.

    print(user["city"])   # KeyError

---

## Modifying Dictionaries

    user["city"] = "Cape Town"
    user["age"] = 26

Keys overwrite existing values if reused.

---

## Iterating Over Dictionaries

### Iterating Over Keys

    for key in user:
        print(key, user[key])

### Why This Matters
Looping over a dictionary gives keys by default.

---

## Checking Key Existence

    if "age" in user:
        print("Key exists")

This prevents KeyError.

---

## Comparing Collections (Important)

### Lists
- Ordered
- Mutable

### Tuples
- Ordered
- Immutable

### Dictionaries
- Key-value mapping
- Mutable
- Access by key, not index

---

## Common PCEP Mistakes

- Confusing list indexing with dictionary keys
- Forgetting lists start at index 0
- Trying to modify a tuple
- Assuming dictionary order matters
- Using the wrong collection type

---

## Summary (Mental Model)
- Use lists for changing sequences
- Use tuples for fixed data
- Use dictionaries for labeled data
- Indexing starts at 0
- Slicing excludes the end index
- Mutability affects behavior and errors

---

## Self-Test (Must Be Solid)

1. What is the difference between a list and a tuple?
2. Why does `numbers[1:3]` exclude index 3?
3. What happens if you access a missing dictionary key?
4. Why are tuples safer for fixed data?
5. What does iterating over a dictionary return by default?

If any answer feels weak, rewrite the examples and test variations.
