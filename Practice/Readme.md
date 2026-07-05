# PYTHON BASICS

## 🟢 TOPIC 1: Variables

- A variable is like a container that stores data.

  ```python
  name = "vrushali"
  age = 21`

  ```

  ### Data Types in Python
  1. int
  2. float
  3. str
  4. bool

### Taking user input

```python
name = input("Enter your name: ")
print("Hello", name)
```

- Important: input() always takes string
- if u want a number: `age = int(input("Enter your age: "))`
- to print type of a variable eg. num1 : `type(num1)`

---

## 🟢 TOPIC 2: Operators in Python

- Operators are used to perform operations on values.

### 1️⃣ Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Description                           | Example  |
| -------- | ------------------------------------- | -------- |
| `+`      | Addition                              | `a + b`  |
| `-`      | Subtraction                           | `a - b`  |
| `*`      | Multiplication                        | `a * b`  |
| `/`      | Division (returns float)              | `a / b`  |
| `%`      | Modulus (remainder)                   | `a % b`  |
| `//`     | Floor Division (removes decimal part) | `a // b` |
| `**`     | Exponent (power)                      | `a ** b` |

### 🔹 Example

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000
```

### 2 Comparison Operators

- Used to compare values → result is True or False

### 3️ Logical Operators

- Used with conditions.

### 4️ Assignment Operators

- Used to assign values.

## 🟢 TOPIC 3: Conditional Statements

### 1) if Statement

Used when we want to execute something only if condition is True.

```python
age = 20
if age >= 20:
    print("You can drive a car")
```

### 2. if – else

Used when we want 2 possible outcomes.

```python
age = 16
if age > 18:
    print("You can drive a car")
else:
    print("You can't drive a car")
```

### 3. if – elif – else

- Used when we have multiple conditions.

```python
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

## 🟢 TOPIC 4: Loops

- Loops are used when we want to repeat something multiple times.

### 1️⃣ for Loop

- Used when we know how many times to repeat.

```python
for i in range(3):
    print(i)  //123
```

```python
for i in range(1, 5):
    print(i)  //01234
```

### 2️⃣ while Loop

- Used when we repeat until condition becomes False.

```python
count = 1
while count <= 10:
    print(count)
    count+=1
```

## 🟢 Topic 5: Strings (VERY important for AI + Bots)

- Strings in python are surrounded by either single quotation marks, or double quotation marks.
- Strings are arrays:
- Like many other popular programming languages, strings in Python are arrays of unicode characters.
- However, Python does not have a character data type, a single character is simply a string with a length of 1.
- Square brackets can be used to access elements of the string.

```python
name = "vrushali"
surName = "Jadhav"
print(name+ " " +surName)
```

### String slicing

```python
Syntax: string[start:end]
```

```python
text = "Hi I am vrushali Jadhav"
print(text[0])    //H
print(len(text))   //23
print(text[0:2])   //Hi
print(text[-1])    //v
```

### String Methods

```python
text = "HeLLo"
print(text.lower())  //hello
print(text.upper())   //HELLO
```

- strip() - it remove spaces

```python
text = " Hello Pari!! "
print(text.strip())   //Hello Pari!!
```

- replace() - it replace the word in string

```python
text = "I like java"
print(text.replace("java", "python"))  //I like python
```

- split() - It splits the words

```python
text= "Ai is powerful"
print(text.split())   //['Ai', 'is', 'powerful']
```

## 🟢 TOPIC 6: LISTS (SUPER IMPORTANT for AI & ML)

- A list is a collection of multiple values in one variable.
- it can store multiple values, mixed data types are allowed.

```python
e.g. data = [10, "Hello", True, 3.5]
numbers = [10, 20, 30, 40]
names = ["Jay", "Ritu", "samay", "Rakhii"]
```

- If strings are for text…
- Lists are for data.

- AI = data.
- So lists = foundation.

- Lists are mutable (changeable).

