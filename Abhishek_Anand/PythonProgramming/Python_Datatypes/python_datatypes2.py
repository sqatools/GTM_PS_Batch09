"""
Python Data Types :

1.  Numbers
    i) Integer
    ii) Float
    iii) Complex Number

2.  Sequential
    i)   String
    ii)  List
    iii) Tuple


3.  Dictionary
4.  Set
5.  Boolean
"""

######################## Tuple ####################
tuple1 = (1, 3.4, 'Hello', [4, 5, 6], (3, 6), {'a': 123}, {4, 6, 8}, True)
print(tuple1, type(tuple1))

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
print(tup2[0])
print(tup2[-1])
print(tup2[2]) # 9
print(tup2[-3]) # ('a', 'b', 'c')
print(tup2[4][1]) # b
print(tup2[5]) # Hello
print(tup2[5][1]) # e

print("_"*50)
#################### dictionary data type ##################
# dictionary = {'Key': 'value'}
dict1 = {'Name': 'Rajat', 'Age': '18', 'email': 'rajat@gmail.com', 'phone':'9999999999'}
print(dict1, type(dict1))
# {'Name': 'Rajat', 'Age': '18', 'email': 'rajat@gmail.com', 'phone': '9999999999'} <class 'dict'>

print(dict1['Name']) # Rajat
print(dict1['phone']) # 9999999999

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

dict2 = {'a': 123, 'b': 456}
print("dict2:" , dict2)
dict2['c'] = 500
#dict2 = {'c': 1631}
print("dict2 :", dict2)


# if we defined duplicate key in the dict the latest value will be considered.
dict3 = {'a': 123, 'b' : 456, 'c': 600, 'a': 500, 'e': 456}
print("dict3 :", dict3)

dict4 = {
    34: 4.5,
    55.6 : 'Hello',
    'Name' : 'John',
    ('a', 'b') : [4, 6, 8, 9],
    True : {'P': 345, 'Q': 789, 'R': 3456},
    # Mutable data types are not allowed as key (list, dict, set)
    # [1, 2, 3] : {4, 6, 8, 1}  #TypeError: unhashable type: 'list'

}
print("dict4 :", dict4) # {34: 4.5, 55.6: 'Hello', 'Name': 'John', ('a', 'b'): [4, 6, 8, 9], True: {'P': 345, 'Q': 789, 'R': 3456}}


# dict does not follow indexing
# print(dict4[0]) # KeyError: 0

print("_"*40)
# remove data from dict

result = dict4.popitem()
print(result)

result2 = dict3.popitem()
print("result2 :", result2) #  ('e', 456)
print("dict3 :", dict3)
# dict3 : {'a': 500, 'b': 456, 'c': 600}

print("_"*50)
################################ Set ########################
set1 = {3, 'c', 7, 'a', 'b', 8, 2, 7, 'a', 9, 3}
print("set1 :", set1)


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

############################# Boolean ################
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