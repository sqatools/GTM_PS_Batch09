# my_list = [2, 3.5, 'Hello', [1, 2, 3], (3, 5, 7), {'a': 123}, {4, 6, 8}, True]
#
# print(my_list, type(my_list))
# [2, 3.5, 'Hello', [1, 2, 3], (3, 5, 7), {'a': 123}, {8, 4, 6}, True] <class 'list'>

print("_"*50)
# my_list = ['a', 'b', 'c', 'd']
# # apply loop on list value
# for l in my_list:
#     print(l*2)

# apply loop on list with index
my_list1 = [" hello ", 2, 4, 5, 10, " what's up ", 2.8]
for i in range(len(my_list1)):
    print(i, my_list1[i], my_list1[i]*3)

print("_"*50)
##############################################
# # write a python program to get all the values list which divisible by
#
# num_list = [2, 4, 5, 6, 8, 10]
# for num in num_list:
#     if num%5 == 0:
#         print(num)
#
#
# print("_"*50)
# ##################### Slicing in List ######################
#
# slice = [6, 9, 6, [8, 7, 3], 2, 3]
# print(slice[1])
# print(slice[1:-3])
# print(slice[:3])
# print(slice[3:])

#print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
list1 = [10, 3, 7]
list2 = [4, 6, 9]
print(list1.__add__(list2))

print("_"*50)
########### Add data to the list ########
# append() method :  This method add data to the list at the end of list

my_list = [20, 10, 40]
my_list.append(85)
print(my_list)
my_list.append(110)
print(my_list)

print("_"*50)
##############################
# insert() method:  This method add data to the list, at specified indexing position.

# insert_num = [7, 8, 4, 9]
# insert_num.insert(1, "hello")
# insert_num.insert(-1, "home")
# print(insert_num)

print("_"*50)
##############################
# extend() method :  This method add data from one list to another list.
str_list = ["jojo","coka cola","fish"]
num_list = [8, 4, 3, 7]
str_list.extend(num_list)
str_list.append(num_list)
print(str_list)

print("_"*50)
##############################
# list concatenation :  we can add two lists data and create another list
# list1 = [6, 8, 9, "yad"]
# list2 = ["a", "b", "c"]
# full_list = list1 + list2
# print(full_list)
#
# print("_"*50)
# ##############################
# # list multiplication : we can repeat the all list values n number time, when multiple list
# # with any number
#
# multi_list = [2, 4, 6, 8, 10]
# print(multi_list*3)

####################### Remove data from list ####################
# remove() method: This method remove any specific value from given and if value is repeated
# multiple time, then it will remove first occurrence of the value.

duplicate_list = [10, 9, 3, 10, 5, 3]
print(duplicate_list)
duplicate_list.remove(10)
duplicate_list.remove(3)
print(duplicate_list)


print("_"*50)
#######################
# pop() method :  This method remove value from specified index position and return it.
#                -> The default index position is -1






