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

for i in range(11,0,-1):
    for j in range(1, i+1):
        print("*", end="")
    print()
print()

for i in range(1,11,1):
    for j in range(1,i+1):
        print("*", end="")
    print()
print()


num=7
count=0
for i in range(2, num):
    if num%i==0:
        count=count+1
if count==0:
    print("PM")
else:
    print("NPM")


for i in range(1,6,1):
    for j in range(1,i+1):
        print("*", end="")
    print()
print()


for i in range(5,0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
print()

num=34
count=0
for i in range(2,34):
    if num%i==0:
        count+=1
if count==0:
        print("PM")
else:
        print("NPM")

num=5
count=0
for i in range(2, 5):
    if num%i==0:
        count+=1
if count==0:
        print("PM")
else:
        print("NPM")


for i in range(1,11,1):
    for j in range(1,i+1):
        print("*", end="")
    print()
print()
















