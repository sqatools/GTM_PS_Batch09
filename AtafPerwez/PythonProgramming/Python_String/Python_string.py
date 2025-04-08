str1 = "Hello"
print(str1, type(str1))

"""
 0  1  2  3  4  +ve
 H  e  l  l  o
-5 -4 -3 -2 -1  -ve 
"""
print(str1[0])  # H
print(str1[-2]) # l

print("_"*50)
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

print("_"*50)
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

print("_"*50)
##################### String formating ##############
str3 = "My name is john and my age is 25, living in Mumbai"

Name = "Rahul"
Age = 20
City = "Bangalore"

# 1. string concatenation
result1 = "My name is "+Name+" and my age is "+str(Age)+", living in "+City
print("result1:", result1)


# 2. string format method.
result2 = "My name is {} and my age is {}, living in {}".format(Name, Age, City)
print("result2:", result2)


# 3. f string formatting.
result3 = f"My name is {Name} and my age is {Age}, living in {City}"
print("result3:", result3)


print("_"*50)
######## convert string to raw string #############
# \t :  add spaces in string
# \n :  add next line in the string.
str4 = r"Hello good morning \t \t \t, hope you are doing good \n \h $%$#@ , we are learning Python"
print(str4)

print("_"*40)
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
print(str_a[3:]) # gramming

# start : -ve and end : +ve
print(str_a[-6:10])  # ammin

# start : +ve and end : -ve
print(str_a[1:-1]) # rogrammin

str_b = "Good Morning"
# start : -ve and end : -ve
print(str_b[-7:-1]) # Mornin
print(str_b[-7:]) # Morning

print("_"*50)
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
print(str_c[1:10:2]) # el ol
print(str_c[2:11:])  # llo world  # default step value is 1

# get right to left output
print(str_c[-1:-9:-1])  # dlrow ol
print(str_c[-5:-2:])  # wor  #default step value is 1


# default end index will be start of string when step value is -ve e.g. [start index:: -ve step value]
str_d = "Python Programming"
print(str_d[-1::-1])  # gnimmargorP nohtyP
print(str_d[-1::-2]) # gimroPnhy


# default end index will be end of string when step value is +ve e.g. [start index::+ve step value]
print(str_d[::]) # Python Programming
print(str_d[1::1]) # # Python Programming

# default start index will be -1, when step value is -ve. e.g str[: end index: -ve step value]
print(str_d[:5:-1])  # gnimmargorP

# reverse of the string
print(str_d[::-1])  # gnimmargorP nohtyP



# slicing Home work
str1 = "Hello good Morning"

output1 = "HHello good Morningg"

output2 = "HHelloo ggoodd MMorningg"

output3 = "oellH doog gorninM"
