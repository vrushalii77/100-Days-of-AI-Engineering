# name = "vrushali"
# surName = "Jadhav"
# print(name+ " " +surName)


# text = "Hi I am vrushali Jadhav"
# print(text[0])
# print(len(text))
# print(text[0:2])
# print(text[-1])


# text = "HeLLo"
# print(text.lower())
# print(text.upper())



# text = " Hello Pari!! "
# print(text.strip())   //Hello Pari!!

# text = "I like java"
# print(text.replace("java", "python"))

# text= "Ai is powerful"
# print(text.split())   //['Ai', 'is', 'powerful']


# ✅ Problem 1: 1)Take a name from user and: 
# 2)Print it in uppercase
# 3)Print it in lowercase
# 4)Print its first character
# 5)Print its last character


name = input("Enter a your name:")
print(name)
print(name.upper())
print(name.lower())
print(name[0])
print(name[-1])


# ✅ Problem 2: # Take a sentence from user and:
# Remove extra spaces
# Replace the word "bad" with "good"
# Print number of characters in sentence
# (Hint: use len())

text = input(" Enter any sentence ")
print(text)
print(text.strip())
print(text.replace("bad", "good"))
print(text.split())
print(len(text))

