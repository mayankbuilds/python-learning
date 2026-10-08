# Python Cheatsheet

## 1. Basic Syntax

```python
print("Hello")

name = "Mayank"
age = 20
price = 99.5
is_active = True
value = None
```

Check a type:

```python
type(value)
```

Comments:

```python
# This is a comment
```

------------------------------------------------------------
## 2. Common Data Types
------------------------------------------------------------

```python
int       # 10
float     # 10.5
str       # "hello"
bool      # True / False
NoneType  # None
list      # [1, 2, 3]
tuple     # (1, 2, 3)
set       # {1, 2, 3}
dict      # {"name": "Mayank"}
```

------------------------------------------------------------
## 3. Type Conversion
------------------------------------------------------------

```python
int("10")
float("10.5")
str(10)
bool(1)
```

Remember:

```python
int("10.5")        # ValueError
int(float("10.5")) # 10
```

------------------------------------------------------------
## 4. Strings
------------------------------------------------------------

```python
text = "Python"
```

Indexing:

```python
text[0]
text[-1]
```

Slicing:

```python
text[start:stop]
text[:3]
text[2:]
text[::2]
```

Useful methods:

```python
text.lower()
text.upper()
text.strip()
text.replace("P", "J")
text.split()
```

f-string:

```python
name = "Mayank"
age = 20

print(f"{name} is {age} years old")
```

Strings are immutable.

------------------------------------------------------------
## 5. Input
------------------------------------------------------------

```python
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))
```

`input()` returns a string.

------------------------------------------------------------
## 6. Operators
------------------------------------------------------------

Arithmetic:

```python
+   -   *   /   //   %   **
```

Comparison:

```python
==  !=  >  <  >=  <=
```

Logical:

```python
and
or
not
```

Membership:

```python
in
not in
```

------------------------------------------------------------
## 7. Conditional Statements
------------------------------------------------------------

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

Example:

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Python uses indentation to define blocks.

------------------------------------------------------------
## 8. Loops
------------------------------------------------------------

### `for`

```python
for x in range(5):
    print(x)
```

### `range()`

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Example:

```python
for x in range(10, 0, -1):
    print(x)
```

### `while`

```python
while condition:
    ...
```

### Loop control

```python
break
continue
```

------------------------------------------------------------
## 9. Functions
------------------------------------------------------------

Basic:

```python
def add(a, b):
    return a + b
```

Call:

```python
result = add(2, 3)
```

Default parameter:

```python
def greet(name="Guest"):
    print(name)
```

Keyword argument:

```python
greet(name="Mayank")
```

Variable positional arguments:

```python
def total(*args):
    return sum(args)
```

Variable keyword arguments:

```python
def show(**kwargs):
    print(kwargs)
```

Keyword-only parameters:

```python
def connect(host, *, port, timeout=30):
    ...
```

Lambda:

```python
square = lambda x: x ** 2
```

Higher-order functions:

```python
map(function, iterable)
filter(function, iterable)
sorted(iterable, key=function)
```

Useful example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

------------------------------------------------------------
## 10. Lists
------------------------------------------------------------

```python
numbers = [10, 20, 30]
```

Access:

```python
numbers[0]
numbers[-1]
numbers[1:3]
```

Modify:

```python
numbers[0] = 100
```

Methods:

```python
numbers.append(40)
numbers.extend([50, 60])
numbers.insert(1, 15)
numbers.remove(20)
numbers.pop()
numbers.pop(1)
numbers.sort()
numbers.reverse()
numbers.count(10)
numbers.index(30)
```

Copy:

```python
copy = numbers.copy()
```

Comprehension:

```python
squares = [x ** 2 for x in range(5)]
evens = [x for x in numbers if x % 2 == 0]
```

------------------------------------------------------------
## 11. Tuples
------------------------------------------------------------

```python
point = (10, 20)
```

Access:

```python
point[0]
```

Tuple unpacking:

```python
x, y = point
```

Swap:

```python
a, b = b, a
```

Tuples are immutable.

------------------------------------------------------------
## 12. Sets
------------------------------------------------------------

```python
numbers = {1, 2, 3}
empty_set = set()
```

Methods:

```python
numbers.add(4)
numbers.remove(2)
numbers.discard(10)
```

Operations:

```python
a | b  # union
a & b  # intersection
a - b  # difference
```

Remove duplicates:

```python
unique = set(numbers)
```

Sets do not support positional indexing.

------------------------------------------------------------
## 13. Dictionaries
------------------------------------------------------------

```python
student = {
    "name": "Mayank",
    "age": 20
}
```

Access:

```python
student["name"]
student.get("age")
student.get("branch", "Unknown")
```

Add/update:

```python
student["branch"] = "CSE AI/ML"
student["age"] = 21
```

Remove:

```python
student.pop("age")
del student["name"]
```

Iteration:

```python
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
```

Comprehension:

```python
squares = {x: x ** 2 for x in range(5)}
```

------------------------------------------------------------
## 14. Exceptions
------------------------------------------------------------

Basic:

```python
try:
    ...
except ValueError:
    ...
```

Multiple exceptions:

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
```

Exception object:

```python
except ValueError as e:
    print(e)
```

`else`:

```python
try:
    ...
except ValueError:
    ...
else:
    ...
```

`finally`:

```python
try:
    ...
except ValueError:
    ...
finally:
    ...
```

Raise:

```python
raise ValueError("Invalid value")
```

Re-raise:

```python
except Exception:
    raise
