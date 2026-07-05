# Day 2 — Operators & Decision Making in Python

# Topics Covered

1. What are Operators?
2. Arithmetic Operators
3. Comparison Operators
4. Logical Operators
5. Assignment Operators
6. Membership Operators
7. Identity Operators
8. if Statement
9. if-else Statement
10. if-elif-else Ladder
11. Nested if
12. Mini Project
13. Common Mistakes
14. Interview Questions
15. Practice Questions
16. Homework
17. AI Engineering Connection

---

# 1. What are Operators?

## Description

Operators are special symbols used to perform operations on variables and values.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

Here, `+` is an operator.

---

## Why Use Operators?

Without operators:

- No calculations
- No comparisons
- No decision making
- No AI computations

AI models constantly use operators internally to calculate predictions and probabilities.

---

## Real Life Example

Suppose:

```text
Notebook = ₹50
Pen = ₹20
```

Total:

```text
50 + 20 = 70
```

---

# 2. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| +        | Addition       | 10 + 5   |
| -        | Subtraction    | 10 - 5   |
| \*       | Multiplication | 10 \* 5  |
| /        | Division       | 10 / 5   |
| //       | Floor Division | 10 // 3  |
| %        | Modulus        | 10 % 3   |
| \*\*     | Power          | 2 \*\* 3 |

---

## Addition

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

---

## Subtraction

```python
print(10 - 5)
```

Output:

```text
5
```

---

## Multiplication

```python
print(10 * 5)
```

Output:

```text
50
```

---

## Division

```python
print(10 / 2)
```

Output:

```text
5.0
```

### Important

Division always returns float.

---

## Floor Division

```python
print(10 // 3)
```

Output:

```text
3
```

Explanation:

```text
10 / 3 = 3.333
Floor division removes decimal.
```

---

## Modulus Operator

Returns remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

Explanation:

```text
10 ÷ 3

Quotient = 3
Remainder = 1
```

---

## Power Operator

```python
print(2 ** 3)
```

Output:

```text
8
```

Explanation:

```text
2 × 2 × 2 = 8
```

---

# 3. Comparison Operators

Used to compare values.

Result is always:

```text
True
or
False
```

| Operator | Meaning            |
| -------- | ------------------ |
| ==       | Equal              |
| !=       | Not Equal          |
| >        | Greater Than       |
| <        | Less Than          |
| >=       | Greater Than Equal |
| <=       | Less Than Equal    |

---

## Equal To

```python
print(10 == 10)
```

Output:

```text
True
```

---

## Not Equal

```python
print(10 != 5)
```

Output:

```text
True
```

---

## Greater Than

```python
print(20 > 10)
```

Output:

```text
True
```

---

## Less Than

```python
print(5 < 10)
```

Output:

```text
True
```

---

## Real-Life Example

Voting eligibility:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

---

# 4. Logical Operators

Used when multiple conditions exist.

---

## AND Operator

Syntax:

```python
condition1 and condition2
```

Both conditions must be True.

Example:

```python
age = 20
citizen = True

print(age >= 18 and citizen)
```

Output:

```text
True
```

---

## OR Operator

Syntax:

```python
condition1 or condition2
```

At least one condition should be True.

Example:

```python
print(True or False)
```

Output:

```text
True
```

---

## NOT Operator

Syntax:

```python
not condition
```

Example:

```python
print(not True)
```

Output:

```text
False
```

---

## Truth Table

### AND

| A   | B   | A and B |
| --- | --- | ------- |
| T   | T   | T       |
| T   | F   | F       |
| F   | T   | F       |
| F   | F   | F       |

---

### OR

| A   | B   | A or B |
| --- | --- | ------ |
| T   | T   | T      |
| T   | F   | T      |
| F   | T   | T      |
| F   | F   | F      |

---

# 5. Assignment Operators

Used to assign values.

---

## Basic Assignment

```python
x = 10
```

---

## Add and Assign

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

Equivalent to:

```python
x = x + 5
```

---

## Subtract and Assign

```python
x -= 2
```

Equivalent to:

```python
x = x - 2
```

---

## Multiply and Assign

```python
x *= 3
```

---

## Divide and Assign

```python
x /= 2
```

---

# 6. Membership Operators

Used to check existence.

---

## in Operator

```python
name = "Vrushali"

print("V" in name)
```

Output:

```text
True
```

---

