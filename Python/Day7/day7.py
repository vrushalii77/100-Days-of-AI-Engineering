# Self Practice questions:
# def welcome():
#     print("Welcome to the Jungle")
# welcome()

# function used to :
# Avoid repetition
# write clean code
# Reuse code
# make debugging easier
# divide big problems into small problems

# def greet(name):
#     print("Hello", name)
# greet("Vrushali")
# greet("Karthik")

# Return Sends result back
# def add(a,b):
#     return a+b
# x=add(5,4)
# print(x)


# Practice Problems
# Easy
# 1. Create function to print your name.

# def my_name(name):
#     print("Hi", name)
# my_name("Vrushali")

# 2. Create function to add two numbers.

# def add(a,b):
#     return a+b
# result = add(10,20)
# print("Addition is: ",result)

# 3. Create function to find square.

# def square(num):
#     return num*num
# result = square(6)
# print("square is: ", result)

# 4. Create function to find cube.

# def cube(num):
#     return num*num*num
# result = cube(3)
# print("cube is: ", result)

# 5. Create function to print table.

# for i in range(1,11):
#     def table(num):
#         print(num*i) 
#     table(5)

# Medium
# 6. Create function for factorial.

# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(4))

# 7. Create function for palindrome.



# 8. Create function for even/odd.

# def even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
# even_odd(19)

# 9. Create function to find largest.

# def largest(a,b,c):
#     if a > b:
#         if a > c:
#             print("Largest ",a)
#     elif b > c:
#         print("Largest: ", b)
#     else:
#         print("Largest: ",c)
# largest(11,9,26)

# 10. Create function to count vowels.
\
# def count_vowel(name):
#     count = 0
#     for i in name:
#         if i in "aeiou":
#             count+=1
#     print(count)
# count_vowel("aabbcc")

# Advanced
# 11. Factorial using recursion.

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)
print(fact(4))

# 12. Fibonacci using recursion.
# 13. Lambda for square.

# square = lambda a: a*a
# print(square(9))

# 14. Map to square list.

# numbers = [1,2,3,4]
# square = list(map(lambda x: x*x, numbers))
# print(square)

# 15. Filter even numbers.

# numbers = [1,2,3,4,5,6,7]
# even_num = list(filter(lambda x: x%2 == 0, numbers))
# print("Even numbers are: ", even_num)

# 16. Reduce to calculate sum.

# from functools import reduce
# numbers = [1,2,3,4,5]
# sum = reduce(lambda a,b: a+b, numbers)
# print(sum)




