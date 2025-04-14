################ Integer #########
###
# int -> float

n1 = 55
f1 = float(n1)
print(f1, type(f1))
# 55.0 <class 'float'>

print("_"*50)
## int -> string ####
n2 = 456567
print(n2, type(n2))
s1 = str(n2)
print(s1, type(s1), s1[1])
str3 = 'Hello'
print(str3)


print("_"*50)
## int -> list #### conversion is not possible

#n3 = 8956948
#l1 = list(n3)
#print(l1) $ TypeError: 'int' object is not iterable

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
l1 = list(str3)
print(l1, type(l1))
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


print("_"*50)
### string -> set ####
str7 = "Python Programming"
s1 = set(str7)
print(s1, type(s1))
# {'t', 'm', 'P', 'n', 'r', 'a', ' ', 'i', 'y', 'g', 'h', 'o'} <class 'set'>

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
print("_"*50)
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


