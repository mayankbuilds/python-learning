# Python File Handling — Notes

## 1. What is File Handling?

**Definition:** File handling is the process of creating, opening, reading, writing, modifying, and closing files using a program.

File handling allows a Python program to communicate with files stored on persistent storage.

### Why do we need files?

Normal variables usually exist while the program is running:

```python
expenses = [200, 100, 500]
```

A file allows data to remain after the program ends.

```text
Python program
      ↓
   writes data
      ↓
 expenses.txt
      ↓
program closes
      ↓
data remains stored
```

This is useful for projects such as a CLI Expense Tracker.

---

## 2. Variables vs Files

| Variable | File |
|---|---|
| Usually temporary program data | Persistent stored data |
| Usually held in RAM | Stored on persistent storage |
| Exists during program execution | Can remain after program ends |
| Accessed directly in program memory | Requires file I/O |

---

## 3. What is I/O?

**I/O = Input / Output**

```text
READ  → File → Program
WRITE → Program → File
```

---

# 4. `open()`

Python provides the built-in `open()` function.

```python
open(filename, mode)
```

Example:

```python
file = open("notes.txt", "r")
```

Here:

```text
open()       → opens the file
"notes.txt"  → filename
"r"          → file mode
file         → file object
```

Important:

> `open()` returns a **file object**. It does not automatically give you the complete file contents.

Reading is separate:

```python
file = open("notes.txt", "r")
content = file.read()
```

Here:

```text
file    → file object
content → actual file data
```

---

# 5. File Modes

| Mode | Meaning |
|---|---|
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |
| `"x"` | Create |

## `"r"` — Read

```python
file = open("notes.txt", "r")
```

Opens the file for reading.

If the file does not exist:

```python
open("missing.txt", "r")
```

raises:

```text
FileNotFoundError
```

## `"w"` — Write / Overwrite

```python
file = open("notes.txt", "w")
file.write("Python")
```

If the file does not exist, it is generally created.

If it already contains data, `"w"` **overwrites the existing content**.

```text
OLD:
Python
FastAPI
AI/ML

       ↓ "w"

NEW:
Hello
```

## `"a"` — Append

```python
file = open("notes.txt", "a")
file.write("\nAI/ML")
```

Existing content remains and new data is added at the end.

```text
Python
FastAPI
AI/ML
```

## `"x"` — Create

```python
file = open("notes.txt", "x")
```

Creates a new file.

If it already exists:

```text
FileExistsError
```

Mental model:

```text
r → read
w → replace/write
a → add at end
x → create only if it doesn't exist
```

---

# 6. Reading Files

The three main methods are:

```python
read()
readline()
readlines()
```

Suppose `notes.txt` contains:

```text
Python
FastAPI
AI/ML
```

## `read()` — Read the remaining contents

```python
file = open("notes.txt", "r")
content = file.read()
print(content)
```

`read()` returns the remaining contents as a **single string**.

Example:

```python
"Python\nFastAPI\nAI/ML"
```

So:

```python
type(content)
```

is:

```text
str
```

## `readline()` — Read one line

```python
file = open("notes.txt", "r")

line1 = file.readline()
line2 = file.readline()
```

Results:

```text
line1 → "Python\n"
line2 → "FastAPI\n"
```

Each call advances the file position.

## File Position

A file object keeps track of its current position.

```text
Python
↑
cursor
FastAPI
AI/ML
```

After one `readline()`:

```text
Python
FastAPI
↑
cursor
AI/ML
```

After another:

```text
Python
FastAPI
AI/ML
↑
cursor
```

## `read()` and file position

```python
file = open("notes.txt", "r")

print(file.read())
print(file.read())
```

The first call consumes the remaining contents. The second call returns:

```python
""
```

because the position is already at EOF (End Of File).

## `readlines()` — Read lines into a list

```python
file = open("notes.txt", "r")
lines = file.readlines()
```

Returns a list of strings:

```python
['Python\n', 'FastAPI\n', 'AI/ML']
```

Therefore:

```python
type(lines)
```

is:

```text
list
```

`readlines()` also starts from the current file position.

---

# 7. `write()`

`write()` writes a string to a file.

```python
file = open("notes.txt", "w")
file.write("Python")
```

Important:

> `write()` writes exactly what you give it. It does not automatically add a newline.

This:

```python
file.write("Python")
file.write("FastAPI")
```

produces:

```text
PythonFastAPI
```

Use `\n` for separate lines:

```python
file.write("Python\n")
file.write("FastAPI\n")
```

Result:

```text
Python
FastAPI
```

---

# 8. `w` vs `a`

### `"w"`

```python
with open("notes.txt", "w") as file:
    file.write("New content")
```

Existing content is overwritten.

### `"a"`

```python
with open("notes.txt", "a") as file:
    file.write("\nMore content")
```

Existing content remains and new content is added at the end.

```text
w → replace
a → add
```

---

# 9. Closing a File

