from pprint import pprint

dict1 = {'Name': 'john', 'age': 45}
print(dict1, type(dict1))

"""
# dict properries.
->  dict is mutable data type
->  dict only contain unique keys.
->  duplicate values are allowed.
->  only immutable data type can key in the dict, int, float, string, set, bool.
->  
"""

list1 = [5, 7, 8, 23, 12, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
result = dict(zip(list2, list1))
print("result:", result)
# {'a': 5, 'b': 7, 'c': 8, 'd': 23, 'e': 12, 'f': 6}


# add data to dict
dict_2 = {'a': 5, 'b': 7, 'c': 8, 'd': 23, 'e': 12, 'f': 6}
dict_2['g'] = 200
print("dict2 :", dict_2)
# {'a': 5, 'b': 7, 'c': 8, 'd': 23, 'e': 12, 'f': 6, 'g': 200}


print("_" * 50)
# Add mutable data type as key
dict_3 = {'a': 5, 'b': 7, 'c': 8, 'd': 23, 'e': 12, 'f': 6}
# dict_3[[4, 6, 7]] = 'Python'
# print("dict3 :", dict3)
# TypeError: unhashable type: 'list'


dict4 = {
    123: "Python",
    34.6: [5, 7, 9, 23],
    'Hello': (5, 7, 9, 23),
    (1, 2, 3): (5, 7, 8, 22),
    True: (5, 7, 8, 22, 34, 45)

}
print("_" * 40)
print("dict 4 :", dict4)

pprint(dict4)

print("_" * 40)
print(dict4[(1, 2, 3)])  # (5, 7, 8, 22)

print("_" * 50)
##########################################
# apply loop on dictionary

dict1 = {'a': 123, 'b': 456, 'c': 789}

for k1, v1 in dict1.items():
    print(k1, ":", v1)

print("_" * 50)
print(dict1.items())  # dict_items([('a', 123), ('b', 456), ('c', 789)])

################## Show dict data ############
print("_" * 50)
dict2 = {'a': [{'Pune': {
    'Fav_Food': 'misal pav', 'historic place': 'shanirwada'
}}, {'Mumbai': {
    'Fav_Food': 'Vada Pav', 'historic place': 'Gateway of India'
}}, 'Chennai'],
    'b': ['India', 'China', 'USA'],
    'c': {'name': 'john', 'phone': 2342343, 'email': 'john123@gmail.com'}
}

print(dict2['c'])
print(dict2['c']['email'])
print(dict2['a'][1]['Mumbai']['Fav_Food'])

############################ Methods In dictionary ##################

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


dict_x = {'a': 123, 'b': 456, 'c': 556}

# add new value to dict
dict_x['d'] = 5566
print(dict_x)
# {'a': 123, 'b': 456, 'c': 556, 'd': 5566}

#######add data from one dict to another dict.##############
dict_y = {'a': 123, 'b': 456, 'c': 556}
dict_z = {'P': 444, 'Q': 555, 'R': 879}

dict_z.update(dict_y)

print("dict_z :", dict_z)

print("_" * 50)
############# Remove data from dictionary.################

# pop method : This method remove data from dictionary using and update the dictionary.
#              and return the value.
dict_P = {'P': 444, 'Q': 555, 'R': 879, "S": 567}

removed_value = dict_P.pop('R')
print(dict_P, "|", removed_value)
# {'P': 444, 'Q': 555, 'S': 567} | 879


print("_" * 50)
#####################################
# popitems() method :  This method will data from dictionary in key value combination
#                    and return removed values in form tuple


dict_Q = {'P': 444, 'Q': 555, 'R': 879, "S": 567, 'T': 444}
var1 = dict_Q.popitem()
print("removed value :", var1)  # ('T', 444)
print("dict_q :", dict_Q)  # {'P': 444, 'Q': 555, 'R': 879, 'S': 567}



print("_" * 50)
#####################################
# clear() method :  clear method remove all the data from dict.

dict_R = {'P': 444, 'Q': 555, 'R': 879, "S": 567, 'T': 444}
dict_R.clear()
print("dict_R :", dict_R)
# dict_R : {}

print("_" * 50)
#####################################
# del keyword :  del keyword will remove entire dict variable from memory.

dict_5 = {'P': 444, 'Q': 555, 'R': 879, "S": 567, 'T': 444}
del dict_5
#print("dict5 :", dict_5)
#NameError: name 'dict_5' is not defined

# remove specific value with the help of del keyword.

dict_6 = {'P': 444, 'Q': 555, 'R': 879, "S": 567, 'T': 444}
del dict_6['R']
print(dict_6)
# {'P': 444, 'Q': 555, 'S': 567, 'T': 444}


print("_" * 50)
#####################################
# copy method :

# shallow copy :

dict_a = {'a': 123, 'b': 567, 'c': 132}
dict_b = dict_a
dict_b['E'] = (5,7, 8)

print("dict_a :", dict_a)
print("dict_b :", dict_b)

# deep copy:
print("_"*50)
# deep copy :

dict_J = {'a': 123, 'b': 567, 'c': 132}
dict_k = dict_J.copy()
dict_k['d'] = 1000

print(dict_J, dict_k)


print("_"*50)
###################################################
users = {'Names': ['rahul', 'rohit', 'ram'],
         'citys' : ['Pune', 'Mumbai', 'Bangalore'],
         'phone' : [345345456, 45435435, 4543543534]
         }


print(users)

users[('a','b', 'c')] = [345, 678, 234]
print(users)

print("_"*50)
####################################
# fromkeys() method :  fromkeys method help to create a dictionary of list of key and consider a
# single for all the keys.

result = dict.fromkeys(['a', 'b', 'c'], 600)
print("result :", result)
# {'a': 600, 'b': 600, 'c': 600}

print("_"*50)
####################################
# setdefault method(): set default method update dictionary with new key if it is not available
#                      -> If key is available then return the existing value.
dict_z  = {'a': 123, 'b': 567, 'c': 132, 'd': 456, 'e': 700}

# Update dictionary with new key and data value
result = dict_z.setdefault('f', 500)
print(result) # 500
print("dictz:", dict_z)
# {'a': 123, 'b': 567, 'c': 132, 'd': 456, 'e': 700, 'f': 500}

# get existing key data from dictionary
result2 = dict_z.setdefault('c', 600)
print("existing value of c :", result2) # 132
print("dictz:", dict_z)
# {'a': 123, 'b': 567, 'c': 132, 'd': 456, 'e': 700, 'f': 500}

print("_"*50)
###################### dict comprehension ##############

dict_A = {'a': 5, 'b': 6, 'c': 7}
print(dict_A['a'])
print(dict_A.items())  # dict_items([('a', 5), ('b', 6), ('c', 7)])

result = { k:dict_A[k]**2 for k in dict_A }
print(result)  # {'a': 25, 'b': 36, 'c': 49}

result2 = { k:v**2 for k, v in dict_A.items() }
print(result2)
# {'a': 25, 'b': 36, 'c': 49}

print("_"*50)
###################################################
# If condition dict comprehension.
# get square of only even values
dict_B = {'a': 5, 'b': 6, 'c': 7, 'd': 23, 'e': 14, 'f': 8}

result3 = {k:v**2 for k, v in dict_B.items() if v%2 == 0}
print("result3 :", result3)
# {'b': 36, 'e': 196, 'f': 64}


# get square of only even values and cube of odd values

result4 = dict([(k,v**2) if v%2 == 0 else (k,v**3) for k, v in dict_B.items()])
print("result 4:", result4)
# {'a': 125, 'b': 36, 'c': 343, 'd': 12167, 'e': 196, 'f': 64}
