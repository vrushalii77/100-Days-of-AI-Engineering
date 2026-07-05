# DAY 1 — Python Basics for AI Engineers

# Topics We Will Learn Today

1. What is Python?
2. Why Python is used in AI
3. Installing & Running Python
4. Variables
5. Data Types
6. Input & Output
7. Type Casting
8. Comments
9. Mini Project
10. Interview Questions
11. Practice Questions
12. Homework

---

# 1. What is Python?

## Description

Python is a programming language used to build:

- Websites
- AI applications
- Machine Learning models
- Automation tools
- Games
- APIs
- Chatbots

It is one of the easiest programming languages.

---

## Why Use Python?

Because Python is:

- Easy to read
- Beginner friendly
- Powerful
- Used in AI and Machine Learning
- Has many libraries

Example:

- NumPy
- Pandas
- TensorFlow
- PyTorch
- Scikit-learn

---

## Real-Life Example

Apps using Python:

- YouTube
- Instagram
- Netflix
- ChatGPT-related tools
- AI assistants
- Recommendation systems

---

# 2. Running Python Program

## Your First Program

```python
print("Hello World")
```

---

## Output

```python
Hello World
```

---

## Explanation Flow

### Step 1

`print()` is used to display output.

### Step 2

Text inside quotes is called a string.

### Step 3

Python prints it on screen.

---

# 3. Variables

# Description

Variables store data.

Think of a variable like a container or box.

Example:

- A water bottle stores water.
- A variable stores data.

---

# Why Use Variables?

Without variables:

- We cannot store values.
- We cannot reuse data.
- We cannot build applications.

---

# Real-Life Example

```text
name = "Vrushali"
```

Imagine:

- Label on box → `name`
- Content inside box → `"Vrushali"`

---

# Syntax

```python
variable_name = value
```

---

# Example 1

```python
name = "Vrushali"

print(name)
```

---

# Output

```python
Vrushali
```

---

# Line-by-Line Explanation

## Line 1

```python
name = "Vrushali"
```

- Variable created → `name`
- Stored value → `"Vrushali"`

---

## Line 2

```python
print(name)
```

Prints stored value.

---

# Example 2

```python
age = 21

print(age)
```

---

# Output

```python
21
```

---

# Rules for Variable Names

✅ Correct

```python
student_name
age
num1
```

❌ Wrong

```python
1name
student-name
class
```

---

# 4. Data Types

# Description

Data type means:
“What kind of data is stored?”

---

# Main Data Types

| Data Type | Example |
| --------- | ------- |
| int       | 10      |
| float     | 5.6     |
| str       | "Hello" |
| bool      | True    |

---

# 4.1 Integer (int)

Whole numbers.

```python
age = 21

print(age)
```

Output:

```python
21
```

---

# 4.2 Float

Decimal numbers.

```python
price = 99.99

print(price)
```

Output:

```python
99.99
```

---

# 4.3 String

Text data.

```python
city = "Pune"

print(city)
```

Output:

```python
Pune
```

---

# 4.4 Boolean

Only:

- True
- False

```python
is_student = True

print(is_student)
```

Output:

```python
True
```

---

# Checking Data Type

Use:

```python
type()
```

---

# Example

```python
age = 21

print(type(age))
```

---

# Output

```python
<class 'int'>
```

---

# Explanation

`type()` tells the datatype.

---

# 5. Input from User

# Description

`input()` takes data from user.

---

# Why Use Input?

Without input:

- Program becomes fixed.
- User cannot interact.

AI apps also take input:

- ChatGPT
- Search engines
- Voice assistants

---

# Example

```python
name = input("Enter your name: ")

print(name)
```

---

# Output

```python
Enter your name: Vrushali
Vrushali
```

---

# Flow Explanation

## Step 1

Program asks:

```python
Enter your name:
```

## Step 2

User types:

```python
Vrushali
```

## Step 3

Stored in variable `name`

## Step 4

Printed on screen.

---

# Important Point

`input()` always returns STRING.

Even if user enters:

```python
21
```

Python stores:

```python
"21"
```

(string)

---

# 6. Type Casting

# Description

Type casting means:
Converting one datatype into another datatype.

---

# Why Use It?

Suppose:

