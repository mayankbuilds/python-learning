# Async Programming

## 1. Synchronous vs Asynchronous Execution

### Synchronous

In synchronous execution, tasks run sequentially.

A task waits for the previous task to complete before the next task can proceed.

```text
Task A → finish
          ↓
Task B → finish
          ↓
Task C
```

Example:

```python
def fetch_data():
    # takes time
    pass

fetch_data()
print("Next task")
```

The program waits for `fetch_data()` to finish before continuing.

### Asynchronous

In asynchronous execution, a task can pause while waiting, allowing other asynchronous work to run.

```text
Task A → waiting...
             ↓
Task B → runs
             ↓
Task A → continues
```

Async is especially useful for operations involving waiting, such as network requests, APIs, and database operations.

---

## 2. Blocking vs Non-Blocking

### Blocking

A blocking operation makes the current flow wait until the operation finishes.

Example situations:

- waiting for a network response
- waiting for a database response
- waiting for file or external I/O

```text
Start
  ↓
Wait for operation
  ↓
Operation finishes
  ↓
Continue
```

### Non-blocking

A non-blocking approach allows other async work to make progress while waiting.

```text
Start
  ↓
Waiting for I/O
  ↓
Other async work runs
  ↓
I/O completes
  ↓
Original work continues
```

---

## 3. `async def`

`async def` defines an **async function**, also called a coroutine function.

```python
async def fetch_data():
    return "data"
```

Calling it:

```python
result = fetch_data()
```

does not immediately give the returned value.

It creates a **coroutine object**.

```text
async def function
       ↓
call function
       ↓
coroutine object
```

The coroutine needs to be awaited or scheduled by an async system.

---

## 4. `await`

`await` is used inside an async function to wait for another awaitable operation.

```python
async def main():
    result = await fetch_data()
    print(result)
```

When the coroutine reaches `await`, it can pause while the awaited operation is in progress.

This allows the async system to run other work instead of simply blocking the whole async event loop.

Mental model:

```text
Coroutine A
    ↓
  await
    ↓
pause while waiting
    ↓
other async work runs
    ↓
operation completes
    ↓
Coroutine A resumes
```

Important:

`await` does **not** mean "run everything simultaneously."

It means the current coroutine can give control back while waiting for an awaitable operation.

---

## 5. Coroutines

A coroutine is the object produced when an `async def` function is called.

Example:

```python
async def greet():
    return "Hello"

coroutine = greet()
```

`coroutine` is a coroutine object.

A coroutine can be run/awaited by an asynchronous system.

Example:

```python
async def main():
    result = await greet()
    print(result)
```

---

## 6. `asyncio`

`asyncio` is Python's standard library for writing asynchronous programs.

Example:

```python
import asyncio

async def greet():
    print("Hello")

asyncio.run(greet())
```

`asyncio.run()` starts an asynchronous program and runs the coroutine.

---

## 7. Event Loop

The **event loop** is responsible for managing and scheduling asynchronous work.

It coordinates coroutines and determines what async work can run while another operation is waiting.

Mental model:

```text
             Event Loop
          /      |            Task A   Task B    Task C
       ↓
    waiting
       ↓
   Task B runs
       ↓
   Task C runs
       ↓
   Task A resumes
```

The event loop is central to Python's async programming model.

---

## 8. Creating Concurrent Async Tasks

Multiple coroutines can be scheduled so they can make progress while other tasks are waiting.

Example:

```python
import asyncio

async def task(name):
    await asyncio.sleep(1)
    print(name)

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )

asyncio.run(main())
```

The tasks can overlap their waiting periods.

This is different from:

```python
await task("A")
await task("B")
await task("C")
```

where each coroutine is awaited before starting the next one.

---

## 9. Async Is Mainly Useful for I/O

Async programming is especially useful when the program spends significant time waiting for external operations.

Examples:

- HTTP/API requests
- database queries
- network communication
- other I/O operations

For example, a web application may need to wait for an API response:

