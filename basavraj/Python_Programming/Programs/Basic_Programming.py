

# Programs

# 1). Python Program to add two integer values.

X,Y=20,50
print(X+Y)

#2). Python Program to subtract two integer values.

X,Y=20,50
print(Y-X)

#3. Python program to multiply two numbers.

a,b=2,6
print(a*b)

# 4). Python program to repeat a given string 5 times.
Name="Basavaraj"
print(Name*5)

#5). Python program to get the Average of given numbers.

x,y,z=10,20,30
avg=(x+y+z)/3
print(avg)


#6). Python program to get the median of given numbers.

#7). Python program to print the square and cube of a given number.

a=3
print(a**2)
print(a**3)

#8). Python program to interchange values between variables.

a,b=10,20
a,b=b,a
print(a,b)

#10). Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab

a=2
b=3
c=(a+b)**2
print(c)
d=a**2+b**2+2*a*b
print(d)
print(c==d)

#11). Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab
a=2
b=3
c=(a-b)**2
print(c)
d=a**2+b**2-2*a*b
print(d)
print(c==d)

#12). Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)

a=3
b=2
c=(a-b)*(a+b)
print(c)

#13). Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a=2
b=2
c=(a+b)**3
print(c)
d=a**3+3*a*b*(a+b)+b**3
print(d)
print(c==d)

#14). Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3


a=19
b=2
c=(a-b)**3
print(c)
d=a**3-3*a**2*b+3*a*b**2-b**3
print(d)
print(c==d)

#15). Python program to calculate the area of the square.
#Formula : area = a*a

a=5
c=a*a
print(c)

#16). Python program to calculate the area of a circle.
#Formula = PI*r*r
r = 5
PI = 3.14
are_of_circle=PI*r*r
print(are_of_circle)

#17). Python program to calculate the area of a cube.
#Formula = 6*a*a

a=5
areofcube=6*a*a
print(areofcube)

#19). Python program to check whether the given number is an Armstrong number or not.
#Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

n=153
temp=n
arm=0
while n>0:
    r=n%10
    arm=arm+r**3
    n=n//10

if arm==temp:
    print("the number is armstrong")
else:
    print("the number is not an armstrong")

#20). Python program to print the current date in the given format
#Output: 2023 Jan 05


import datetime
date = datetime.datetime.now()

print (date.strftime (" %Y %b %d "))

#23). Python program to get the factorial of the given number.

n=5
fact=1
if n==0:
    print("factorial of zero and one is 1 ")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

#24). Python program to reverse a given number.
n=123
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)

#26). Python program to check given number is palindrome or not.
n=123
temp=n
palind=0
while n>0:
    r=n%10
    palind=palind*10+r
    n=n//10
if temp==palind:
    print("the number is palindrome")
else:
    print("the number is not a palindrome")

#28). Python program to check the prime number.


n=5
c=0
if n>0:
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
if c==2:
    print("the number is prime")
else:
    print("the number is not a prime")

#29). Python program to check leap year.
year=2025
if year%400==0 or year%4==0:
    print("leap year")
elif year%400==0 and year%100!=0:
    print("leap year")
else:
    print("the entered year is not an leap year")

#30). Python program to check for the anagram

word="basavaraja"

if sorted(word)==sorted(set(word)):
    print("anagram")
else:
    print("not an anagram")

#34). Python program to convert Decimal to Binary.
n = 10
print(f"The binary representation of {n} is {bin(n)[2:]}")

#35). Python program to find the sum of natural numbers.
n=123
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)








