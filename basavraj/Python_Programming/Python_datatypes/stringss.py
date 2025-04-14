
str1 = "Hello"
print(str1, type(str1))

"""
 0  1  2  3  4  +ve
 H  e  l  l  o
-5 -4 -3 -2 -1  -ve 
"""
print(str1[0])  # H
print(str1[-2])  # l

print("_" * 50)
# apply loop on string
str2 = "Python"

# apply loop without indexing
for char in str2:
    print(char)

"""
P
y
t
h
o
n

"""

print("_" * 50)
# apply loop with indexing
str_len = len(str2)
print("string length :", str_len, str2)
for i in range(str_len):
    print(i, str2[i])

"""
string length : 6 Python
0 P
1 y
2 t
3 h
4 o
5 n
"""

print("_" * 50)
##################### String formating ##############
str3 = "My name is john and my age is 25, living in Mumbai"

Name = "Rahul"
Age = 20
City = "Bangalore"

# 1. string concatenation
result1 = "My name is " + Name + " and my age is " + str(Age) + ", living in " + City
print("result1:", result1)

# 2. string format method.
result2 = "My name is {} and my age is {}, living in {}".format(Name, Age, City)
print("result2:", result2)

# 3. f string formatting.
result3 = f"My name is {Name} and my age is {Age}, living in {City}"
print("result3:", result3)

print("_" * 50)
######## convert string to raw string #############
# \t :  add spaces in string
# \n :  add next line in the string.
str4 = r"Hello good morning \t \t \t, hope you are doing good \n \h $%$#@ , we are learning Python"
print(str4)

print("_" * 40)
############## string slicing ####################
# Rule 1: str[start index: end index]
"""
->  Output will contains result from left to right.
->  Output value will include start index and exclude the end index.
->  if we don't defined the start index, then default start index is 0 e.g. str[:end index]
->   if we don't defined the end index, then default end index would be end of the string.
     e.g. str[start index:]
->   
"""

str_a = "Programming"

print(str_a[3:8])  # gramm

# default start index is 0
print(str_a[:8])  # Programm

# default end index will end of string.
print(str_a[3:])  # gramming

# start : -ve and end : +ve
print(str_a[-6:10])  # ammin

# start : +ve and end : -ve
print(str_a[1:-1])  # rogrammin

str_b = "Good Morning"
# start : -ve and end : -ve
print(str_b[-7:-1])  # Mornin
print(str_b[-7:])  # Morning

print("_" * 50)
#############################################################
# Rule 2: str[start index: end index: step value]
"""
->  Output may contains value from "left to right" or "right to left".
->  Output will include start index and exclude last index.
->  default start index will be zero, when step value is +ve. e.g str[: end index: +ve step value]
->  default end index will be end of string when step value is +ve e.g. [start index::+ve step value]
->  default start index will be -1, when step value is -ve. e.g str[: end index: -ve step value]
->  default end index will be start of string when step value is -ve e.g. [start index:: -ve step value]
->  default step values is 1
"""

str_c = "Hello world"
# get left to right output
print(str_c[2:8:1])  # llo wo
print(str_c[1:10:2])  # el ol
print(str_c[2:11:])  # llo world  # default step value is 1

# get right to left output
print(str_c[-1:-9:-1])  # dlrow ol
print(str_c[-5:-2:])  # wor  #default step value is 1

# default end index will be start of string when step value is -ve e.g. [start index:: -ve step value]
str_d = "Python Programming"
print(str_d[-1::-1])  # gnimmargorP nohtyP
print(str_d[-1::-2])  # gimroPnhy

# default end index will be end of string when step value is +ve e.g. [start index::+ve step value]
print(str_d[::])  # Python Programming
print(str_d[1::1])  # # Python Programming

# default start index will be -1, when step value is -ve. e.g str[: end index: -ve step value]
print(str_d[:5:-1])  # gnimmargorP

# reverse of the string
print(str_d[::-1])  # gnimmargorP nohtyP

# slicing Home work
print("_"*50)
str1 = "Hello good Morning"
"""

output1 = "HHello good Morningg"

output2 = "HHelloo ggoodd MMorningg"

output3 = "oellH doog gorninM"
"""

# slicing Home work
str1 = "Hello good Morning"

