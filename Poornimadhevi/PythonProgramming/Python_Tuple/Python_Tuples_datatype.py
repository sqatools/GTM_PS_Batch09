tup1 = (4, 4.5, 'Hello', [4, 6, 7], (2, 6, 8), {'a': 123}, {4, 5, 7}, True)
print(tup1, type(tup1))
# (4, 4.5, 'Hello', [4, 6, 7], (2, 6, 8), {'a': 123}, {4, 5, 7}, True) <class 'tuple'>


print("_"*50)
# Apply loop on tuple values
tup2 = (5, 6, 8, 12, 45, 78)
for val in tup2:
    print(val)

"""
5
6
8
12
45
78

"""
print("_"*50)
# Apply loop on tuple with indexing
tup2 = (15, 6, 18, 12, 45, 78)

for i in range(len(tup2)):
    print(i, tup2[i])

"""
0 15
1 6
2 18
3 12
4 45
5 78
"""
print("_"*50)
###################### Slicing in the tuple ########################
# write a program to get values with the help of indexing.

tup3 =(5, 8, 2, 6, 9, 12, 56)

print(tup3[2:5])  # (2, 6, 9)
print(tup3[-2:-7:-1]) # (12, 9, 6, 2, 8)
print(tup3[0::2]) # (5, 2, 9, 56)
print(tup3[5:]) # (12, 56)
print(tup3[-1:-8:-1]) # (56, 12, 9, 6, 2, 8, 5)
print(tup3[::-1]) # (56, 12, 9, 6, 2, 8, 5)

print("_"*50)
############################# Methods in tuples ##########################
print(dir(tuple))

# 'count', 'index'

# count method : This method return total number occurrence of any particular value.

tup4 =(5, 8, 2, 6, 9, 12, 56, 5, 4, 2, 5, 6, 5)
print("count of 5 :", tup4.count(5))
# count of 5 : 4

# index method :  This method return the index position of any given value
print("Index of 56 :", tup4.index(56)) #
# Index of 56 : 6


########################
# del keyword :  through del we can delete entire tuple variable from memory.
tup5 = (5, 7, 9, 2)
del tup5

# print("tup5 :", tup5)
# NameError: name 'tup5' is not defined


print("_"*50)
# Repeat tuple values with multiplication with any number.
tup6 = (7, 9, 34, 56)
result = tup6*2
print("result :", result) # (7, 9, 34, 56, 7, 9, 34, 56)


print("_"*50)
#########################################
#Q1 write a python program to reverse the tuples values with the help while loop
tup_a = (3, 5, 7, 8, 'a', 'b')

output = []
n = -1
while n >= -len(tup_a):
    output.append(tup_a[n])
    n -= 1

# ('b', 'a', 8, 7, 5, 3)
print(tuple(output))

print("_"*40)
#Q2 : write a python to get following output
# compare both the tuple value, if both values are same, then keep it as it is in the output.
# If values are different than add both values.
tup_b = (5, 7, 8, 1, 4)
tup_c = (6, 7, 9, 1, 5)

#output = (11, 7, 17, 1, 9)
result = []


for i in range(len(tup_b)):
    if tup_b[i] == tup_c[i]:
        result.append(tup_b[i])
    else:
        result.append(tup_b[i]+tup_c[i])

print("Get result :", tuple(result))
# (11, 7, 17, H1, 9)

###################### Max, min, Sum of values #################
tup6 = (4, 6, 8, 12, 45, 78)
print("max value :", max(tup6))
print("min value :", min(tup6))
print("sum value :", sum(tup6))


######### write tuple comprehension ##########

# write a program to get square of all the values from given tuple with tuple comprehension.
# Note :  tuple comprehension return the generator object instead of tuple values directly
#         if want to get value in tuple
tup_x = (5, 7, 9, 2, 4)
square = tuple((x**2 for x in tup_x))
print(square) # (25, 49, 81, 4, 16)

# for val in square:
#     print(val)

# (25, 49, 81, 4, 16)

# Home work
# tuple comprehension: need to practice.py.
# 1. tuple comp with if condition
# 2. tuple comp with if and else condition.
# 3  tuple comp with nested loop.


# write a python program to generate given output :

str1 = "Hello we are Learning Python Program"
output = [('Hello', 5), ('we', 2), ('are', 3), ('Learning', 8), ('Python', 6), ('Program', 7)]
