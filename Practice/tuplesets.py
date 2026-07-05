# ✅ Problem 1 (Tuple): Create a tuple of 5 numbers.
# Print:1) First element
# 2) Last element
# 3) Length of tuple

tupl1 = (1,2,3,4,5)
print(tupl1[0])
print(tupl1[-1])
print(len(tupl1))


# ✅ Problem 2 (Set):1) Take 5 numbers from user and store in a set. Then:
# 1) Print the set
# 2) Add a new number
# 3) Remove one number


set1 = set()
i = 1
while i<=5:
    num = int(input("Enter a number"))
    set1.add(num)
    i+=1
print(set1)

newNum = set1.add(6)
print("After adding new num :", set1)

removeNum = set1.remove(2)
print("After removing a num :", set1)

