###
#Int--> Float, String, boo

n2=55
f1 = float(n2)
print(f1,type(f1))

#Int --> String
n3=2333
s2 = str(n3)
print(s2, type(s2), s2[0],s2[1],s2[2])

#Int cannot be converted to List, set, dictionary , tupple ( not iterable)

#Int - Boolean (Any non zero value is true)
s2 = 0
s3 = bool(s2)
print(s3 , type(s3))

#float to String

F1=2345
S1 = str(F1)
print(S1, type(S1), S1[3])

#float to int(only considers whole number)
F1=2345.23
I1=int(F1)
print(I1,type(F1),type(I1))

#float to boolean(Any non zero value is true)
B1=bool(I1)
B2=0
B3 = bool(B2)
print(B1,B3,type(B1),type(B3),type(B2))

#String into Integer (cannot contain string to integers when has charachters/can be done when numbers)
X1= "123"
X2= str(X1)
X3= int(X2)
print(X3*2,type(X3),type(X2))

#String to float
X4= float(X1)
print(X4,type(X4))

#String to boolean
X6 = str (X4)
X5 = bool(X6)
print(X5,type(X5))

#Lists
#List to Int and float not possible.
#List to dictionary not possible


#List to string(brackets, commas are all strings. so the space of each item will be considered)
L1 = [1,2,-4]
S1 = str(L1)
print(S1,type(L1),type(S1),S1[3], S1[-3])

#List to tuple
T1= tuple(L1)
print(T1,type(T1))

#List to dictionary is possible when 2 lists are present with zip function

L1 = [1,2,3]
L2 = ['a','b','c']
L3 = []
print(list(zip(L2,L1)))
result = dict(zip(L2,L1))
print(result,type(result))


#List to Set

s1=set(L2)
print(s1,type(s1))

#list to boolean
B1 = bool(L3)
B2 = bool(L1)
print(B1,B2)

#tuple to integer and float conversion not possible

#tuple to string
t1= (1,2,3,4)
S1 = str(t1)
print(S1,type(S1),S1[-1])

#tuple to list
l1=list(t1)
print((l1,type(l1)))

#tuple to dic not possible unless zip
t1 = ('a','b','c')
t2 = (1,2,3)
t3= tuple(zip(t1,t2))
print(t3)
d1= dict(t3)
print(d1,d1['a'])












