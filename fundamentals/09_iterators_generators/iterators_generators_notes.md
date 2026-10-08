# Iterators & Generators

## 1. Iterable vs Iterator

An **iterable** is an object that can be iterated over.

Examples:
- list
- tuple
- string
- set
- dictionary
- range

An **iterator** produces values one at a time and keeps track of its current position.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
```

After all values are consumed, `next(iterator)` raises `StopIteration`.

Mental model:

```text
Iterable -> iter() -> Iterator
```

---

## 2. `iter()`

`iter()` creates an iterator from an iterable.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)
```

---

## 3. `next()`

`next()` asks an iterator for its next value.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
```

When there are no more values, `StopIteration` is raised.

---

## 4. How a `for` Loop Works

A `for` loop uses the iterator protocol internally.

Conceptually:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break
```

So:

```python
for x in numbers:
    print(x)
```

is conceptually:

```text
iter() -> next() -> next() -> next() -> StopIteration
```

Important:
- `iter()` is called once when iteration starts.
- `next()` is called repeatedly.
- `StopIteration` signals that iteration is finished.

---

## 5. Iterator Protocol

An iterator follows two important methods:

```python
__iter__()
__next__()
```

- `__iter__()` returns the iterator itself.
- `__next__()` returns the next value.
- `__next__()` raises `StopIteration` when there are no more values.

---

## 6. Custom Iterator

```python
class Count:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration
```

Usage:

```python
counter = Count(3)

for number in counter:
    print(number)
```

Output:

```text
1
2
3
```

The iterator keeps its state in `self.current`.

---

# Generators

## 7. What Is a Generator?

A **generator** is a simple way to create an iterator.

Generators use the `yield` keyword.

```python
def count():
    yield 1
    yield 2
    yield 3
```

Calling:

```python
numbers = count()
```

creates a **generator object**.

The function does not execute all at once.

---

## 8. `yield`

`yield` produces a value and **pauses** the function.

```python
def count():
    yield 1
    yield 2
    yield 3

numbers = count()

print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
```

After yielding a value, execution pauses.

When `next()` is called again, execution resumes from where it stopped.

Mental model:

```text
yield value
    ↓
pause
    ↓
next()
    ↓
resume
    ↓
yield next value
```

The generator remembers its execution state.

---

## 9. Generator vs Custom Iterator

A custom iterator requires methods such as `__iter__()` and `__next__()`.

The same idea can often be written more simply with a generator:

```python
def count(limit):
    current = 1

    while current <= limit:
        yield current
        current += 1
```

Generators automatically handle the iterator machinery for you.

---

## 10. `return` vs `yield`

### `return`

`return` ends the function.

```python
def test():
    return 10
```

### `yield`

`yield` produces a value and pauses execution.

```python
def test():
    yield 10
    yield 20
```

Key difference:

```text
return -> finish the function
yield  -> pause and produce a value
```

---

## 11. Generator Expressions

A generator expression looks like a list comprehension but uses parentheses.

```python
numbers = (x ** 2 for x in range(4))
```

It produces values lazily:

```python
print(next(numbers))  # 0
print(next(numbers))  # 1
print(next(numbers))  # 4
print(next(numbers))  # 9
```

After all values are consumed, another `next()` raises `StopIteration`.

---

## 12. List Comprehension vs Generator Expression

### List comprehension

```python
numbers = [x ** 2 for x in range(4)]
```

Creates and stores all values immediately.

### Generator expression

```python
numbers = (x ** 2 for x in range(4))
```

Produces values one at a time when requested.

Mental model:

```text
List comprehension:
create everything -> store everything

Generator:
create one -> use it -> create next
```

Generators are useful for large amounts of data because they can avoid storing all results in memory at once.

---

## 13. Important Mental Model

```text
Iterable
   ↓ iter()
Iterator
   ↓ next()
Next value
   ↓
next()
   ↓
Next value
   ↓
StopIteration
```

Generator:

```text
Generator function
       ↓
     yield
       ↓
Generator object
       ↓
     next()
       ↓
Values one at a time
```

---

## 14. Common Mistakes

### Mistake 1: Thinking every iterable is an iterator

```python
numbers = [1, 2, 3]

next(numbers)  # TypeError
```

A list is iterable, but it is not itself an iterator.

Correct:

```python
iterator = iter(numbers)
next(iterator)
```

### Mistake 2: Forgetting `StopIteration`

An iterator eventually runs out of values.

```python
iterator = iter([1, 2])

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # StopIteration
```

`for` loops handle this automatically.

### Mistake 3: Thinking `yield` finishes the function

`yield` pauses execution.

```python
def numbers():
    yield 1
    yield 2
```

The function resumes from the previous `yield` when `next()` is called again.

### Mistake 4: Confusing a generator object with generated values

```python
numbers = (x ** 2 for x in range(4))
```

`numbers` is a generator object, not a list of values.

---

## 15. Quick Revision

| Concept | Meaning |
|---|---|
| Iterable | Object that can be iterated over |
| `iter()` | Creates an iterator |
| Iterator | Produces values one at a time |
| `next()` | Gets the next value |
| `StopIteration` | Signals iteration is finished |
| `__iter__()` | Returns an iterator |
| `__next__()` | Produces the next value |
| Generator | Easy way to create an iterator |
| `yield` | Produces a value and pauses execution |
| Generator expression | Lazy expression using `(...)` |

## Checklist

- [x] Iterable vs Iterator
- [x] `iter()`
- [x] `next()`
- [x] `StopIteration`
- [x] How `for` loops work internally
- [x] Iterator protocol
- [x] Custom iterators
- [x] Generators
- [x] `yield`
- [x] Generator expressions
- [x] List comprehension vs generator expression
- [x] `return` vs `yield`
