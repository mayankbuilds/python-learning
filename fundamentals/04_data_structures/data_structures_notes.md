# Python Data Structures — Notes

> Python Learning roadmap: Lists, Tuples, Sets, Dictionaries.

## 1. Lists

A **list** is an ordered, mutable collection.

```python
numbers = [10, 20, 30, 40]
```

### Indexing and slicing
```python
numbers[0]      # 10
numbers[-1]     # 40
numbers[1:3]    # [20, 30]
```
Slicing follows `[start:stop]`; `stop` is excluded.

### Mutability
```python
numbers[0] = 100
```
Lists can be changed after creation.

### Common methods
```python
numbers.append(50)       # add one object
numbers.extend([60, 70]) # add elements from an iterable
numbers.insert(1, 99)    # insert at index
numbers.remove(20)       # remove first occurrence; ValueError if absent
x = numbers.pop(1)       # remove by index and return value
x = numbers.pop()        # remove and return last item
del numbers[0]           # delete item
```

`remove()` modifies the list and returns `None`.

### `sort()` vs `sorted()`
```python
numbers.sort()           # mutates original; returns None
new_numbers = sorted(numbers)  # returns new sorted list
```

### Membership
```python
20 in numbers
20 not in numbers
```

### Other useful methods
```python
numbers.index(30)  # first matching index; ValueError if absent
numbers.count(20)  # number of occurrences
```

## 2. References and Copying

```python
a = [1, 2, 3]
b = a
```
`a` and `b` refer to the **same list object**.

A shallow copy:
```python
b = a.copy()
b = a[:]
```
creates a new outer list.

### Nested-list warning
```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99
```
The inner lists are still shared, so both can reflect the change. A shallow copy copies only the outer list.

## 3. List Comprehensions

Basic form:
```python
[expression for item in iterable]
```

Transform:
```python
[x * 2 for x in numbers]
```

Filter:
```python
[x for x in numbers if x % 2 == 0]
```

Transform + filter:
```python
[x**2 for x in numbers if x % 2 == 0]
```

Conditional output:
```python
["Even" if x % 2 == 0 else "Odd" for x in numbers]
```

Important:
- `if` at the end filters/removes elements.
- `if/else` before `for` keeps every element and chooses what to store.

## 4. Nested Lists / 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access:
```python
matrix[1]       # [4, 5, 6]
matrix[1][2]    # 6
```

General pattern:
```python
matrix[row][column]
```

Modify:
```python
matrix[0][1] = 99
```

Loop through rows:
```python
for row in matrix:
    print(row)
```

Loop through every element:
```python
for row in matrix:
    for value in row:
        print(value)
```

Flatten with a nested comprehension:
```python
result = [value for row in matrix for value in row]
```

Filter:
```python
result = [value for row in matrix for value in row if value > 3]
```

Transform:
```python
result = [value * value for row in matrix for value in row]
```

Mental model:
```text
matrix -> row -> value
```

## 5. Tuples

A **tuple** is an ordered, immutable collection.

```python
student = ("Mayank", 21, "CSE")
```

| List | Tuple |
|---|---|
| Mutable | Immutable |
| `[]` | `()` |
| Can change elements | Cannot change elements |

Indexing and slicing work:
```python
data[0]
data[-1]
data[0:2]
```

This fails:
```python
numbers = (10, 20, 30)
numbers[0] = 100
```
→ `TypeError`

### Tuple packing
```python
data = 10, 20, 30
```
`data` is a tuple.

### Tuple unpacking
```python
person = ("Mayank", 21, "CSE")
name, age, branch = person
```

### Swapping
```python
a, b = b, a
```

## 6. Sets

A **set** is an unordered collection of unique elements.

```python
numbers = {10, 20, 30, 20}
```
Duplicates are removed.

Sets do not support positional indexing:
```python
numbers[0]  # TypeError
```

Empty set:
```python
set()
```

Important:
```python
{}
```
is an empty **dictionary**, not a set.

### Add/remove
```python
numbers.add(4)
numbers.remove(3)   # KeyError if missing
numbers.discard(3)  # does nothing if missing
```

| Method | If element is missing |
|---|---|
| `remove(x)` | `KeyError` |
| `discard(x)` | Does nothing |

