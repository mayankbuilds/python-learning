# Python Modules & Packages — Notes

## 1. What is a Module?

A **module** is a Python file (`.py`) that contains reusable code such as functions, classes, and variables.

Example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

`calculator.py` is a module.

---

## 2. Why Use Modules?

Modules help us:

- reuse code
- organize large programs
- separate responsibilities
- make code easier to maintain

Instead of putting everything into one huge Python file, related functionality can be separated into modules.

---

## 3. Importing a Module

Suppose we have:

```text
calculator.py
```

We can import it:

```python
import calculator
```

Then access its functions using:

```python
calculator.add(2, 3)
calculator.multiply(4, 5)
```

Mental model:

```text
calculator.py
     ↓
   import
     ↓
calculator.add()
calculator.multiply()
```

---

## 4. `from ... import ...`

Instead of importing the entire module name:

```python
import calculator

calculator.add(2, 3)
```

we can import a specific object:

```python
from calculator import add

add(2, 3)
```

Here `add` can be used directly.

---

## 5. Importing Multiple Objects

```python
from calculator import add, multiply
```

Now:

```python
add(2, 3)
multiply(4, 5)
```

can be called directly.

---

## 6. Aliases with `as`

A module can be given another name:

```python
import calculator as calc
```

Then:

```python
calc.add(2, 3)
```

We can also alias an imported function:

```python
from calculator import add as addition

addition(2, 3)
```

---

## 7. Standard Library Modules

Python provides many built-in modules in its standard library.

Example:

```python
import math

print(math.sqrt(25))
```

Another example:

```python
import random

print(random.randint(1, 10))
```

These modules provide reusable functionality without us having to implement everything ourselves.

---

## 8. Creating and Using Your Own Module

Suppose the project contains:

```text
project/
├── main.py
└── calculator.py
```

`calculator.py`:

```python
def add(a, b):
    return a + b
```

`main.py`:

```python
import calculator

result = calculator.add(10, 20)
print(result)
```

Output:

```text
30
```

The important idea is that `main.py` is using reusable code from `calculator.py`.

---

## 9. `__name__`

Every Python module has a special variable called:

```python
__name__
```

Its value depends on how the file is being used.

### When the file is run directly

If we run:

```bash
python calculator.py
```

then inside `calculator.py`:

```python
__name__ == "__main__"
```

### When the file is imported

If another file does:

```python
import calculator
```

then inside `calculator.py`:

```python
__name__ == "calculator"
```

Mental model:

```text
Direct execution
calculator.py
      ↓
__name__ = "__main__"


Imported
main.py → calculator.py
             ↓
       __name__ = "calculator"
```

---

## 10. `if __name__ == "__main__":`

This pattern is extremely common:

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(2, 3))
```

The code inside the `if` block runs when the file is executed directly.

It does not run just because the module is imported.

Example:

```text
calculator.py
     ↓
imported by main.py
     ↓
function definitions available
     ↓
__name__ == "calculator"
     ↓
main block does not execute
```

This allows a file to contain reusable code and optional direct-execution code at the same time.

---

## 11. Package

A **package** is a way of organizing related Python modules into a directory.

Example:

```text
utils/
├── calculator.py
└── string_utils.py
```

Here:

```text
utils
 ↓
package

calculator.py
 ↓
module

string_utils.py
 ↓
module
```

Mental model:

> Module = one Python file  
> Package = directory that organizes related modules

---

## 12. `__init__.py`

A package commonly contains:

```text
utils/
├── __init__.py
├── calculator.py
└── string_utils.py
```

`__init__.py` is a special file associated with Python packages.

It can be empty, or it can contain package initialization code and exports.

Modern Python also supports namespace packages that can work without `__init__.py`, but the traditional package structure commonly uses it.

---

## 13. Importing from a Package

Suppose:

```text
project/
├── main.py
└── utils/
    ├── __init__.py
    └── calculator.py
```

`calculator.py`:

```python
def add(a, b):
    return a + b
```

From `main.py`:

```python
from utils.calculator import add

print(add(10, 20))
```

Output:

```text
30
```

The path can be understood as:

```text
utils
  ↓
calculator
  ↓
add
```

---

## 14. Module vs Package

| Concept | Meaning | Example |
|---|---|---|
| Module | A Python file containing reusable code | `calculator.py` |
| Package | A directory used to organize related modules | `utils/` |
| Function | Reusable block of code | `add()` |

Example:

```text
project/
├── main.py
└── utils/
    ├── __init__.py
    ├── calculator.py
    └── string_utils.py
```

Here:

- `main.py` → module
- `utils` → package
- `calculator.py` → module
- `string_utils.py` → module
- `add()` → function

---

## 15. Real Project Structure

As applications become larger, modules and packages help separate responsibilities.

Example:

```text
project/
├── main.py
├── services/
│   ├── user_service.py
│   └── payment_service.py
├── models/
│   └── user.py
└── utils/
    └── helpers.py
```

Possible responsibility separation:

```text
services/
    business logic

models/
    data-related structures

utils/
    reusable helper functions

main.py
    application entry point
```

This becomes especially useful in backend applications.

---

## 16. Import Mental Model

Think of:

```python
from utils.calculator import add
```

as:

```text
utils
  ↓
package
  ↓
calculator
  ↓
module
  ↓
add
  ↓
function
```

And:

```python
import calculator
```

as:

```text
calculator.py
      ↓
    module
      ↓
 imported as calculator
```

---

## 17. Common Mistakes

### Mistake 1: Confusing module and package

```text
calculator.py → module
utils/         → package
```

Do not call both the same thing.

### Mistake 2: Forgetting the function name

If:

```python
def multiply(a, b):
    return a * b
```

then call:

```python
multiply(5, 4)
```

not:

```python
multiple(5, 4)
```

### Mistake 3: Confusing direct execution and import

```python
if __name__ == "__main__":
```

is about whether the file is being run directly.

### Mistake 4: Assuming `__name__` is always `"__main__"`

It is `"__main__"` when that module is the directly executed entry point.

When imported, it normally receives its module name.

---

## 18. Quick Revision

```text
MODULE
  ↓
.py file containing reusable code

PACKAGE
  ↓
directory organizing related modules

import module
  ↓
use module.object

from module import object
  ↓
use object directly

as
  ↓
create an alias

__name__
  ↓
tells how the module is being used

if __name__ == "__main__":
  ↓
runs only when the file is executed directly
```

---

## Checklist

- [x] What is a module
- [x] Why modules are useful
- [x] `import module`
- [x] `from module import name`
- [x] Importing multiple objects
- [x] Aliases with `as`
- [x] Standard library modules
- [x] Creating your own module
- [x] `__name__`
- [x] Direct execution vs importing
- [x] `if __name__ == "__main__":`
- [x] What is a package
- [x] `__init__.py`
- [x] Importing from a package
- [x] Module vs package
- [x] Real project organization
