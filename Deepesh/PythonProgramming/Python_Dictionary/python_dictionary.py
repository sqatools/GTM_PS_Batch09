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
