# Easy
# Add two numbers.
# a = 20
# b = 20
# print(a+b)

# Subtract two numbers.
# a = 20
# b = 20
# print(a-b)

# Find remainder.
# a = 20
# b = 20
# print(a//b)

# Find square of a number.
# a = 20
# print(a**2)

# Check whether number is positive.
# a = int(input("Enter a number: "))
# if a>0:
#     print("Number is positive")



# Medium
# Check voting eligibility.
# age = int(input("Enter your age: "))
# if age>18:
#     print("Eligile to vote")
# else:
#     print("Not eligible to vote")

# Check even or odd.
# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# Find larger among two numbers.
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# if num1>num2:
#     print(num1, "is largest")
# else:
#     print(num2, "is largest")

# Check pass or fail.
# marks = 60
# if marks>50:
#     print("Pass")
# else:
#     print("fail")

# Calculate bonus based on salary.


# Advanced Beginner
# Student grading system.
# if marks>=90:
#     print("A")
# elif marks>=75:
#     print("B")
# elif marks>=70:
#     print("C")
# else:
#     print("Fail bro!!")


# ATM withdrawal system.
# amount = 1000;
# withdrawl_money = int(input("Enter a withdrawl money amount: "))
# if(withdrawl_money <= amount):
#     print("Amount withdrawl successfully")
# else:
#     print("Sorry. Your accont does not have that much money.")

# Login system using username and password.
# uname = "vrushali"
# password = 123
# uname_access = input("Enter your uname: ") 
# password_access = int(input("Enter your pass: ")) 
# if (uname_access == uname) & (password_access ==password):
#     print("Login Successful")
# else:
#     print("Plz check your credentials")

# Largest among three numbers.
num1 = 20
num2 = 80
num3 = 60

if num1 > num2:
    if num1 > num3:
        print(num1, "is largest.")
    else:
        print(num3, "is largest.")
else:
    if num2 > num3:
        print(num2, "is largest.")
    else:
        print(num3, "is largest.")

# Scholarship eligibility checker.


# Mini Challenge
# Build a Simple AI Career Advisor:
# Take:Student Name and Marks
# Rules:
# 90+ → AI Engineer
# 75+ → Software Developer
# 60+ → Data Analyst
# Below 60 → Keep Practicing
# Print the career suggestion based on marks.

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if marks>= 90:
    print("AI Engineer")
elif marks>=75:
    print("Software Developer")
elif marks>=60:
    print("Data Analyst")
else:
    print("Keep Practicing")