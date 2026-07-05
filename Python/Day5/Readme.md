# Day 5 — Lists in Python (Most Important Data Structure in AI & Machine Learning)

# Topics Covered

1. What is a List?
2. Why do we need Lists?
3. Creating Lists
4. List Indexing
5. Negative Indexing
6. List Slicing
7. List Mutability
8. Traversing Lists
9. List Methods
10. Nested Lists
11. List Operations
12. Membership Operators
13. Useful Functions
14. List Comprehension
15. Real-Life Examples
16. AI Engineering Connection
17. Interview Questions with Answers
18. Practice Questions
19. Homework

---

# 1. What is a List?

## Description

A list is an ordered collection of multiple values stored inside square brackets `[]`.

Example:

```python
marks = [70, 80, 90, 100]
```

---

## Why Use Lists?

Without lists:

```python
student1 = 70
student2 = 80
student3 = 90
student4 = 100
```

With lists:

```python
marks = [70, 80, 90, 100]
```

Advantages:

- Store multiple values
- Reduce variables
- Easy data processing
- Used heavily in AI and Machine Learning

---

## Real-Life Example

Student marks:

```text
70
80
90
100
```

Store as:

```python
marks = [70,80,90,100]
```

---

# 2. Creating Lists

## Integer List

```python
numbers = [1,2,3,4,5]

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

## String List

```python
names = ["Vrushali","Rahul","Priya"]

print(names)
```

Output:

```text
['Vrushali', 'Rahul', 'Priya']
```

---

## Mixed List

```python
data = [1, "AI", 3.14, True]

print(data)
```

Output:

```text
[1, 'AI', 3.14, True]
```

---

# 3. List Indexing

Example:

```python
fruits = ["Apple","Banana","Orange","Mango"]
```

| Element | Apple | Banana | Orange | Mango |
| ------- | ----- | ------ | ------ | ----- |
| Index   | 0     | 1      | 2      | 3     |

---

## First Element

```python
print(fruits[0])
```

Output:

```text
Apple
```

---

## Second Element

```python
print(fruits[1])
```

Output:

```text
Banana
```

---

## Last Element

```python
print(fruits[3])
```

Output:

```text
Mango
```

---

# 4. Negative Indexing

| Element | Apple | Banana | Orange | Mango |
| ------- | ----- | ------ | ------ | ----- |
| Index   | -4    | -3     | -2     | -1    |

Example:

```python
print(fruits[-1])
```

Output:

```text
Mango
```

---

# 5. List Slicing

## Syntax

```python
list[start:stop]
```

---

## Example

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output:

```text
[20,30,40]
```

---

## Example

```python
print(numbers[:3])
```

Output:

```text
[10,20,30]
```

---

## Example

```python
print(numbers[2:])
```

Output:

```text
[30,40,50]
```

---

## Reverse List

```python
print(numbers[::-1])
```

Output:

```text
[50,40,30,20,10]
```

---

# 6. Lists are Mutable

Unlike strings, lists can be modified.

Example:

```python
numbers = [10,20,30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100,20,30]
```

---

## Difference

| String    | List    |
| --------- | ------- |
| Immutable | Mutable |

---

# 7. Traversing Lists

## Method 1

```python
numbers = [10,20,30]

for item in numbers:
    print(item)
```

Output:

```text
10
20
30
```

---

## Method 2

```python
for i in range(len(numbers)):
    print(numbers[i])
```

Output:

```text
10
20
30
```

---

# 8. List Methods

---

## append()

Adds element at the end.

```python
numbers = [1,2,3]

numbers.append(4)

print(numbers)
```

Output:

```text
[1,2,3,4]
```

---

## insert()

```python
numbers = [1,2,3]

numbers.insert(1,100)

print(numbers)
```

Output:

```text
[1,100,2,3]
```

---

## remove()

```python
numbers = [10,20,30]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10,30]
```

---

## pop()

```python
numbers = [10,20,30]

numbers.pop()

print(numbers)
```

Output:

```text
[10,20]
```

---

## clear()

```python
numbers = [1,2,3]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

---

## sort()

```python
numbers = [4,2,1,5]

numbers.sort()

print(numbers)
```

Output:

```text
[1,2,4,5]
```

---

## reverse()

```python
numbers = [1,2,3]

numbers.reverse()

print(numbers)
```

Output:

```text
[3,2,1]
```

---

## count()

```python
nums = [1,1,2,3]

print(nums.count(1))
```

Output:

```text
2
```

---

## index()

```python
nums = [10,20,30]

print(nums.index(20))
```

Output:

```text
1
```

---

# 9. List Operations

## Concatenation

```python
a = [1,2]
b = [3,4]

print(a+b)
```

Output:

```text
[1,2,3,4]
```

---

## Repetition

```python
print([1]*5)
```

Output:

```text
[1,1,1,1,1]
```

---

# Membership Operator

```python
print(10 in [10,20,30])
```

Output:

```text
True
```

---

