#1). Python program to check given number is divided by 3 or not.
print("-"*50)
n=7
if n%3==0:
    print("the given number is divisible by 3")
else:
    print("the given mumber is not divisible by 3")

print("-"*50)

#2). If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1,30+1):
    if i%3==0:
        print(i,end=" ")
print()
print("-"*50)

#3). If else program to assign grades as per total marks
""" 
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
#marks=int(input("enter the marks :"))
marks=100
if marks<40:
    print("Fail")
elif marks>=40 and marks<=50:
    print("grade C")
elif marks>=51 and marks<=60:
    print("grade B")
elif marks>=61 and marks<=70:
    print("grade A")
elif marks>=71 and marks<=80:
    print("grade A+")
elif marks>=81 and marks<=90:
    print("grade A++")
elif marks>=91 and marks<=100:
    print("EXCELLENT")
else:
    print("entered invalid marks")

print("-"*50)

#4). Python program to check the given number divided by 3 and 5.

num=15
if num%3==0 and num%5==0:
    print("the given number is divided by 3 and 5")
else:
    print("the given number is not divided by 3 and 5")

print("-"*50)

#5). Python program to print the square of the number if it is divided by 11
n=33
if n%11==0:
    print(n**2)

print("-"*50)

#6). Python program to check given number is a prime number or not.
n=5
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    print("prime")
else:
    print("not a prime")

print("-"*50)

#7). Python program to check given number is odd or even.

n=8
if n%2==1:
    print("add")
else:
    print("even")

print("-"*50)
#8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

f=[0,1,1,2,3,5,8,13,21,34,55,89]
#n=int(input("enter the number :"))
n=89
if n in f:
    print("the entered number is fibonacci series")
else:
    print("the entered number is not fibonacci series")

print("-"*50)

#9). Python program to check authentication with the given username and password.
"""
name="basavaraja"
pas=12345
username=input("enter the username :")
password=int(input("entered the password :"))
if name==username and pas==password:
    print("login is successful")
else:
    print("invalid username or passsword")
    
print("-"*50)
    
"""
#10). Python program to validate user_id in the list of user_ids
id = [1,2,3,5,6,7,8]
#entered_id= int(input("Enter ID number: "))
entered_id=3
if entered_id in id:
    print("Valid ID")
else:
    print("Invalid ID")

print("-"*50)

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

#n=int(input("enter the number :"))
n=3
if n%2==0:
    print(n**2)
elif n%3==0:
    print(n**3)

print("-"*50)

#12). Python program to describe the interview process.

#round1 = input("Enter round1 result:")
#round2 = input("Enter round2 result:")
round1="passed"
round2="paased"

if round1 == "passed":
    print("Congrats your 1st round is clear")
    if round2 == "passed":
        print("Congrats 2nd round is clear, you are placed")
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")

print("-"*50)

#14). Python program to find the largest number among three numbers.
a,b,c=10,30,20
if a>b or a>c:
    print("a is large")
elif b>a or b>c:
    print("b is large")
else:
    print("c is large")

print("-"*50)

#15). Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

#n=int(input("enter the age of person :"))
n=22
if n>=0 and n<=18:
    print("not eligible for vote")
else:
    print("eligible for vote")

print("-"*50)
#16). Python program to check whether any given number is a palindrome.

n=111
temp=n
palind=0
while n>0:
    r=n%10
    palind=palind*10+r
    n=n//10
if temp==palind:
    print("palindrome")
else:
    print("not a palindrome")

print("-"*50)

#17). Python program to check if any given string is palindrome or not.
#n=input("enter the string:")
n="gadag"
s=n[::-1]
if n==s:
    print("string is palindrome")
else:
    print("not a palindrome")

print("-"*50)

#19). Python program to check whether the given number is positive or not.
n=10
if n>0:
    print("True")
else:
    print("False")

print("-"*50)

#20). Python program to check whether the given number is negative or not.

n = -10
if n < 0:
    print("True")
else:
    print("False")

print("-" * 50)

#21). Python program to check whether the given number is positive or negative and even or oddnum = int(input("Enter a number: "))

#num = int(input("Enter a number: "))
num=22
if num>0:
    if num%2 == 0:
        print("The given number is positive and even")
    else:
        print("The given number is positive and odd")
else:
    if num%2 == 0:
        print("The given number is negative and even")
    else:
        print("The given number is negative and odd")

print("-" * 50)

#22). Python program to print the largest number from two numbers.

a,b=20,30
if a>b:
    print("a is largest")
elif a==b:
    print("a and b same value")
else:
    print("b is largest")

print("-" * 50)

#23). Python program to check whether a given character is uppercase or not.
char ="A"
if char.isupper():
    print("True")
else:
    print("False")

print("-" * 50)
#24). Python program to check whether the given character is lowercase or not.
char = "B"

if char.islower():
    print("True")
else:
    print("False")

print("-" * 50)
#25). Python program to check whether the given number is an integer or not.
num1 = 54

if type(num1) == int:
    print("True")
else:
    print("False")

print("-" * 50)
#26). Python program to check whether the given number is float or not.
num1 = 12.6

if type(num1) == float:
    print("True")
else:
    print("False")
print("-" * 50)
#27). Python program to check whether the given input is a string or not.
str1 = "Hello"

if type(str1) == str:
    print("True")
else:
    print("False")

print("-" * 50)

#28). Python program to print all the numbers from 10-15 except 13

for i in range(10,15+1):
    if i==13:
        continue
    print(i,end=" ")

print("-" * 50)







