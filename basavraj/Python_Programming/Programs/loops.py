#1). Write a Python loops program to find those numbers
# which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
print("program 1")
for num in range(1500,2700):
    if num%7==0 and num%5==0:
        print(num,end="\n")

print("-"*50)

#2). Python Loops program to construct the following pattern, using a nested for loops.
"""Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

#3). Python Loops program that will add the word from the user to the empty string

#str1=input("enter the string:")
print("program 3")
str1="python"
str2=""
for i in str1:
    str2=str2+i
print(str2)

print("-"*50)

#4). Python Loops program to count the number of
# even and odd numbers from a series of numbers using python.
print("program 4")
l= (1, 2, 3, 4, 5, 6, 7, 8, 9)
even=0
odd=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even numbers",even)
print("odd numbers",odd)
print("-"*50)
#5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

# Loop through numbers from 0 to 6
print("program 5")
for num in range(7):
    # Skip 3 and 6 using continue
    if num == 3 or num == 6:
        continue
    print(num,end=" ")
print()
print("-"*50)

#6). Write a program to get the Fibonacci series between 0 to 20 using python.

print("program 6")
a,b=0,1
while a<=20:
    print(a,end=" ")
    a,b=b,a+b
print()
print("-"*50)

#7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.
print("program 7")
for i in range(1,31):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

print("-"*50)

#8). Write a program that accepts a word from the user
# and converts all uppercases in the word to lowercase using python.
print("program 8")
str1="SQAtoolS"
for i in str1:
    if i.isupper():
        print(i.lower(),end="")
    else:
        print(i,end="")
print()
print("-"*50)

#9). Python loops program that accepts a string and
# calculates the number of digits and letters using python.
print("program 9")
str1="python1234"
c=0
d=""
for i in str1:
    if i.isalpha():
        c=c+1
    elif i.isdigit():
        d=d+i
print("letters",c)
print("digits",d)
n=int(d)
print(n,type(n))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)

print("-"*50)

#10). Python for loop program to print the alphabet pattern ‘O’ using python.

#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
print("program 10")

n=20
c=1
while c<=n:
    print(c,end=" ")
    c=c+1
print()
print("-"*50)
#12). Write a program to print all natural numbers in reverse (
# from n to 1) using a while loop in python.
print("program 12")
n=20
count=n
while count!=0:
    print(count,end=" ")
    count=count-1

print()
print("-"*50)

#13). Python Loops program to print all alphabets from a to z using for loop
"""  Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
"""
print("program 13")
for i in range(65, 91):  # 65 to 90 inclusive
    print(chr(i), end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")
print()
print("-"*50)

#14). Python Loops program to print all even numbers between 1 to 100 in python.
print("program 14")
for i in range(1,101):
    if i%2==0:
        print(i,end=" ")

print()
print("-"*50)

#15). Python Loops program to print all odd numbers between 1 to 100 using python
print("program 15")
for i in range(1,101):
    if i%2==1:
        print(i,end=" ")

print()
print("-"*50)
#16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
print("program 16")
#n=int(input("enter the number:"))
n=5
s=0
for i in range(1,n+1):
    s=s+i
print(s)

print("-"*50)

#17). Python program to find the sum of all even numbers between 1 to n using python.
print("program 17")
#n=int(input("enter the number:"))
n=10
s1=0
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
        s1=s1+i
print()
print(s1)
print("-"*50)

#18). Python Loops program to find the sum of all odd numbers between 1 to n using python
print("program 18")
#n=int(input("enter the number:"))
n=10
s1=0
for i in range(1,n+1):
    if i%2==1:
        print(i,end=" ")
        s1=s1+i
print()
print(s1)
print("-"*50)

#19). Write a program to count the number of digits in a number using python.
print("program 19")
n="959134"
c=0
for i in n:
    c=c+1
print(c)
print("-"*50)

#20). Write a program to find the first and last digits of a number using python.
print("program 20")
n="959134"
print(n[0],n[-1])
print("-"*50)

#21). Write a program to find the sum of the first and last digits of a number using python.
print("program 21")
n=1234
n2=str(n)
print(n2,type(n2))
s=0
for i in range(len(n2)):
    if i==0:
        s=s+int(n2[i])
    elif i==len(n2)-1:
        s=s+int(n2[i])
print(s)
print("-"*50)

#22). Write a program to calculate the sum of digits of a number using python.
print("program 22")
#n=int(input("enter the number :"))
n=4567
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)
print("-"*50)

#23). Write a program to calculate the product of digits of a number using python.
"""print("program 23")
n=9876
n2=str(n)
for i in n2:
    print(int(i))
"""
#24).Python loops program to enter a number and print its reverse using python.
print("program 24")
n=4321
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
print("-"*50)

#25). Write a program to check whether a number is a palindrome or not using python loops.
print("program 25")
n=121121
temp=n
palind=0
while n>0:
    r=n%10
    palind=palind*10+r
    n=n//10
if temp==palind:
    print("number is palindrome")
else:
    print("number is not a palindrome")
print("-"*50)

#26). Program to find the frequency of each digit in a given integer using Python Loops.

print("program 26")
n=112344537895
n2=list(str(n))
print(n2)
d={}
for i in n2:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
print("-"*50)
