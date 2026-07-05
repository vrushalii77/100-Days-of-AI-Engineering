# Day 7 — Functions, Scope, Recursion, Lambda, Map, Filter & Reduce

# Topics Covered

1. What is a Function?
2. Why use Functions?
3. Function Syntax
4. Function Calling
5. Parameters and Arguments
6. Return Statement
7. Types of Functions
8. Variable Scope
9. Recursion
10. Lambda Functions
11. Map
12. Filter
13. Reduce
14. AI Engineering Connection
15. Interview Questions
16. Practice Questions

---

# 1. What is a Function?

## Description

A function is a reusable block of code that performs a specific task.

Example:

Instead of writing:

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

We can write:

```python
def welcome():
    print("Welcome")
```

---

## Why Use Functions?

Functions help us:

- Avoid repetition
- Write clean code
- Reuse code
- Make debugging easier
- Divide big problems into small problems

---

## Real-Life Example

Think of a washing machine:

```text
Input Clothes
      ↓
Processing
      ↓
Output Clean Clothes
```

A function works the same way:

```text
Input
   ↓
Process
   ↓
Output
```

---

# 2. Function Syntax

```python
def function_name():
    statements
```

Example:

```python
def greet():
    print("Hello")
```

---

# 3. Calling a Function

```python
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
```

---

# Example

```python
def my_name():
    print("My name is Vrushali")

my_name()
```

Output:

```text
My name is Vrushali
```

---

# 4. Parameters and Arguments

## Parameter

Variables defined inside the function.

```python
def greet(name):
```

"name" is a parameter.

---

## Argument

Actual value passed during function call.

```python
greet("Vrushali")
```

"Vrushali" is an argument.

---

# Example

```python
def greet(name):
    print("Hello", name)

greet("Vrushali")
greet("Rahul")
```

Output:

```text
Hello Vrushali
Hello Rahul
```

---

# 5. Return Statement

The return keyword sends the result back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

## Why Return?

Without return:

```python
def add(a,b):
    print(a+b)
```

You cannot reuse the answer.

With return:

```python
x = add(10,20)
```

You can reuse the value.

---

# 6. Types of Functions

## Type 1: No Parameter No Return

```python
def hello():
    print("Hello")

hello()
```

Output:

```text
Hello
```

---

## Type 2: Parameter No Return

```python
def square(n):
    print(n*n)

square(5)
```

Output:

```text
25
```

---

## Type 3: No Parameter Return

```python
def get_number():
    return 100

print(get_number())
```

Output:

```text
100
```

---

## Type 4: Parameter Return

```python
def multiply(a,b):
    return a*b

print(multiply(5,4))
```

Output:

```text
20
```

---

# 7. Variable Scope

## Local Variable

A variable declared inside a function.

```python
def demo():
    x = 100
    print(x)

demo()
```

Output:

```text
100
```

Outside the function:

```python
print(x)
```

Output:

```text
NameError
```

---

## Global Variable

A variable declared outside a function.

```python
x = 500

def demo():
    print(x)

demo()
```

Output:

```text
500
```

---

# Example

```python
salary = 50000

def employee():
    bonus = 10000

    print(salary)
    print(bonus)

employee()
```

Output:

```text
50000
10000
```

---

# 8. Recursion

## What is Recursion?

A function calling itself.

Example:

```python
def hello():
    hello()
```

This creates infinite recursion.

---

## Real-Life Example

```text
5th stair
↓
4th stair
↓
3rd stair
↓
2nd stair
↓
1st stair
↓
Stop
```

---

## Factorial Using Recursion

Mathematically:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursively:

```text
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1
```

Code:

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))
```

Output:

```text
120
```

---

## Recursion Flow

```text
factorial(5)

5*factorial(4)

5*4*factorial(3)

5*4*3*factorial(2)

5*4*3*2*factorial(1)

return 1

5*4*3*2*1

120
```

---

## Important Rule of Recursion

Every recursive function requires:

### Base Case

```python
if n==1:
    return 1
```

### Smaller Problem

```python
factorial(n-1)
```

---

# Fibonacci Using Recursion

```python
def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

print(fib(6))
```

Output:

```text
8
```

---

# 9. Lambda Functions

## What is Lambda?

A lambda function is a small anonymous function.

Normal function:

```python
def square(x):
    return x*x
