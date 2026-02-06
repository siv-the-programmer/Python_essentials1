# Python Essentials 1 – Modules and Packages
## PCEP Study Guide

---

## Purpose of This Module
Modules and packages teach Python **code organization and reuse**.

PCEP tests whether you understand:
- what a module is
- how importing works
- namespace behavior
- basic standard library usage
- the meaning of `__name__`

---

## What Is a Module
A **module** is a file containing Python code.

- Functions
- Variables
- Classes

Any `.py` file is a module.

Example:
- `math.py`
- `random.py`
- `my_script.py`

---

## Why Modules Exist
Modules allow you to:
- reuse code
- organize large programs
- avoid name collisions

Without modules, all code would exist in one file.

---

## Importing a Module

### Basic Import

    import math
    print(math.sqrt(16))

### Mental Model
- Python loads the module
- Creates a namespace
- You access members using `module.name`

---

## Importing Specific Names

    from math import sqrt
    print(sqrt(25))

### Difference from `import math`
- No module prefix needed
- Only imported names are available

---

## Importing Multiple Names

    from math import sqrt, pi
    print(pi)

---

## Aliasing Imports

    import math as m
    print(m.sqrt(9))

### Why Aliasing Is Used
- Shorter names
- Avoid conflicts

---

## Namespace Concept (PCEP CRITICAL)

Each module has its **own namespace**.

    import math
    print(math.pi)

`pi` exists in the `math` namespace, not the global one.

### PCEP Trap
This fails:

    print(pi)

Unless you explicitly import it.

---

## Standard Library Modules (PCEP Scope)

Common modules you must recognize:
- `math`
- `random`
- `sys`

Example:

    import random
    print(random.randint(1, 10))

---

## What Is a Package
A **package** is a collection of modules.

Conceptually:
- Folder containing modules
- Used to group related code

PCEP expects recognition, not package creation.

---

## The `__name__` Variable (IMPORTANT)

Every Python file has a special variable called `__name__`.

    print(__name__)

### When a File Is Run Directly

    __name__ == "__main__"

### When a File Is Imported

    __name__ == "module_name"

---

## Why `__name__ == "__main__"` Exists

It allows code to:
- run only when executed directly
- not run when imported

Example:

    if __name__ == "__main__":
        print("Run directly")

---

## PCEP Traps and Mistakes

- Forgetting module prefixes
- Confusing `import x` vs `from x import y`
- Assuming imports copy code (they don’t)
- Misunderstanding `__name__`

---

## Summary (Mental Model)
- Modules are Python files
- Imports load modules into memory
- Namespaces prevent conflicts
- Packages group modules
- `__name__` tells how code is executed

---

## Self-Test (Must Be Solid)

1. What is a module?
2. Why does `math.sqrt()` work but `sqrt()` may not?
3. What is the difference between importing a module and importing a name?
4. What does `__name__ == "__main__"` check?
5. Why are namespaces important?

If unsure, re-import modules and test variations.
