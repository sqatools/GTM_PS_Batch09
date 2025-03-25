a = 20
print(id(a))  # 140719858076376
# a : variable
# = : assignment operator
# 10 : value to store
# Address of variable
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

