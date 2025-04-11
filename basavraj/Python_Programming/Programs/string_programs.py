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
#23). Write a Python program to get common words from strings.
"""Input String1 = “Very Good Morning, How are You”
Input String2 = “You are a Good student, keep it up”
Output = “You Good are”
"""
str1="Very Good Morning, How are You"
str2="You are a Good student, keep it up"
s1=str1.split()
s2=str2.split()

for i in s1:
    c=0
    for j in s2:
        if i==j:
            c=c+1
    if c==1:
        print(i,end=" ")
print()
print("_"*50)
#24). Write a Python program to find the smallest and largest word in a given string.
#Input = “Learning is a part of life and we strive”
#Output = “a”, “Learning”
# solution in program no 7

#25). Check whether the given string is a palindrome (similar) or not.
#Input= sqatoolssqatools
#Output= Given string is not a palindrome
str1="sqatoolssqatools"
str2=str1[::-1]
if str1==str2:
    print("string is palindrome")
else:
    print("string is not palindrome")
print("_"*50)

#26). Write a program using python to reverse the words in a string.
#Input= sqatools python
#Output= slootaqs
s1="sqatools python"
s2=s1.split()
for i in s2:
    if i==s2[0]:
        print(i[::-1])
print()
print("-"*50)

#27). Write a program to calculate the length of a string.
#Input= “python”
#Output = 6
s1="python"
s=0
for i in s1:
    s=s+1
print(s)
print("-"*50)
#28). Write a program to calculate the frequency of each character in a string.
#Input = “sqatools”
#Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}
s="sqatools"
d={}
for char in s:
    if char in d:
        d[char]=d[char]+1
    else:
        d[char]=1
print(d)
print("_"*50)

#29). Write a program to combine two strings into one.
str1="basav"
str2="araja"
def addtwostring(str1,str2):
    res=""
    for char in str1:
        res=res+char
    for char in str2:
        res=res+char

    print(res)
str1="basav"
str2="araja"
addtwostring(str1,str2)
print("_"*50)
#30). Write a program to print characters at even places in a string.
str1="python programming"
for i in range(0,len(str1)-1,2):
    print(str1[i],end=" ")
print()
print("-"*50)

#31). Write a program to check if a string has a number or not.
#Input = ‘python1’
#Output = ‘Given string have a number’
str1="pyhton123"
flag=0
for i in str1:
    if i.isdigit():
        flag=1
        break

if flag:
    print("Given string have a number")
else:
    print("Given string is not have a number")

print("-"*50)
