print("_"*50)
# addition of two numbers

numb1 = 31
numb2 = 16

addition = numb1+numb2
print("sum :", addition)

print("*"*50)

# multiplication of values
var1 = numb1*numb2
print("multiplication :", var1)

print("_"*50)
# subtraction
print("*"*50)
print("subtraction :", 500-numb2)

print("_"*50)
#### division ###


v1 = 50
v2 = 3

print("division with single /:", v1/v2)
print("division with multiple //:", v1//v2)


print("_"*50)
#### get square and cube of given number ####

n1 = 5
print("square value :", n1**2)
print("cube value:", n1**3)


print("_"*50)
#### get remainder value ###########
v2 = 20
v3 = 3

print("reminder value:", v2 % v3)

print("*"*50)
#### compare 2 values ####
p1 = 40
p2 = 50
p3 = 40

print(p1 == p2)  # False
print(p1 == p3)   # True
print(id(p1) == id(p3))  # True
print(p1 != p2)  # True

print("_"*50)
########################
"""
1.  (a+b)^2 = a^2 + b^2 + 2ab
2.  (a-b)^2 = a^2 + b^2 - 2ab

"""
#  (a-b)^2 = a^2 + b^2 - 2ab

a = 10
b = 5
LHS = (a-b)**2
print("LHS output is :", LHS )

RHS = a**2 + b**2 - 2*a*b
print("RHS output is:", RHS)


print("_"*50)
####################################
# calculate simple interest
# P = principal amount
# R = rate of interest
# T = time in a years
P = 10000
R = 9
T = 5

Amount = (P*R*T)/100
print("Total amount is:", Amount)

