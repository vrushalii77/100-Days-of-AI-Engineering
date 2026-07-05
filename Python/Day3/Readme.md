# Day 3 — Loops in Python (Foundation of AI Programming)

# Topics Covered

1. What are Loops?
2. Why do we need loops?
3. for loop
4. range() function
5. while loop
6. Infinite loop
7. break
8. continue
9. pass
10. Nested loops
11. Pattern programs
12. Real-life examples
13. AI Engineering connection
14. Interview Questions with Answers
15. Practice Questions
16. Homework

---

# 1. What are Loops?

## Description

A loop is used to execute the same block of code multiple times.

Without loops:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

With loops:

```python
for i in range(5):
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
Hello
Hello
```

---

## Why Use Loops?

Loops help us:

- Reduce code
- Save time
- Automate tasks
- Process large amounts of data
- Build AI and Machine Learning systems

---

## Real-Life Example

Suppose a teacher checks attendance of 100 students.

Instead of writing:

```text
Check student1
Check student2
Check student3
...
Check student100
```

the teacher repeats the same task.

That repetition is called a loop.

---

# Types of Loops

There are two major loops:

```text
1. for loop
2. while loop
```

---

# 2. for Loop

## Description

A for loop executes a block of code a fixed number of times.

---

## Syntax

```python
for variable in sequence:
    statements
```

---

## Example

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## Flow

Iteration 1:

```text
i = 0
```

Iteration 2:

```text
i = 1
```

Iteration 3:

```text
i = 2
```

Continue until:

```text
i = 4
```

---

# 3. range() Function

range() generates numbers.

---

## range(stop)

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## range(start, stop)

```python
for i in range(1,6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## range(start, stop, step)

```python
for i in range(0,10,2):
    print(i)
```

Output:

```text
0
2
4
6
8
```

---

# Example: Print Name

```python
for i in range(5):
    print("Vrushali")
```

Output:

```text
Vrushali
Vrushali
Vrushali
Vrushali
Vrushali
```

---

# Example: Multiplication Table

```python
num = 5

for i in range(1,11):
    print(num*i)
```

Output:

```text
5
10
15
20
25
30
35
40
45
50
```

---

# Example: Sum of First N Numbers

```python
sum = 0

for i in range(1,6):
    sum += i

print(sum)
```

Output:

```text
15
```

---

## Flow

```text
sum = 0

1 -> sum = 1
2 -> sum = 3
3 -> sum = 6
4 -> sum = 10
5 -> sum = 15
```

---

# 4. while Loop

## Description

while loop executes until the condition becomes False.

---

## Syntax

```python
while condition:
    statements
```

---

## Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

---

## Flow

```text
i = 1

1 <= 5
print 1

2 <= 5
print 2

...

6 <= 5

False

Stop
```

---

# Real-Life Example

ATM PIN attempts.

```python
attempt = 1

while attempt <= 3:
    print("Try PIN")
    attempt += 1
```

Output:

```text
Try PIN
Try PIN
Try PIN
```

---

# 5. Infinite Loop

A loop that never stops.

Example:

```python
while True:
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
...
```

---

## Why Dangerous?

- Program freezes
- CPU usage increases
- Computer slows down

---

# 6. break Statement

break immediately exits the loop.

---

## Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## Flow

```text
0 print
1 print
2 print
3 print
4 print

5 found

break

stop
```

---

# 7. continue Statement

continue skips current iteration.

---

## Example

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

---

## Flow

```text
0 print
1 print
2 skip
3 print
4 print
```

---

# 8. pass Statement

pass means:

```text
Do nothing
```

Used as a placeholder.

---

## Example

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 9. Nested Loops

Loop inside another loop.

---

## Example

```python
for i in range(3):

    for j in range(2):
        print(i,j)
```

Output:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

---

## Flow Diagram

```text
i=0
    j=0
    j=1

i=1
    j=0
    j=1

i=2
    j=0
    j=1
```

---

# Pattern Program 1

```python
for i in range(1,6):
    print("*"*i)
```

Output:

```text
*
**
***
****
*****
```

---

# Pattern Program 2

```python
for i in range(5,0,-1):
    print("*"*i)
