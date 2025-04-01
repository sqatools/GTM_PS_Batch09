# Boolean
a = 10
b = 11
print (a==b)

#Integer , Float , String
d, e, f = 12, 13.2 , "Hello"
print (type(d))
print(type(e))
print(type(f))

# Multiply
print(f*5)

# ID of the list
print(id(d))
d=e
print(id(d))
print(id(e))


#Tuple
tup1 = (12 , 45 , 456, [2,3,4] , "Hello")
print(tup1[3])
print(tup1[-4])
print(tup1[-1])
print(tup1[3][0])

#Dictionary
dict1 = {'name':'shrinidhi', 'age': '37', 'gender' : 'female' }
print(dict1['name'])
print(dict1['age'])
print(dict1['gender'])
print(dict1.popitem())
print(dict1.popitem())
print(dict1.popitem())

#Set
Set1 = {1,3, 6 , 'c', 'd', 'e', 'x', 7, 'x'}
print(type(Set1), Set1)
Set1.add(100)
print(type(Set1), Set1)

print(Set1)

# Boolean
n1=10
n2=40
n3=50
print (n1==n2)
print(n1==n1)





