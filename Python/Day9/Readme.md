# Day 9 – The Four Pillars of Object-Oriented Programming (OOP)

> **Goal:** Learn the four fundamental pillars of OOP that are used in Java, Python, C++, AI libraries, Machine Learning frameworks, and large software systems.

---

# Topics Covered

1. What are the Four Pillars of OOP?
2. Encapsulation
3. Inheritance
4. Polymorphism
5. Abstraction
6. AI Engineering Connection
7. Interview Questions
8. Practice Questions
9. Revision Notes

---

# What are the Four Pillars of OOP?

```text
                OOP
                 │
    ┌────────────┼────────────┐
    │            │            │
Encapsulation Inheritance Polymorphism
                 │
            Abstraction
```

These four concepts help us write:

- Clean Code
- Reusable Code
- Secure Code
- Professional Software

---

# 1. Encapsulation

## Description

Encapsulation means:

> **Wrapping data (variables) and methods (functions) together inside a single class.**

It also allows us to hide important data from outside users.

---

## Why Use Encapsulation?

- Protect sensitive data
- Prevent accidental modification
- Keep code organized
- Improve maintainability

---

## Real-Life Example

Think about an ATM.

You can only perform:

- Deposit
- Withdraw
- Check Balance

You **cannot** directly access:

- Bank Database
- PIN Verification Logic
- Internal Server

The ATM hides its internal implementation.

This is **Encapsulation**.

---

## Example 1

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)

s1 = Student("Vrushali", 95)
s1.display()
```

### Output

```text
Vrushali
95
```

---

## Private Variables

Private variables are created using **double underscore (`__`)**.

```python
class Bank:

    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.show_balance()
```

### Output

```text
10000
```

Trying this:

```python
print(b.__balance)
```

### Output

```text
AttributeError
```

because the variable is private.

---

## Diagram

```text
+----------------------+
|       Bank           |
|----------------------|
| __balance            |
| deposit()            |
| withdraw()           |
| show_balance()       |
+----------------------+
```

---

# 2. Inheritance

## Description

Inheritance means:

> **A child class inherits properties and methods from a parent class.**

---

## Why Use Inheritance?

- Reuse code
- Avoid duplication
- Easy maintenance
- Better organization

---

## Real-Life Example

```text
Animal
 │
 ├── Dog
 ├── Cat
 └── Lion
```

Every animal can eat.

Dogs don't need to rewrite the `eat()` method.

---

## Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## Example

```python
class Animal:

    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

d = Dog()
d.eat()
```

### Output

```text
Eating...
```

---

## Flow

```text
Dog Object
     │
     ▼
eat()

Method not found?

     ▼

Search Parent Class

     ▼

Found

     ▼

Execute
```

---

## Types of Inheritance

### Single Inheritance

```text
A
│
B
```

---

### Multilevel Inheritance

```text
A
│
B
│
C
```

---

### Multiple Inheritance

```text
A      B
 \    /
   C
```

---

# 3. Polymorphism

## Description

The word comes from:

```text
Poly = Many
Morph = Forms
```

Meaning:

> **One method behaves differently depending on the object.**

---

## Why Use Polymorphism?

- Flexibility
- Easy extension
- Cleaner code

---

## Real-Life Example

A person can speak:

- English
- Marathi
- Hindi

Same action (**speak**)

Different outputs.

---

## Example

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
```

### Output

```text
Bark
Meow
```

---

## Operator Overloading

```python
print(5 + 5)
print("Hello " + "World")
```

### Output

```text
10
Hello World
```

The `+` operator behaves differently.

This is polymorphism.

---

## Method Overriding

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()
```

### Output

```text
Bark
```

---

# 4. Abstraction

## Description

Abstraction means:

> **Show only the necessary details and hide the implementation.**

---

## Why Use Abstraction?

- Hide complexity
- Improve security
- Easier to use
- Better design

---

## Real-Life Example

When driving a car:

You know:

- Start
- Brake
- Accelerate

You don't know:

- Engine Timing
- Fuel Injection
- Piston Movement

The internal complexity is hidden.

---

## Abstract Class

Python provides the **abc** module.

```python
from abc import ABC, abstractmethod
```

---

## Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()
```

