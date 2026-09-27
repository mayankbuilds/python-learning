# Object-Oriented Programming (OOP) — Python Notes

## 1. OOP Basics
**Definition:** Object-Oriented Programming organizes code around objects containing data and methods that operate on that data.

- Class = blueprint
- Object = instance of a class

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

## 2. Attributes
Attributes are data associated with an object or class.

```python
class Student:
    college = "NSEC"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

- Instance attributes can have different values for different objects.
- Class attributes are shared/accessed through the class and its instances.

## 3. `__init__()` and `self`

`__init__()` runs when an object is created and is commonly used to initialize attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

`self` refers to the current object.

In `self.name = name`:
- left side = attribute of current object
- right side = parameter

## 4. Methods

A method is a function defined inside a class.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)
```

Methods can accept parameters and return values.

## 5. Encapsulation

**Definition:** Encapsulation bundles data and the methods that operate on it while controlling access to that data.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

### `_attribute`
A single leading `_` means the attribute is intended to be internal/protected **by convention**. It is not truly private.

### `__attribute`
A double leading underscore triggers **name mangling**.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
```

Outside code cannot normally access it as `account.__balance`.

## 6. Inheritance

**Definition:** Inheritance allows a child class to acquire attributes and methods from a parent class.

```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")
```

- Animal = parent/base class
- Dog = child/derived class

A child can reuse parent functionality and add its own functionality.

## 7. `super()`

`super()` gives the child access to the parent's implementation.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

`super().__init__(name)` calls the parent's constructor.

**Important:** `super()` does not create a parent object.

## 8. Method Overriding

A child class can provide its own implementation of an inherited method.

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

`Dog.speak()` overrides `Animal.speak()`.

## 9. Polymorphism

**Definition:** Polymorphism means "many forms" — the same method/interface can behave differently depending on the object.

```python
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()
```

```python
make_sound(Dog())
make_sound(Cat())
```

Same interface, different behavior.

## 10. Abstraction

**Definition:** Abstraction hides unnecessary implementation details and exposes essential functionality.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
```

- `ABC` = Abstract Base Class
- `@abstractmethod` means concrete child classes must implement the method.
- An abstract class with unimplemented abstract methods cannot normally be instantiated.

Mental model:

```text
Parent → defines WHAT is required
Child  → decides HOW it is implemented
```

## 11. Class Methods

A class method works with the class and conventionally receives `cls`.

```python
class Student:
    college = "NSEC"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college
```

```python
Student.change_college("ABC")
```

- `self` → current object/instance
- `cls` → current class

Class methods can also be used as alternative constructors.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

## 12. Static Methods

A static method needs neither `self` nor `cls`.

```python
class MathUtils:
    @staticmethod
    def square(n):
        return n * n
```

```python
MathUtils.square(5)  # 25
```

Use it when functionality is logically related to the class but does not depend on object or class data.

### Three method types

```text
Instance method → self → object data
Class method    → cls  → class data
Static method   → none → neither object nor class data
```

## 13. Properties — `@property`

`@property` lets a method be accessed like an attribute.

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks
```

```python
student.marks
```

instead of `student.get_marks()`.

### Setter

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")
```

Properties provide controlled reading/writing and validation while keeping normal attribute syntax.

## 14. Composition

**Definition:** Composition means a class contains an object of another class. It represents a **HAS-A** relationship.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```

A Car **has an Engine**.

### Inheritance vs Composition

```text
Inheritance  → IS-A
Composition  → HAS-A

Dog IS-A Animal       → inheritance
Car HAS-A Engine      → composition
Computer HAS-A CPU    → composition
Phone HAS-A Battery   → composition
```

## 15. Four Major OOP Pillars

### Encapsulation
Controls access to internal data/behavior.

### Inheritance
Allows a child class to reuse and extend parent functionality.

### Polymorphism
Allows the same method/interface to behave differently for different objects.

### Abstraction
Hides unnecessary details and exposes essential functionality.

## 16. Important Differences

### `_name` vs `__name`
- `_name` → internal/protected by convention
- `__name` → name mangling/private-style

### `self` vs `cls`
- `self` → current object
- `cls` → current class

### Inheritance vs Composition
- IS-A → inheritance
- HAS-A → composition

### Inheritance vs Overriding
- Inheritance → child receives parent functionality
- Overriding → child provides its own version of an inherited method

### `super()`
Lets the child reuse the parent's implementation.

## 17. Common Mistakes

- Confusing a class with an object.
- Forgetting `self` in instance methods.
- Confusing `self` with `cls`.
- Thinking `_name` is truly private.
- Thinking `super()` creates a parent object.
- Confusing inheritance with overriding.
- Confusing inheritance (`IS-A`) with composition (`HAS-A`).
- Trying to instantiate an abstract class with unimplemented abstract methods.

## 18. OOP Checklist

- [x] Classes and Objects
- [x] Attributes
- [x] `__init__()` and `self`
- [x] Methods
- [x] Instance vs Class Attributes
- [x] Encapsulation
- [x] `_attribute` and `__attribute`
- [x] Inheritance
- [x] `super()`
- [x] Method Overriding
- [x] Polymorphism
- [x] Abstraction
- [x] Class Methods
- [x] Static Methods
- [x] Properties
- [x] Composition

## Final Mental Model

```text
OOP
├── Classes & Objects
├── Attributes & Methods
├── Encapsulation
├── Inheritance
│   └── super()
├── Polymorphism
│   └── overriding
├── Abstraction
│   └── ABC / abstractmethod
├── Class methods
├── Static methods
├── Properties
└── Composition
    └── HAS-A relationship
```

**Learning rule:** Understand what each concept solves and when to use it; do not memorize definitions alone.
