# numbers = [10, 20, 30, 40]
# names = ["Jay", "Ritu", "samay", "Rakhii"]
# print(numbers[0])
# numbers[1] = 100
# print(numbers)

# numbers = [1,2,3]
# numbers.append(4)
# print(numbers)

# numbers = [1,2,3]
# numbers.insert(1, 7)
# print(numbers)


# numbers = [1,2,3,5]
# numbers.remove(3)
# print(numbers)


# numbers = [1,2,3,4,5,6]
# for i in numbers:
#     print(i)


# ✅ Problem 1: 1)Create a list of 5 numbers taken from user.
# Then: Print the list
#  Print the largest number
# Print the smallest number
# (Hint: use max() and min())


# length = 5
# i=1
# numbers = []
# while i <= length:
#     num = int(input("Enter a number:"))
#     numbers.append(num)
#     i+=1
# print(numbers)
# print("Max number: ", max(numbers))
# print("Max number: ", min(numbers))
    

# ✅ Problem 2: 1) Take 5 names from user and store in list. Then:
# 2)Convert all names to uppercase
# 3)Print updated list

i = 1
names = []
while i <= 5:
    name = input("Enter a name:")
    names.append(name)
    i+=1
print(names)
for i in names:
    print(i.upper())

