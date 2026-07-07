# One thing behaves differently in different situations.
# Real-Life Example
# Human speaks:
# English
# Hindi
# Marathi
# Japanese

# Same action.
# Different behavior.


# Method overloading
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("meww")
d = Dog()
c = Cat()
d.sound()
c.sound()

# Method Overriding
class Animal:
    def sound(self):
        print("speakkkkkkkkkkkk")
class Dog(Animal):
    def sound(self):
        print("Hellloo")
d = Dog()
d.sound()
