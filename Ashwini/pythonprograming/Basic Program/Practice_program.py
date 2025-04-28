# substraction of two number
num1 = 20
num2 = 50
print("substration is:", 40 - num1)
print("-" * 40)

# multiply two number
var1 = num1 * num2
print("result of multiply number is:", var1)
print("_" * 50)
# addition of two integer value
num3 = 39
num4 = 20
print("addition of two number is:", num3 + num4)

print("_" * 50)

# Python program to repeat a given string 5 times.
# Input :str1 = “SQATools”

print("repeated string is:", ("str1" * 5))
print("-" * 50)

"""Python program to get the Average of given numbers.
Formula: sum of all the number/ total number"""

a = 40
b = 50
c = 30
print("sum of all number:", (a + b + c) / 3)
print("_" * 50)

""" Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729"""
num1 = 9
print("square of value :", num1 ** 2)
print("cube of value :", num1 ** 3)

print("_" * 50)
"""Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r"""
PI = 3.14
r = 10
h = 50
print("area of cylinder is:", (2 * PI * r * h + 2 * PI * r * r))
print("-" * 50)

"""Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14"""
r = 40
print("area of circle is:", (PI * r * r))
print("-" * 50)
"""Python program to calculate the area of a cube.
Formula = 6*a*a"""
a = 20
print("area of cube is:", (6 * a * a))
print("-" * 50)
"""Python program to calculate the area of the square.
Formula : area = a*a"""

a1 = 40
print("area of square is:", (a1 * a1))
print("-" * 50)

""" 1.  (a+b)^2 = a^2 + b^2 + 2ab
    2.  (a-b)^2 = a^2 + b^2 - 2ab

"""
#  (a-b)^2 = a^2 + b^2 - 2ab
a = 8
b = 6
lhs = (a - b) ** 2
print("LHS output  :", lhs)

rhs = a ** 2 + b ** 2 - 2 * a * b

print("RHS output :", rhs)
print("-" * 50)
# (a+b)^2 = a^2 + b^ + 2ab
a = 4
b = 9
lhs = (a + b) ** 2
print("LHS output:", lhs)
rhs = a ** 2 + b ** 2 + 2 * a * b
print("Rhs output:", rhs)
####a^2 – b^2 = (a-b)(a+b)#######
a = 3
b = 2
lhs = (a ** 2) - (b ** 2)
print("lhs is :", lhs)
rhs = (a - b) * (a + b)
print("Rhs is:", rhs)

"""Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10"""
a = 10
b = 20
a, b = b, a
print("Interchange value:", a)
print("Interchange value:", b)
print("-" * 50)
""" Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)"""
# a^2+b^2=c^2
a = 3
b = 4
c = 5

lhs = (a ** 2) + (b ** 2)
print("LHS is:", lhs)
rhs = (c ** 2)
print("RHS is:", rhs)

user = int(input("Enter the Age:"))
if user >= 18:
    print("Ready for vaoting:")
else:
    print("not rady for vating:")

print("-" * 50)

Item1 = int(input("Enter the item1:"))
Item2 = int(input("Enter the item2:"))
Item3 = int(input("Enter the item3:"))

Total = Item1 + Item2 + Item3
if Total > 1000:
    discount = Total * (20 / 100)
    total_amount = discount
    print("total amount =:", total_amount)
else:
    print("total amount=:", Total)

print("-" * 50)

"""Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time"""
p = 20
r = 10
t = 25
print("calculate simple interset is:", p + (p / r) * t)

print("-" * 50)

# Python program to calculate compound interest.


p = int(input("Enter principle amount: "))
r = float(input("Enter interest rate: "))
n = int(input("Enter number of years: "))

amount = p * ((1 + r / 100) ** n)
print("Compoud interest: ", amount)
"""
p = 400
r = 45.7
n = 2017
print("compund interset is:", p*((1+r/100)**n))
"""