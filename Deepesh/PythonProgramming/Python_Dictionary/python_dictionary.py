from pprint import pprint

dict1 = {'Name': 'john', 'age': 45}
print(dict1, type(dict1))


"""
# dict properries.
->  dict is mutable data type
-> dict only contain unique keys.
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


print("_"*50)
# Add mutable data type as key
dict_3 = {'a': 5, 'b': 7, 'c': 8, 'd': 23, 'e': 12, 'f': 6}
# dict_3[[4, 6, 7]] = 'Python'
# print("dict3 :", dict3)
# TypeError: unhashable type: 'list'


dict4 = {
    123: "Python",
    34.6 : [5, 7, 9, 23],
    'Hello': (5, 7, 9, 23),
    (1, 2, 3) : (5, 7, 8, 22),
    True :  (5, 7, 8, 22, 34, 45)

}
print("_"*40)
print("dict 4 :", dict4)

pprint(dict4)

print("_"*40)
print(dict4[(1, 2, 3)]) # (5, 7, 8, 22)


