################ Integer #########
###
# int -> float
n1 = 55
f1 = float(n1)
print(f1, type(f1))  # 55.0 <class 'float'>


print("_"*50)
## int -> string ####
n2 = 456567
print(n2, type(n2))
s2 = str(n2)
print(s2, type(s2), s2[2])
# 456567 <class 'str'> 6
str3 = 'Hello'
print(str3)


print("_"*50)
## int -> list #### conversion is not possible
# n3 = 8956948
# l1 = list(n3)
#print(l1)
# TypeError: 'int' object is not iterable

print("_"*50)
## int -> tuple #### conversion is not possible
print("_"*50)
## int -> dictionary #### conversion is not possible
print("_"*50)
## int -> set #### conversion is not possible

print("_"*50)
## int -> boolean ####
v1 = 0
print(v1, type(v1))
b1 = bool(v1)
print(b1, type(b1))  # False <class 'bool'>

v2 = 503
print(v2, type(v2))
b2 = bool(v2)
print(type(b2), b2)  # <class 'bool'> True


##################### Float ###################
print("_"*50)
## float -> int ####

f1 = 56.78
n1 = int(f1)
print(n1, type(n1))
# 56 <class 'int'>


print("_"*50)
## float -> string ####
f2 = 678.293
print(f2, type(f2))
s2 = str(f2)
print(s2, type(s2), s2[-2])
# 678.293 <class 'str'> 9

print("_"*50)
## float -> list #### conversion is not possible
## float -> dict #### conversion is not possible
## float -> set #### conversion is not possible

print("_"*50)
## float -> boolean ####

x1 = 0.0
b1 = bool(x1)
print(b1, type(b1)) # False <class 'bool'>

x2 = 45.67
b2 = bool(x2)
print(b2, type(b2)) # True <class 'bool'>


########################## String ################
print("_"*50)
### string -> int ####
"""
s1 = "Hello"
n1 = int(s1)
print(n1, type(n1))
# can not convert string into integer when it contains character as value
# ValueError: invalid literal for int() with base 10: 'Hello'
"""

# string to int conversion is possible when string contains only numbers.
s2 = "987654"
print(s2, type(s2)) # 987654 <class 'str'>
n2 = int(s2)
print(n2, type(n2)) # 987654 <class 'int'>
print(n2*2) # 1975308


print("_"*50)
### string -> float ####
s3 = "567.89"
f3 = float(s3)
print(f3, type(f3), f3*10)
# 567.89 <class 'float'> 5678.9


print("_"*50)
### string -> list ####
str3 = "Python"
l3 = list(str3)
print(l3, type(l3))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

print("_"*50)
### string -> tuple ####
str4 = "Python"
t3 = tuple(str4)
print(t3, type(t3))
# ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>


