# ✅ Problem 1: 1)Create a dictionary that stores: name, age, course
# Take input from user and store in dictionary.
# Then print all key-value pairs using loop.

# name = input("Enter a  name: ")
# age = int(input("Enter a age:"))
# course = input("Enter a course: ")

# dict1 ={}
# dict1["name"] = name
# dict1["age"] = age
# dict1["course"] = course

# print(dict1)
# for key in dict1:
#     print(key, " ",dict1[key])




# ✅ Problem 2: Create a dictionary with 3 students and their marks.
# Example:
# {
#    "Amit": 85,
#    "Riya": 92,
#    "Karan": 78
# }
# Then:
# Print the student with highest marks
# (Hint: use max() with key parameter)


stud_marks = {
   "Amit": 85,
   "Riya": 92,
   "Karan": 78
}
for key in stud_marks:
    print( max(stud_marks[key]))