```

Output:

```text
*****
****
***
**
*
```

---

# Pattern Program Using Nested Loop

```python
for i in range(1,6):

    for j in range(i):
        print("*",end="")

    print()
```

Output:

```text
*
**
***
****
*****
```

---

# Mini Project

## Number Guessing Game

```python
secret = 7

while True:

    guess = int(input())

    if guess == secret:
        print("Correct")
        break

    else:
        print("Try Again")
```

---

# Sample Output

```text
2
Try Again

5
Try Again

7
Correct
```

---

# Common Beginner Mistakes

---

## Mistake 1

```python
while i<5:
    print(i)
```

Forgot:

```python
i += 1
```

Result:

```text
Infinite loop
```

---

## Mistake 2

Wrong indentation:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

## Mistake 3

Confusing break and continue.

```text
break    → stop loop
continue → skip iteration
```

---

# AI Engineering Connection

Loops are used everywhere in AI.

---

## Training Model

```python
for epoch in range(100):
    train_model()
```

---

## Reading Images

```python
for image in dataset:
    process(image)
```

---

## NLP

```python
for word in sentence:
    analyze(word)
```

---

## Neural Networks

```python
for layer in network:
    calculate()
```

Without loops:

```text
AI
Machine Learning
Deep Learning
```

cannot exist.

---

# Interview Questions with Answers

---

## Q1. What is a loop?

Answer:

A loop is a programming construct used to execute the same block of code repeatedly until a condition becomes false or a sequence ends.

---

## Q2. What are the types of loops in Python?

Answer:

There are two loops:

```text
1. for loop
2. while loop
```

---

## Q3. Difference between for loop and while loop?

| for loop         | while loop         |
| ---------------- | ------------------ |
| Fixed iterations | Unknown iterations |
| Uses sequence    | Uses condition     |
| Easier           | More flexible      |

---

## Q4. What is range()?

Answer:

range() generates a sequence of numbers.

Examples:

```python
range(5)
range(1,5)
range(1,10,2)
```

---

## Q5. What is an infinite loop?

Answer:

A loop that never terminates.

Example:

```python
while True:
    print("Hello")
```

---

## Q6. What is break?

Answer:

break immediately terminates the loop.

Example:

```python
for i in range(10):
    if i==5:
        break
```

---

## Q7. What is continue?

Answer:

continue skips the current iteration and moves to the next iteration.

---

## Q8. What is pass?

Answer:

pass is a placeholder statement that does nothing.

Example:

```python
if True:
    pass
```

---

## Q9. What are nested loops?

Answer:

A loop inside another loop is called nested loop.

---

## Q10. What happens if increment is forgotten in while loop?

Answer:

It creates an infinite loop.

Example:

```python
i=1

while i<5:
    print(i)
```

---

## Q11. Can while loop replace for loop?

Answer:

Yes.

Example:

```python
i=0

while i<5:
    print(i)
    i+=1
```

---

## Q12. Where are loops used in AI?

Answer:

Loops are used in:

- Training models
- Processing datasets
- Neural networks
- Image processing
- NLP
- Deep learning

---

# Practice Questions

## Easy

1. Print 1 to 10
2. Print 10 to 1
3. Print even numbers
4. Print odd numbers
5. Print your name 10 times

---

## Medium

6. Multiplication table
7. Sum of first N numbers
8. Factorial
9. Count digits
10. Reverse a number

---

## Advanced

11. Prime number
12. Fibonacci series
13. Armstrong number
14. Palindrome number
15. Number guessing game

---

# Revision Notes

## Loops

```python
for
while
```

---

## Loop Controls

```python
break
continue
pass
```

---

## range()

```python
range(stop)

range(start,stop)

range(start,stop,step)
```

---

# Summary

Today you learned:

✅ for loop  
✅ while loop  
✅ range()  
✅ break  
✅ continue  
✅ pass  
✅ nested loops  
✅ pattern programs  
✅ AI usage of loops

These concepts are used everywhere in AI, Machine Learning, Data Science, NLP, and Deep Learning.
