print(dir(tuple))

# 1 Python tuple program to create a tuple with 2 lists of data.
#Output= ((4, 7), (6, 1), (8, 4))
list1 = [4, 6, 8]
list2 = [7, 1, 4]

tup=(tuple(zip(list1,list2)))
print(tup)
print("-"*60)
# 2 Python tuple program to find the maximum value from a tuple.
#Output = 69
tup = (41, 15, 69, 55)
print("maximum value of tuple is:",max(tup))
print("-"*60)
# 3 Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
#Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
tup1=[4,6,3,8]

list =[(val, pow(val,2)) for val in tup1]
print(list)
print("-"*50)
# 4 Python tuple program to create a tuple with different datatypes.
#Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})
tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
print("Tuple: ",tup)
print("-"*50)
# 5 Python tuple program to convert a tuple into a string.
tup2 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
#Output = Sqatools
for word in tup2:
    print(word,end="")
print("-"*60)
# 6 Python tuple program to create a tuple having squares of the elements from the list.
#Output = (1, 81, 25, 49, 36)
tup3 = [1, 9, 5,  7, 6]
squares=tuple(x**2 for x in tup3)
print(squares)
print("-"*60)
# 7 Python tuple program to multiply adjacent elements of a tuple.
#Output =  (2,6,12)
tup4 = (1,2,3,4)
for val in tup4:
    print(val*val)

print("-"*50)
# 8 Python tuple program to convert a list into a tuple and multiply each element by 2.
tup5 = [12,65,34,77]
#Output = (24, 130, 68, 154)

multiply=tuple(val*2 for val in tup5)
print(multiply)
print("-"*50)
# 9 Python tuple program to find the length of a tuple.
tup6=('v','i','r','a','t')
print("length of tup6:",len(tup6))

print("-"*60)
# 10 Python tuple program to convert a tuple into a dictionary.
tup7=((5,'s'),(6,'l'))
#Output = { s: 5, l: 6 }
D=dict(tup7)
print("Dictionary: ",D)
# 11 Python tuple program to convert a list of tuples in a dictionary.
tup8 = [ ('s', 2), ('q', 1), ('a', 1), ('s', 3), ('q', 2), ('a', 4) ]
#Output ={ s: [ 2, 3 ], q: [ 1, 2 ], a: [ 1 ,4 ] }
D={}
for k,v in tup8:
   D.setdefault(k,[]).append(v)
print(D)