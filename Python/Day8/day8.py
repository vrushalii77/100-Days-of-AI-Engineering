
# Easy
# ==========================================
# Problem 1: Create Student class.
# ==========================================

class Student:
    pass
print(Student)

# ==========================================
# Problem 2: Create Employee class.
# ==========================================
 
class Employee:
    pass
print(Employee)


# ==========================================
# Problem 3: Create Car class.
# ==========================================


class Car:
    pass
print(Car)


# ==========================================
# Problem 4: Create Mobile class.
# ==========================================


class Mobile:
   pass
print(Mobile)


# ==========================================
# Problem 5: Create Laptop class.
# ==========================================


class Laptop:
    pass
print(Laptop)

# Medium

# ==========================================
# Problem 6: Create constructor for Student.
# ==========================================

class Student:
    def __init__(self):
        print("Student Constructor")
s1 = Student()


# ==========================================
# Problem 7: Create constructor for Employee.
# ==========================================


class Employee:
    def __init__(self):
        print("Emp constructor")
e1 = Employee()


# ==========================================
# Problem 8: Create constructor for Product.
# ==========================================


class Product:
    def __init__(self):
        print("Product Constructor")
p1 = Product()


# ==========================================
# Problem 9:  Print student details.
# ==========================================


class Student:
    def __init__(self, name , rollNo, marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks
    def display(self):
        print(self.name," ", self.rollNo, " ", self.marks)
s1 = Student("Pritee", 34, 90)
s2 = Student("Jay", 42, 86)
s3 = Student("Dinesh", 22, 50)
s1.display()
s2.display()
s3.display()


# ==========================================
# Problem 10: Print employee details.
# ==========================================


class Employee:
    def __init__(self,id,  name , salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(self.id," ", self.name, " ", self.salary)
e1 = Employee(1, "Pritee", 90000)
e2 = Employee(2, "Jay", 86000)
e3 = Employee(3, "Dinesh", 50000)
e1.display()
e2.display()
e3.display()

# Advanced Beginner

# ==========================================
# Problem 11: Student Result System.
# ==========================================

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name, " ", self.marks)
s1 = StudentResult("Manasi", 80)
s2 = StudentResult("janhavi", 78)
s1.display()
s2.display()

# ==========================================
# Problem 12: Bank Account class.
# ==========================================

class Bank:
    def __init__(self, name, accountNumber):
        self.name = name
        self.accountNumber = accountNumber
    def display(self):
        print(self.name, " ", self.accountNumber)
b1 = Bank("mohit", 11)
b2 = Bank("Akanksha", 12)
b1.display()
b2.display()

# ==========================================
# Problem 13: ATM Machine class.
# ==========================================


class AtmMachine:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def display(self):
        print(self.name, " ", self.money)
a1 = AtmMachine("Jiya", 90000)
a2 = AtmMachine("Deepak", 70000)
a1.display()
a2.display()

# ==========================================
# Problem 14: Library class.
# ==========================================


class Library:
    def __init__(self, bookName, price):
        self.bookName = bookName
        self.price = price
    def display(self):
        print(self.bookName, " ", self.price)
l1 = Library("Marathi", 60)
l2 = Library("English", 70)
l1.display()
l2.display()

# ==========================================
# Problem 15: AI Career Predictor class.
# ==========================================

class AiCareerPredictor:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    def display(self):
        position = ""
        if self.marks>= 90:
            position= "AI Engineer"
        elif self.marks>=80:
            position= "Software Developer"
        else:
            position= "Better luck next time!!"
        print(self.name, " ", self.marks, " ",position) 

a1 = AiCareerPredictor("Alia", 90)
a2 = AiCareerPredictor("Sharvari", 89)
a1.display()
a2.display()


# class Student:
#     pass
# s1 = Student()
# print(s1)

# class Student:
#     def display(self):
#         print("hii")
# s1 = Student()
# s2 = Student()
# s1.display()
# s2.display()

# self is a reference to the current object.
# Whenever you create an object from a class, Python automatically passes that object as the first argument to its instance methods.
# You don't pass self yourself—Python does it for you.


# Constructor
# Special function that runs automatically when object is created

# class Student1:
#     def __init__(self):
#         print("Hello Jiii, I am Constructor")
# s1 = Student1()


# Parameterized Constructor
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name)
#         print(age)
# s1 = Student("Vrushali", 22)

# Instance Variables
# Variables belonging to an object.
# class Student:
#     def __init__(self):
#         self.name = "Vrushali"
#         self.age = 22
# s1 = Student()
# print(s1.name)

# Instance Methods
# Methods belonging to objects.
# class Student1:
#     def hello(self):
#         print("Hello hi")
# s1 = Student1()
# s1.hello()

# Mini Project: Student Information system
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def studInfo(self):
#         print(self.name)
#         print(self.age)
        
# s1 = Student("Sweettt", 22)
# s1.studInfo()