print("_" * 40)
output1 = "HHello good Morningg"
# solution1
print(f"{str1[0]}{str1}{str1[-1]}")  # HHello good Morningg
print("_" * 40)
output2 = "HHelloo ggoodd MMorningg"
# solution2
word1 = str1[:5]
word2 = str1[6:10]
word3 = str1[11:]

output3 = "oellH doog gorninM"
print(f"{word1[0]}{word1}{word1[-1]} {word2[0]}{word2}{word2[-1]}  {word3[0]}{word3}{word3[-1]}")
# HHelloo ggoodd  MMorningg
print("_"*40)
output3 = "olleH doog gninroM"
 # solution
print(f"{word1[::-1]} {word2[::-1]} {word3[::-1]}")

print(dir(str))
"""
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
  'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

 # str() # class
 # str.upper() # method
 # for :  keyword
 # dir() : function


 """
########
# upper() and lower() methods
# upper() method convert string into upper case.
# lower() method convert string into lower case.

str1 = "Hello Good Morning"
print("Upper result :", str1.upper())  # HELLO GOOD MORNING
print("Lower result :", str1.lower())  # hello good morning

##############################################
# isupper() and islower() method:
# isupper() :  This method check given string is in upper case or not.
# islower() :  This method check given string is in lower case or not.

str2 = "Python Programming"
str3 = "GOOD MORNING"
str4 = "learning python"

print("str2 is upper:", str2.isupper())  # False
print("str2 is lower:", str2.islower())  # False

print("str3 is upper:", str3.isupper())  # True
print("str4 is lower:", str4.islower())  # True

print("_" * 50)
#########################################
# swapcase() method :  This method convert string characters upper to lower and lower to upper.

str5 = "Hello GoOd MoRnIng"
print(str5.swapcase())  # hELLO gOoD mOrNiNG

print("_" * 50)
#########################################
# capatilize() method : This method change the first character of entire sentence into capital case

str6 = "we Are Learning Python"
print(str6.capitalize())
# We are learning python

print("_" * 50)
#########################################
# title() method :  This method convert first letter of each word into capital case.

str7 = "india is besT cricket tEam"
print(str7.title())
# India Is Best Cricket Team

print("_" * 50)
#########################################
# istitle() method:  This method check given string in following the rules of title or not.

str8 = "Virat is best cricketer"
str9 = "Sachin Is God Of Cricket"
print("str8 is title :", str8.istitle())  # False
print("str9 is title :", str9.istitle())  # True

print("_" * 50)
#########################################
# count() method : This method count the occurrences of any particular character/substring

str10 = "India will win world cup Wi India"
print("count of w :", str10.count('w'))
# count of w : 3

print("count of substring wi :", str10.count('wi'))
# count of substring wi : 2

print("count of substring India :", str10.count('India'))
# count of substring India : 2

print("all character count :", len(str10))
# all character count : 33


print("_" * 50)
#########################################
# split() method : This method break the string in list words with specifies delimeters.

str11 = "India will win world cup Wi India"

str12 = "We_Are_Learning_Python Programming"

word_list = str11.split(" ")
print(word_list)  # ['India', 'will', 'win', 'world', 'cup', 'Wi', 'India']
print("count of words :", len(word_list))  # count of words : 7

word_list2 = str12.split("_")
print(word_list2)  # ['We', 'Are', 'Learning', 'Python', 'Programming']

word_list3 = str12.split("P")
print("word_list3:", word_list3)  # ['We_Are_Learning_', 'ython_', 'rogramming']

# use same method multiple times
str13 = "Very_good_morning Python_Programming"

print(str13.split(" "))  # ['Very_good_morning', 'Python_Programming']

print(str13.split(" ")[0].split("_"))  # ['Very', 'good', 'morning']

print(str13.split(" ")[0].split("_")[1].upper())  # GOOD

print("_" * 50)
#########################################
# replace() method : This method replace any word with target value.
# replace method accept three param
# replace(old, new, count)
# count is optional parameter, that replace number of occurrences
str14 = "Very good Python morning Python Programming"

# remove all spaces
result = str14.replace(" ", "")
print("result:", result)
print("only char count without space :", len(result))  # 32

# replace word Python with Java
result2 = str14.replace("Python", "Java")
print("result2 :", result2)  # Very good morning Java Programming

result3 = str14.replace("Python", "C++", 1).replace("morning", "evening")
print("result3 :", result3)
# result3 : Very good C++ evening Python Programming