## not in Operator

```python
print("z" not in name)
```

Output:

```text
False
```

---

# 7. Identity Operators

Used to check whether two variables point to the same object.

---

## is Operator

```python
a = 10
b = a

print(a is b)
```

Output:

```text
True
```

---

## is not Operator

```python
print(a is not b)
```

Output:

```text
False
```

---

# 8. if Statement

Used to make decisions.

---

## Syntax

```python
if condition:
    statement
```

---

## Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Output:

```text
Eligible to vote
```

---

# 9. if-else Statement

Used when there are two outcomes.

---

## Syntax

```python
if condition:
    statement
else:
    statement
```

---

## Example

```python
age = 15

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Not Eligible
```

---

## Real-Life Example

ATM withdrawal:

```python
balance = 1000
amount = 1500

if amount <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")
```

---

# 10. if-elif-else Ladder

Used when multiple conditions exist.

---

## Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Output:

```text
Grade B
```

---

# Flow

Marks = 85

Check:

```text
85 >= 90
```

False

Check:

```text
85 >= 75
```

True

Print:

```text
Grade B
```

---

# 11. Nested if

if inside another if.

---

## Example

```python
age = 20

if age >= 18:
    if age >= 21:
        print("Can enter VIP zone")
```

Output:

```text
Can enter VIP zone
```

---

## Real-Life Example

Scholarship eligibility:

```python
marks = 85
income = 200000

if marks >= 80:
    if income <= 300000:
        print("Scholarship Approved")
```

---

# Mini Project

## Student Grading System

```python
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

# Common Beginner Mistakes

## Mistake 1

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## Mistake 2

Wrong indentation:

```python
if age >= 18:
print("Eligible")
```

Correct:

```python
if age >= 18:
    print("Eligible")
```

---

## Mistake 3

Wrong operator:

```python
if username == uname & password == pass:
```

Correct:

```python
if username == uname and password == pass:
```

---

## Mistake 4

Using input without conversion:

```python
age = input()

if age >= 18:
```

Correct:

```python
age = int(input())
```

---

# Interview Questions

1. What are operators?
2. Difference between `/` and `//`?
3. What does `%` operator do?
4. Difference between `=` and `==`?
5. What is logical AND?
6. What is logical OR?
7. What is logical NOT?
8. What is nested if?
9. Difference between if and if-else?
10. What is elif?
11. Difference between `and` and `&`?
12. What are membership operators?
13. What are identity operators?

---

# Practice Questions

## Easy

1. Add two numbers.
2. Subtract two numbers.
3. Find remainder.
4. Find square of a number.
5. Check positive number.

---

## Medium

6. Check voting eligibility.
7. Check even or odd.
8. Find largest among two numbers.
9. Check pass or fail.
10. Calculate bonus.

---

## Advanced

11. Student grading system.
12. ATM withdrawal system.
13. Login system.
14. Largest among three numbers.
15. Scholarship eligibility checker.

---

# Homework

## Task 1

Take age and print:

```text
Eligible to Vote
```

or

```text
Not Eligible to Vote
```

---

## Task 2

Take two numbers and print:

- Addition
- Subtraction
- Multiplication
- Division

---

## Task 3

Take marks and print:

- A
- B
- C
- Fail

using if-elif-else.

---

# AI Engineering Connection

AI models continuously make decisions:

Examples:

- Spam or Not Spam
- Cat or Dog
- Fraud or Genuine
- Positive or Negative Review
- Recommendation or No Recommendation

All these AI systems use:

- Operators
- Comparisons
- Conditions
- Decision making

The concepts learned today are the foundation of Machine Learning algorithms.

---

# Revision Notes

## Arithmetic Operators

```python
+
-
*
/
//
%
**
```

---

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

---

## Logical Operators

```python
and
or
not
```

---

## Membership Operators

```python
in
not in
```

---

## Identity Operators

```python
is
is not
```

---

## Decision Making Statements

```python
if
if-else
if-elif-else
nested if
```

---

# Summary

Today you learned:

✅ Arithmetic Operators  
✅ Comparison Operators  
✅ Logical Operators  
✅ Assignment Operators  
✅ Membership Operators  
✅ Identity Operators  
✅ if Statement  
✅ if-else Statement  
✅ if-elif-else  
✅ Nested if  
✅ Real-world decision making

These concepts are the backbone of AI decision-making systems.
