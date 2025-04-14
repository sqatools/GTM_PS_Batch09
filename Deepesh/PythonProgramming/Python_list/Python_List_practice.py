list1 = [2, 3.5, 'Hello', [1, 2, 3], (3, 5, 7), {'a': 123}, {4, 6, 8}, True]

print(list1, type(list1))
# [2, 3.5, 'Hello', [1, 2, 3], (3, 5, 7), {'a': 123}, {8, 4, 6}, True] <class 'list'>

print("_"*50)
list2 = ['a', 'b', 'c', 'd']
# apply loop on list value
for val in list2:
    print(val*2)
"""
aa
bb
cc
dd
"""


print("_"*50)
list3 = ['a1', 'b1', 'c1', 'd1']
# apply loop on list with index
list_length = len(list3)
print("list length :", list_length)

for i in range(list_length):
    print(i,  list3[i], list3[i]*3)

"""
list length : 4
0 a1 a1a1a1
1 b1 b1b1b1
2 c1 c1c1c1
3 d1 d1d1d1
"""

print("_"*50)
##############################################
# write a python program to get all the values list which divisible by
list4 = [5, 7, 9, 10, 3, 15]
for val in list4:
    if val%5 == 0:
        print(val)

"""
5
10
15
"""

print("_"*50)
##################### Slicing in List ######################
list5 = [4, 6, 8, 12, [3, 6, 8], 5, 15]

print(list5[4]) # [3, 6, 8]
print(list5[4][1]) # 6
print(list5[0:4])  # [4, 6, 8, 12]
print(list5[-2:-5:-1]) # [5, [3, 6, 8], 12]
print(list5[::2])  #  [4, 8, [3, 6, 8], 15]
print(list5[-4:-8:-1]) # [12, 8, 6, 4]
print(list5[3::-1]) # [12, 8, 6, 4]
print(list5[::-1]) # [15, 5, [3, 6, 8], 12, 8, 6, 4]





print("_"*50)
##################### List Methods #################
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

n1 = [5, 6]
n2 = [7, 8]
print(n1+n2)
print(n1.__add__(n2))

print("_"*50)
########### Add data to the list ########
# append() method :  This method add data to the list at the end of list
list_a = [5, 7, 9, 12]
list_a.append(100)
print("list_a :", list_a)
list_a.append(500)
print("list_a :", list_a)


print("_"*50)
##############################
# insert() method:  This method add data to the list, at specified indexing position.

list_b = [5, 7, 9, 12, 5, 17, 8]
list_b.insert(2, "Hello")
print("list_b :", list_b)
# [5, 7, 'Hello', 9, 12, 5, 17, 8]

list_b.insert(0, "Python")
print("list_b :", list_b)
# ['Python', 5, 7, 'Hello', 9, 12, 5, 17, 8]

list_b.insert(-2, "Programming")
print("list_b :", list_b)
# list_b : ['Python', 5, 7, 'Hello', 9, 12, 5, 'Programming', 17, 8]


# listc = [4, 6, 78]
# print(listc.append(30))
# print(listc)


print("_"*50)
##############################
# extend() method :  This method add data from one list to another list.
list_d = [5, 6, 8, 9]
list_e = ['a', 'b', 'c', 'd']
list_e.extend(list_d)
print("list e :", list_e)
list_f = [4, 6, 7]
list_f.append(list_d)
print("list_f :", list_f)
# [4, 6, 7, [5, 6, 8, 9]]


print("_"*50)
##############################
# list concatenation :  we can add two lists data and create another list

list_g = [55, 77, 88, 'Hello']
list_h = [11, 12, 13, 4.5]

result = list_g + list_h
print("result :", result) # [55, 77, 88, 11, 12, 13]
print("list g:", list_g) # [55, 77, 88]
print("list h:", list_h) # [11, 12, 13]


print("_"*50)
##############################
# list multiplication : we can repeat the all list values n number time, when multiple list
# with any number

list_i = [3, 6, 'a', 'b']
result = list_i*4
print("result :", result)
# [3, 6, 'a', 'b', 3, 6, 'a', 'b', 3, 6, 'a', 'b', 3, 6, 'a', 'b']

print("_"*50)
####################### Remove data from list ####################
# remove() method: This method remove any specific value from given and if value is repeated
# multiple time, then it will remove first occurrence of the value.

list_j = [5, 7, 9, 'a', 'b', 'c', 5, 7]
list_j.remove(7)
print("list j :", list_j)
# list j : [5, 9, 'a', 'b', 'c', 5, 7]

list_j.remove('b')
print("list j :", list_j)
# list j : [5, 9, 'a', 'c', 5, 7]


print("_"*50)
#######################
# pop() method :  This method remove value from specified index position and return it.
#                -> The default index position is -1

list_k = [44, 66, 77, 1, 4, 'a', 'b']

# remove value from default index -1
val = list_k.pop()
print("removed value :", val) # removed value : b
print("list_k:", list_k) # [44, 66, 77, 1, 4, 'a']

# remove from specified index
val2 = list_k.pop(2)
print("removed value :", val2) # removed value : 77
print("list_k:", list_k) # [44, 66, 1, 4, 'a']

print("_"*50)
#######################
# clear() method :  This method remove all the data from list, and only empty list will remain.
list_l = [55, 7, 1, 17, 8]
list_l.clear()

print("list_l :", list_l)
list_l : []

print("_"*50)
#######################
# del keyword : this keyword remove entire variable from memory.

list_m = [4, 6, 8, 22, 55, 11, 45]
del list_m
# print("list_m:", list_m)
# NameError: name 'list_m' is not defined


# remove specific number of element from list
list_n = [4, 6, 8, 22, 55, 11, 45]
del list_n[2:4]
print("listn :", list_n) # [4, 6, 55, 11, 45]

del list_n[-3]
print("listn :", list_n) # [4, 6, 11, 45]
