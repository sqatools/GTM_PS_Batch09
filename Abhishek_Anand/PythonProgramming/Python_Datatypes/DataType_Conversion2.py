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
b3= True
l3 = list(b3)
print(l3, type(l3))
"""
# TypeError: 'bool' object is not iterable

## bool -> tuple ###  conversion not possible
## bool -> dict ###  conversion not possible
## bool -> set ###  conversion not possible