### Membership
```python
20 in numbers
```

### Set operations
Given:
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

Union:
```python
A | B
A.union(B)
# {1, 2, 3, 4, 5, 6}
```

Intersection:
```python
A & B
A.intersection(B)
# {3, 4}
```

Difference:
```python
A - B  # {1, 2}
B - A  # {5, 6}
```
Direction matters.

### Remove duplicates
```python
numbers = [1, 2, 2, 3, 3, 4]
unique = set(numbers)
```
If a list is required:
```python
unique = list(set(numbers))
```
Do not rely on the original list order with this approach.

## 7. Dictionaries

A **dictionary** stores key-value pairs.

```python
student = {
    "name": "Mayank",
    "age": 21,
    "branch": "CSE"
}
```

Mental model:
```text
key -> value
```

### Access
```python
student["name"]
student["age"]
```
Dictionary access is by key, not list position.

### Add/update
```python
student["college"] = "NSEC"  # add
student["age"] = 22          # update
```

General rule:
```python
dictionary[key] = value
```
- key exists → update
- key absent → add

### `get()`
```python
student["email"]              # KeyError if missing
student.get("email")          # None if missing
student.get("email", "Not provided")  # default if missing
```

### Key membership
```python
"name" in student
```
checks keys.

### Removing
```python
age = student.pop("age")  # removes and returns value
del student["name"]       # removes entry
student.clear()           # removes all entries
```

### `keys()`, `values()`, `items()`
```python
student.keys()
student.values()
student.items()
```

### Loops
Keys:
```python
for key in student:
    print(key)
```

Values:
```python
for value in student.values():
    print(value)
```

Both:
```python
for key, value in student.items():
    print(key, value)
```

## 8. Nested Dictionaries

A dictionary can contain dictionaries.

```python
students = {
    "s1": {"name": "A", "marks": 80},
    "s2": {"name": "B", "marks": 65}
}
```

Access:
```python
students["s1"]          # entire s1 dictionary
students["s1"]["marks"] # 80
```

Mental model:
```text
students -> s1 -> marks -> 80
```

## 9. Dictionary Comprehensions

Basic form:
```python
{key: value for item in iterable}
```

Example:
```python
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
```

Result:
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

With a condition:
```python
even_squares = {
    x: x**2
    for x in numbers
    if x % 2 == 0
}
```

Result:
```python
{2: 4, 4: 16}
```

### Comprehension comparison
```python
[x*x for x in numbers]       # list
{x*x for x in numbers}       # set
{x: x*x for x in numbers}    # dictionary
```

Dictionary comprehensions use `key: value`.

## 10. Common Mistakes

- `append()` adds one object; `extend()` adds elements from an iterable.
- `sort()` changes the original and returns `None`; `sorted()` returns a new sorted list.
- `b = a` is not a copy; it creates another reference.
- Shallow copies still share nested inner lists.
- List comprehension uses `[]`; dictionary comprehension uses `{}` with `key: value`.
- Filtering and conditional output are different.
- In nested comprehensions, use the current row:
  ```python
  [value for row in matrix for value in row]
  ```
- `{}` is an empty dictionary; `set()` is an empty set.
- `student["email"]` can raise `KeyError`; `student.get("email")` returns `None` when missing.

## 11. Quick Mental Models

```text
LIST
Ordered + Mutable
Use when data changes.

TUPLE
Ordered + Immutable
Use for fixed groups of values.

SET
Unique + Unordered
Use for uniqueness, membership, and set operations.

DICTIONARY
Key -> Value
Use when data is accessed by meaningful keys.
```

## 12. Checklist

- [x] Lists
- [x] Indexing and slicing
- [x] List mutability
- [x] List methods
- [x] `sort()` vs `sorted()`
- [x] References and shallow copying
- [x] List comprehensions
- [x] Nested lists / 2D lists
- [x] Nested loops
- [x] Nested list comprehensions
- [x] Tuples
- [x] Tuple packing/unpacking
- [x] Sets
- [x] Set operations
- [x] Removing duplicates
- [x] Dictionaries
- [x] Dictionary methods
- [x] Dictionary loops
- [x] Nested dictionaries
- [x] Dictionary comprehensions
