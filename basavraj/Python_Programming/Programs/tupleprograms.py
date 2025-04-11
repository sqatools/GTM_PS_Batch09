#1). Python tuple program to create a tuple with 2 lists of data.
"""Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
Output= ((4, 7), (6, 1), (8, 4))
"""
print("program 1")
list1 = [4, 6, 8]
list2 = [7, 1, 4]
list3=tuple(zip(list2,list2))
print(list3)
print("-"*50)

#2). Python tuple program to find the maximum value from a tuple.
#Input = (41, 15, 69, 55)
#Output = 69
print("program 2")
t=(41, 15, 69, 55)
# print(max(t))
maxx=t[0]
for i in t:
    if i>maxx:
        maxx=i
print(maxx)
print("-"*50)
#3). Python tuple program to find the minimum value from a tuple.
#Input = (36,5,79,25)
#Output = 5
print("program 3")
t1=(36,5,79,25)
print(min(t1))
print("-"*50)

#4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
#Input = [4,6,3,8]
#Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
print("program 4")
input_list = [4, 6, 3, 8]
output = [None] * len(input_list)  # Pre-allocate list size
index = 0

for i in input_list:
    tup = (i, i * i)
    output[index] = tup
    index += 1

print(output)

list1 = [4,6,3,8]

tup = [(val, pow(val, 2)) for val in list1]
print(tup)
print("-"*50)
#5). Python tuple program to create a tuple with different datatypes.
print("program 5")
tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
print("Tuple: ",tup)
print("-"*50)

#6). Python tuple program to create a tuple and find an element from it by its index no.
print("program 6")
t1= (4, 8, 9, 1)
print(t1[1])
print("-"*50)

#7). Python tuple program to assign values of tuples to several variables and print them.
print("program 7")
t1=(1,2,3)
(a,b,c)=t1
print(a,b,c)
print("-"*50)
#8). Python tuple program to add an item to a tuple.
print("program 8")
tup = (18,65,3,45)
print("Old tuple: ",tup)
tup = list(tup)
tup.append(15)
tup = tuple(tup)
print("New tuple: ",tup)
print("-"*50)
#9). Python tuple program to convert a tuple into a string.
print("program 9")
str1=('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
res=""
for char in str1:
    res=res+char
print(res)
print("".join(str1))
print("-"*50)
#10). Python tuple program to get the 2nd element from the front and the 3rd element
# from the back of the tuple.
#Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
#Output= q o
print("program 10")
str1=('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
print(str1[1],str1[-3])
print("-"*50)

#11). Python tuple program to check whether an element exists in a tuple or not.
print("program 11")
tup = ('p','y','t','h','o','n')
if 'p' in tup:
    print("True")
else:
    print("False")

print("-" * 50)
#12). Python tuple program to add a list in the tuple.
print("program 12")
L=[12,67]
A=(6,8,4)
t1=tuple(L)
print(t1+A)
print("-" * 50)
#13). Python tuple program to find sum of elements in a tuple.
print("program 13")
A=(4,6,2)
s=0
for i in A:
    s=s+i

print(s)
print("-" * 50)

#14). Python tuple program to add row-wise elements in Tuple Matrix
"""Input:
A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
B = (3,6)
Output:
[[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]
"""
print("program 14 doubt")
print("-" * 50)

