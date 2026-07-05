# class MyClass:
#     x = "hello yaar name..!!"
# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()
# print(p1.x)
# print(p2.x)
# print(p3.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Name", 23)
print(p1.name)
print(p1.age)