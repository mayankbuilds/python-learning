# Common Python Mistakes

This file contains mistakes and traps worth remembering while learning
Python. Keep this focused on mistakes that can cause incorrect behavior,
confusion, or bugs.

------------------------------------------------------------
## 1. `=` vs `==`
------------------------------------------------------------

`=` assigns a value.

```python
x = 10
```

`==` compares two values.

```python
x == 10
```

Mental model:

```text
=   -> assign
==  -> compare
```

------------------------------------------------------------
## 2. `input()` Always Returns a String
------------------------------------------------------------

Even if the user enters a number:

```python
age = input("Enter age: ")
```

`age` is a `str`.

Convert it when numeric input is required:

```python
age = int(input("Enter age: "))
```

For decimal input:

```python
price = float(input("Enter price: "))
```

------------------------------------------------------------
## 3. `int("10.5")` Is Invalid
------------------------------------------------------------

This raises `ValueError`:

```python
int("10.5")
```

Correct:

```python
float("10.5")
```

or:

```python
int(float("10.5"))
```

------------------------------------------------------------
## 4. `print()` vs `return`
------------------------------------------------------------

`print()` displays something.

```python
def add(a, b):
    print(a + b)
```

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b
```

A function without an explicit `return` returns `None`.

------------------------------------------------------------
## 5. Forgetting That `return` Ends a Function
------------------------------------------------------------

Code after an executed `return` does not run.

```python
def test():
    return 10
    print("Hello")  # never runs
```

------------------------------------------------------------
## 6. Function vs Function Call
------------------------------------------------------------

These are different:

```python
add
```

refers to the function.

```python
add(2, 3)
```

calls the function.

This matters when passing functions as arguments.

------------------------------------------------------------
## 7. Local vs Global Variables
------------------------------------------------------------

A variable created inside a function is normally local to that function.

```python
x = 10

def test():
    x = 20
    return x
```

Calling `test()` returns `20`, but the global `x` is still `10`.

Avoid unnecessary global state.

------------------------------------------------------------
## 8. Mutable Objects Can Change
------------------------------------------------------------

Lists are mutable:

```python
numbers = [1, 2, 3]
numbers[0] = 100
```

Now:

```python
[100, 2, 3]
```

Strings and tuples are immutable.

------------------------------------------------------------
## 9. Assignment Can Create Another Reference
------------------------------------------------------------

This does NOT create a copy:

```python
a = [1, 2, 3]
b = a
```

Both names refer to the same list.

```python
b.append(4)
```

also changes `a`.

Use a shallow copy when appropriate:

```python
b = a.copy()
```

or:

```python
b = a[:]
```

------------------------------------------------------------
## 10. `append()` vs `extend()`
------------------------------------------------------------

`append()` adds one object:

```python
numbers = [1, 2]
numbers.append([3, 4])
```

Result:

```python
[1, 2, [3, 4]]
```

`extend()` adds elements from an iterable:

```python
numbers = [1, 2]
numbers.extend([3, 4])
```

Result:

```python
[1, 2, 3, 4]
```

------------------------------------------------------------
## 11. `sort()` vs `sorted()`
------------------------------------------------------------

`sort()` modifies the original list and returns `None`.

```python
numbers.sort()
```

`sorted()` creates and returns a new sorted list.

```python
new_numbers = sorted(numbers)
```

------------------------------------------------------------
## 12. `remove()` vs `pop()`
------------------------------------------------------------

`remove(value)` removes by value.

```python
numbers.remove(20)
```

`pop(index)` removes by index and returns the removed value.

```python
value = numbers.pop(1)
```

Calling `pop()` without an index removes the last element.

------------------------------------------------------------
## 13. `remove()` vs `discard()` for Sets
------------------------------------------------------------

For sets:

```python
my_set.remove(10)
```

raises `KeyError` if `10` does not exist.

```python
my_set.discard(10)
```

does nothing if `10` does not exist.

------------------------------------------------------------
## 14. `{}` Is an Empty Dictionary
------------------------------------------------------------

This:

```python
x = {}
```

creates an empty dictionary.

An empty set is:

```python
x = set()
```

------------------------------------------------------------
## 15. Dictionary Missing Key
------------------------------------------------------------

This raises `KeyError` if the key does not exist:

```python
student["age"]
```

Safer lookup:

```python
student.get("age")
```

Or provide a default:

```python
student.get("age", 0)
```

------------------------------------------------------------
## 16. Dictionary Membership Checks Keys
------------------------------------------------------------

```python
"name" in student
```

checks whether `"name"` is a key.

It does not check values.

------------------------------------------------------------
## 17. Shallow Copy and Nested Lists
------------------------------------------------------------

A shallow copy creates a new outer list, but nested mutable objects can still be shared.

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)
```

The inner list is shared, so `a` can also change.

------------------------------------------------------------
## 18. `range()` Stop Value Is Exclusive
------------------------------------------------------------

```python
range(1, 5)
```

produces:

```text
1 2 3 4
```

It does not include `5`.

For a countdown:

```python
range(n, 0, -1)
```

produces:

```text
n ... 2 1
```

------------------------------------------------------------
## 19. `and` and `or` Return Operands
------------------------------------------------------------

Python's `and` and `or` do not necessarily return `True` or `False`.

Example:

```python
result = "" or "Hello"
```

Result:

```python
"Hello"
```

