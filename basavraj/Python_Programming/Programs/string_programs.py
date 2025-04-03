#1). Write a Python program to get a string made of the first and the  last 2 chars from
# a given string. If the string length is less than 2, return instead of the empty string
print("program 1")
str1="basavaraja"
str2=len(str1)
if str2<2:
    print(True)
else:
    print(str1[:2]+str1[-2:])
print("-"*50)
#2). Python string program that takes a list of strings and returns the length of the longest string.
print("program 2")
str1="hi basavaraja how are you"
str2=str1.split()
m=0
for i in str2:
    if len(i)>m:
        m=len(i)
        word=i
print(word)
print(m)
print("-"*50)
#3). Python string program to get a string made of 4 copies
# of the last two characters of a specified string (length must be at least 2).
print("program 3")
str2="basava"
print(str2[-2:]*4)
print("-"*50)

#4). Python string program to reverse a string if it’s length is a multiple of 4.
print("program 4")
str1="basavaraja"
str2=len(str1)
if str2%4==0:
    print(str1*4)
else:
    print(str1)
print("-"*50)

#5). Python string program to count occurrences of a substring in a string.

#6). Python string program to test whether a passed letter is a vowel or consonant.
print("program 6")
str1="basav hi how are you"
vowels="aeiouAEIOU"
v=[]
c=[]
for i in str1:
    if i in vowels:
        v.append(i)
    else:
       c.append(i)
print("vowels :"," ".join(v))
print("consonant :"," ".join(c))
print("-"*50)

#7). Find the longest and smallest word in the input string.
#8). Print most simultaneously repeated characters in the input string.
str1="basavaraja"
for i in str1:
