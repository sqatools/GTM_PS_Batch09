# Variables
import math

a=10
print(a)
# Single variables with single value
p=10
q=20
r=30
print(p,id(p))
print(q,id(q))
print(r,id(r))

# Multiple variables with multiple values
x,y,z = 10, 20, 30
print((x,id(x)), (y,id(y)), (z,id(z)))

# Multiple variables with single value
a=b=c = 100
print(a,id(a))
print(b,id(b))
print(c,id(c))

# single variable with multiple values
a= 10, 20, 30
print(a,id(a))

d=20
d=30
print(d)

# Class of 20/03/2025 #

# Practicing the variables by executing the programs#

# 1. Python Program to add two integer values.#

a= 30
b = 20
c = a+b
print(c)

# 2. Python Program to subtract two integer values. #

a = 50
b = 40
c= a-b
print(c)

# 3. Python program to multiply two numbers. #

a=10
b=20
c=a*b
print(c)

# 4. Python program to repeat a given string 5 times. #
a="SQATools"
b = a*5
print(b)

# 5. Python program to get the Average of given numbers.#
a = 40
b = 50
c = 30
d = (a+b+c)/3
print(d)

# 6. Python program to print the square and cube of a given number.#
num1 = 9
print(num1**2)
print(num1**3)

# 7. Python program to interchange values between variables.#

a = 10
b = 20
a,b = b,a
print("The value of a is", a)
print("The value of b is", b)

# 8. Python program to solve this Pythagoras theorem.#
#Theorem : (a2 + b2 = c2)
a= 10
b = 20
c = ((a**2)+(b**2))
print(math.sqrt(c))

# 9. Python program to solve the given math formula.#
# Formula : (a + b)2 = a^2 + b^2 + 2ab
a=100
b=200
lhs=((a+b)**2)
rhs=((a**2)+(b**2)+(2*a*b))
print(lhs, rhs)

#  10. Python program to solve the given math formula.#
# Formula : (a – b)2 = a^2 + b^2 – 2ab

a=100
b=200
lhs=((a-b)**2)
rhs=((a**2)+(b**2)-(2*a*b))
print(lhs, rhs)

# 11. Python program to solve the given math formula.#
# Formula : a2 – b2 = (a-b)(a+b)

a=3
b=6
lhs=((a**2)-(b**2))
rhs= (a-b)*(a+b)
print(lhs, rhs)

# 12. Python program to solve the given math formula. Formula : (a + b)3 = a3 + 3ab(a+b) + b3 #

a=2
b=4
lhs=((a+b)**3)
rhs=(a**3)+((3*a*b)*(a+b))+(b**3)
print(lhs, rhs)

# 13. Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a=2
b=4
lhs=((a-b)**3)
rhs=(a**3)-(3*(a**2)*b)+(3*a*(b**2))-(b**3)
print(lhs, rhs)

# 14. Python program to calculate the area of the square.
# Formula : area = a*a

a=100
area=a*a
print(area)

"""
15. Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14
"""
r=3
pi=3.14
area=pi*(r**2)
print(area)

#16. 17). Python program to calculate the area of a cube.
#Formula = 6*a*a

a=10
area=6*a*a
print(area)

#17. Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r

pi=3.14
r=2
h=3
a=2*pi*r*h
b=2*pi*r*r
area=a+b
print(area)

#18). Python program to calculate simple interest.
#Formula = P+(P/r)*t
#P = Principal Amount
#r = Annual interest rate
#t = time

p=float(input("Enter the Principle Amount"))
r=int(input("Enter the Annual interest rate"))
t=int(input("Enter the time"))
si=p+(p/r)*t
print(si)

#19.  Python program to calculate the volume of a sphere.
#Formula = (4/3*pi*r^2)
#r = radius
#pi = 3

pi=3.14
r=5
volume=(4/3)*pi*(r**2)
print(volume)

#20. Python program to find the square root of a number.
##Note: Use the math library to get the square root.
a=float(input("Enter the number which we want find the square root"))
sqrt=math.sqrt(a)
print(sqrt)