```python
numbers = [10, 20, 30, 40]
numbers[1] = 100
print(numbers)  //[10,100,30,40]
```

### List methods

- append() → Add element at end

```python
numbers = [1,2,3]
numbers.append(4)   //[1,2,3,4]
```

- insert() → Add at specific position

```python
numbers = [1,2,3]
numbers.insert(1, 7)   //[1,7,2,3]
```

- remove() → Remove specific value

```python
numbers = [1,2,3,5]
numbers.remove(3)   //[1,2,5]
```

- pop() → Remove by index

```python
numbers.pop(0)  //[2,3,5]
```

- len() → Length of list

```python
print(len(numbers))
```

- Looping Through List

```python
numbers = [1,2,3,4,5,6]
for i in numbers:
    print(i)
```

## 🟢 TOPIC 7: FUNCTIONS (VERY IMPORTANT)

- A function is a block of code that performs a specific task. You can use it
  whenever you want by calling its name, which saves you from writing the same
  code multiple times.

  ```python
  Basic syntax:
  def function_name():
    print("Hello")

  to call function:
  function_name()
  ```

  ```python
  2️⃣ Function with Parameters
  def greet(name):
    print("Hello", name)    //parameter
  greet("Vrushali")     //argument
  ```

  ```python
  3️⃣ Function with Return Value
  def add(a, b):
    return a + b
  result = add(5, 3)
  print(result)
  ```

## 🟢 TOPIC 8: DICTIONARIES (VERY IMPORTANT for AI & APIs)

- Dictionaries are used to store data in key-value pairs.
- This is how:
- JSON works
- APIs send data
- AI model responses are structured

```python
person = {
    "name": "Vrushali",
    "age": 21,
    "city": "Pune"
}
```

- keys must be unique

```python
2️⃣ Accessing Values
print(person["name"])
print(person["age"])
```

```python
3️⃣ Adding or Updating Values
person["age"] = 22     # update
person["email"] = "vrushali@gmail.com"   # add new
```

```python
4️⃣ Looping Through Dictionary
for key in person:
    print(key, ":", person[key])
```

## 🟢 TOPIC 9: TUPLES & SETS

- A tuple is like a list… but immutable (cannot be changed).

```python
numbers = (10, 20, 30)
```

- difference form list
  List → [] Tuple → ()

  ```python
  1. Accessing Elements
  print(numbers[0])
  print(numbers[-1])

  ```

```python
  - you can not modify tuple
  numbers[0] = 99   # ERROR
```

- Why Tuples Matter?

1. Faster than lists
2. Used for fixed data
3. Used in ML datasets
4. Used as dictionary keys

### Set = collection of unique elements.

- ✔ No duplicates, ✔ No indexing, ✔ Unordered

```python
nums = {1, 2, 3, 4}
```

- Duplicate removed automatically.

- Why Sets Are Important in AI?

1. Removing duplicates from data
2. Finding unique words
3. Vocabulary building in NLP
4. Comparing datasets

## 🟢 Now We Level Up: OOP (Object-Oriented Programming)

Very important for:

1. Real software
2. AI systems
3. ML pipelines
4. Web apps
5. Everything serious

- A way of organizing code by creating "blueprints" (called classes) to represent real-world
  things like a student, car, or house. These blueprints help you create objects (individual
  examples of those things) and define their behavior.

- class: A class is a blueprint or template for creating objects.
- Object: An object is a specific instance of a class.

```python
class MyClass:
    x = "hello yaar name..!!"
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)
```

- You can delete objects by using the del keyword: del p1
- class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

```python
class Person:
  pass
```

```python
 Python __init__() Method
```

-All classes have a built-in method called **init**(), which is always executed when the class is being initiated.

- The **init**() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Name", 23)
print(p1.name)
print(p1.age)
```

- Note: The **init**() method is called automatically every time the class is being used to create a new object.

```python
- You can also set default values for parameters in the __init__() method:
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
```
