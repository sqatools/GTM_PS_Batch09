# 1 Python string program that takes a list of strings and returns the length of the longest string.
string = ["i", "am", "learning", "python"]
temp = 0

for word in string:
    a = len(word)
    if a > temp:
        temp = a

print(temp)
# 2 write a python to get longgest word from given string.
str1 = "We are Learning python programming"
long_len = 0

word_list = str1.split()
print(word_list)
for word in word_list:  # We, are, Learning, Python, Programming
    word_len = len(word)  # 2, 3, 8, 6, 11
    # print(word, word_len)
    if word_len > long_len:  # 2 > 0 | 3 > 2 | 8> 3 | 6> 8 | 11> 8
        long_len = word_len  # 2, 3, 8, 11
        long_word = word  # We, Are, Learning, Programming
    else:
        continue

print(long_word, long_len)

# 3 Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
string1 = "Python"
if len(string1) < 2:
    print(True)
else:
    print(string1[:2] + string1[-2:])

print("-" * 50)
# 4 Python string program to get a string made of 4 copies of the last two characters of
# a specified string (length must be at least 2).
string2 = "Python"
print(string2[-2:] * 4)

print("-" * 60)
# 5 Python string program to reverse a string if it’s length is a multiple of 4.
str2 = "Morninng"
if len(str2) % 4 == 0:
    print(str2[::-1])
print("-" * 60)
# 6 Python string program to count occurrences of a substring in a string.
str3 = "we are learning python "
print(str3.count("n"))

print("-" * 60)
# 7 Python string program to test whether a passed letter is a vowel or consonant.
str4 = "Pythonisgood"

for char in str4:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(f"{char} is vowel")
    else:
        print(f"{char} is constant")

print("-" * 60)
# 8 Find the longest and smallest word in the input string.

string = "we are learning python"
list1 = string.split(" ")

print("Longest word: ", max(list1, key=len))
print("Smallest word: ", min(list1, key=len))

print("-" * 60)
""" 9 Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”"""

str5 = "Programming"
result = " "
for char in str5:
    if char in result:
        result = result + "$"
    else:
        result = result + char

print("Result :", result)

# . 10 Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”
str6 = "SqaTool"
print(str6[-1] + str6[1:-1] + str6[0])

print("-" * 50)
""" 11 Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”"""

str7 = "Sqa Tools Learning"
vowel = "aeiouAEIOU"
result = ""
for char in str7:
    if char in vowel:
        result = result + char * 3
    else:
        result = result + char * 2

print(result)
print("-" * 50)
""" 12 Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”"""

string3 = "Cricket Plays Virat"
list = string3.split()
word1 = string3[:7]
word2 = string3[8:13]
word3 = string3[14:]
print(word3 + word2 + word1)

print("-" * 60)
""" 13 Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”"""
str_a = "JAVA is the Best Programming Language in the Market"
list = str_a.split()
print(str_a.replace('JAVA', 'Python'))

print("-" * 60)
""" 14 Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.
"""

str_b = ["There", "are", "Many", "Programming", "Language"]
result = " ".join(str_b)
print("result :", result)

print("-" * 60)
""" 15 Write a Python program to get common words from strings.
Input String1 = “Very Good Morning, How are You”
Input String1 = “You are a Good student, keep it up”
Output = “You Good are”"""
str1 = "Very Good Morning, How are You"
str2 = "You are a Good student,keep it up"
list = []
for word in str1.split():
    if word in str2.split():
        list.append(word)

# 16 Write a program to calculate the length of a string.
# Input= “python”
# Output = 6
str_d = "python"
str_len = len(str_d)
print(str_len)

print("-" * 60)
"""17 Write a program to combine two strings into one.
Input: 
A = ’abc’
B = ’def’
Output = abcdef"""
str_e = "abc"
str_f = "def"
print(str_e + str_f)
print("-" * 60)
""" 18 Write a python program to split and join a string
Input =‘Hello world’
Output = [‘Hello’, ‘world’]
            Hello-world
"""
str_g = "Hello world"
new_str_g = str_g.split()
print(new_str_g)
print("-".join(new_str_g))

print("-" * 50)
""" 19 Write a python program to convert a string into a list of words.
Input= ‘learning python is fun’
Output = [learning, python, is, fun] """
string = "learning python is fun"
list1 = string.split(" ")
print(list1)