```

------------------------------------------------------------
## 15. Modules
------------------------------------------------------------

Import a module:

```python
import math
```

Use it:

```python
math.sqrt(25)
```

Import a specific name:

```python
from math import sqrt
```

Alias:

```python
import math as m
```

Own module:

```text
calculator.py
```

```python
from calculator import add
```

------------------------------------------------------------
## 16. `__name__`
------------------------------------------------------------

Common pattern:

```python
if __name__ == "__main__":
    main()
```

Direct execution:

```text
__name__ == "__main__"
```

Imported module:

```text
__name__ == module name
```

------------------------------------------------------------
## 17. Packages
------------------------------------------------------------

Example:

```text
utils/
    __init__.py
    calculator.py
    validators.py
```

Import:

```python
from utils.calculator import add
```

A package organizes related modules.

------------------------------------------------------------
## 18. File Handling
------------------------------------------------------------

Open:

```python
file = open("data.txt", "r")
```

Preferred:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Modes:

```text
r -> read
w -> write / overwrite
a -> append
x -> create, fail if exists
```

Read:

```python
file.read()
file.readline()
file.readlines()
```

Write:

```python
file.write("Hello
")
```

Useful path concepts:

```python
import os

os.getcwd()
```

------------------------------------------------------------
## 19. OOP
------------------------------------------------------------

Class:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"
```

Object:

```python
person = Person("Mayank")
person.greet()
```

Instance attribute:

```python
self.name
```

Class attribute:

```python
class Person:
    species = "Human"
```

Inheritance:

```python
class Student(Person):
    pass
```

`super()`:

```python
class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch
```

Method overriding:

```python
class Student(Person):
    def greet(self):
        return "Hello from Student"
```

Abstract class:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

Class method:

```python
@classmethod
def create(cls):
    return cls()
```

Static method:

```python
@staticmethod
def add(a, b):
    return a + b
```

Property:

```python
@property
def balance(self):
    return self._balance
```

Composition:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

Mental models:

```text
Inheritance -> IS-A
Composition -> HAS-A
```

------------------------------------------------------------
## 20. Iterators
------------------------------------------------------------

Create iterator:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
```

Get values:

```python
next(iterator)
```

When exhausted:

```text
StopIteration
```

Iterator protocol:

```python
__iter__()
__next__()
```

A `for` loop conceptually uses:

```python
iterator = iter(iterable)

while True:
    try:
        value = next(iterator)
    except StopIteration:
        break
```

------------------------------------------------------------
## 21. Generators
------------------------------------------------------------

Generator function:

```python
def count():
    yield 1
    yield 2
    yield 3
```

Use:

```python
numbers = count()

next(numbers)
next(numbers)
next(numbers)
```

`yield`:

```text
produce value -> pause -> resume later
```

Generator expression:

```python
numbers = (x ** 2 for x in range(5))
```

List comprehension creates/stores values immediately.

Generator expressions produce values lazily.

------------------------------------------------------------
## 22. Decorators
------------------------------------------------------------

Basic pattern:

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result

    return wrapper
```

Use:

```python
@decorator
def greet():
    print("Hello")
```

Equivalent idea:

```python
greet = decorator(greet)
```

Decorators are useful for:

```text
logging
timing
authentication
validation
caching
access control
```

------------------------------------------------------------
## 23. Virtual Environments
------------------------------------------------------------

Create:

```bash
python -m venv .venv
```

Activate on Linux/macOS:

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

Add to `.gitignore`:

```text
.venv/
```

------------------------------------------------------------
## 24. pip
------------------------------------------------------------

Install:

```bash
pip install requests
```

List:

```bash
pip list
```

Package information:

```bash
pip show requests
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

------------------------------------------------------------
## 25. Environment Variables
------------------------------------------------------------

Shell:

```bash
export API_KEY="secret"
```

Python:

```python
import os

api_key = os.getenv("API_KEY")
```

Keep secrets out of Git.

Typical `.gitignore`:

```text
.env
.env.*
```

------------------------------------------------------------
## 26. Async Programming
------------------------------------------------------------

Define async function:

```python
async def fetch_data():
    ...
```

Calling it creates a coroutine object.

Await it:

```python
result = await fetch_data()
```

Run an async program:

```python
import asyncio

asyncio.run(main())
```

Run independent async operations together:

```python
await asyncio.gather(
    task_a(),
    task_b(),
    task_c()
)
```

Event loop:

```text
manages and schedules async work
```

Async is especially useful for I/O-bound operations:

```text
API requests
database queries
network operations
```

Mental model:

```text
async def
   ↓
coroutine
   ↓
await
   ↓
pause while waiting
   ↓
event loop runs other async work
   ↓
operation completes
   ↓
coroutine resumes
```

Async does not automatically mean parallel CPU execution.

------------------------------------------------------------
## 27. Most Important Python Patterns
------------------------------------------------------------

### Function

```python
def function(arg):
    return result
```

### List comprehension

```python
result = [expression for item in iterable]
```

### Conditional comprehension

```python
result = [expression for item in iterable if condition]
```

### Dictionary comprehension

```python
result = {key: value for item in iterable}
```

### Exception handling

```python
try:
    ...
except Exception:
    ...
```

### File handling

```python
with open("file.txt") as file:
    data = file.read()
```

### Main guard

```python
if __name__ == "__main__":
    main()
```

### Decorator

```python
@decorator
def function():
    ...
```

### Generator

```python
def generator():
    yield value
```

### Async function

```python
async def function():
    result = await something()
```

------------------------------------------------------------
## 28. Python Learning Checklist
------------------------------------------------------------

- [x] Basics
- [x] Control Flow
- [x] Functions
- [x] Data Structures
- [x] Exception Handling
- [x] Modules & Packages
- [x] File Handling
- [x] OOP
- [x] Iterators & Generators
- [x] Decorators
- [x] Virtual Environments & pip
- [x] Async Programming