### Output

```text
Bark
```

---

Trying this:

```python
a = Animal()
```

### Output

```text
TypeError
```

because abstract classes cannot be instantiated.

---

# AI Engineering Connection

Almost every AI library uses these concepts.

### Example

```python
class AIModel:

    def predict(self):
        pass

class CNN(AIModel):

    def predict(self):
        print("CNN Prediction")

class LSTM(AIModel):

    def predict(self):
        print("LSTM Prediction")

cnn = CNN()
lstm = LSTM()

cnn.predict()
lstm.predict()
```

### Output

```text
CNN Prediction
LSTM Prediction
```

This demonstrates:

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

# Difference Between Encapsulation and Abstraction

| Encapsulation          | Abstraction           |
| ---------------------- | --------------------- |
| Hides data             | Hides implementation  |
| Uses private variables | Uses abstract classes |
| Focuses on security    | Focuses on simplicity |

---

# Difference Between Inheritance and Polymorphism

| Inheritance    | Polymorphism                  |
| -------------- | ----------------------------- |
| Reuses code    | Changes behavior              |
| Parent → Child | Same method, different output |

---

# Interview Questions

## Q1. What are the four pillars of OOP?

**Answer:**

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## Q2. What is Encapsulation?

**Answer:**

Wrapping data and methods together inside a class and protecting data using access control.

---

## Q3. What is Inheritance?

**Answer:**

A mechanism where one class acquires properties and methods of another class.

---

## Q4. What is Polymorphism?

**Answer:**

One interface with multiple implementations.

---

## Q5. What is Abstraction?

**Answer:**

Showing only essential information while hiding implementation details.

---

## Q6. What is Method Overriding?

**Answer:**

A child class provides its own implementation of a method already defined in the parent class.

---

## Q7. Can we create an object of an abstract class?

**Answer:**

No.

---

## Q8. What is a private variable?

**Answer:**

A variable prefixed with `__` that cannot be accessed directly from outside the class.

---

# Practice Questions

## Easy

1. Create Animal and Dog class.
2. Create Person and Student class.
3. Create Vehicle and Car class.
4. Create Employee class with private salary.
5. Override a display method.

---

## Medium

6. Create Bank class using encapsulation.
7. Create multilevel inheritance.
8. Create method overriding example.
9. Create abstract Shape class.
10. Create abstract Payment class.

---

## Advanced

11. ATM system.
12. Employee management system.
13. Vehicle management system.
14. Library management system.
15. AI Model prediction system.

---

# Revision Notes

```text
OOP = Object-Oriented Programming

Encapsulation = Hide Data

Inheritance = Reuse Code

Polymorphism = One Interface, Multiple Behaviors

Abstraction = Hide Complexity
```

---

## Memory Trick

```text
E → Encapsulation → Enclose data

I → Inheritance → Inherit features

P → Polymorphism → Perform differently

A → Abstraction → Avoid unnecessary details
```

Remember it as:

> **EIPA** (Encapsulation → Inheritance → Polymorphism → Abstraction)

---

# Summary

Today I learned:

✅ Encapsulation

✅ Private Variables

✅ Inheritance

✅ Single, Multilevel & Multiple Inheritance

✅ Polymorphism

✅ Method Overriding

✅ Operator Overloading

✅ Abstraction

✅ Abstract Classes

✅ AI Engineering use of OOP

---

# Progress Tracker

```text
Day 1  ✅ Variables & Data Types
Day 2  ✅ Operators & Conditions
Day 3  ✅ Loops
Day 4  ✅ Strings
Day 5  ✅ Lists
Day 6  ✅ Tuple, Set & Dictionary
Day 7  ✅ Functions
Day 8  ✅ OOP Basics (Class, Object, Constructor)
Day 9  ✅ Four Pillars of OOP

Next → Day 10: Exception Handling, File Handling, Modules & Packages
```
