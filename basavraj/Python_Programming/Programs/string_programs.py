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
str1="hi i am learning python programming"
str2=str1.split()
maxx=len(str2[0])
minn=len(str2[0])
for i in str2:
    if len(i)>maxx:
        maxx=len(i)
        longest_word=i
    if len(i)<minn:
        minn=len(i)
        smallest_word=i

print("longest word is ::",longest_word)
print("lenght of the longest word is::",maxx)
print("smallest word is:",smallest_word)
print("lenght of smallest word is::",minn)
print("-"*50)
#8). Print most simultaneously repeated characters in the input string.
str1="basavaraja m turakani"
d={}
for i in str1:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

    most_frequent=None
    max_count=0
    for i,count in d.items():
        if count>max_count:
            most_frequent=i
            max_count=count
print(most_frequent,max_count)
print("-"*50)

#9). Write a Python program to calculate the length of a string with loop logic.
str1="pyhtonprogramming"
c=0
for i in str1:
    c=c+1
print(c)
print("-"*50)
#10). Write a Python program to replace the second occurrence of any char with the special character $.
str1 = "programming"
result = ""
d = {}

for i in str1:
    if i in d:
        d[i] += 1
        if d[i] == 2:
            result += "$"
        else:
            result += i
    else:
        d[i] = 1
        result += i

print("Original:", str1)
print("Modified:", result)
print("-"*50)

#11). Write a python program to get to swap the last character of a given string.
str1="Basavaraj"
print(str1[-1]+str1[1:-1]+str1[0])
print("-"*50)

#12). Write a python program to exchange the first and last character of each word from the given string.
string ="Its Online Learning"
str1=string.split()
for i in str1:
    print(i[::-1],end=" ")

print("-"*50)

#13). Write a python to count vowels from each word in the given string show as dictionary output
#Input = “We are Learning Python Codding”
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
str1="we are leearning the python programming"
str2=str1.split()
d={}
vowels="aeiouAEIOU"
for word in str2:
    c=0
    for char in word:
        if char in vowels:
            c=c+1
    d[word]=c

print(d)
print("-"*50)

#14). Write a python to repeat vowels 3 times and consonants 2 times.
#Input = “Sqa Tools Learning”
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
str1="Sqa Tools Learning"
for i in str1:
    if i in ["a","e","i","o","u"]:
        print(i*3,end="")
    else:
        print(i*2,end="")
print()
print("-"*50)

#15). Write a python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”
str2="cricket plays virat"
str3=str2.split()
word=str3[::-1]
output=" ".join(word)
print(output)
print("-"*50)

#16). Write a python program to get all the digits from the given string.
"""Input =
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
str1="""Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen"""
str2=str1.split()
d=[]
for i in str2:
    if i.isdigit():
        d.append(i)
    else:
        continue
print(d)
print("-"*50)

#17). Write a python program to replace the words “Java” with “Python” in the given string.
#Input = “JAVA is the Best Programming Language in the Market”
#Output = “Python is the Best Programming Language in the Market”
str1="JAVA is the Best Programming Language in the Market"
str2=str1.replace("JAVA","Python")
print(str2)
print("-"*50)
#18). Write a Python program to get all the palindrome words from the string.
#Input = “Python efe language aakaa hellolleh”
#output = [“efe”, “aakaa”, “hellolleh”]
str1="Python efe language aakaa hellolleh"
str2=str1.split()
for i in str2:
    if i==i[::-1]:
        print(i,end=" ")
    else:
        continue
print()
print("-"*50)
#19). Write a Python program to create a string with a given list of words.
#Input = [“There”, “are”, “Many”, “Programming”, “Language”]
#Output = There are many programming languages.
str1=["There", "are", "Many", "Programming", "Language"]
print(" ".join(str1))
print("-"*50)

#20). Write a Python program to remove duplicate words from the string.
#Input = “John jany sabi row john sabi”
#output = “John jany sabi row”
#Input string
string = "John jany sabi row John sabi"
list1 = string.split(" ")
list2 = []

for val in list1:
    if val not in list2:
        list2.append(val)

#Printing output
print(" ".join(list2))
print("_"*50)
#21). Write a Python to remove unwanted characters from the given string.
#Input = “Prog^ra*m#ming”
#Output = “Programming"
str1="Prog^ra*m#ming"
for char in str1:
    if char.isalpha():
        print(char,end="")
    else:
        continue
print()
print("-"*50)