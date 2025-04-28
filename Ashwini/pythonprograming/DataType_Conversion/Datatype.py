#############Integer############
###int->float####
import json

n1 = 55
f1 = float(n1)
print(f1, type(f1))  # 55.0 <class 'float'>

print("_" * 50)
## int -> string ####
n2 = 34521
print(n2, type(n2))
s2 = str(n2)
print(s2, type(s2), s2[2])
# 456567 <class 'str'> 6
str3 = 'Hello'
print(str3)

##### int ->list ##########   Conversion is not possible
"""n2 = 879654
l1 = list(n2)
print(l1)"""
# TypeError: 'int' object is not iterable
#### int-> Tuple ##### conversion is not possible
#### int-> dictionry #### conversion is not possible
#### int-> set #### conversion is not possible
####### int-> boolean ###
v1 = 0
print(v1, type(v1))
b1 = bool(v1)
print(b1, type(b1))

v2 = 504
print(v2, type(v2))
b2 = bool(v2)

print(type(b2), type(b2))

############## Float ##############

##### float->int ####
f1 = 56.42
n1 = int(f1)
print(n1, type(n1))

print("-" * 50)
### float-> string ###
f2 = 456.89
print(f2, type(f2))
s2 = str(f2)
print(s2, type(s2), s2[-3])

print("-" * 50)
### float-> list ### conversion is not possible

### float-> set ### conversion is not possible

### float-> dictionary ### conversion is not possible

print("-" * 50)
### float -> boolean####
x1 = 0.0
b1 = bool(x1)
print(b1, type(b2))

x2 = 43.67
b2 = bool(x2)
print(b2, type(b2))
print("-" * 50)

################### string ############
### string-> int ####
"""s1 = "cool"
n1 = int(s1)
print(n1, type(n1))
# con not convert string into intger when it contains charchater as value
# ValueError: invalid literal for int() with base 10: 'cool'"""
s2 = "89520"
print(s2, type(s2))
n2 = int(s2)
print(n2, type(n2))
print(n2 * 2)

### string-> flaot ####
s3 = "56.87"
f3 = float(s3)
print(f3, type(f3), f3 * 10)
print("-" * 50)
######## string -> list ####
str3 = "java"
l3 = list(str3)
print(l3, type(l3))

print("-" * 50)
#### string -> tuple ####
str4 = "python"
t3 = tuple(str4)
print(t3, type(t3))

print("-" * 50)
#### string->dictionry ####
"""" str5 = "helll"
d1 = dict(str5)
print(d1)
# valueError: dictionary update sequence element #0 has length 1; 2 is required
"""
import json

str6 = '{"name":"ram", "email":"ajhg@gmail.com", "phone":564322}'
print(str6, type(str6))
data = json.loads(str6)
print(data, type(data))
print(data['phone'])
print("-" * 50)

#### string -> set #####
str7 = "good Mornig"
s1 = set(str7)
print(s1, type(s1))

###string-> boolean ###
s8 = ""
b1 = bool(s8)
print(b1, type(b1))

s9 = "hello"
b2 = bool(s9)
print(b2, type(b2))

print("-" * 50)

############ List ############
### list -> int #####
"""l1 = [4, 3, 2]
n1 = int(l1)
print(n1, type(n1))
#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list' """

#### list-> float ####### conversion is not possible
print("-" * 50)
### list -> string ####
l2 = [5, 6, 7, 8]
s2 = str(l2)
print(s2, type(s2))
print(s2[0], s2[3], s2[-2])
s3 = "[3, 5, 7, 9]"
print(s3[0], s3[1], s3[-1])
print("-" * 50)

####list-> tuple###
l3 = [3, 5, 6, 8, 9]
t3 = tuple(l3)
print(t3, type(t3))
print("-" * 50)
#### list -> dictionary###
# list to dict conversion is not possible
l1 = ['a', 'b', 'c', 'd']
l2 = [22, 66, 99, 44]
result = dict(zip(l1, l2))
print(result, type(result))
print("-" * 50)

### list -> set####
l3 = [4, 5, 6, 2, 8, 9]
s3 = set(l3)
print(s3, type(s3))
print("-" * 50)
#### list-> boolean####
l4 = []

b1 = bool(l4)
print(b1, type(b1))

l5 = [6, 7, 9]
b2 = bool(l5)
print(b2, type(b2))
print("-" * 50)

############## tuple ##########
##### tuple -> int ########## conversion is not possible
#### tuple-> float ### conversion is not possible
### tuple -> string ####
t1 = (3, 5, 7, 8, 9)
s1 = str(t1)
print(s1, type(s1), s1[0], s1[3])

#### tuple -> list ##