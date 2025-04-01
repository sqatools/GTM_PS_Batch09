#Adding integer values
import math

from numba.cuda.printimpl import real_print_impl
from pyasn1.codec.ber.decoder import PrintableStringDecoder

a=5
b=5
c=a+b
print("c=", c)

a=2
b=3
c=7
d=a+b+c
print("d=", d)

#Subtraction of integer values
a=12
b=10
c=a-b
print("c=", c)

a=11
b=12
c=2
d=a-b-c
print("d=", d)

#multiplication
a=4
b=8
c=a*b
print("c=", c)

#Repeat string 5 times
Str1="SQATools"
print(Str1*5)

#Average of numbers
a = 40
b = 50
c = 30
d=(a+b+c)//3
print("d:", d)

#square and Cube
num1 = 9
print(num1**2)
print(num1**3)

# Python program to repeat a given string 5 times.
str1="SQATools"
print(str1*5)

#Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
a=3
b=4
LHS=a**2-b**2
RHS=(a-b)*(a+b)
print("LHS", LHS)
print("RHS", RHS)

#Python program to calculate the area of a circle.
#Formula = PI*r*r
Pi=3.14
r=4
f=Pi*(r**2)
print("f:", f)

#Python program to calculate the area of a cube.
#Formula = 6*a*a
a=4
Area=6*(a**2)
print("Area:", Area)

#Python program to calculate the volume of a sphere.
#Formula = (4/3*pi*r^2)
pi=3
r=5
a=(4/3*pi*r*r)
print(a)

#Python program to calculate the area of the square.
#Formula : area = a*a
a=4
Area=a**2
print(Area)

#Python program to calculate simple interest.
#Formula = P+(P/r)*t
P=12
r=3
t=2
f=P+(P/r)*t
print(f)

#Python program to find the square root of a number.
#Note: Use the math library to get the square root.
#a=float(input("enter the number"))
#sqrt = math.sqrt(a)
#print(sqrt)

#Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
#a=3
#b=2
#c2=(a**2)+(b**2)
#print(c2)
#c= math.sqrt(c2)
#print(c)

#Calculate the compound interest using the formula p((1+r/100)**n).
p=3
r=8
n=6
c=p*(((1+r/100)**n))
print(c)

#Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab
a=4
b=5
LHS=((a+b))**2
RHS=a**2+b**2+2*a*b
print(LHS)
print(RHS)

#Python program to solve the given math formula.
#Formula : (a - b)2 = a^2 + b^2 - 2ab
a=4
b=5
LHS=((a-b))**2
RHS=a**2+b**2-2*a*b
print(LHS)
print(RHS)

#Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a=6
b=5
LHS=((a+b))**3
RHS=a**3+3*a*b*((a+b))+b**3
print(LHS)
print(RHS)

#Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
a=6
b=5
LHS=((a-b))**3
RHS=a**3-3*(a**2)*b+3*a*(b**2)-b**3
print(LHS)
print(RHS)

#Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r
pi=3.14
r=4
h=5
f=(2*pi*r*h)+(2*pi*r*r)
print(f)
###################Data Types############

a=6
print(a, type(a))

b= -12.678
print(b, type(b))

c=10+20J
print(c, type(c))
print(c.real)
print(c.imag)

print("""hafjafjkjnfjndgnjgjngnsjfng \n
dbjkvfsjnfjjgnfgnjfjd \n
uukgybjb\t\t\tjybhjbybhjbh
hjbhbjbjbbjbjhb
""")

List1= [2,-3.5,2.45,'Hello',[1,2,3],(3,7,9),{'a':123},{5,7},True,10+20J]
print(List1, type(List1))
print(List1[3][4])
print(List1[3][-4])
List1.append(45)
print(List1, type(List1))

Tuple1= (2,-3.5,2.45,'Hello',[1,2,3],(3,7,9),{'a':123},{5,7},True,10+20J)
print(Tuple1, type(Tuple1))
print(Tuple1[3][4])
print(Tuple1[3][-4])
#Tuple1.append(45)
#print(Tuple1, type(Tuple1))

dict1= {'name': 'Harish','age':20,'class':12,'mail':'gmail.com'}
print(dict1['name'])
print(dict1['class'])


set1={1, 2, 3, 'harish', 8, 9, 2, 6}
print(set1, type(set1))
set1.add(100)
print(set1)














