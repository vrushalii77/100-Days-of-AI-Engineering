# Day 6 — Tuples, Sets, Dictionaries & Hashing (Foundation of AI Data Structures)

# Topics Covered

## Part 1 — Tuples

1. What is a Tuple?
2. Why use Tuple?
3. Tuple vs List
4. Tuple Operations
5. Tuple Methods
6. Tuple Unpacking

---

## Part 2 — Sets

7. What is a Set?
8. Why use Set?
9. Set Operations
10. Set Methods
11. Union
12. Intersection
13. Difference

---

## Part 3 — Dictionaries

14. What is Dictionary?
15. Key-Value Pairs
16. Dictionary Methods
17. Traversing Dictionary
18. Nested Dictionary

---

## Part 4 — Hashing

19. What is Hashing?
20. Why Hashing is Fast?
21. Hash Table Concept
22. Real-Life Examples

---

# PART 1 — TUPLES

# What is a Tuple?

## Description

A tuple is an **ordered and immutable collection** of elements.

```python
student = ("Vrushali", 22, "AI")
```

---

## Why Use Tuple?

Tuples are used when data should **never change**.

Example:

```python
birth_date = (20, 4, 2003)
```

You don't want someone to accidentally modify:

```python
birth_date[0] = 15
```

This will produce:

```text
TypeError
```

---

## Creating Tuples

```python
t = (1,2,3)

print(t)
```

Output:

```text
(1, 2, 3)
```

---

## Tuple Indexing

```python
t = (10,20,30,40)

print(t[0])
print(t[-1])
```

Output:

```text
10
40
```

---

## Tuple Slicing

```python
t = (10,20,30,40,50)

print(t[1:4])
```

Output:

```text
(20, 30, 40)
```

---

## Tuple Immutability

Wrong:

```python
t = (10,20,30)

t[0] = 100
```

Output:

```text
TypeError
```

---

## Tuple Methods

### count()

```python
t = (1,1,1,2,3)

print(t.count(1))
```

Output:

```text
3
```

---

### index()

```python
t = (10,20,30)

print(t.index(20))
```

Output:

```text
1
```

---

## Tuple Unpacking

```python
student = ("Vrushali",22)

name, age = student

print(name)
print(age)
```

Output:

```text
Vrushali
22
```

---

## Tuple vs List

| List        | Tuple       |
| ----------- | ----------- |
| Mutable     | Immutable   |
| []          | ()          |
| Slower      | Faster      |
| More Memory | Less Memory |

---

## AI Example

Machine Learning models often return tuples.

```python
result = ("Accuracy",95)
```

---

# PART 2 — SETS

# What is a Set?

## Description

A set is an unordered collection of unique elements.

```python
s = {1,2,3,4}
```

---

## Why Use Sets?

Sets automatically remove duplicates.

Example:

```python
numbers = [1,2,3,1,2,3]

print(set(numbers))
```

Output:

```text
{1,2,3}
```

---

## Creating Sets

```python
s = {1,2,3,4}

print(s)
```

Output:

```text
{1,2,3,4}
```

---

## Add Element

```python
s.add(5)

print(s)
```

Output:

```text
{1,2,3,4,5}
```

---

## Remove Element

```python
s.remove(2)

print(s)
```

Output:

```text
{1,3,4,5}
```

---

## Union

```python
a = {1,2,3}
b = {3,4,5}

print(a.union(b))
```

Output:

```text
{1,2,3,4,5}
```

---

## Intersection

```python
print(a.intersection(b))
```

Output:

```text
{3}
```

---

## Difference

```python
print(a.difference(b))
```

Output:

```text
{1,2}
```

---

## Membership

```python
print(5 in a)
```

Output:

```text
False
```

---

# Why Are Sets Fast?

Sets use **Hashing**.

Search Complexity:

```text
List : O(n)
Set  : O(1)
```

---

## Real-Life Example

Instagram username availability checking:

```text
"Is this username already taken?"
```

Uses hashing and sets.

---

# PART 3 — DICTIONARIES

# What is a Dictionary?

A dictionary stores data as:

```text
KEY : VALUE
```

Example:

```python
student = {
    "name":"Vrushali",
    "age":22,
    "course":"AI"
}
```

---

## Why Use Dictionary?

Without dictionary:

```python
name = "Vrushali"
age = 22
course = "AI"
```

With dictionary:

```python
student = {
    "name":"Vrushali",
    "age":22,
    "course":"AI"
}
```

---

## Access Values

```python
print(student["name"])
```

Output:

```text
Vrushali
```

---

## Add Data

```python
student["city"] = "Pune"
```

---

## Update Data

```python
student["age"] = 23
```

---

## Delete Data

