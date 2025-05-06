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
# write a python program to get all the values list which divisible by 5
list4 = [5, 7, 9, 10, 3, 15]
for i in list4:
    if i % 5 == 0:
        print(i)
    else:
        continue
"""
5
10
15
"""

print("_"*50)
##################### Slicing in List ######################
list5 = [4, 6, 8, 12, [3, 6, 8], 5, 15]

print(list5[4]) # [3, 6, 8]
print(list5[4][1])# 6
print(list5[:4])  # [4, 6, 8, 12]
print(list5[-2:-5:-1]) # [5, [3, 6, 8], 12]
print(list5[::2])  #  [4, 8, [3, 6, 8], 15]
print(list5[-4::-1]) # [12, 8, 6, 4]
print(list5[3::-1])# [12, 8, 6, 4]
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
list_a.append(500)
print(list_a)
list_a.append(99)
print(list_a)

print("_"*50)
##############################
# insert() method:  This method add data to the list, at specified indexing position.

list_b = [5, 7, 9, 12, 5, 17, 8]
list_b.insert(2,"Hello")
print(list_b)
#[5, 7, 'Hello', 9, 12, 5, 17, 8]

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
print(list_e)
list_f = [4, 6, 7]
#list_f.extend(list_d)
list_f.append(list_d)
print(list_f)

list_g = [55, 77, 88, 'Hello']
list_h = [11, 12, 13, 4.5]

result = list_g + list_h
print("List concatenation : ",result)
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
print(list_j)
# list j : [5, 9, 'a', 'b', 'c', 5, 7]

list_j.remove('b')
print(list_j)
#[5, 9, 'a', 'c', 5, 7]

print("_"*50)
#######################
# pop() method :  This method remove value from specified index position and return it.
#                -> The default index position is -1

list_k = [44, 66, 77, 1, 4, 'a', 'b']

# remove value from default index -1
list_k.pop()
print(list_k)
#[44, 66, 77, 1, 4, 'a'] pop default index is -1, so removed -1 index value b

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
#list_l : [] list is empty

print("_"*50)
#######################
# del keyword : this keyword remove entire variable from memory.

list_m = [4, 6, 8, 22, 55, 11, 45]
del list_m
#print("list_m:", list_m), throws an error because list_m is deleted from memory
# NameError: name 'list_m' is not defined


# remove specific number of element from list
list_n = [4, 6, 8, 22, 55, 11, 45]
del list_n[2:4]
print("list n:",list_n)#[4, 6, 55, 11, 45]
del list_n[-3]
print("listn :", list_n) # [4, 6, 11, 45]


print("_"*50)
########################
# replace data in the list

list_p = [4, 66, 22, 77, 11, 34]
list_p[0] = 99
print(list_p)#[99, 66, 22, 77, 11, 34]

# replace multiple values
list_p[2:5] = [100, 200, 300]
print("list_p :", list_p)
# [400, 66, 100, 200, 300, 34]

print("_"*50)
########################
# index method : This method return the index position of any specific element.
#                ->  If the value is repeated  multiple times, then first value index will be
#                    return as output.

list_q = ['a', 'b', 'c', 'd']
print("Index of c : ", list_q.index('c'))#Index of c :  2

print("_"*50)
########################
# count() method : Count method return the number of occurrences of any particular value.
list_r = ['a', 'b', 'c', 'd', 'a', 'b', 'a', 'd']
print("No of a : ", list_r.count('a'))
#No of a :  3
print("No of values in list_r : ", len(list_r))
#No of values in list_r :  8

print("_"*50)
########################
# sort method() : sort method, do sorting of given list values and modify the original list
                  # sort method can sort the list in ascending and descending order.

list_s = [5, 1, 6, 9, 23, 12]

# ascending order sorting
list_s.sort()
print("list_s ascending order : ",list_s)
#list_s ascending order :  [1, 5, 6, 9, 12, 23]

list_s.sort(reverse=True)
print("list_s descending order : ", list_s)
#list_s descending order :  [23, 12, 9, 6, 5, 1]

print("_"*50)
########################
# sorted function() : sorted function sort the list values in ascending and descending order
#                     and return as result, it does not modify the original list


list_t = [15, 11, 16, 19, 23, 33, 19,  43, 21]
result1 = sorted(list_t)
print(result1)
#[11, 15, 16, 19, 19, 21, 23, 33, 43]

result2 = sorted(list_t, reverse=True)
print(result2)
#[43, 33, 23, 21, 19, 19, 16, 15, 11]

list_x = ['hello', 'Python', 'Apple', 'Mango']
result3 = sorted(list_x)
print(result3)

# ['Apple', 'Mango', 'Python', 'hello'] for alphabets sorting based on ASCII values

print("_"*50)
########################
# reversed function() :  This function reverse the list values and return as result, does not
#                        modify original list

list_22 = [33, 6, 8, 12, 56, 89, 234]
result2 = list(reversed(list_22))
print(result2)#[234, 89, 56, 12, 8, 6, 33]

print("list_22 :", list_22)
# [33, 6, 8, 12, 56, 89, 234]


print("_"*50)
##############################
# copy method in list

# shallow copy: when we assign one list value to another list, then we will create reference
#               list data, If we modify any of the list, then changes will reflect on both the
#               list.

list1 = [4, 6, 8, 12, 56]
list2 = list1
list2.append(200)
list1.append(100)

list1.remove(6)
print("List1", list1)
print("list2",list2)

#List1 [4, 8, 12, 56, 200, 100]
#list2 [4, 8, 12, 56, 200, 100]

print("_"*50)
# Deep Copy : when we copy data from one list to another, then it is called deep copy.
#             if we modify any of the list value then changes will reflect in same list only.

list_x = [5, 7, 9, 22, 445, 6]
list_y = list_x.copy()

list_x.append(100)
list_y.append(200)
print("list_x :", list_x) # [5, 7, 9, 22, 445, 6, 100]
print("list_y :", list_y) # [5, 7, 9, 22, 445, 6, 200]

print("_"*50)
################## Max value, Min value and Sum of the list ##################
list_r = [44, 66, 88, 2, 4, 6]

print("Max value = ", max(list_r))#Max value =  88
print("Min value = ", min(list_r))#Min value =  2
print("Sum of the list = ", sum(list_r))#Sum of the list =  210

print("_"*50)
######################### List Comprehension ####################

list_u = [6, 8, 2, 5, 7, 9, 12, 13]
# get all even values
for val in list_u:
    if val%2 == 0:
        print(val, end=" ")


print()

# solve same problem with list comprehension
# list comprehension return result in the list data type.
result4 = [x for x in list_u if x % 2 == 0]
print(result4)

print("_"*40)
# write a python list comprehension to get below result
list2 = [5, 7, 9, 12, 6]
output = [(5, 'odd'), (7, 'odd'), (9, 'odd'), (12, 'even'), (6, 'even')]

result = [(val, 'even') if val%2 == 0 else (val, 'odd') for val in list2]
print(result)

print("_"*40)
# nested loop with list comprehension
result2  = [(x, y) for x in ['a', 'b', 'c'] for y in ['P', 'Q']]
print(result2)
# [('a', 'P'), ('a', 'Q'), ('b', 'P'), ('b', 'Q'), ('c', 'P'), ('c', 'Q')]


result3  = [(x, y) for x in ['add1', 'add2', 'add3'] for y in ['Item1', 'Item2']]
print(result3)
# [('add1', 'Item1'), ('add1', 'Item2'), ('add2', 'Item1'), ('add2', 'Item2'), ('add3', 'Item1'), ('add3', 'Item2')]

