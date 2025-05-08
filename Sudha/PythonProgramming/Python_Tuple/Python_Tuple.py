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
    print(i,tup2[i])

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
 # (5, 2, 9, 56)
# (12, 56)
 # (56, 12, 9, 6, 2, 8, 5)
 # (56, 12, 9, 6, 2, 8, 5)