Traditional approach:

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
```

`close()` closes the file.

```text
open()  → start using the file
close() → finish using the file
```

---

# 10. `with open()` — Preferred Pattern

Manual closing can fail to happen if an exception occurs before `close()`.

Python provides `with` to manage the file safely.

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

When the `with` block finishes, Python automatically handles closing the file.

Mental model:

```text
with open()
     ↓
open file
     ↓
use file
     ↓
leave block
     ↓
automatically close
```

This is the practical pattern to remember.

### Other modes

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

```python
with open("notes.txt", "a") as file:
    file.write("\nFastAPI")
```

General pattern:

```python
with open(filename, mode) as file:
    # work with the file
```

---

# 11. File Paths

A path tells Python where a file is located.

## Relative Path

```python
open("notes.txt")
```

The file is located relative to the **current working directory**.

## File inside a folder

Given:

```text
project/
├── main.py
└── data/
    └── notes.txt
```

Use:

```python
open("data/notes.txt")
```

## Parent Directory: `../`

`../` means:

> Go up one directory.

Example:

```text
../main.py
```

means go to the parent directory and look for `main.py`.

```text
../../
```

means go up two directories.

## Absolute Path

An absolute path specifies the complete location.

Linux:

```text
/home/user/project/notes.txt
```

Windows:

```text
C:\Users\User\project\notes.txt
```

Relative paths are often preferable for portable projects when practical.

---

# 12. Current Working Directory

Python has a **current working directory (CWD)**.

You can inspect it with:

```python
import os

print(os.getcwd())
```

If the CWD is:

```text
/home/user/project
```

then:

```python
open("notes.txt")
```

looks for:

```text
/home/user/project/notes.txt
```

Important:

> Relative paths are interpreted from the current working directory.

---

# 13. Practical Example

```python
with open("file_practice.txt", "w") as file:
    file.write("Python\nFastAPI\nAI/ML\n")

with open("file_practice.txt", "a") as file:
    file.write("DSA\n")

with open("file_practice.txt", "r") as file:
    content = file.read()
    print(content)
```

Final file:

```text
Python
FastAPI
AI/ML
DSA
```

This combines:

- `with open()`
- `"w"`
- `"a"`
- `"r"`
- `write()`
- `read()`
- `\n`

---

# 14. Common Exceptions

### `FileNotFoundError`

Occurs when trying to open a nonexistent file for reading:

```python
open("missing.txt", "r")
```

### `FileExistsError`

Occurs when using `"x"` to create a file that already exists:

```python
open("notes.txt", "x")
```

Incorrect paths or insufficient permissions can also cause file-related exceptions.

---

# 15. Important Mental Models

### File object vs file contents

```python
file = open("notes.txt", "r")
content = file.read()
```

```text
file    → file object
content → actual file data
```

### Reading

```text
read()      → remaining content → str
readline()  → next line         → str
readlines() → remaining lines   → list
```

### Modes

```text
r → read
w → write / overwrite
a → append
x → create
```

### File lifecycle

```text
open
 ↓
work with file
 ↓
close
```

Prefer:

```text
with open()
     ↓
work with file
     ↓
automatic closing
```

---

# 16. Common Mistakes

- `open()` gives a **file object**, not the complete file contents.
- `read()` returns a string.
- `readlines()` returns a list.
- `readline()` reads one line at a time.
- Reading methods advance the file position.
- Once the position reaches EOF, another `readline()` returns `""`.
- `"w"` overwrites existing content.
- `"a"` preserves existing content and adds at the end.
- `"x"` creates a new file and fails if it already exists.
- `write()` does not automatically add `\n`.
- Prefer `with open(...)` so the file is properly managed.
- `"r"` on a nonexistent file raises `FileNotFoundError`.

---

# 17. Revision Table

| Concept | Key Point |
|---|---|
| File handling | Working with stored files |
| `open()` | Opens a file and returns a file object |
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |
| `"x"` | Create |
| `read()` | Remaining content as `str` |
| `readline()` | Next line as `str` |
| `readlines()` | Remaining lines as `list` |
| `write()` | Writes a string |
| `close()` | Closes a file |
| `with open()` | Automatically manages closing |
| Relative path | Path relative to CWD |
| `../` | Parent directory |
| CWD | Current working directory |
| `FileNotFoundError` | File not found |
| `FileExistsError` | File already exists when using `"x"` |

---

## Checklist

- [x] What is file handling
- [x] Variables vs files
- [x] I/O
- [x] `open()`
- [x] File object
- [x] `r` mode
- [x] `w` mode
- [x] `a` mode
- [x] `x` mode
- [x] `read()`
- [x] `readline()`
- [x] `readlines()`
- [x] File position
- [x] `write()`
- [x] `\n`
- [x] `close()`
- [x] `with open()`
- [x] Relative paths
- [x] Absolute paths
- [x] `../`
- [x] Current working directory
- [x] Common file exceptions
- [x] Practical file exercise
