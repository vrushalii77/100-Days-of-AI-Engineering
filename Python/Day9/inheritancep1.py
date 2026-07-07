# One class acquires properties of another class.

class Animal:
    def eat(self):
        print("Eating")

class Cat(Animal):
    pass

c1 = Animal()
c1.eat()

# eg 2
class Person:
    def display(self):
        print("Hello cherryyyyy!!")
class Student(Person):
    pass
s1 = Student()
s1.display()

# eg 3
class Animal:
    def sound(self):
        print("meww")
class Cat:
    def sound(self):
        print("Bark")
a1 = Animal()
c1 = Cat()
a1.sound()
c1.sound()


# One class acquires properties of another class.
# Animal
#    |
#    +------ Dog
#    |
#    +------ Cat

# class Animal:
#     def eat(self):
#         print("eating")
# class Dog(Animal):
#     pass
# d = Dog()
# d.eat()

# eg2 - Multilevel
# class Animal:
#     def eat(self):
#         print("Eating..")
# class Dog(Animal):
#     def walk(self):
#         print("Walking..")
# class Cat(Dog):
#     pass

# c = Cat()
# c.eat()
# c.walk()

# eg3 - Multiple
class Animal:
    def walk(self):
        print("Walking..")

class Dog:
    def sound(self):
        print("Bark..")
class Cat(Animal, Dog):
    pass
c1 = Cat()
c1.sound()
c1.walk()




    

