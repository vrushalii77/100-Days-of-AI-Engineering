# Easy
# 1. Print first element.
# 2. Print last element.
# 3. Print middle element.
# 4. Reverse a list.
# 5. Find length.

# list1 = [23,56,24,86,55]
# print("First element: ", list1[0])
# print("Last element: ", list1[-1])
# print("Middle element: ", list1[len(list1)//2])
# print("Reverse element: ", list1[::-1])
# print("Length of list: ", len(list1))


# Medium
# 6. Find maximum.
# 7. Find minimum.
# 8. Find sum.
# 9. Count even numbers.
# 10. Count odd numbers.

# list1 = [7,4,8,2,6,9]
# print("Maximum element is: ", max(list1))
# print("Minimum element is: ", min(list1))
# print("Sum of elements are: ", sum(list1))

# count_even = 0
# for i in list1:
#     if i %2 == 0:
#         count_even +=1
# print("Even no. count is: ", count_even)

# count_odd = 0
# for i in list1:
#     if i%2 !=0:
#         count_odd +=1
# print("Odd no. count is: ", count_odd)


# Advanced
# 11. Find duplicates.

# list1 = [1,2,3,1,2]
# visited =[]
# duplicate =[]
# for i in list1:
#     if i in visited:
#         duplicate.append(i)
#     else:
#         visited.append(i)     
# print(duplicate)

# 12. Remove duplicates.

# list1 = [1,2,3,1,2]
# visited = []
# for i in list1:
#     if i not in visited:
#         visited.append(i)
# print("Without duplicate elements: ", visited)

# 13. Find second largest.

# list1 = [7,4,8,2,6,9]
# max1 = max(list1)
# max2 = list1[0]
# for i in list1:
#     if i> max2 and i != max1:
#         max2=i
# print(max1, "and", max2)
    
# 14. Rotate list.
# list1 = [7,4,8,2,6,9]
# rotatied_list = [list1[-1]]+ list1[:-1]
# print("Rotated list is: ",rotatied_list)

# 15. Merge two lists.
# list1 = [1,2,3]
# list2 = [4,5,6]
# print(list1+list2)

# HomeWork
# 1. Take 5 numbers from user and store in list.
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(numbers)




