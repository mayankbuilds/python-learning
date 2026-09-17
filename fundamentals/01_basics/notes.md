# Python Basics

## 1. Variables

Python variables are names bound to objects.

```python
x = 10
```

Think:

```text
x ───► 10
```

Assignment does not mean that `x` is a fixed typed box.

Python is dynamically typed, so a name can be rebound to objects of different types.

```python
x = 10
x = "hello"
```

Now `x` refers to a string.

---

## 2. Common Built-in Types

| Type | Example |
| :--- | :--- |
| `int` | `10` |
| `float` | `10.5` |
| `str` | `"hello"` |
| `bool` | `True`, `False` |
| `NoneType` | `None` |

Check a value's type:

```python
x = 10
print(type(x))
```

---

## 3. `=` vs `==`

### `=`
Assignment / binding.

```python
x = 10
```

### `==`
Equality comparison.

```python
x == 10
```

It produces a Boolean:

```python
True
False
```

---

## 4. Rebinding

```python
x = 10
y = x

x = 20
```

Now:

```text
x ───► 20
y ───► 10
```

Changing what `x` refers to does not automatically change `y`.

---

## 5. Dynamic Typing

Python determines the runtime type from the object.

```python
x = 10
print(type(x))       # int

x = "hello"
print(type(x))       # str
```

The name `x` can refer to different types at different times.

---

## 6. Type Conversion

Common conversions:

```python
int("10")       # 10
float("10.5")   # 10.5
str(100)        # "100"
float(10)       # 10.0
int(10.8)       # 10
```

Important:

```python
int("10.5")             # ValueError
int(float("10.5"))      # 10
```

`int()` can convert a numeric value such as `10.8` to `10`, but direct parsing of `"10.8"` as an integer fails.

---

## 7. Type Annotations

```python
age: int = 20
```

This communicates the intended type.

It does NOT automatically prevent:

```python
age = "hello"
```

from being assigned at runtime.

Type annotations are mainly useful for documentation and static type checking.

---

## Strings

### 8. Creating Strings

```python
name = "Mayank"
language = 'Python'
```

Both single and double quotes can be used.

### 9. String Indexing

Python uses zero-based indexing.

```text
String:  M  a  y  a  n  k
Index:   0  1  2  3  4  5
```

Examples:

```python
name[0]      # M
name[2]      # y
name[-1]     # k
name[-3]     # a
```

Negative indexing starts from the end.

### 10. String Slicing

General syntax:

```python
text[start:stop]
```

Start is included. Stop is excluded.

```python
text = "Python"

text[1:4]    # "yth"
text[:3]     # "Pyt"
text[3:]     # "hon"
text[:]      # "Python"
```

Mental model:

```text
[start : stop)
  ↑       ↑
included excluded
```

### 11. Negative Slicing

```python
text = "Python"

text[-4:-1]    # "tho"
```

Always map the indexes first if unsure.

### 12. Strings Are Immutable

You cannot modify an existing string in-place.

```python
text = "Python"

text[0] = "J"     # Error
```

Instead, create a new string:

```python
text = "J" + text[1:]
```

Now:

```text
text → "Jython"
```

### 13. String Methods

Common methods:

```python
text.upper()
text.lower()
text.capitalize()
text.strip()
```

Example:

```python
name = "Mayank"

x = name.upper()

print(name)    # Mayank
print(x)       # MAYANK
```

Because strings are immutable, `upper()` returns a new string.

---

## 14. `input()`

`input()` returns user input as a string.

```python
x = input()
```

If the user enters:

```text
25
```

then:

```python
type(x)
```

is:

```text
<class 'str'>
```

To read an integer:

```python
age = int(input())
```

To read a float:

```python
price = float(input())
```

---

## Important Mistakes / Traps

### Trap 1 — `input()` is not automatically numeric

```python
x = input()
```

Even if the user enters `100`, `x` is a `str`.

### Trap 2 — Direct decimal-string conversion

```python
int("10.5")  # Raises ValueError
```

Use:

```python
int(float("10.5"))  # 10
```

if the intended operation is to parse the decimal and then convert it to an integer.

### Trap 3 — Rebinding is not mutation

```python
x = 10
y = x

x = "hello"
```

The integer `10` was NOT converted into `"hello"`.

`x` was simply rebound to a different object.

---

## Quick Reference

```python
# Type
type(x)

# Conversion
int(x)
float(x)
str(x)

# Input
x = input()
x = int(input())
x = float(input())

# Indexing
text[0]
text[-1]

# Slicing
text[start:stop]
text[:stop]
text[start:]
text[:]

# String methods
text.upper()
text.lower()
text.capitalize()
text.strip()
```