```text
Request
   ↓
Waiting for API
   ↓
Other async request can run
   ↓
API response arrives
   ↓
Continue original request
```

This can improve resource utilization when handling many I/O-bound operations.

---

## 10. Async Does Not Automatically Mean Parallelism

Async and parallelism are different ideas.

### Async / concurrency

Tasks can make progress by yielding control while waiting.

```text
Task A → wait
Task B → run
Task B → wait
Task C → run
Task A → resume
```

### Parallelism

Multiple pieces of work actually execute at the same time, typically using multiple CPU cores.

For the Python web/backend context, async is primarily valuable for **I/O-bound concurrency**, not automatically for CPU-heavy work.

---

## 11. Async vs Sync Example

### Synchronous idea

```python
def fetch():
    # wait for I/O
    pass

def main():
    fetch()
    fetch()
    fetch()
```

Each operation blocks the current flow until it completes.

### Asynchronous idea

```python
async def fetch():
    # async I/O
    pass

async def main():
    await fetch()
    await fetch()
    await fetch()
```

This is asynchronous code, but these three `await`s are still sequential.

To overlap independent operations, tasks can be scheduled together:

```python
await asyncio.gather(
    fetch(),
    fetch(),
    fetch()
)
```

---

## 12. Async in FastAPI

FastAPI supports asynchronous route handlers.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello"}
```

The `async def` route handler allows asynchronous operations inside the request handler.

For example:

```python
@app.get("/users")
async def get_users():
    users = await fetch_users_from_database()
    return users
```

If the database operation is asynchronous, the handler can await it without blocking the event loop in the same way a blocking operation would.

---

## 13. Important Mental Model

Remember:

```text
async def
    ↓
defines coroutine function

call async function
    ↓
coroutine object

await coroutine/awaitable
    ↓
pause current coroutine while waiting

event loop
    ↓
manages and schedules async work

I/O wait
    ↓
other async work can make progress
```

---

## 14. Common Mistakes

### Mistake 1: Thinking `async def` runs immediately

```python
async def hello():
    print("Hello")

hello()
```

Calling `hello()` creates a coroutine object. It does not simply execute the function like a normal synchronous function.

---

### Mistake 2: Forgetting `await`

Inside an async function:

```python
result = fetch_data()
```

may only give you a coroutine object if `fetch_data()` is async.

You commonly need:

```python
result = await fetch_data()
```

---

### Mistake 3: Thinking async means everything runs simultaneously

Async provides concurrency by allowing tasks to make progress while others are waiting.

It does not automatically make CPU-heavy code execute in parallel.

---

### Mistake 4: Using async unnecessarily

Async is most useful when there is meaningful waiting, especially I/O.

Making every function `async` does not automatically make a program faster.

---

## 15. Quick Revision

| Concept | Meaning |
|---|---|
| Synchronous | Tasks proceed sequentially |
| Asynchronous | Tasks can make progress while another async task waits |
| Blocking | Current flow waits for an operation |
| Non-blocking | Other async work can proceed while waiting |
| `async def` | Defines a coroutine function |
| Coroutine | Object produced when an async function is called |
| `await` | Pauses current coroutine while awaiting an operation |
| `asyncio` | Python's standard async programming library |
| Event loop | Manages and schedules async work |
| I/O-bound | Work that spends time waiting for external operations |
| Parallelism | Multiple work executes at the same time |

## Checklist

- [x] Synchronous vs asynchronous execution
- [x] Blocking vs non-blocking
- [x] `async def`
- [x] Coroutines
- [x] `await`
- [x] `asyncio`
- [x] Event loop
- [x] Concurrent async tasks
- [x] I/O-bound use cases
- [x] Async vs parallelism
- [x] Async in FastAPI
- [x] Common mistakes

## Final Mental Model

```text
async def
   ↓
coroutine
   ↓
await
   ↓
pause during I/O
   ↓
event loop runs other async work
   ↓
I/O completes
   ↓
coroutine resumes
```
