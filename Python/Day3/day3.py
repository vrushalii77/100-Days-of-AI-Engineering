# Easy
# 1. Print numbers 1 to 10.

# for i in range(1,11):
#     print(i)

# 2. Print numbers 10 to 1.

# for i in range(10, 0, -1):
#     print(i)

# 3. Print even numbers from 1 to 20.

# for i in range(2,21,2):
#     print(i)

# 4. Print odd numbers from 1 to 20.

# for i in range(1,21,2):
#     print(i)

# 5. Print your name 10 times.

# for i in range(10):
#     print("Vrushali")

#  Medium
# 6. Print multiplication table.

# num = 4
# for i in range(1, 11):
#     print(num*i)

# 7. Find sum of first N numbers.

# N=6
# sum = 0;
# for i in range(1, N+1):
#     sum+=i
# print(sum)

# 8. Find factorial.
# N=5
# fact = 1
# for i in range(1,N+1):
#     fact*=i
# print(fact)


# 9. Count digits in number.
# num = 12345
# count = 0
# while num>0:
#     num = num // 10
#     count +=1
# print(count)

# 10. Reverse a number.
# num = 1234
# rev = 0
# while num >0:
#     last = num % 10
#     rev = rev * 10 +last
#     num = num //10
# print(rev)

# Advanced
# 11. Prime number checker.

# num = 17
# isPrime = True
# if num <2:
#     isPrime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#            isPrime = False
#            break
# if isPrime:
#     print("Prime")
# else:
#     print("Not a prime")


# 12. Fibonacci series.

# num1 = 0
# num2 = 1
# n = 10
# for i in range(n):
#     print(num1)
#     next_num = num1+num2
#     num1 = num2
#     num2 = next_num


# 13. Armstrong number.

# num = 123
# og = num
# cube = 0
# while num >0:
#     last = num % 10
#     cube +=(last*last*last)
#     num = num //10
# if og == cube:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# 14. Palindrome number.

# num = 121121
# og = num
# rev = 0
# while num >0:
#     last = num %10
#     rev = rev *10 +last
#     num = num //10
# if rev == og :
#     print("Palindrome")
# else:
#     print("Not a Plindrome")


# 15. Number guessing game.'
# ogNum = 123

# while True:
#     num = int(input("Enter a number: "))
#     if num == ogNum:
#         print("Right")
#         break
#     else:
#         print("No a right bro! Try again")




# HomeWork
# print 1 t0 100
# for i in range(1,101):
#     print(i)

# Print: 100 t0 1
# for i in range(100, 0, -1):
#     print(i)

# Task 3
# Print:
# *
# **
# ***
# ****
# *****

# for i in range(5,0,-1):
#     print("*"*i)


# # Mini Project
# num = int(input("Enter a number of records u want: "))
# while num>0:
#     name = input("Enter a Student name: ")
#     print("Student recorded Successfully!!")
#     num-=1

               

