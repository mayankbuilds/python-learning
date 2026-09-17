# Python Control Flow

## 1. `if`

Used to execute code conditionally.

```python
age = 20

if age >= 18:
    print("Adult")
```

Python uses `:` to start a block and indentation to define the block.

---

## 2. `if` / `elif` / `else`

```python
marks = 72

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")
```

Python checks conditions from top to bottom.

The first condition that is `True` is executed.

---

## 3. Comparison Operators

```python
x == y     # equal
x != y     # not equal
x > y      # greater than
x < y      # less than
x >= y     # greater than or equal
x <= y     # less than or equal
```

Comparisons produce `True` or `False`.

---

## Logical Operators

### 4. `and`

Both conditions must be true for the combined condition to be true.

```python
age = 20
student = True

if age >= 18 and student:
    print("Allowed")
```

### 5. `or`

At least one condition must be true.

```python
age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Allowed")
```

### 6. `not`

Reverses a Boolean value.

```python
x = True

if not x:
    print("False")
```

---

## Truthy and Falsy

Python allows values to be evaluated in Boolean contexts.

Common falsy values:
- `False`
- `0`
- `0.0`
- `""`
- `None`

Many other values are truthy:
- `True`
- `1`
- `-5`
- `"hello"`

Example:

```python
username = ""

if username:
    print("Username exists")
else:
    print("No username")
```

Output:

```text
No username
```

---

## Short-Circuit Evaluation

`and` and `or` return operands, not necessarily `True` or `False`.

### `and`

```python
10 and 20    # 20
0 and 20     # 0
```

Mental model:

```text
A and B

if A is falsy → return A
otherwise     → return B
```

### `or`

```python
10 or 20     # 10
0 or 20      # 20
```

Mental model:

```text
A or B

if A is truthy → return A
otherwise      → return B
```

---

## Loops

### 7. `for`

Used to iterate over a sequence/range.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### 8. `range()`

General form:

```python
range(start, stop, step)
```

The `stop` value is excluded.

Examples:

```python
range(5)
# 0 1 2 3 4

range(1, 5)
# 1 2 3 4

range(1, 10, 2)
# 1 3 5 7 9

range(5, 0, -1)
# 5 4 3 2 1
```

**Important:**

If moving backwards, use a negative step:

```python
range(5, 0, -1)
```

### 9. `for` + condition

Example: print even numbers.

```python
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
```

`%` gives the remainder.

`i % 2 == 0` means `i` is even.

### 10. `while`

Repeats while a condition remains true.

```python
x = 1

while x <= 5:
    print(x)
    x += 1
```

Output:

```text
1
2
3
4
5
```

### 11. `while True`

Can be used to create a loop that is intentionally infinite.

```python
while True:
    x = int(input())

    if x == 0:
        break

    print(x)
```

The loop terminates using `break`.

### 12. `break`

Immediately terminates the entire loop.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

### 13. `continue`

Skips the remaining code of the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

---

## `break` vs `continue`

| Statement | Effect |
| :--- | :--- |
| `break` | Terminates the entire loop |
| `continue` | Skips current iteration |

---

## Common Patterns

### Print 1 to N

```python
n = int(input())

for i in range(1, n + 1):
    print(i)
```

### Print N to 1

```python
n = int(input())

for i in range(n, 0, -1):
    print(i)
```

### Print even numbers

```python
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
```

### Sentinel-controlled loop

```python
while True:
    x = int(input())

    if x == 0:
        break

    print(x)
```

---

## Common Mistakes / Traps

### Trap 1 — `range(n)` excludes `n`

```python
range(10)
```

produces:

```text
0 → 9
```

not `0 → 10`.

### Trap 2 — Forgetting the negative step

Wrong:

```python
range(5, 0)
```

Correct:

```python
range(5, 0, -1)
```

### Trap 3 — `break` vs `continue`

```text
break:
STOP LOOP

continue:
SKIP THIS ITERATION
       ↓
NEXT ITERATION
```

### Trap 4 — First matching `elif`

```python
x = 95

if x >= 60:
    print("Pass")
elif x >= 90:
    print("Excellent")
```

Output:

```text
Pass
```

Because the first condition is already true.

---

## Quick Reference

```python
if condition:
    ...
elif condition:
    ...
else:
    ...

for i in range(start, stop, step):
    ...

while condition:
    ...

break
continue

and
or
not
```