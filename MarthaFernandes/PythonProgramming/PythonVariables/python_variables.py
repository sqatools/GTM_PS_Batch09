
a = 20
# a : variable
# = : assignment operator
# 10 : value to store


# Address of variable
print(id(a))  # 140719858076376
# print : in-built function :  print function shows the output on console
# id : in-build function : that return the memory address of variable

print("Hello world") # Hello world
print("value of a :", a) # value of a : 20
print(a)

p = 30
q = 40
r = 50
print(p, q, r)

#######################################
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


####################################
# Assign one value to multiple variables

X = Y = Z = 100
print("value X :", X, id(X)) # value X : 100 140719858079256
print("value Y :", Y, id(Y)) # value Y : 100 140719858079256
print("value Z :", Z, id(Z)) # value Z : 100 140719858079256


###############################################
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

### addition of values ###
num1= 40
num2 = 50
num3 = num1 +num2
print("addition:", num3)
print("addition:", num1+num2)

### multiplication of values ###
var1 = num1+num2


### division###
v1=50
v2=3
print ("division with sngle / :", v1/v2)
# when we divide number with double ///, then it returns the whole value without pointer
print ("division with double// : v1//v2")

#### get square and cube of given number ####
n1=5
print("square of value :", n1++2)_# square of value :25
print ("cube of a number", n1++3)_# cube of value :125

#### get the remainder value #######
v2 = 20
v3 = 3
print(" remainder value:", v2%v3) #remainder value :2

#### compare 2 values ####
p1=40
p2=50
p3=40

print(p1==p2) # false
print(p1==p3) # true
print (id(p1)==id(p2))
print (p1!=p2) #true


######################
1. (a+b)^2 = a^2  b^2 +2ab

#########################
calculate simple interest
P=20000
R=8
T=5

A = (P*T*R) / 100
# P = principal amount
# R = rate of interest
# T = time of interest

print ("Simple interest: ", A)_# 8000.0

