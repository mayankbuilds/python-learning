# Python Functions

## Function Basics
A function is a reusable block of code designed to perform a specific task.

```python
def greet():
    print("Hello, Mayank")

greet()
```

A function executes when it is called.

## Parameters and Arguments
- Parameter: variable in the function definition.
- Argument: actual value passed when calling the function.

```python
def greet(name):
    print(f"Hello {name}")

greet("Mayank")
```

## `print()` vs `return`
`print()` displays a value. A function without an explicit `return` returns `None`.

```python
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result)
```

Output:
```text
30
None
```

`return` sends a value back to the caller and immediately terminates the function.

```python
def add(a, b):
    return a + b
```

## Scope

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Output:
```text
20
10
```

The inner `x` is local and does not modify the global `x`.

Python name lookup generally follows **LEGB**: Local, Enclosing, Global, Built-in.

## Default Parameters

```python
def power(base, exponent=2):
    return base ** exponent

power(5)      # 25
power(5, 3)   # 125
```

A required parameter cannot follow a default parameter.

```python
def test(a=10, b):  # Invalid
    pass
```

```python
def test(a, b=10):  # Valid
    pass
```

## Positional and Keyword Arguments

```python
def introduce(name, age):
    print(name, age)

introduce("Mayank", 20)
introduce(age=20, name="Mayank")
introduce("Mayank", age=20)
```

Positional arguments must come before keyword arguments.

## `*args`
`*args` collects a variable number of positional arguments into a tuple.

```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
```

`args` is a conventional name; it can be changed.

```text
*args → variable positional arguments → tuple
```

## `**kwargs`
`**kwargs` collects a variable number of keyword arguments into a dictionary.

```python
def show(**kwargs):
    print(kwargs)

show(name="Mayank", age=20, course="AIML")
```

Output:
```text
{'name': 'Mayank', 'age': 20, 'course': 'AIML'}
```

```text
**kwargs → variable keyword arguments → dictionary
```

## Keyword-Only Parameters
A bare `*` makes parameters after it keyword-only.

```python
def connect(host, *, port, timeout=30):
    pass
```

Valid:
```python
connect("localhost", port=8000)
connect(host="localhost", port=8000)
connect("localhost", port=8000, timeout=10)
```

Invalid:
```python
connect("localhost", 8000)
```

Important distinction:
- `*args` collects positional arguments.
- bare `*` makes following parameters keyword-only.

## Lambda Functions
A lambda is a small anonymous function.

```python
square = lambda x: x * x
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
```

Syntax:
```text
lambda parameters: expression
```

Lambdas are useful for small functions, commonly with `map()`, `filter()`, and `sorted()`.

## `map()`
`map()` applies a function to every element.

```python
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
```

Result:
```text
[2, 4, 6, 8, 10]
```

`map()` transforms elements. In Python 3 it returns a map object, so `list()` is used when a list is needed.

## `filter()`
`filter()` keeps elements for which the condition is true.

```python
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
```

Result:
```text
[2, 4, 6]
```

```text
map()    → transform elements
filter() → select elements satisfying a condition
```

## `sorted()` with Lambda
Use `key` to specify what value should be used for sorting.

```python
students = [
    ("Mayank", 85),
    ("Rahul", 72),
    ("Aman", 91)
]

result = sorted(students, key=lambda student: student[1], reverse=True)
```

`student[1]` is the second tuple element, so marks are used as the sorting key.

## First-Class Functions
Python functions are first-class objects. They can be stored in variables, passed as arguments, and returned from functions.

### Store a function

```python
def multiply(a, b):
    return a * b

operation = multiply
print(operation(5, 4))
```

`operation = multiply` stores a reference to the function; it does not call it.

### Pass a function

```python
def add_one(x):
    return x + 1

def apply(func, value):
    return func(value)

print(apply(add_one, 10))
```

### Return a function

```python
def create_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = create_multiplier(3)
print(triple(10))
```

`triple` refers to the returned inner `multiply` function.

## Closures
A closure occurs when an inner function remembers/accesses a variable from its enclosing function even after the enclosing function has returned.

```python
def create_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

Each returned function retains access to its enclosing `n`. Closures are an important foundation for understanding decorators.

## Docstrings
A docstring documents a function and is written immediately inside it.

```python
def square(n):
    """Return the square of n."""
    return n * n
```

It can be accessed with:

```python
print(square.__doc__)
```

A docstring is documentation associated with the function, unlike an ordinary comment.

## Type Hints
Type hints communicate intended types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int` → expected `int`
- `b: int` → expected `int`
- `-> int` → expected return type

Type hints do not by themselves enforce runtime types.

## Common Mistakes

1. Confusing `print()` and `return`: use `return` when the caller needs the value.
2. Forgetting that `return` ends the function.
3. Confusing parameter and argument.
4. Confusing `*args` and `**kwargs`.
5. Thinking type hints enforce types at runtime.
6. Confusing a function (`square`) with a function call (`square(5)`).
7. Using unnecessary global result variables; prefer local state and `return`.

## Quick Reference

```python
def add(a, b):
    return a + b

def greet(name="Mayank"):
    return f"Hello {name}"

def test(*args):
    ...

def test(**kwargs):
    ...

def connect(host, *, port):
    ...

square = lambda x: x * x
list(map(lambda x: x * 2, numbers))
list(filter(lambda x: x % 2 == 0, numbers))
sorted(students, key=lambda x: x[1], reverse=True)

operation = add
apply(add_one, 10)
```

## Completion Checklist
- [x] Function definition and calling
- [x] Parameters and arguments
- [x] `print()` vs `return`
- [x] Return terminates a function
- [x] Local/global scope and LEGB basics
- [x] Default parameters
- [x] Positional and keyword arguments
- [x] `*args`
- [x] `**kwargs`
- [x] Keyword-only parameters
- [x] Lambda functions
- [x] `map()`
- [x] `filter()`
- [x] `sorted(key=...)`
- [x] First-class functions
- [x] Returning functions
- [x] Closures
- [x] Docstrings
- [x] Type hints
