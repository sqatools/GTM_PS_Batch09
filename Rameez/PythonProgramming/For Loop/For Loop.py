## Print values with two differences ##
for i in range(1,10,2):
    print(i)
print("*"*50)

## Print values with one difference ##
for i in range(1,10,1):
    print(i)
print("*"*50)

## Get output with default start value(0) and default step value(1) ##
for i in range(20):
    print(i)
print("*"*50)

## print output with negative step ##
for i in range(11,0,-1):
    print(i)
print("*"*50)

## Print output with all negative in reverse order##
for i in range(-11,-1,1):
    print(i)
print("*"*50)

## Print output with all negative ##
for i in range(-1,-11,-1):
    print(i)
print("*"*50)

## Write a python program to print the table of given number ##

num=5
for j in range(1,11,1):
    print(num, "*", j, "=", (num*j))
print("*"*50)

## write a python program to get factorial of any given number ##
n1=5
fact = 1
for i in range(n1,0,-1):
    fact=fact*i
    print(fact)
print("*"*50)

## print sum of all the number
output=0
for i in range(1,11,1):
    output=output+i
    print(output)
print("*"*50)

## Write a python program for the fibonacci series ##
a=0
b=1
for i in range(10):
    a,b=b,a+b
    print(b)

## Homework Pattern Program ##
for i in range(5,0,-1):
    for j in range(1, i+1):
        print("*", end="")
    print()


## Class Pattern Program##
for i in range(1,6):
    for j in range(1, i+1):
        print("*", end="")
    print()


## find the given value is prime or not ##
num=100
count=0
for i in range(2,num):
    if num%i==0:
        count+=1
if count==0:
    print("Prime Number")
else:
    print("Not a prime Number")

## In below with each value of i entire inner loop will execute with j as 1,2,3

for i in range(1,5):
    print("Address:", i)
    for j in range(1,4):
        print("Package:", j)

## write a python program to get all the numbers which are divisible by 3 and 5 from the given tuple ##
t1=(12,13,14,15,16,18,19,20,25)
for i in t1:
    if i%3==0 and i%5==0:
        print(i)

## write a python program to get even numbers from list ##
l1=[4,13,16,8,11,2,6,12,3]
for i in l1:
    if i%2==0:
        print(i)

## write a python program to get even number from list
l1=[4,16,8,2,6,12]
for i in l1:
    print(i)
## Write a program to print "A" character using * ##
for i in range(1,7):
    for j in range(1,6):
        if i==1:
            if j==1 or j==5:
                print(" ", end="")
            else:
                print("*", end="")
        elif i in [2,3,5,6]:
            if j==1 or j==5:
                print("*", end="")
            else:
                print(" ", end="")
        elif i==4:
            print("*", end="")
    print()
print("*"*100)
## write a program to print "o" character using * ##

for i in range(1,8):
    for j in range(1,6):
        if i in [1,7]:
            if j==1 or j==5:
                print(" ", end="")
            else:
                print("*", end="")
        elif i in [2,3,4,5,6]:
            if j==1 or j==5:
                print("*", end="")
            else:
                print(" ", end="")
    print()
print("*"*100)
## Homework Pattern "Diamond Shape" ##

for i in range(1,6):
    for j in range(1,6):
        if i in [1,5]:
            if j==3:
                print("*", end="")
            else:
                print(" ", end="")
        elif i in [2,4]:
            if j==1 or j==5:
                print(" ", end="")
            else:
                print("*", end="")
        elif i==3:
            print("*", end="")
    print()
print("*"*100)
## Write a program to print "o" character using the numbers ##
for i in range(1,8):
    for j in range(1,6):
        if i in [1,7]:
            if j==1 or j==5:
                print(" ", end="")
            else:
                print(i, end="")
        elif i in [2,3,4,5,6]:
            if j==1 or j==5:
                print(i, end="")
            else:
                print(" ", end="")
    print()