'''a = 20
# a : variable
# = : assignment operator
# 10 : value to store'''

a=10
b=20
print(a,"_"*10,b)

print("print id a:", id(a))
print("print id b:", id(b))

'''# Address of variable
print(id(a))  # 140719858076376
# print : in-built function :  print function shows the output on console
# id : in-build function : that return the memory address of variable

print("Hello world") # Hello world
print("value of a :", a) # value of a : 20
print(a)

p = 30
q = 40
r = 50
print(p, q, r)'''


p = 51
q = 5
r = 52
print(p,q,r)
print("id of pqr:",id(p),"\n",id(q),"\n",id(r)) ## if multiple variables with same value then their address is also same


'''#######################################
# if multiple variables with same value then their address is also same
x = 50
y = 50


print("address of x:", x, id(x)) # address of x: 50 140719814561752
print("address of y:", y, id(y)) # address of y: 50 140719814561752
x = 100
print("address of x:", x, id(x)) # address of x: 100 140719814563352

#################################
# assign multiple value to multiple variable at a time
P, Q, R  = 40, 50, 60
print("Value P :", P)  # Value P : 40
print("Value Q :", Q)  # Value Q : 50
print("Value R :", R)  # Value R : 60
'''
A,B,C= 0.1, --3, +40

print(A,B,C)

'''####################################
# Assign one value to multiple variables

X = Y = Z = 100
print("value X :", X, id(X)) # value X : 100 140719858079256
print("value Y :", Y, id(Y)) # value Y : 100 140719858079256
print("value Z :", Z, id(Z)) # value Z : 100 140719858079256'''

A=B=C=200
print(A,B,C)

'''###############################################
# Rules to defined variable name
# -> 1. Variable name should not contain space in name.
#a d c = 50 : invalid
abc = 50 # valid
a_b_c = 60 # valid

# 2. Can not start variable name with numbers.
# 1_var = 60 : invalid
var_1 = 70 # valid
abc_123_pqr = 40 # valid

# 3. There is no limit for variable name length
abc_xyz_pqr_hello_python = 40 # valid

# 4. Can not contain special character in variable name except underscore
# var_1$* = 700 : invalid
var_123 = 600 # valid

var5676789 = 'Python' # valid

# 5. Variable names are case-sensitive.

Name = 'Rahul'
NAME = 'Mohan'
nAME = 'Mohit'
name = 'Ravi'
naME = 'Aditya'

print(" Name :", Name)
print("NAME :", NAME)
print("nAME :",nAME)
print("name :", name)
print("name :", naME)

"""
Math operation on variables

+ :  plus operator
- :  subtraction
* :  multiplication
/ and // : division
== :  equal to operator
!= : not equal to
** : power operator
%  : remainder operator
"""

print("_"*50)
### addition of values ###
num1 = 40
num2 = 50
num3 = num1 + num2
print("addition :", num3)
print("addition2 :", num1+ num2)

### multiplication of values ##
var1 = num1*num2
print("multiplication :", var1)

### subtraction of values###
print("subtraction :", 500 - num1)


#### division #####
v1 = 50
v2 = 3

# when we divide number with single /, then it return the pointer output.
print("division with single / :", v1/v2) # 16.666666666666668

# When we divide number with double //, then it returns the whole value without pointer
print("division with double // :", v1//v2) # 16

#### get square and cube of given number ####
n1 = 5

print("square of value :", n1**2) # square of value : 25
print("cube of value :", n1**3) # cube of value : 125

#### get remainder value ###########
v2 = 20
v3 = 3
print("remainder value :", v2%v3)  # remainder value : 2

#### compare 2 values ####
p1 = 40
p2 = 50
p3 = 40

print(p1 == p2)  # False
print(p1 == p3)   # True
print(id(p1) == id(p3)) # True
print(p1 != p2)  # True


print("_"*50)
########################
"""
1.  (a+b)^2 = a^2 + b^2 + 2ab
2.  (a-b)^2 = a^2 + b^2 - 2ab

"""
#  (a-b)^2 = a^2 + b^2 - 2ab
a = 4
b = 7
lhs = (a-b)**2
print("LHS output  :", lhs)

rhs = a**2 + b**2 - 2*a*b

print("RHS output :", rhs)

####################################
# calculate simple interest
P = 20000
r = 8
t = 5
A = (P*t*r)/100
# P = principal amount
# r = rate of interest
# t = time in a years

print("Simple interest :", A) # 8000.0
'''