```python
age = input("Enter age: ")
```

User enters:

```python
21
```

Python stores:

```python
"21"
```

(string)

But for calculations we need integer.

---

# Integer Conversion

```python
age = int(input("Enter age: "))

print(age)
print(type(age))
```

---

# Output

```python
Enter age: 21
21
<class 'int'>
```

---

# Float Conversion

```python
price = float(input("Enter price: "))

print(price)
```

---

# Output

```python
Enter price: 99.5
99.5
```

---

# String Conversion

```python
num = 10

print(str(num))
```

---

# Output

```python
10
```

---

# Boolean Conversion

```python
print(bool(1))
print(bool(0))
```

---

# Output

```python
True
False
```

---

# 7. Comments

# Description

Comments are notes for programmers.

Python ignores comments.

---

# Why Use Comments?

- Makes code readable
- Explains logic
- Helpful in big projects

---

# Single Line Comment

```python
# This is comment
print("Hello")
```

---

# Multi-line Comment

```python
"""
This is
multi-line comment
"""
```

---

# 8. Mini Project — Student Introduction Program

# Problem Statement

Take:

- student name
- age
- city

and print complete introduction.

---

# Code

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("My name is", name)
print("I am", age, "years old")
print("I live in", city)
```

---

# Output

```python
Enter your name: Vrushali
Enter your age: 21
Enter your city: Pune

My name is Vrushali
I am 21 years old
I live in Pune
```

---

# Common Beginner Mistakes

## Mistake 1

```python
name = Vrushali
```

❌ Wrong

Because string must be inside quotes.

✅ Correct

```python
name = "Vrushali"
```

---

## Mistake 2

```python
age = input()
print(age + 5)
```

❌ Error

Because input gives string.

✅ Correct

```python
age = int(input())
print(age + 5)
```

---

## Mistake 3

Wrong indentation.

Python is indentation-sensitive.

---

# Interview Questions

## Basic Questions

1. What is Python?
2. Why is Python popular in AI?
3. What is variable?
4. Difference between int and float?
5. What does `input()` do?
6. Why do we use type casting?
7. What is comment?
8. What is output of:

```python
print(type("10"))
```

9. Difference between:

```python
10
"10"
```

10. What are Python data types?

---

# Required Details to Master This Topic

You should know:

- How variables work
- How input works
- Difference between string and integer
- Type conversion
- Basic syntax
- Output printing

---

# Practice Questions

# Easy Level

1. Print your name.

2. Store your age in variable and print it.

3. Store your city and print it.

4. Create variables for:
   - name
   - college
   - marks

5. Print datatype of:
   - 10
   - 5.5
   - "Hello"
   - True

---

# Medium Level

6. Take user name input and print welcome message.
7. Take 2 numbers and print sum.
8. Take age and print after 5 years.
9. Convert float into integer.
10. Convert integer into string.

---

# Advanced Beginner

11. Take student details and print formatted output.
12. Check datatype before and after conversion.
13. Create mini calculator for addition.
14. Ask user favorite programming language.
15. Take salary input and print yearly salary.

---

# Homework

## Task 1

Create program:

- Take user name
- Take favorite AI field
- Print:

```text
Hello Vrushali, you want to become AI Engineer.
```

---

## Task 2

Take:

- marks in 3 subjects
- print total

---

## Task 3

Take:

- first name
- last name

Print full name.

---

# Real AI Engineering Connection

Everything in AI starts with:

- Variables
- Data storage
- Input
- Output

Example:
When user types message in ChatGPT:

- input() concept works internally
- Variables store messages
- Data types manage text

So today’s concepts are the foundation of AI systems.

---

# Revision Notes

## Important Functions

| Function | Use                |
| -------- | ------------------ |
| print()  | display output     |
| input()  | take input         |
| type()   | check datatype     |
| int()    | convert to integer |
| float()  | convert to float   |
| str()    | convert to string  |

---

# Summary of Day 1

Today you learned:

- Python basics
- Variables
- Data types
- Input/output
- Type casting
- Comments

These are the foundation of all AI programming.

---

# Mini Challenge

Build this:

```text
AI Student Profile Generator
```

Take:

- name
- age
- goal
- favorite language

Then print professional output.

---
