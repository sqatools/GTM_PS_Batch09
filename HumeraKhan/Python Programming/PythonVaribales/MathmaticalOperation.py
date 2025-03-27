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

print("square of value :", n1**2)    # square of value : 25
print("cube of value :", n1**3)      # cube of value : 125

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
# 1 (a+b)^2 = a^2 + b^2 + 2ab
a=5
b=7
lhs = (a+b)**2
print("LHS output  :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("RHS output :", rhs)

# 2 (a-b)^2 = a^2 + b^2 - 2ab
a = 4
b = 7
lhs = (a-b)**2
print("LHS output  :", lhs)

rhs = a**2 + b**2 - 2*a*b
print("RHS output :", rhs)

####################################
#Calculate simple interest
P = 20000     # P = principal amount
r = 8         # r = rate of interest
t = 5         # t = time in a years
A = (P*t*r)/100

print("Simple interest :", A) # 8000.0
