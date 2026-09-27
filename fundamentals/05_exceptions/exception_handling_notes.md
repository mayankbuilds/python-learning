# Python Exception Handling — Notes

## 1. What is an Exception?

An **exception** is an error/event that occurs during program execution and interrupts the normal flow of the program.

Examples:

```python
10 / 0
```
→ `ZeroDivisionError`

```python
int("abc")
```
→ `ValueError`

```python
numbers = [1, 2, 3]
numbers[5]
```
→ `IndexError`

---

## 2. `try` and `except`

Basic structure:

```python
try:
    # code that might cause an exception
except:
    # handle the exception
```

Example:

```python
try:
    x = 10 / 0
except:
    print("Something went wrong")
```

Once an exception occurs inside `try`, Python skips the remaining code in that `try` block and searches for a matching `except`.

---

## 3. Catching Specific Exceptions

Prefer a specific exception when you know what can go wrong:

```python
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid number")
```

Common exceptions learned:

- `ValueError` — invalid value for an operation.
- `TypeError` — inappropriate object type.
- `IndexError` — sequence index is out of range.
- `ZeroDivisionError` — division by zero.
- `KeyError` — missing dictionary key.

---

## 4. Multiple `except` Blocks

```python
try:
    x = int(input("Enter number: "))
    result = 10 / x

except ValueError:
    print("Please enter an integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Only the matching handler executes.

---

## 5. Exception Object with `as`

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(e)
```

`e` contains the exception object/message.

---

## 6. Exception Execution Flow

```python
try:
    print("A")
    x = 10 / 0
    print("B")

except ZeroDivisionError:
    print("C")

print("D")
```

Output:

```text
A
C
D
```

`B` is skipped because the exception occurs before it.

---

## 7. `else`

`else` runs **only when no exception occurs** in the `try` block.

```python
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Successfully converted:", x)
```

Mental model:

```text
try     → attempt operation
except  → runs if exception occurs
else    → runs if no exception occurs
```

---

## 8. `finally`

`finally` runs **whether an exception occurs or not**.

```python
try:
    # operation
except:
    # handle error
finally:
    # always runs
```

Example:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
finally:
    print("Finished")
```

Output:

```text
Error
Finished
```

A common purpose of `finally` is cleanup, such as ensuring a resource is released.

---

## 9. `raise`

`raise` lets your program intentionally raise an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Here `-5` is valid Python data, but our program considers it invalid.

Mental model:

```text
Python detects invalid operation
        ↓
automatic exception

Program detects invalid application data
        ↓
raise an exception
```

---

## 10. `raise` with `try/except`

```python
try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)
```

The program can raise an exception and another part can decide how to handle it.

---

## 11. `raise` Stops Normal Execution

```python
print("A")

raise ValueError("Something went wrong")

print("B")
```

`B` is never executed.

---

## 12. Raising Exceptions in Functions

```python
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("Invalid amount")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
```

The function detects an invalid situation and raises an exception.

The caller can handle it:

```python
try:
    result = withdraw(1000, 1500)
except ValueError as e:
    print(e)
```

Mental model:

```text
Function
   ↓
detect invalid situation
   ↓
raise
   ↓
caller handles exception
```

---

## 13. Re-raising an Exception

Inside an `except` block:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Logging the error")
    raise
```

A bare `raise` re-raises the same exception.

---

## 14. Complete Example

```python
try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as e:
    print("Invalid age:", e)

else:
    print("Valid age:", age)

finally:
    print("Finished")
```

Possible cases:

Input `21`:

```text
Valid age: 21
Finished
```

Input `-5`:

```text
Invalid age: Age cannot be negative
Finished
```

Input `hello`:

```text
Invalid age: ...
Finished
```

The same `ValueError` handler can handle both Python-generated and manually raised `ValueError`s.

---

## 15. Quick Mental Model

```text
try
 ↓
attempt risky operation
 ↓
exception?
 ├── yes → except
 └── no  → else
       \    /
        finally
```

`raise` means:

> Program considers this situation invalid → raise an exception.

---

## 16. Common Mistakes

- Prefer specific exceptions such as `except ValueError:` when appropriate.
- Code after `raise` in the same normal flow does not execute.
- `else` runs only when no exception occurs.
- `finally` runs whether or not an exception occurs.
- `raise` can be caught by `except`.
- `10 / 0` causes Python to raise an exception automatically.
- `raise ValueError(...)` intentionally raises an exception.
- Bare `raise` inside an `except` re-raises the current exception.

---

## Checklist

- [x] What exceptions are
- [x] `try`
- [x] `except`
- [x] Specific exception handling
- [x] Multiple `except` blocks
- [x] `as e`
- [x] Exception execution flow
- [x] `else`
- [x] `finally`
- [x] `raise`
- [x] Raising exceptions in functions
- [x] Re-raising with bare `raise`
