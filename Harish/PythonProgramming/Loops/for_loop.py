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

for i in range(6,1,-1):
    for j in range(1,i):
        print("*", end="")
    print()
print()


#write a program to print A letter with * pattern

"""
   * * *
 *       *
 *       *
 * * * * *
 *       *
 *       *
"""

for i in range(1, 7):
    for j in range(1, 6):
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

print("_"*100)

"""
  * * *    # i = 1
*       *  # i = 2
*       *  # i = 3
*       *  # i = 4
*       *  # i = 5
  * * *    # i = 6
"""

for i in range(1, 7):
    for j in range(1,6):
        if i in [1,6]:
            if j==1 or j==5:
                print(" ", end="")
            else:
                print("*", end="")
        elif i in [2,3,4,5]:
            if j==1 or j==5:
                print("*", end="")
            else:
                print(" ", end="")

    print()
print("_"*100)

# Home work
"""
    *
  * * *
* * * * *   
  * * *
    *  
"""
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5:
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

print("_" * 100)

"""
  1 1 1    # i = 1
2       2  # i = 2
3       3  # i = 3
4       4  # i = 4
5       5  # i = 5
  6 6 6    # i = 6
"""

for i in range(1,7):
    for j in range(1,6):
        if i==1 or i==6:
            if j==1 or j==5:
                print(" ", end="")
            else:
                print(i, end="")
        elif i in[2,3,4,5]:
            if j==1 or j==5:
                print(i, end="")
            else:
                print(" ", end="")
    print()


"""
****
****
****
****

"""
for i in range(1,5):
    for j in range(1,5):
        if i in [1,2, 3, 4]:
            if j in [1,2, 3, 4]:
                print("*", end="")
    print()

print("_" * 100)

"""
   *
  **
 ***
****
 ***
  **
   *
"""


for i in range(1,8):
    for j in range(1,5):
        if i in [1,7]:
            if j==4:
                print("*", end="")
            else:
                print(" ", end="")
        elif i in [2,6]:
            if j in [3,4]:
                print("*", end="")
            else:
                print(" ", end="")
        elif i in [3,5]:
            if j in [2,3,4]:
                print("*", end="")
            else:
                print(" ", end="")
        elif i==4:
            print("*", end="")
    print()

print("_" * 100)

"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(1,6):
   for j in range(1,6):
       if i==1:
           if j==1:
               print("*", end="")
           else:
               print(" ", end="")
       elif i == 2:
           if j in [1,2]:
               print("*", end="")
           else:
               print(" ", end="")
       elif i == 3:
           if j in [1, 2, 3]:
               print("*", end="")
           else:
               print(" ", end="")
       elif i == 4:
           if j in [1, 2, 3, 4]:
               print("*", end="")
           else:
               print(" ", end="")
       elif i == 5:
                print("*", end="")
   print()



"""
*****
****
***
**
*

"""
for i in range(6,1,-1):
    for j in range(1,i):
        print("*", end="")
    print()


num=7
count=0
for i in range(2, 7):
    if num%i==0:
        count+=1
if count==0:
    print("PM")
else:
    print("NPM")






