# 10. Nested Lists

List inside another list.

```python
matrix = [
    [1,2],
    [3,4]
]

print(matrix)
```

Output:

```text
[[1,2],[3,4]]
```

---

## Access Nested Element

```python
print(matrix[1][0])
```

Output:

```text
3
```

---

# Real-Life Example

Student Database:

```python
students = [
    ["Vrushali",22],
    ["Rahul",24],
    ["Priya",23]
]
```

---

# 11. Useful Functions

## len()

```python
numbers = [1,2,3,4]

print(len(numbers))
```

Output:

```text
4
```

---

## max()

```python
print(max(numbers))
```

Output:

```text
4
```

---

## min()

```python
print(min(numbers))
```

Output:

```text
1
```

---

## sum()

```python
print(sum(numbers))
```

Output:

```text
10
```

---

# 12. List Comprehension

## Traditional Way

```python
square = []

for i in range(5):
    square.append(i*i)

print(square)
```

Output:

```text
[0,1,4,9,16]
```

---

## List Comprehension

```python
square = [i*i for i in range(5)]

print(square)
```

Output:

```text
[0,1,4,9,16]
```

---

## Example

```python
even = [i for i in range(20) if i%2==0]

print(even)
```

Output:

```text
[0,2,4,6,8,10,12,14,16,18]
```

---

# Mini Project

## Student Marks Analyzer

```python
marks = [70,80,90,95,85]

print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Average:", sum(marks)/len(marks))
```

Output:

```text
Maximum: 95
Minimum: 70
Average: 84.0
```

---

# AI Engineering Connection

Lists are used everywhere in AI.

---

## Dataset

```python
dataset = [10,20,30,40]
```

---

## Image Representation

```python
image = [
    [255,0],
    [0,255]
]
```

---

## Features

```python
features = [height, weight, age]
```

---

## Neural Network Weights

```python
weights = [0.2,0.5,0.8]
```

---

## Token IDs

```python
tokens = [101,2054,2003]
```

---

## Predictions

```python
predictions = [0.9,0.1]
```

---

# Common Beginner Mistakes

## Mistake 1

```python
numbers.append([4,5])
```

Output:

```text
[1,2,3,[4,5]]
```

---

## Mistake 2

Confusing:

```python
sort()
```

and

```python
sorted()
```

---

## Mistake 3

```python
numbers[100]
```

Output:

```text
IndexError
```

---

# Interview Questions with Answers

## Q1. What is a list?

Answer:

A list is an ordered, mutable collection of elements.

---

## Q2. Are lists mutable?

Answer:

Yes.

Example:

```python
numbers[0] = 100
```

---

## Q3. Difference between list and tuple?

| List    | Tuple     |
| ------- | --------- |
| Mutable | Immutable |
| []      | ()        |

---

## Q4. Difference between append() and extend()?

append():

```python
a.append([3,4])
```

Output:

```python
[1,2,[3,4]]
```

extend():

```python
a.extend([3,4])
```

Output:

```python
[1,2,3,4]
```

---

## Q5. Difference between remove() and pop()?

| remove()      | pop()         |
| ------------- | ------------- |
| Removes value | Removes index |

---

## Q6. What is List Comprehension?

Answer:

A shorter way of creating lists.

Example:

```python
[i*i for i in range(5)]
```

---

## Q7. How are lists used in AI?

Answer:

- Datasets
- Features
- Images
- Neural Networks
- Tokenization
- Predictions

---

# Practice Questions

## Easy

1. Print first element.
2. Print last element.
3. Print middle element.
4. Reverse list.
5. Find length.

---

## Medium

6. Find maximum.
7. Find minimum.
8. Find sum.
9. Count even numbers.
10. Count odd numbers.

---

## Advanced

11. Find duplicates.
12. Remove duplicates.
13. Find second largest.
14. Rotate list.
15. Merge two lists.

---

# Homework

## Task 1

Take 5 numbers from user and store in a list.

---

## Task 2

Print:

```text
Maximum
Minimum
Average
```

---

## Task 3

Reverse list without using reverse().

---

## Task 4

Find second largest element.

---

# Revision Notes

```python
List:
[]
```

```python
Indexing:
[]
```

```python
Slicing:
[start:stop:step]
```

```python
Reverse:
[::-1]
```

```python
Methods:

append()
insert()
remove()
pop()
clear()
sort()
reverse()
count()
index()
```

```python
Functions:

len()
max()
min()
sum()
```

```python
List Comprehension:

[i for i in iterable]
```

---

# Summary

Today you learned:

✅ Lists  
✅ Indexing  
✅ Slicing  
✅ Mutable Objects  
✅ List Methods  
✅ Nested Lists  
✅ List Operations  
✅ List Comprehension  
✅ AI Dataset Representation  
✅ Interview Questions

These concepts are the foundation of:

- Machine Learning
- Deep Learning
- NLP
- Computer Vision
- Generative AI
- LLMs
- Data Science
