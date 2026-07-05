# Tuple
# 1. Print first element.
# 2. Print last element.
# 3. Count occurrence.
# 4. Find index.
# 5. Tuple unpacking.

tuple1 = (1,4,2,6,7,3,1)
print("First element: ", tuple1[0])
print("Last element: ", tuple1[-1])
print("Count of element: ", tuple1.count(1))
print("index of 6 is: ", tuple1.index(6))

tuple2 = ("Vrushali", 22)
name , age = tuple2
print(name)
print(age)


# Set
# 6. Remove duplicates.
# 7. Find union.
# 8. Find intersection.
# 9. Find difference.
# 10. Check membership.

set1 = {1,2,3,1,4}
set2 = {4,5,6}
print("Removing duplicates: ", set1)
print("union: ", set1.union(set2))
print("Intersection duplicates: ", set1.intersection(set2))
print("difference duplicates: ", set1.difference(set2))
print(5 in set1)


# Dictionary
# 11. Create student dictionary.
# 12. Add new key.
# 13. Update value.
# 14. Delete key.
# 15. Print all keys and values.

students = {
   "Student1": { "name": "Swati", "age" : 22},
   "Student2":{"name": "Vaibhavi", "age": 22}  
}

students["Student2"]["city"] = "Pune"
print(students)

students["Student1"]["name"] = "Jiyaa"
print(students)

del students["Student2"]["city"]
print(students)

for key,value in students.items():
    print(key, value)