```

Lambda:

```python
square = lambda x: x*x

print(square(5))
```

Output:

```text
25
```

---

## Multiple Parameters

```python
add = lambda a,b: a+b

print(add(10,20))
```

Output:

```text
30
```

---

## Why Use Lambda?

Lambda functions are used heavily in:

- Data Science
- Machine Learning
- Pandas
- AI libraries

---

# 10. Map

## What is Map?

Map applies a function to every element.

Example:

```python
numbers = [1,2,3,4]

result = list(
    map(
        lambda x:x*x,
        numbers
    )
)

print(result)
```

Output:

```text
[1,4,9,16]
```

---

## Map Flow

```text
1 → 1²
2 → 2²
3 → 3²
4 → 4²
```

---

# 11. Filter

## What is Filter?

Filter keeps only the required elements.

```python
numbers = [1,2,3,4,5,6]

result = list(
    filter(
        lambda x:x%2==0,
        numbers
    )
)

print(result)
```

Output:

```text
[2,4,6]
```

---

## Filter Flow

```text
1 ❌
2 ✅
3 ❌
4 ✅
5 ❌
6 ✅
```

---

# 12. Reduce

Reduce combines all elements into one result.

First import:

```python
from functools import reduce
```

Example:

```python
from functools import reduce

numbers = [1,2,3,4]

result = reduce(
    lambda x,y:x+y,
    numbers
)

print(result)
```

Output:

```text
10
```

---

## Reduce Flow

```text
1+2=3

3+3=6

6+4=10
```

---

# AI Engineering Connection

## Data Preprocessing

```python
def preprocess(text):
    return text.lower()
```

---

## Prediction Function

```python
def predict(features):
    return "Cat"
```

---

## Activation Function

```python
def relu(x):
    return max(0,x)
```

---

## Token Processing

```python
tokens = list(
    map(
        lambda x:x.lower(),
        words
    )
)
```

---

# Interview Questions with Answers

---

## Q1. What is a function?

Answer:

A reusable block of code that performs a specific task.

---

## Q2. Difference between parameter and argument?

Example:

```python
def add(a,b):
```

a,b = parameters

```python
add(10,20)
```

10,20 = arguments

---

## Q3. What is return?

Answer:

Return sends a value back to the caller.

---

## Q4. Difference between local and global variable?

| Local           | Global           |
| --------------- | ---------------- |
| Inside function | Outside function |

---

## Q5. What is recursion?

Answer:

A function calling itself.

---

## Q6. What is lambda?

Answer:

A one-line anonymous function.

---

## Q7. Difference between map and filter?

| Map       | Filter |
| --------- | ------ |
| Transform | Select |

---

## Q8. What is reduce?

Answer:

Reduce combines multiple values into one value.

---

# Practice Questions

## Easy

1. Create function to print your name.
2. Create function to add two numbers.
3. Create function to find square.
4. Create function to find cube.
5. Create function to print table.

---

## Medium

6. Create function for factorial.
7. Create function for palindrome.
8. Create function for even/odd.
9. Create function to find largest.
10. Create function to count vowels.

---

## Advanced

11. Factorial using recursion.
12. Fibonacci using recursion.
13. Lambda for square.
14. Map to square list.
15. Filter even numbers.
16. Reduce to calculate sum.

---

# Important Note for My AI Journey

Recursion, Lambda, Map, Filter, and Reduce are difficult topics for beginners.

Current Status:

```text
Functions           ✅ Learned
Parameters          ✅ Learned
Return              ✅ Learned
Scope               ✅ Learned

Recursion           🟡 Learn Later
Lambda              🟡 Learn Later
Map                 🟡 Learn Later
Filter              🟡 Learn Later
Reduce              🟡 Learn Later
```

These topics can be revisited later during DSA and Advanced Python.

---

# Revision Notes

```python
def function():
    pass
```

```python
return value
```

```python
local variable
```

```python
global variable
```

```python
lambda x:x*x
```

```python
map()
```

```python
filter()
```

```python
reduce()
```

---

# Summary

Today I learned:

✅ Functions
✅ Parameters
✅ Arguments
✅ Return
✅ Function Types
✅ Local Variables
✅ Global Variables
✅ Recursion Basics
✅ Lambda Basics
✅ Map
✅ Filter
✅ Reduce
✅ AI Applications of Functions
