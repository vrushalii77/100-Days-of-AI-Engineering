# Day 4 — Strings in Python (Foundation of AI, NLP & LLMs)

# Topics Covered

1. What is a String?
2. Why do we need Strings?
3. Creating Strings
4. String Indexing
5. Negative Indexing
6. String Slicing
7. String Immutability
8. String Traversal
9. String Operators
10. Useful String Methods
11. Escape Characters
12. Real-Life Examples
13. AI Engineering Connection
14. Interview Questions with Answers
15. Practice Questions
16. Homework

---

# 1. What is a String?

## Description

A string is a sequence of characters enclosed inside:

- Single quotes `' '`
- Double quotes `" "`
- Triple quotes `''' '''`

Examples:

```python
name = "Vrushali"

city = 'Pune'

message = '''Hello World'''
```

---

## Why Use Strings?

Strings are used to store:

- Names
- Emails
- Passwords
- User messages
- Prompts
- AI datasets
- Search queries
- Chat conversations

---

## Real-Life Example

```text
Name: Vrushali
Email: vrushali@gmail.com
Message: Hello ChatGPT
```

All of these are strings.

---

# 2. Creating Strings

## Using Double Quotes

```python
name = "Vrushali"

print(name)
```

Output:

```text
Vrushali
```

---

## Using Single Quotes

```python
city = 'Pune'

print(city)
```

Output:

```text
Pune
```

---

## Using Triple Quotes

```python
message = '''
Hello
World
'''

print(message)
```

Output:

```text
Hello
World
```

---

# 3. String Indexing

Every character has a position.

Example:

```python
name = "PYTHON"
```

| Character | P   | Y   | T   | H   | O   | N   |
| --------- | --- | --- | --- | --- | --- | --- |
| Index     | 0   | 1   | 2   | 3   | 4   | 5   |

---

## Access First Character

```python
print(name[0])
```

Output:

```text
P
```

---

## Access Third Character

```python
print(name[2])
```

Output:

```text
T
```

---

## Access Last Character

```python
print(name[5])
```

Output:

```text
N
```

---

# Flow

```text
PYTHON

0 -> P
1 -> Y
2 -> T
3 -> H
4 -> O
5 -> N
```

---

# 4. Negative Indexing

Python can count from right to left.

| Character      | P   | Y   | T   | H   | O   | N   |
| -------------- | --- | --- | --- | --- | --- | --- |
| Negative Index | -6  | -5  | -4  | -3  | -2  | -1  |

---

## Example

```python
print(name[-1])
```

Output:

```text
N
```

---

## Example

```python
print(name[-2])
```

Output:

```text
O
```

---

# 5. String Slicing

## Description

Slicing extracts part of a string.

---

## Syntax

```python
string[start:stop]
```

---

## Example

```python
name = "PYTHON"

print(name[0:3])
```

Output:

```text
PYT
```

Explanation:

```text
Start = Included
Stop = Excluded
```

---

## Example

```python
print(name[2:5])
```

Output:

```text
THO
```

---

## Example

```python
print(name[:4])
```

Output:

```text
PYTH
```

---

## Example

```python
print(name[2:])
```

Output:

```text
THON
```

---

## Example

```python
print(name[:])
```

Output:

```text
PYTHON
```

---

# Slicing with Step

Syntax:

```python
string[start:stop:step]
```

---

## Example

```python
print(name[0:6:2])
```

Output:

```text
PTO
```

---

## Reverse String

```python
print(name[::-1])
```

Output:

```text
NOHTYP
```

---

# Flow Diagram

```text
PYTHON

0 1 2 3 4 5

Take every second character:

P T O
```

---

# 6. String Immutability

## Description

Strings cannot be modified after creation.

---

## Wrong

```python
name = "PYTHON"

name[0] = "J"
```

Output:

```text
TypeError
```

---

## Correct

```python
name = "PYTHON"

name = "J" + name[1:]

print(name)
```

Output:

```text
JYTHON
```

---

## Why Are Strings Immutable?

- Security
- Faster execution
- Better memory optimization

---

# 7. Traversing Strings

## Method 1

```python
name = "PYTHON"

for ch in name:
    print(ch)
```

Output:

```text
P
Y
T
H
O
N
```

---

## Method 2

```python
for i in range(len(name)):
    print(name[i])
```

Output:

```text
P
Y
T
H
O
N
```

---

# 8. String Operators

---

## Concatenation

```python
first = "Hello"
second = "World"

print(first + second)
```

Output:

```text
HelloWorld
```

---

## Repetition

```python
print("AI"*3)
```

Output:

```text
AIAIAI
```

---

## Membership Operator

```python
print("A" in "AI")
```

Output:

```text
True
```

---

# 9. Important String Methods

---

## upper()

```python
name = "vrushali"

print(name.upper())
```

Output:

```text
VRUSHALI
```

---

## lower()

```python
name = "VRUSHALI"

print(name.lower())
```

Output:

```text
vrushali
```

---

## capitalize()

```python
name = "vrushali"

print(name.capitalize())
```