```python
del student["city"]
```

---

# Dictionary Methods

## keys()

```python
print(student.keys())
```

---

## values()

```python
print(student.values())
```

---

## items()

```python
print(student.items())
```

---

## get()

```python
print(student.get("name"))
```

Output:

```text
Vrushali
```

---

# Traversing Dictionary

```python
student = {
    "name":"Vrushali",
    "age":22
}

for key, value in student.items():
    print(key, value)
```

Output:

```text
name Vrushali
age 22
```

---

# Nested Dictionary

```python
students = {

    "Student1":{
        "name":"Vrushali",
        "age":22
    },

    "Student2":{
        "name":"Rahul",
        "age":23
    }
}
```

---

# PART 4 — HASHING

# What is Hashing?

Hashing converts data into a unique number called a **hash value**.

Example:

```text
"Vrushali"

↓

4521568
```

Python stores:

```text
4521568 → Memory Address
```

---

## Why Hashing?

Without hashing:

```text
Search = O(n)
```

With hashing:

```text
Search = O(1)
```

---

## Real-Life Examples

### Google Search

```text
URL lookup
```

Uses hashing.

---

### ChatGPT

```text
Word

↓

Token ID

↓

Hash Table Lookup
```

---

### Password Storage

Instead of storing:

```text
admin123
```

Store:

```text
HAF763JDJD838
```

using hashing algorithms.

---

# AI Engineering Connection

## Dictionary

```python
word_to_id = {
    "I":101,
    "love":102,
    "AI":103
}
```

---

## Set

```python
unique_words = {
    "AI",
    "Python",
    "ML"
}
```

---

## Tuple

```python
prediction = (
    "Cat",
    98.5
)
```

---

## Hashing

Used in:

- ChatGPT token lookup
- Search engines
- Databases
- Redis cache
- Machine learning pipelines

---

# Interview Questions with Answers

## Q1. Difference between List and Tuple?

| List    | Tuple     |
| ------- | --------- |
| Mutable | Immutable |
| []      | ()        |

---

## Q2. Why are tuples faster?

### Answer:

Because tuples are immutable and optimized internally.

---

## Q3. Can sets contain duplicates?

### Answer:

No.

Sets automatically remove duplicates.

---

## Q4. Why are sets fast?

### Answer:

Because sets use hashing.

---

## Q5. Difference between Dictionary and List?

| List        | Dictionary |
| ----------- | ---------- |
| Index Based | Key Based  |

---

## Q6. What is Hashing?

### Answer:

Hashing converts data into a unique hash value for fast lookup.

---

## Q7. Time Complexity of Dictionary Lookup?

### Answer:

```text
O(1)
```

---

# Practice Questions

## Tuple

1. Print first element.
2. Print last element.
3. Count occurrence.
4. Find index.
5. Tuple unpacking.

---

## Set

6. Remove duplicates.
7. Find union.
8. Find intersection.
9. Find difference.
10. Check membership.

---

## Dictionary

11. Create student dictionary.
12. Add new key.
13. Update value.
14. Delete key.
15. Print all keys and values.

---

# Mini Project

## Student Database

```python
students = {

    "Vrushali":{
        "marks":90,
        "course":"AI"
    },

    "Rahul":{
        "marks":75,
        "course":"Python"
    }
}

for student, data in students.items():

    print(student)

    for key, value in data.items():
        print(key, ":", value)
```

---

# Homework

## Task 1

Create a tuple of 5 numbers.

Print:

- First element
- Last element
- Length

---

## Task 2

Remove duplicates from:

```python
[1,2,3,1,2,4]
```

---

## Task 3

Create dictionary:

```python
{
    "name":"Vrushali",
    "age":22,
    "city":"Pune"
}
```

Print all values.

---

## Task 4

Create frequency counter.

Input:

```text
banana
```

Output:

```text
b : 1
a : 3
n : 2
```

---

# Revision Notes

```python
Tuple:
()
```

```python
Set:
{}
```

```python
Dictionary:
{
   key:value
}
```

```text
Tuple:
Immutable
```

```text
Set:
Unique Values
```

```text
Dictionary:
Key-Value Storage
```

```text
Hashing:
O(1) Search
```

---

# Summary

Today you learned:

✅ Tuples
✅ Tuple Unpacking
✅ Sets
✅ Set Operations
✅ Dictionaries
✅ Dictionary Methods
✅ Nested Dictionaries
✅ Hashing
✅ Hash Tables
✅ AI Data Structures
✅ Interview Questions

These concepts are heavily used in:

- Machine Learning
- Deep Learning
- NLP
- ChatGPT
- Search Engines
- Databases
- Redis
- Software Engineering
- AI Systems