They also use short-circuit evaluation.

------------------------------------------------------------
## 20. `break` vs `continue`
------------------------------------------------------------

`break` exits the loop completely.

```python
for x in numbers:
    if x == 3:
        break
```

`continue` skips the current iteration and moves to the next one.

```python
for x in numbers:
    if x == 3:
        continue
```

------------------------------------------------------------
## 21. `*args` vs `**kwargs`
------------------------------------------------------------

`*args` collects extra positional arguments into a tuple.

```python
def test(*args):
    print(args)
```

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def test(**kwargs):
    print(kwargs)
```

------------------------------------------------------------
## 22. Type Hints Do Not Enforce Types at Runtime
------------------------------------------------------------

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints describe the expected types. Python does not automatically enforce them at runtime.

------------------------------------------------------------
## 23. `__name__` and `__main__`
------------------------------------------------------------

When a Python file is executed directly:

```python
__name__ == "__main__"
```

When imported, `__name__` is normally the module name.

Common pattern:

```python
if __name__ == "__main__":
    main()
```

This runs `main()` only when the file is executed directly.

------------------------------------------------------------
## 24. `read()` vs `readline()` vs `readlines()`
------------------------------------------------------------

`read()` returns the remaining file content as one string.

```python
content = file.read()
```

`readline()` reads the next line.

```python
line = file.readline()
```

`readlines()` returns the remaining lines as a list.

```python
lines = file.readlines()
```

------------------------------------------------------------
## 25. `w` vs `a` File Mode
------------------------------------------------------------

`w` writes and overwrites existing content.

```python
open("file.txt", "w")
```

`a` appends to existing content.

```python
open("file.txt", "a")
```

------------------------------------------------------------
## 26. Prefer `with open(...)`
------------------------------------------------------------

Instead of manually managing `close()`:

```python
file = open("data.txt", "r")
data = file.read()
file.close()
```

prefer:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The context manager handles closing the file.

------------------------------------------------------------
## 27. Exception Flow
------------------------------------------------------------

When an exception occurs inside `try`, Python skips the remaining statements
in that `try` block and looks for a matching `except`.

```python
try:
    print("A")
    10 / 0
    print("B")  # skipped
except ZeroDivisionError:
    print("Error")
```

------------------------------------------------------------
## 28. `else` and `finally`
------------------------------------------------------------

`else` runs only if no exception occurs in `try`.

`finally` runs whether an exception occurs or not.

```python
try:
    ...
except ValueError:
    ...
else:
    ...
finally:
    ...
```

------------------------------------------------------------
## 29. `raise` vs `return`
------------------------------------------------------------

`return` sends a normal result back.

```python
return value
```

`raise` signals an exception.

```python
raise ValueError("Invalid value")
```

------------------------------------------------------------
## 30. Module vs Package
------------------------------------------------------------

A module is generally a Python file:

```text
calculator.py
```

A package organizes related modules:

```text
utils/
    calculator.py
    validators.py
```

------------------------------------------------------------
## 31. Iterable vs Iterator
------------------------------------------------------------

A list is iterable:

```python
numbers = [1, 2, 3]
```

but it is not itself an iterator.

```python
next(numbers)  # TypeError
```

Create an iterator:

```python
iterator = iter(numbers)
next(iterator)
```

------------------------------------------------------------
## 32. `yield` vs `return`
------------------------------------------------------------

`return` finishes the function.

`yield` produces a value and pauses a generator.

```python
def numbers():
    yield 1
    yield 2
```

The generator resumes when `next()` is called again.

------------------------------------------------------------
## 33. Decorator Must Return the Wrapper
------------------------------------------------------------

A decorator normally returns the wrapper:

```python
def decorator(func):
    def wrapper():
        func()

    return wrapper
```

Without `return wrapper`, the decorated function will not work as intended.

------------------------------------------------------------
## 34. Decorator Must Usually Return the Original Result
------------------------------------------------------------

If the wrapped function returns a value:

```python
def add(a, b):
    return a + b
```

the wrapper should preserve it:

```python
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```

------------------------------------------------------------
## 35. Use `@wraps`
------------------------------------------------------------

When writing decorators:

```python
from functools import wraps

@wraps(func)
def wrapper(*args, **kwargs):
    ...
```

This preserves important metadata such as the original function name and docstring.

------------------------------------------------------------
## 36. Virtual Environment Mistakes
------------------------------------------------------------

Make sure the correct virtual environment is activated before installing
project dependencies.

```bash
source .venv/bin/activate
```

Do not commit the virtual environment itself.

Add:

```text
.venv/
```

to `.gitignore`.

------------------------------------------------------------
## 37. Do Not Commit Secrets
------------------------------------------------------------

Do not hardcode or commit API keys, passwords, database credentials, or
other secrets.

Use environment variables and keep local `.env` files out of Git.

------------------------------------------------------------
## 38. Async Function Calls Produce Coroutines
------------------------------------------------------------

Calling:

```python
async def fetch():
    ...
```

like:

```python
result = fetch()
```

produces a coroutine object.

Inside async code, an async operation commonly needs:

```python
result = await fetch()
```

------------------------------------------------------------
## 39. Async Does Not Automatically Mean Parallel
------------------------------------------------------------

Async is mainly useful for concurrency, especially while waiting for I/O.

It does not automatically make CPU-heavy operations run in parallel.

------------------------------------------------------------