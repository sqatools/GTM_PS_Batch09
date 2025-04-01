"""
Python Data Types :
1.  Numbers
    1.1) Integer
    1.2) Float
    1.3) Complex Number
2.  Sequential
    2.1)   String
    2.2)  List
    2.3) Tuple
3.  Dictionary
4.  Set
5.  Boolean
"""

############ 1.1 Integer #################
"""
# properties of integer
->  Integer is immutable data type, once it is defined we can not change it.
->  Integer can contains any position and negative value.
->  Only whole will be consider as int
->  There is no limit to defined data in int variable

"""
n1 = 0
n2 = 4
n3 = 100
n4 = 45435435434354545454222333333333
n5 = -5644545
print(n1, type(n1)) # 0 <class 'int'>
print(n2, type(n2)) # 4 <class 'int'>
print(n3, type(n3)) # 100 <class 'int'>
print(n4, type(n4)) # 45435435434354545454222333333333 <class 'int'>
print(n5, type(n5)) # -5644545 <class 'int'>

# when we multiply string with number, then it repeats the string that number of times.
var1 = 'Hello'
print(var1*5)

print("_"*50)
############ 1.2 Float #################
"""
->  Float is immutable data type.
->  Float only contains pointer values. e.g 4.5, 5.6, 0.23
->  Any positive and negative values can be float data type
->  There is no limit for float data type
"""
f1 = 0.0
f2 = 12.34
f3 = 4543543543.776899
f4 = -45676.789
f5 = 0.45454545
f6 = 9.0
print("f1 :", f1, type(f1)) # 0.0 <class 'float'>
print("f2 :", f2, type(f2)) # 12.34 <class 'float'>
print("f3 :", f3, type(f3)) # 4543543543.776899 <class 'float'>
print("f4 :", f4, type(f4)) # -45676.789 <class 'float'>
print("f5 :", f5, type(f5)) # 0.45454545 <class 'float'>
print("f6 :", f6, type(f6)) # 9.0 <class 'float'>

print("_"*50)
############ 1.3 Complex Number #################
# var1 = x + yj
# x = real value
# y = imaginary value

var2 = 10 + 20j
print(var2, type(var2))
print("real value :", var2.real) # real value : 10.0
print("imaginary value:", var2.imag)  # imaginary value: 20.0

var3 = 0+50j
print(var3, type(var3)) # 50j <class 'complex'>

var5 = 50j + 70
print(var5, type(var5)) # (70+50j) <class 'complex'>

var6 = "40 + 60j"
print(var6, type(var6)) # 40 + 60j <class 'str'>

var4 = 40+0j
print(var4, type(var4)) # (40+0j) <class 'complex'>

print(70,'Hello', 80+90j) # 70 Hello (80+90j)


print("_"*50)
############ 2.1 string data type #################
"""
# String Properties
1.  String is immutable data type, once it is defined can not update it.
2.  String follows positive and negative indexing.
3.  There is no limit for string to define.
4.  String value defined different types of quotes single quotes, double quotes, single triple quote, double triple quote.
5.  String can contains any data , numbers, special character
"""
s1 = 'h'
s2 = "Hello Python"
s3 = "We are learning Python Programming"
s4 = '''
1. Good Morning
2. Good Evening
3. Python Programming
'''
s5 = """
The STRING database contains information 
from numerous sources, including experimental\n
data, computational prediction methods and 
public text collections. It is freely accessible 
and it is regularly updated
"""
s6 = "My name is 'John' and live in mumbai"
s7 = 'My name is "John" and live in mumbai %^%RT&^%d45564654654e '
s8 = "1. The STRING database \t\t contains information from \n2. numerous sources, including \t\t experimental \n3. data, computational \t\t prediction methods and "

# \n = line break
# \t = line space

print(s1, type(s1))
print("_"*50)
print(s2, type(s2))
print("_"*50)
print(s3, type(s3))
print("_"*50)
print(s4, type(s4))
print("_"*50)
print(s5, type(s5))
print("_"*50)
print(s6, type(s6))
print("_"*50)
print(s7, type(s7))
print("_"*50)
print(s8, type(s8))

str_a  = "Python"

"""
 0  1  2  3  4   5   +ve
 P  y  t  h  o   n
-6 -5 -4 -3  -2  -1  -ve
"""

print("first char :", str_a[0])  # first char : P
print("third index char :", str_a[3])  # third index char : h
print("get h with -ve indexing :", str_a[-3]) # get h with -ve indexing : h

str9 = "My name is 'John' and live in mumbai"
print("get m with -ve index :", str9[-4]) #  m


print("_"*50)
############ 2.2 List data type #################
"""
# Properties of List
->  List is mutable data type, we can modify the list content
->  List define with square bracket
->  List can contains all different types of values, int, float, sting, list, tuple, dictionary, set, boolean, complex number
->  List follows the positive and negative indexing as like string
->  There is no limit to defined values in the list
->  List values are comma seperated.
"""
#        0  1     2        3          4          5            6      7     8       9
list1 = [2, 3.5, 'Hello', [4, 6, 7], (3, 7, 9), {'a': 123}, {5, 7}, True, 40+50j, None]
#      -10  -9    -8       -7         -6        -5           -4      -3    -2     -1
#
print(list1, type(list1))  # <class 'list'>