print("_"*50)
### string -> dict ####
"""
str5 = "Good Morning"
d1 = dict(str5)
print(d1)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""

# when string follows the dictionary pattern and all values are defined in json key value
# format then we can convert into dictionary with the help of json module.
import json
str6 = '{"Name": "JOhn", "email":"john@gmail.com", "phone": 545435435}'
print(str6, type(str6))
# {"Name": "JOhn", "email":"john@gmail.com", "phone": 545435435} <class 'str'>

data = json.loads(str6)
print(data, type(data))
# {'Name': 'JOhn', 'email': 'john@gmail.com', 'phone': 545435435} <class 'dict'>
print(data['email']) # john@gmail.com



print("_"*50)
### string -> set ####
str7 = "Python Programming"
s1 = set(str7)
print(s1, type(s1))
# {'n', 'o', 't', 'y', 'm', 'h', 'g', 'i', 'a', 'r', 'P', ' '} <class 'set'>


print("_"*50)
### string -> bool ####
s8 = ""
b1 = bool(s8)
print(b1, type(b1)) # False <class 'bool'>

s9 = "Hello"
b2 = bool(s9)
print(b2, type(b2)) # True <class 'bool'>



################################# List ######################################
print("_"*50)
### List -> int ###### conversion is not possible
"""
l1 = [4, 6, 7]
n1 = int(l1)
print(n1, type(n1))
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
"""


### List -> float ###### conversion is not possible
print("_"*51)
### List -> string ###
l2 = [5, 7, 8, 9]
s2 = str(l2)
print(s2, type(s2)) # [5, 7, 8, 9] <class 'str'>
print(s2[0], s2[1], s2[-2], s2[-1]) # [ 5 9 ]

s3 = "[4, 6, 7]"
print(s3[0], s3[1], s3[-1], s3[4]) # [ 4 ] 6


print("_"*50)
### List -> tuple ###
l3 = [5, 7, 9, 2, 5]
t3 = tuple(l3)
print(t3, type(t3))
# (5, 7, 9, 2, 5) <class 'tuple'>

print("_"*50)
### List -> dictionary ###
# list to dict conversion is possible

# if we have 2 list and convert into dict, then we can do it with help zip function
l1 = ['a', 'b', 'c', 'd']
l2 = [33, 66, 89, 23]
#print(list(zip(l1, l2))) # [('a', 33), ('b', 66), ('c', 89), ('d', 23)]
result = dict(zip(l1, l2))
print(result, type(result))
# {'a': 33, 'b': 66, 'c': 89, 'd': 23} <class 'dict'>


print("_"*50)
### List -> set ###
l3 = [5, 7, 9, 2, 5, 7, 9]
s3 = set(l3)
print(s3, type(s3))
# {9, 2, 5, 7} <class 'set'>


print("_"*50)
### List -> boolean ###
l4 = []
b1 = bool(l4)
print(b1, type(b1)) # False <class 'bool'>

l5 = [4, 6]
b2 = bool(l5)
print(b2, type(b2)) # True <class 'bool'>




########################### Tuple ###################

print("_"*50)
### tuple -> int ### conversion is not possible
### tuple -> float ### conversion is not possible

### tuple -> string ###

t1 = (5, 7, 9, 22)
s1 = str(t1)
print(s1, type(s1), s1[0], s1[4])
# (5, 7, 9, 22) <class 'str'> ( 7

print("_"*50)
### tuple -> list ###
t2 = (5, 7, 9, 22)
l2 = list(t2)
print(l2) # [5, 7, 9, 22]

print("_"*50)
### tuple -> dictionary ### convertion is not possible
# direct conversion is not possible

t4= ('a', 'b', 'c')
t5 = (123, 456, 789, 234)
result = dict(zip(t4, t5))
print("result :", result) # {'a': 123, 'b': 456, 'c': 789}


print("_"*50)
### tuple -> set ###
t6 = (4, 6, 78, 2, 5, 7, 4, 6)
s4 = set(t6)
print(s4, type(s4))
# {2, 4, 5, 6, 7, 78} <class 'set'>

print("_"*50)
### tuple -> bool ###

t1 = ()
print(t1, type(t1))
b1 = bool(t1)
print(b1, type(b1)) # False <class 'bool'>

t2 = (3, 5)
b2 = bool(t2)
print(b2, type(b2)) # True <class 'bool'>

############################
t5 = (5)
print(t5, type(t5))

x = 10
y = 50
operation = (x+y)*10


####################### dictionary ###############
## dict -> int ## conversion is not possible
## dict -> float ## conversion is not possible
print("_"*50)
#### dict -> string ###
d1 = {'a': 234, 'b': 456}
s1 = str(d1)
print(s1, type(s1))
print(s1[0], s1[6]) # {'a': 234, 'b': 456} <class 'str'>
 #{ 2


print("_"*50)
#### dict -> list ###
d2 = {'a': 234, 'b': 456, 'c': 567}
l2 = list(d2)
print(l2, type(l2))
# ['a', 'b', 'c'] <class 'list'>


print("_"*50)
#### dict -> tuple ###
d2 = {'a': 234, 'b': 456, 'c': 567}
t2 = tuple(d2)
print(t2, type(t2))
# ('a', 'b', 'c') <class 'tuple'>


print("_"*50)
#### dict -> set ###
d3 = {'a': 234, 'b': 456, 'c': 567}
s3 = set(d3)
print(s3, type(s3))
# {'a', 'c', 'b'} <class 'set'>
print(d3['a']) # 234


print("_"*50)
#### dict -> bool ###
d1= {}
b1 = bool(d1)
print(b1, type(b1)) # False <class 'bool'>

d2 = {'a': 456, 'b': 789}
print(d2, type(d2))  # {'a': 456, 'b': 789} <class 'dict'>
b2 = bool(d2)
print(b2, type(b2)) # True <class 'bool'>


print("_"*50)
########################## Set #####################
### set ->  Int #### conversion is not possible
### set ->  float ### conversion is not possible
### set ->  string ###
set1 = {5, 7, 9, 22, 44, 'a'}
str1 = str(set1)
print(str1, type(str1))
print(str1[1]) # 5

print("_"*50)
### set ->  list ###
set2 = {5, 7, 9, 22, 44, 'a'}
l2 = list(set2)
print(l2, type(l2))
# [5, 22, 7, 9, 44, 'a'] <class 'list'>


print("_"*50)
### set ->  tuple ###
set3 = {5, 7, 9, 22, 44, 'a'}
t3 = tuple(set3)
print(t3, type(t3))
# (5, 'a', 7, 22, 9, 44) <class 'tuple'>

print("_"*50)
### set ->  dict ### conversion is not possible

print("_"*50)
### set ->  boolean ###
set3 = set()
print(set3, type(set3))
b1 = bool(set3)
print(b1, type(b1)) # False <class 'bool'>

set4 = {5, 7, 8}
b2 = bool(set4)
print(b2, type(b2)) # True <class 'bool'>


#################### Boolean ###################
print("_"*50)
## bool -> int ###
b1 = True
n1 = int(b1)
print(n1, type(n1)) # 1 <class 'int'>

print("_"*50)
## bool -> float ###
b1 = False
f1 = float(b1)
print(f1, type(f1))  # 0.0 <class 'float'>


print("_"*50)
## bool -> string ###
b3 = True
s3 = str(b3)
print(s3, type(s3), s3[0])
# True <class 'str'> T


# obj = classname()

print("_"*50)
## bool -> list ###  conversion not possible
"""
"""b3= True
l3 = list(b3)
print(l3, type(l3))"""
"""
# TypeError: 'bool' object is not iterable

## bool -> tuple ###  conversion not possible
## bool -> dict ###  conversion not possible
## bool -> set ###  conversion not possible

######convert list to tuple #######

lis = [10, 20, 100, "varinder"]
print(lis)
tup = tuple(lis)
print("my result would display in tuple:", tup, type(tup))
