a=10
print(a)  # it will print the value of a
print(id(a)) #it will print the addres "a" value
##############################
a=10
b=10
print(a,b)
print(id(a),id(b)) # here a and b are sharing the same memory bcz both variable having the same value

###############################
a,b=10,20  # here 10 value assigning to the a and 20 assigning to b
print("value of a is =",a)
print("value of b is =",b)
print(id(a),id(b))  # here both a and b sharing the different memory

###############################
a=b=c=10     # here a,b and c having the same value
print(a,b,c)
print(id(a),id(b),id(c)) # whenever we are assinging same value to the multiple variables address will be same

#################################

x=10
print(id(x))
x=30
print(x) # here latest x value will print
print(id(x)) # latest x value address will print

########################################

# Rules to defined variable name
# 1 variable name should not cantain space in between thr variable name ex = xx yy
# 2 variable should not the numbers ex= 1var
# 3 variable should not cantain the special characters
# 4 variable name are case sensitive ex = name, NAME,Name,nAmE,NAme all are same

Name = 'Basavaraja'
NAME = 'virat'
nAME = 'Aarvi'
name = 'Ravi'
naME = 'Aditya'

print("Name :", Name)
print("NAME :", NAME)
print("nAME :", nAME)
print("name :", name)
print("name :", naME)



print("#"*50)
#Math operation on variables
"""
+ :  plus operator
- :  subtraction
* :  multiplication
/ and // : division
== :  equal to operator
!= : not equal to
** : power operator
%  : remainder operator
"""
print("#"*50)
# ADDITION
a,b=10,20
c=a+b
print(c)

a=b=c=10
print(a+b+c)

# Subctration
a=20
b=10
c=a-b
print(c)

a,b=30,40
print(b-a)

# MULTIPLICATION

a,b,c=2,3,5
c=a*b*c
print(c)

a=b=c=d=10
print(a*b*c*d)

# DIVISION

a=10
b=4
c=3

print(a/b)
print(a//c)

x,y,z=75,44,66
print(x/y)
print(x//y)
print(z/y)
print(z//y)

# equal ==
a,b=10,10
print(a==b)

a,b,c=10,10,20

print(a == b != c)
print(a == b == c)
print(a != c != b)

# ** power operator

a=10
b=2
print(a**2)

print(b**2)

# remainder  operator

a=10
b=2
print(10%2)
print(a%3)
print(a%4)
print(a%6)
print(a%7)
print(a%9)



