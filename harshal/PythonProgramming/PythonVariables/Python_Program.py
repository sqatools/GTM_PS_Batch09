a1=10
b1=20
c1=a1+b1
print("Addition of", a1, "and", b1 , "is", c1)

print("_"*50)
j="Harshal "
print(j * 5)

print("_"*50)

#5). Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number
#Input:
#a = 40
#b = 50
#c = 30

a = 40
b = 50
c = 30
avg=(a + b + c)/3
print(avg)

print("_"*50)

#7). Python program to print the square and cube of a given number.
#Input :
#num1 = 9

num1=9
sqr=num1**2
cube=num1**3
print("Squre of", num1, "is", sqr, "and cube is", cube)

print("_"*50)

#8). Python program to interchange values between variables.
#Input :
#a = 10
#b = 20

a = 10
b = 20
a , b = b , a
print("Value of a is", a)
print("Value of b is", b)

print("_"*50)

#9). Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
import math
aa=3
bb=4
c=math.sqrt=(aa**2)+(bb**2)
print("As per Pythagorous theoram" ,aa, "+", bb, "=", c)

print("_"*50)

#10). Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab
a=2
b=3
c=(a**2 + b**2 + (2*a*b))
print("(a + b)^2 =", c)

print("_"*50)

#12). Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
a=5
b=6
c=(a-b) * (a+b)
print("a^2 - b^2 =",c)

print("_"*50)

n1=20
n2=30
print(n1==n2)

print("_"*50)

n1=450
n2=800
n3=200
if(n1>n2) and (n1>n3):
    print(n1,"is greater than",n2,"and",n3)
elif (n2>n1) and (n2>n3):
    print(n2,"is greater than",n1,"and",n3)
elif (n3>n1) and (n3>n2):
    print(n3,"is greater than",n1,"and",n2)

    print("_"*50)

num=5
for j in range(1,11,1):
    print(num,"*",j,"=",j*num)

    print("_"*50)

for i in range(1,11):
    print(i)

    print("_"*50)

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

print("_"*50)

for i in range(6,1):
    for j in range(6,i+1):
        print(" *")
print()

print("_"*50)


n=5
while n<=50:
    print(n)
    n+=5