Output:

```text
Vrushali
```

---

## title()

```python
text = "hello world"

print(text.title())
```

Output:

```text
Hello World
```

---

## strip()

```python
name = "   vrushali   "

print(name.strip())
```

Output:

```text
vrushali
```

---

## replace()

```python
text = "I love Java"

print(text.replace("Java","Python"))
```

Output:

```text
I love Python
```

---

## find()

```python
text = "PYTHON"

print(text.find("T"))
```

Output:

```text
2
```

---

## count()

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## startswith()

```python
email = "vrushali@gmail.com"

print(email.startswith("v"))
```

Output:

```text
True
```

---

## endswith()

```python
print(email.endswith(".com"))
```

Output:

```text
True
```

---

## split()

```python
text = "I Love AI"

print(text.split())
```

Output:

```python
['I', 'Love', 'AI']
```

---

## join()

```python
lst = ['I','Love','AI']

print("-".join(lst))
```

Output:

```text
I-Love-AI
```

---

# 10. Escape Characters

---

## New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

## Tab Space

```python
print("Hello\tWorld")
```

Output:

```text
Hello    World
```

---

## Double Quotes

```python
print("I am \"Vrushali\"")
```

Output:

```text
I am "Vrushali"
```

---

# Real-Life Example

## Email Validator

```python
email = "vrushali@gmail.com"

if '@' in email:
    print("Valid")
else:
    print("Invalid")
```

Output:

```text
Valid
```

---

# Mini Project

## Password Strength Checker

```python
password = input("Enter Password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
```

---

# AI Engineering Connection

Strings are everywhere in AI.

---

## ChatGPT Prompt

```python
prompt = "Explain AI"
```

---

## NLP

```python
sentence = "I love AI"
```

---

## Tokenization

```python
words = sentence.split()
```

Output:

```python
['I','love','AI']
```

---

## Search Engine

```python
query = "Best AI course"
```

---

## Sentiment Analysis

```python
review = "Movie was awesome"
```

---

## LLM Input

```python
user_prompt = "Write Python code"
```

---

# Common Beginner Mistakes

---

## Mistake 1

```python
name[0] = "A"
```

Wrong.

Strings are immutable.

---

## Mistake 2

Thinking:

```python
name[1:3]
```

means:

```text
1,2,3
```

Wrong.

Stop index is excluded.

---

## Mistake 3

Thinking:

```python
find()
```

returns:

```text
True/False
```

Wrong.

It returns position.

---

# Interview Questions with Answers

---

## Q1. What is a string?

Answer:

A string is a sequence of characters enclosed inside quotes.

---

## Q2. Are strings mutable?

Answer:

No.

Strings are immutable.

Example:

```python
name[0] = "A"
```

produces:

```text
TypeError
```

---

## Q3. Difference between indexing and slicing?

| Indexing         | Slicing             |
| ---------------- | ------------------- |
| Single character | Multiple characters |

---

## Q4. What is negative indexing?

Answer:

Accessing elements from right to left.

Example:

```python
name[-1]
```

---

## Q5. Difference between split() and join()?

split():

```text
String → List
```

join():

```text
List → String
```

---

## Q6. Difference between find() and index()?

| find()     | index()      |
| ---------- | ------------ |
| Returns -1 | Throws error |

---

## Q7. Why are strings immutable?

Answer:

- Security
- Performance
- Memory optimization

---

## Q8. How are strings used in AI?

Answer:

- NLP
- LLMs
- Prompt Engineering
- Search Engines
- Chatbots
- Sentiment Analysis

---

# Practice Questions

## Easy

1. Print first character.
2. Print last character.
3. Print middle character.
4. Reverse string.
5. Count vowels.

---

## Medium

6. Check palindrome.
7. Count spaces.
8. Count words.
9. Replace character.
10. Find largest word.

---

## Advanced

11. Email validator.
12. Password validator.
13. Character frequency counter.
14. Remove duplicates.
15. String compression.

---

# Homework

## Task 1

Take name input.

Print:

```text
First Character
Last Character
Length
```

---

## Task 2

Reverse a string.

Example:

```text
HELLO
```

Output:

```text
OLLEH
```

---

## Task 3

Check palindrome.

Example:

```text
madam
```

Output:

```text
Palindrome
```

---

## Task 4

Count vowels.

Example:

```text
Vrushali
```

Output:

```text
3
```

---

# Revision Notes

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
String Methods:

upper()
lower()
capitalize()
title()
strip()
replace()
find()
count()
split()
join()
startswith()
endswith()
```

---

# Summary

Today you learned:

✅ Strings  
✅ Indexing  
✅ Negative Indexing  
✅ Slicing  
✅ Reverse String  
✅ String Immutability  
✅ String Traversal  
✅ String Methods  
✅ Escape Characters  
✅ AI Applications of Strings

These concepts are the foundation of:

- NLP
- LLMs
- ChatGPT
- Prompt Engineering
- Search Engines
- AI Chatbots
- Retrieval Systems
