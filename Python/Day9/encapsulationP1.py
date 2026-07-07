# Keeping data and methods together inside one class.
# Data + Functions = One Package

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)
s1 = Student("Priyaa", 88)
s1.display()



# Private Variables
# Python uses double underscore.

class Bank:
    def __init__(self):
        self.__balance = 1000
    def show(self):
        print(self.__balance)
b1 = Bank()
b1.show()