print("-" * 60)
""" 20 Write a python program to swap commas and dots in a string.
Input = sqa,tools.python
Output = sqa.tools,python"""
str14 = "sqa,tools.python"
print(str14.replace(",", "."))

print("-" * 50)
""" 21 Write a program to get all the email id’s from given string using python.
Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com 
we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.”””
Output = [‘john@gmail.com’, ‘ jay@lic.com’, ‘hari@facebook.com’, ‘mery@hotmail.com’ ]"""
str8 = """We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com 
 we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string."""
list2 = str8.split()
list3 = []
for char in list2:
    for val in char:
        if val == "@":
            list3.append(char)

print(list3)

print("-" * 60)
""" 22 Write a program to get a list of all the mobile numbers from the given string using python.
Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
Output = [‘8988858683’, ‘2312245566’, ‘4532892234’, ‘9999234355’]"""
str9 = """We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 
         we want 453452 to get 4532892234 all the mobile numbers 9999234355"""
list4 = str9.split()
list5 = []
for val in list4:
    if len(val) == 10 and val.isnumeric():
        list5.append(val)

print(list5)

print("-" * 60)
# 23 Write a Python program to calculate the length of a string with loop logic.
str15 = "Hello good Morning"
count = 0

for char in str15:
    count += 1
print("Length of the string using loop logic: ", count)
print("Length of the string using len(): ", len(str15))

print("-" * 60)
"""24 Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”"""

str16 = "Its Online Learning"
word1 = str16[:3]
word2 = str16[4:10]
word3 = str16[11:]
print(f"{word1[::-1]},{word2[-1]}{word2[1:-1]}{word2[0]},{word3[-1]}{word3[1:-1]}{word3[0]}")

print("-" * 60)
""" 25 Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”"""
str17 = "John jany sabi  row john sabi"
new_str = str17.split()
list6 = []
for val in new_str:
    if val not in list6:
        list6.append(val)
print(" ".join(list6))

print("-" * 60)
""" 26 Check whether the given string is a palindrome (similar) or not.
Input= sqatoolssqatools
Output= Given string is not a palindrome"""

str18 = "sqatoolssqatools"
str19 = str18[::-1]
if str17 == str19:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")

print("-" * 50)
""" 27 Write a program to check if a string has a number or not.
Input = ‘python1’
Output = ‘Given string have a number’"""

string4 = "python1"
count = 0
for char in string4:
    if char.isnumeric():
        count += 1

if count > 0:
    print("Given string have a number")
else:
    print("Given string does not have a number")

print("-" * 60)
"""28 Write a python program to count the number of vowels in a string.
Input= ‘I am learning python’
Output= 6"""
string5 = "I am Learning python"
vowel = "aeiouAEIOU"
count = 0
for char in string5:
    if char in vowel:
        count += 1
print(count)

print("-" * 60)
""" 29 Write a python program to count the number of consonants in a string.
Input= ‘sqltools’
Output= 6"""
string6 = "sqltools"
vowel = "aeiou"
count = 0
for char in string6:
    if char not in vowel:
        count += 1
print(count)

"""31. Write a python program to replace multiple words with certain words.
Input = “I’m learning python at Sqatools”
Replace python with SQA  and sqatools with TOOLS 
Output = “I’m learning SQA at TOOLS “"""
string7 = "I m Learning python at sqatools"
print(string7.replace("python", "SQA").replace("sqatools", "TOOLS"))

print("-" * 60)
""" 32 Write a python program to replace different characters in the string at once.
Input = ‘Sqatool python’
Replace a with 1,
Replace t with 2,
Replace o with 3
Output = ‘sq1233l py2h3n”"""

string8 = "Sqatool python"
print(string8.replace("a", "1").replace("t", "2").replace("o", "3"))

print("-" * 60)
""" 33 Write a python program to remove empty spaces from a list of strings.
Input = [‘Python’, ‘ ‘, ‘ ‘, ‘sqatools’]
Output = [‘Python’, ‘sqatools’] """
string9 = """Python’, ‘ ‘, ‘ ‘, ‘sqatools’"""
list_1 = string9.split()
print(string9.strip())

print("-" * 60)