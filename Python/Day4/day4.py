# Easy
# 1. Print first character.
# 2. Print last character.
# 3. Print middle character.
# 4. Reverse string.
# 5. Count vowels.
# name = "vrushali"
# print("First Character: ", name[0])
# print("Last Character: ", name[-1])
# print("Middle character: ", name[len(name)//2])
# print("Reverse String: ", name[::-1])

# vowel = 0
# for ch in name:
#     if ch in "aeiou":
#         vowel+=1   
# print("Total vowels are: ",vowel)


# Medium
# 6. Check palindrome string.
# name = input("Enter a name: ")
# rev_name = name[::-1]
# print("reverse of name: ", rev_name)
# if(name == rev_name):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# 7. Count spaces.
# count_space = 0
# name = " Vru shali Jadha v"
# for ch in name:
#     if ch == " ":
#         count_space +=1
# print("Count of space is: ", count_space)

# 8. Count words.
# name = "I am Vrushali Jadhav "
# print("count of words are: ", len(name.split()))

# 9. Replace character.
# name = "Vrushali"
# name = "S"+name[1:]
# print(name)

# 10. Find largest word.
sentence = "I love artificial intelligence"
words = sentence.split()
print(words)
largest = words[0]
for i in words:
    if len(i)>len(largest):
        largest = i
print(largest)


# Advanced
# 11. Email validator.
# email = "rushali@gmail.com"
# if '@' in email:
#     print("Email Validated")
# else:
#     print("Wrong email")

# 12. Password validator.
# password = input("Enter a password: ")
# if len(password)>8:
#     print("Strong Pass")
# else:
#     print("Weak Password")

# 13. Character frequency counter.
# name = "aaabbccccc"
# visited = ""
# for ch in name:
#     if ch not in visited:
#         print(ch, ":", name.count(ch))
#         visited+=ch


# 14. Remove duplicates.
# name = "aabbccdd"
# visited = ""
# for ch in name:
#     if ch not in visited:
#         visited+= ch
# print(visited)



# 15. String compression.

# name = "aabbcc"
# count = 1
# for i in range(len(name)-1):
#     if name[i] == name[i+1]:
#         count+=1
#     else:
#         print(name[i],count, sep="", end="")
#         count = 1
# print(name[-1],count, sep="")



