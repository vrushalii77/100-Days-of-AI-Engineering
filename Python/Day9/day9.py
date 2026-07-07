# Practice Problem

# Easy
# ==========================================
# Problem 1: Create Animal and Dog class.
# ==========================================

class Animal:
    pass
class Dog:
    pass

# ==========================================
# Problem 2: Create Person and Student class.
# ==========================================# 

class Person:
    pass
class Student:
    pass
# ==========================================
# Problem 3: Create Vehicle and Car class.
# ==========================================# 

class Vehicle:
    pass
class Car:
    pass

# ==========================================
# Problem 4: Create Employee class with private salary.
# ==========================================# 

class Employee:
    def amount(self):
        self.__salary = 1000
    def showSalary(self):
        print("Salary is: ", self.__salary)
e1 = Employee()
e1.amount()
e1.showSalary()

# ==========================================
# Problem 5: Override a display method.
# ==========================================# 

class Person:
    def display(self):
        print("Hello this is Person")
class child(Person):
    def display(self):
        print("Hello this is child")
c = child()
c.display()


# Medium
# ==========================================
# Problem 6: Create Bank class using encapsulation.
# ==========================================# 

class Bank:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.deposit(1000)
b.show_balance()


# ==========================================
# Problem 7: Create multilevel inheritance.
# ==========================================# 

class GrandParent:
    def hi(self):
        print("Hi from Grand Parents")
class Parent(GrandParent):
    def hello(self):
        print("Hi from Parents")
class Child(Parent):
    def sayHi(Self):
        print("Hi from child")
c = Child()
c.hi()
c.hello()
c.sayHi()



# ==========================================
# Problem 8: Create method overriding example.
# ==========================================# 

class A:
    def sayHi(self):
        print("...")
class B(A):
    def sayHi(self):
        print("Heyyyyyy")
b = B()
b.sayHi()


# ==========================================
# Problem 9: Create abstract shape class.
# ==========================================# 

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    

# ==========================================
# Problem 10: Create abstract payment class.
# ==========================================#

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def showBalance(self):
        pass
    

# Advanced
# ==========================================
# Problem 11: ATM system.
# ==========================================

class AtmSystem:
    def __init__(self, amount, deposite, withdraw):
        self.amount = amount
        self.deposite = deposite
        self.withdraw = withdraw
    def display(self):
        print("Amount is: ", self.amount)
        print("Deposite is: ", self.deposite)
        print("Withdraw is: ", self.withdraw)
a = AtmSystem(200,20,30)
a.display()


# ==========================================
# Problem 12: Employee management system.
# ==========================================

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def showEmployees(self):
        print(self.id, self.name, self.salary)
e1 = Employee(1, "Priya", 11000)
e2 = Employee(2, "Charan", 12000)
e1.showEmployees()
e2.showEmployees()

# ==========================================
# Problem 13: Vehicle management system.
# ==========================================
class Vehicle:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def displayVehicle(self):
        print(self.id, self.name)
v1 = Vehicle(1, "Audi")
v2 = Vehicle(2, "BMW")
v1.displayVehicle()
v2.displayVehicle()

# ==========================================
# Problem 14: Library management system.
# ==========================================

class Library:
    def __init__(self, id, bookName):
        self.id = id
        self.bookName = bookName
    def displayBooks(self):
        print(self.id, self.bookName)
l1 = Library(1, "Marathi")
l2 = Library(2, "hindi")
l1.displayBooks()
l2.displayBooks()

# ==========================================
# Problem 15: AI Model prediction system.
# ==========================================




# Solve these:

# Bank Account using encapsulation.
# Animal-Dog inheritance.
# Employee method overriding.
# Shape abstraction.
# AI Career Predictor using inheritance.
 