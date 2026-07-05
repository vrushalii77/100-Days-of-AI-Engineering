# def sayHi():
#     print("Hiiii Vrushali")
# sayHi()


# ✅ Problem 1: 1)Create a function that:
# 2) Takes two numbers as parameters
# 3) Returns the larger number

def num(a, b):
    if a>b:
        return a
    else:
        return b
max= num(6,7)
print("Max: ", max)


# ✅ Problem 2: 1) Create a function that:
# 2) Takes a string
# 3) Returns the reversed string
# (Hint: use slicing [::-1])

def sayName(name):
    return name[::-1]
revStr = sayName("Aaroshi")
print(revStr)