# Day 8 — Object-Oriented Programming (OOP) Basics: Class, Object, Constructor

# Topics Covered

1. What is OOP?
2. Why use OOP?
3. What is a Class?
4. What is an Object?
5. Creating Classes
6. Creating Objects
7. Constructors (`__init__`)
8. Parameterized Constructors
9. Instance Variables
10. Instance Methods
11. The `self` Keyword
12. Mini Project
13. Interview Questions
14. Practice Questions

---

# PART 1 — What is OOP?

## Description

OOP stands for **Object-Oriented Programming**.

It is a programming paradigm where we organize code using:

- Objects
- Classes
- Variables
- Methods

Instead of writing everything separately, we group related data and functions together.

---

## Why Use OOP?

Without OOP:

```python
student_name = "Vrushali"
student_age = 22
student_marks = 95
```

For 100 students:

```text
student1_name
student2_name
student3_name
...
student100_name
```

This becomes difficult to manage.

Using OOP:

```python
student1 = Student()
student2 = Student()
student3 = Student()
```

Advantages:

- Reusable code
- Cleaner code
- Easy maintenance
- Better organization
- Real-world modeling

---

## Real-Life Example

Think about a car.

### Properties

```text
color
brand
speed
price
```

### Actions

```text
start()
stop()
accelerate()
brake()
```

In OOP:

```text
Object = Data + Functions
```

---

# PART 2 — What is a Class?

## Description

A class is a blueprint or template used to create objects.

Example:

```text
House Blueprint
        ↓
Actual House
```

Similarly:

```text
Class
   ↓
Object
```

---

## Syntax

```python
class Student:
    pass
```

---

## Example

```python
class Student:
    pass

print(Student)
```

Output:

```text
<class '__main__.Student'>
```

---

# PART 3 — What is an Object?

## Description

An object is an actual instance of a class.

Example:

```text
Blueprint
    ↓
Actual Product
```

Example:

```python
class Student:
    pass

s1 = Student()

print(s1)
```

Output:

```text
<__main__.Student object at 0x...>
```

---

# PART 4 — Creating Our First Class

Example:

```python
class Student:

    def display(self):
        print("Hello Student")

s1 = Student()

s1.display()
```

Output:

```text
Hello Student
```

---

## Flow

Step 1:

```python
class Student:
```

Create blueprint.

Step 2:

```python
s1 = Student()
```

Create object.

Step 3:

```python
s1.display()
```

Call method.

---

# PART 5 — Multiple Objects

```python
class Student:

    def hello(self):
        print("Hello")

s1 = Student()
s2 = Student()

s1.hello()
s2.hello()
```

Output:

```text
Hello
Hello
```

---

# PART 6 — Constructor

## What is Constructor?

A constructor is a special function that runs automatically when an object is created.

Python constructor:

```python
__init__()
```

---

## Example

```python
class Student:

    def __init__(self):
        print("Constructor Called")

s1 = Student()
```

Output:

```text
Constructor Called
```

Notice:

```python
s1.__init__()
```

was never called manually.

Python called it automatically.

---

## Real-Life Example

When you turn on your mobile phone:

```text
Power On
    ↓
Boot Process Starts Automatically
```

Similarly:

```python
student = Student()
```

automatically calls:

```python
__init__()
```

---

# PART 7 — Parameterized Constructor

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

        print(name)
        print(age)

s1 = Student("Vrushali",22)
```

Output:

```text
Vrushali
22
```

---

## Memory Visualization

```text
s1
 |
 +---->
        name = Vrushali
        age = 22
```

---

# PART 8 — Instance Variables

Variables belonging to an object.

Example:

```python
class Student:

    def __init__(self):

        self.name = "Vrushali"
        self.age = 22

s1 = Student()

print(s1.name)
print(s1.age)
```

Output:

```text
Vrushali
22
```

---

# PART 9 — Instance Methods

Methods belonging to an object.

Example:

```python
class Student:

    def hello(self):
        print("Hello")

s1 = Student()

s1.hello()
```

Output:

```text
Hello
```

---

# PART 10 — Understanding self

This is one of the most important concepts in OOP.

Think:

```text
self = current object
```

Example:

```python
class Student:

    def intro(self):
        print(self)

s1 = Student()

s1.intro()
```

Internally Python converts:

```python
s1.intro()
```

to:

```python
Student.intro(s1)
```

Therefore:

```python
self
```

means:

```text
Current Object
```

---

## Example

```python
class Student:

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student("Vrushali")

s1.display()
```

Output:

```text
Vrushali
```

---

# AI Engineering Example

Most AI libraries use OOP.

Example:

```python
class AIModel:

    def predict(self):
        print("Prediction")

model = AIModel()

model.predict()
```

Output:

```text
Prediction
```

Examples from AI:

```text
NumPy Arrays
Pandas DataFrames
Scikit-Learn Models
PyTorch Models
TensorFlow Models
```

All are based on OOP.

---

# Mini Project

## Student Information System

```python
class Student:

    def __init__(self,name,marks):

        self.name = name
        self.marks = marks

    def display(self):

        print("Name :",self.name)
        print("Marks:",self.marks)

s1 = Student("Vrushali",95)

s1.display()
```

Output:

```text
Name : Vrushali
Marks: 95
```

---

# Interview Questions

## Q1. What is OOP?

Answer:

Object-Oriented Programming is a programming paradigm that uses classes and objects.

---

## Q2. What is a class?

Answer:

A class is a blueprint used to create objects.

Example:

```python
class Student:
    pass
```

---

## Q3. What is an object?

Answer:

An object is an instance of a class.

Example:

```python
s1 = Student()
```

---

## Q4. What is a constructor?

Answer:

A constructor is a special function that automatically executes when an object is created.

---

## Q5. What is `__init__()`?

Answer:

It is Python's constructor method.

---

## Q6. What is `self`?

Answer:

`self` refers to the current object.

---

## Q7. Difference between Class and Object?

| Class     | Object          |
| --------- | --------------- |
| Blueprint | Actual Instance |

---

## Q8. Is constructor mandatory?

Answer:

No.

Example:

```python
class Student:
    pass
```

works perfectly.

---

# Practice Questions

## Easy

1. Create Student class.
2. Create Employee class.
3. Create Car class.
4. Create Mobile class.
5. Create Laptop class.

---

## Medium

6. Create constructor for Student.
7. Create constructor for Employee.
8. Create constructor for Product.
9. Print student details.
10. Print employee details.

---

## Advanced Beginner

11. Student Result System.
12. Bank Account class.
13. ATM Machine class.
14. Library class.
15. AI Career Predictor class.

---

# Revision Notes

```text
OOP
```

```text
Class = Blueprint
```

```text
Object = Instance
```

```python
class Student:
```

```python
s1 = Student()
```

```python
def __init__():
```

```python
self
```

```text
self = Current Object
```

```text
Object = Data + Methods
```

---

# Summary

Today I learned:

✅ OOP Basics
✅ Class
✅ Object
✅ Constructor
✅ Parameterized Constructor
✅ Instance Variables
✅ Instance Methods
✅ self Keyword
✅ Multiple Objects
✅ OOP Design Thinking
✅ AI Library OOP Structure

---

# Learn Later Reminder

```text
Recursion           🟡 Learn Later
Lambda              🟡 Learn Later
Map                 🟡 Learn Later
Filter              🟡 Learn Later
Reduce              🟡 Learn Later
```

These topics can be revisited later during Advanced Python and DSA.