print(list1[3]) # [4, 6, 7]
print(list1[3][2])  # 7
# get value with -ve indexing
print(list1[-4])  # {5, 7}

list2 = [5, 7, 8]
list2.append(100)
print(list2) # [5, 7, 8, 100]

######################## 2.3 Tuple ####################
tuple1 =  (1, 3.4, 'Hello', [4, 5, 6], (3, 6), {'a': 123}, {4, 6, 8}, True)
print(tuple1, type(tuple1))
# (1, 3.4, 'Hello', [4, 5, 6], (3, 6), {'a': 123}, {8, 4, 6}, True) <class 'tuple'>

"""
Properties of Tuple
->  Tuple is immutable data type, once it is defined can not change the values.
->  Tuple can contain all types data, int, float, complex, str, list, tuple, dict, bool.
->  Tuple follows positive negative indexing as like string and list.
->  Tuple store data in with round brackets.
->  In terms of performance, tuple is faster than list.
"""
#      0   1  2  3  4                 5       6
tup2 = (4, 7, 9, 4, ('a', 'b', 'c'), 'Hello', 14)
#      -7 -6  -5 -4 -3                -2       -1

print(tup2[2]) # 9
print(tup2[-3]) # ('a', 'b', 'c')
print(tup2[4][1]) # b
print(tup2[5]) # Hello
print(tup2[5][1]) # e


print("_"*50)
#################### 3 Dictionary data type ##################
# dict1 = {'key':'value'}
dict1 = {'Name': 'rahul gupta', 'age': 20, 'email': 'rahul@gmail.com', 'phone': 656456546}
print(dict1, type(dict1))

# {'Name': 'rahul gupta', 'age': 20, 'email': 'rahul@gmail.com', 'phone': 656456546} <class 'dict'>

print(dict1['Name']) # rahul gupta
print(dict1['phone']) # 656456546

"""
Properties of dictionary

1. Dictionary is mutable data type, we can change data any point of time.
2. Dictionary store data in key value format e.g.  {'a': 123}
3. Dictionary store data with unique key, duplicate keys are not allowed.
   if we will duplicate keys, then latest defined key data will be considered.
4. Dictionary value can contains duplicate data.
5. Only immutable data type can be key in dictionary, int, float, string, tuple, boolean.
6. All type of data can be value in the dictionary.
7. Dictionary does not follow positive and negative indexing
8. Dictionary store data with LIFO algo (LAST IN FIRST OUT)
"""

dict2 = {'a': 123, 'b' : 456}
print("dict2 :", dict2) # {'a': 123, 'b': 456}
dict2['c'] = 500
print("dict2 :", dict2) # dict2 : {'a': 123, 'b': 456, 'c': 500}


# if we defined duplicate key in the dict the latest value will be considered.
dict3 = {'a': 123, 'b' : 456, 'c': 600, 'a': 500, 'e': 456}
print("dict3 :", dict3) # dict3 : {'a': 500, 'b': 456, 'c': 600, 'e': 456}


dict4 = {
    34: 4.5,
    55.6 : 'Hello',
    'Name' : 'John',
    ('a', 'b') : [4, 6, 8, 9],
    True : {'P': 345, 'Q': 789, 'R': 3456},
    # Mutable data types are not allowed as key (list, dict, set)
    # [1, 2, 3] : {4, 6, 8, 1}  #TypeError: unhashable type: 'list'

}
print("dict4 :", dict4)     #{34: 4.5, 55.6: 'Hello', 'Name': 'John', ('a', 'b'): [4, 6, 8, 9], True: {'P': 345, 'Q': 789, 'R': 3456}}


# dict does not follow indexing
# print(dict4[0]) # KeyError: 0

print("_"*40)
# remove data from dict
result = dict4.popitem()
print("result :", result)

print("dict4 :", dict4)


result2 = dict3.popitem()
print("result2 :", result2)         #('e', 456)
print("dict3 :", dict3)
# dict3 : {'a': 500, 'b': 456, 'c': 600}

print("_"*50)
################################ 4 Set ########################
set1 = {3, 'c', 7, 'a', 'b', 8, 2, 7, 'a', 9, 3}
print("Set1 :", set1)
"""
Properties :
->  Set is mutable data type, we modify it.
->  Set store unique data, duplicate values are not allowed.
->  Set store data in random order.
->  Set can contain only immutable data type, int, float, string, tuple, boolean, complex number.
->  Set does not follow indexing.
"""

set2 = {3, 5, 7, 'a', 'b', 3}
print(set2, type(set2))  # {3, 7, 5, 'a', 'b'} <class 'set'>

set2.add(100)
print("set2 :", set2) # set2 : {3, 100, 5, 'a', 7, 'b'}

#set3 = {3, 5, 7, 'a', 'b', 3, [3, 5, 7]}
#print("set3 :", set3)
# TypeError: unhashable type: 'list'

############################# 5 Boolean ################
"""
Properties :
->  Boolean is immutable data type.
->  Boolean accepts the only 2 values True or False
->  Generally booleans value will the output of any specific condition
"""

val1 = True
val2 = False

n1 = 10
n2 = 40
n3 = 10
print(n1 == n2) # False
print(n2 == n3) # False
print(n1 == n3) # True

