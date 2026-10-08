# Decorators

## 1. What Is a Decorator?

A **decorator** is a function that takes another function, adds or changes behavior, and returns a function.

Mental model:

```text
Original function
       ↓
   Decorator
       ↓
Modified / wrapped function
```

Decorators are useful when you want to add common behavior without changing the original function's code.

---

## 2. Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper
```

Use it:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)

greet()
```

Output:

```text
Before function
Hello
After function
```

Here:

```python
my_decorator(greet)
```

returns `wrapper`, so `greet` now refers to the wrapper function.

---

## 3. `@` Decorator Syntax

Python provides a shorter syntax:

```python
@my_decorator
def greet():
    print("Hello")
```

This is equivalent to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

### Important

```python
@decorator
def function():
    ...
```

means approximately:

```python
function = decorator(function)
```

The decorator is applied when the function is defined.

---

## 4. Wrapper Function

The inner function is commonly called a **wrapper**.

```python
def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper
```

The wrapper controls when and how the original function runs.

```text
Call wrapper
    ↓
Extra behavior
    ↓
Original function
    ↓
More extra behavior
```

---

## 5. Decorators with Arguments

A decorator should usually use `*args` and `**kwargs` when the wrapped function can accept different arguments.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")

        result = func(*args, **kwargs)

        print("End")
        return result

    return wrapper
```

Example:

```python
@decorator
def add(a, b):
    return a + b

print(add(2, 3))
```

Output:

```text
Start
End
5
```

### Why `*args` and `**kwargs`?

They allow the wrapper to accept:

- any number of positional arguments
- any number of keyword arguments

and pass them to the original function.

---

## 6. Returning the Original Result

A common mistake is forgetting to return the result.

Wrong:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # forgot return

    return wrapper
```

Then the decorated function returns `None`.

Correct:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
```

---

## 7. `functools.wraps`

Decorators replace the original function with the wrapper.

Because of this, function metadata such as the function's name and docstring can be lost.

Use:

```python
from functools import wraps
```

Example:

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")

        result = func(*args, **kwargs)

        print("End")
        return result

    return wrapper
```

`@wraps(func)` preserves important metadata from the original function.

For example:

```python
print(add.__name__)
```

can remain:

```text
add
```

instead of:

```text
wrapper
```

---

## 8. Practical Example: Logging

Decorators are useful for adding logging without modifying every function.

```python
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished {func.__name__}")
        return result

    return wrapper
```

Usage:

```python
@log_call
def add(a, b):
    return a + b

print(add(2, 3))
```

The original `add()` function does not need to contain the logging code.

---

## 9. Why Decorators Are Useful

Decorators are useful for behavior that should be applied to many functions.

Common examples:

- logging
- timing
- authentication/authorization
- validation
- caching
- access control
- retry behavior

Instead of repeating the same code inside many functions, the behavior can be placed in a decorator.

---

## 10. Decorators and Closures

Decorators use concepts already learned:

- functions are first-class objects
- functions can be passed as arguments
- functions can be returned
- nested functions
- closures

Example:

```python
def decorator(func):
    def wrapper():
        func()

    return wrapper
```

The `wrapper` function remembers the `func` variable from the enclosing scope.

This is a **closure**.

Mental model:

```text
decorator(func)
      ↓
 wrapper remembers func
      ↓
 wrapper returned
```

---

## 11. Decorators in FastAPI

FastAPI heavily uses decorators.

Example:

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

Here:

```python
@app.get("/")
```

is decorator syntax.

It tells FastAPI that `home()` should handle requests for the `/` route.

Another example:

```python
@app.post("/users")
def create_user():
    ...
```

The decorator connects the Python function to a web route.

---

## 12. Common Mistakes

### Mistake 1: Forgetting to return the wrapper

Wrong:

```python
def decorator(func):
    def wrapper():
        func()
```

Correct:

```python
def decorator(func):
    def wrapper():
        func()

    return wrapper
```

---

### Mistake 2: Forgetting `*args` and `**kwargs`

A wrapper without arguments may fail when decorating functions that receive arguments.

Use:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

---

### Mistake 3: Forgetting to return the original result

Wrong:

```python
def wrapper(*args, **kwargs):
    func(*args, **kwargs)
```

Correct:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

---

### Mistake 4: Forgetting `@wraps`

Without `@wraps`, useful function metadata can be replaced by wrapper metadata.

Use:

```python
from functools import wraps
```

and:

```python
@wraps(func)
```

---

## 13. Quick Revision

| Concept | Meaning |
|---|---|
| Decorator | Function that modifies/wraps another function |
| Wrapper | Inner function that controls the decorated function |
| `@decorator` | Short syntax for `function = decorator(function)` |
| `*args` | Accepts positional arguments |
| `**kwargs` | Accepts keyword arguments |
| `@wraps(func)` | Preserves original function metadata |
| Closure | Inner function remembers variables from enclosing scope |

## Core Pattern

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

## Checklist

- [x] What decorators are
- [x] Basic decorator
- [x] Wrapper functions
- [x] `@decorator` syntax
- [x] `*args` and `**kwargs`
- [x] Returning the original result
- [x] `functools.wraps`
- [x] Practical logging example
- [x] Decorators and closures
- [x] FastAPI decorator usage
- [x] Common mistakes
