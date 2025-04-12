######## Nested Loop #############
#in below program with nested loop with each value of i entire inner loop will execute with
# j as 1, 2, 3.
# outer loop
for i in range(1, 5):  # i = 1
    print("Address i:", i)
    # inner loop
    for j in range(1, 4):  # 1, 2, 3
        print("package j:", j)

    print("_" * 50)

# write a python program to get list of all prime number from 1 to 50
prime_count = 0
non_prime_count = 0
for num in range(2, 50):  # num=2, 3, 4, 5
    count = 0  # 0
    for i in range(2, num):  # (2, 5)  #2, 3, 4
        if num % i == 0:  # 5%4 == 0
            count += 1  #

    # print(num,":", count)
    if count == 0:
        print(num, end=" ")
        prime_count += 1
    else:
        non_prime_count += 1

print()
print("Prime count :", prime_count)
print("Non prime count :", non_prime_count)

print("_" * 50)
################################################
# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):  # i=1, 2, 3, 4
    for j in range(1, i + 1):  # (1,5)
        print("*", end=" ")

    print()
print()
# HW: write a pattern with nested loop
"""

* * * * * 
* * * *
* * *
* *
*
"""
print("class home work")
for i in range(1,6):
    for j in range(5-i,-1,-1):
        print("*",end=" ")
    print()
#range(start,end,step difference)
#range(1, 10, 1)
#in range output, will consider the start and exclude the the end value
for val in range(1, 10, 2):
    print(val)
print("-"*50)

# WAP to print the table of given number
n = 5
for i in range(1, 11, 1):
    print(i, "*", n, "=", i*n)
print("-"*60)
# print output wit negative step value
for i in range(5, 0, -1):
    print(i)



print("-"*50)

for x in range(0, 5):
    for y in range(0, 5-x):
        print(" * ", end=" ")

    print('')

print("-"*50)


#WAP to print A  in * pattern


"""Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")

    print('')
for x in range(0, 4):
    for y in range(0, 4-x):
        print("*", end=" ")

    print('')

print("-"*60)
#Python Loops program to count the number of even and odd numbers from a series of numbers using python.
#Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in range(1, 10, 1):

    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("count number of even number:", even)
print("count number of odd number:", odd)


#WAP to find the print the fabonaccies series.
#1, 2, 3, 5, 8, 13, 21, 34
#
a = 0
b = 1
for _ in range(10):
    a, b = b, a+b
    print(b, end=" ")

print("-"*50)

#write a python program to get sum of all the values from 1 to 10.
output = 0

for i in range(1, 11):
    output = output + i # 0 + 1 = 1, 1+2 = 3, 3+3 = 6, 6+4=10,
    # 10+5 = 15 , 15+6 = 21, 21+7 = 28, 28+8 = 36, 36+9=45, 45+10 = 55

    print("Output :", output)
    # Output : 55


"""
Output : 1
Output : 3
Output : 6
Output : 10
Output : 15
Output : 21
Output : 28
Output : 36
Output : 45
Output : 55

"""

"""Python loops program to print the pattern T using Python Loops.

       Output :

       * * * * * * * * *
       * * * * * * * * *
               * * *
               * * *
               * * *
               * * *
               * * *"""

for i in range(1, 8):#i=7

    for j in range(1, 10):#j=9
        if i == 1 or i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            if j==4 or j==5:

                print("*",end=" ")
            else:
                print("",end="")

    print()


print("-"*50)
for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2,3,4,5]:
             if j == 1 or j == 5:
                print("*", end=" ")
             else:
                print(" ", end=" ")

    print()

print("-"*50)

#WAP to print A letter with * pattern.
for i in range(1, 7):#i=1,i=2,i=3,i=4,i=5,i=6 column
    for j in range(1, 6):#j=1,j=2,j=3,j=4,j=5 row
        if i == 1:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2, 3, 5, 6]:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 4:
                print("*", end=" ")



    print()

print("-"*50)

for i in range(1, 6):
    for j in range(1,i+1):
        print("A",end="")
    print()
print("="*50)
"""
    *
   * *
 * * * *
* * * * * 
 * * * * 
  *  * 
    *
"""






print("-"*60)
"""AAAAAA
BBBBBB
CCCCCC
DDDDDD
EEEEEE
FFFFFF
GGGGGG
HHHHHH"""
for i in range(0,8):#i=column
     for j in range(0,6):#j=row
        print(chr(65 + i), end="")

     print()
print("_"*60)
for i in range(5):
        # prints spaces
        for j in range(5 - i - 1):
            print(' ', end='')

        # prints odd number of characters
        for k in range(2 * i + 1):
            print(chr(65 + k), end='')

        print()


print("-"*60)

"""
    *
   * *
 * * * *
* * * * * 
 * * * * 
  *  * 
    *
"""

for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

print("-"*50)

"""1 1 1   
2       2 
3       3 
4       4 
5       5 
  6 6 6   
"""
for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print(i, end=" ")
        elif i in [2, 3, 4, 5]:
            if j == 1 or j == 5:
                print(i, end=" ")
            else:
                print(" ", end=" ")
    print( )
print("-"*50)
"""  * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
"""
for i in range(7):
      for j in range(6-i):
          print(" ", end="")
      for k in range(i):
          print("* ", end="")
      print()


print("-"*60)
"""
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 
"""
for i in range(7, 0, -1):
    for j in range(7 - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()
for i in range(1, 7+1):
    for j in range(7-i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

print("-"*50)
"""
1
22
333
4444
55555
666666
"""
for i in range(7):
    for j in range(i):

        print(i,end="")
    print()

print("-"*60)
"""
1
12
123
1234
12345
123456
1234567

"""
for i in range(0,7+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("-"*60)
for i in range(0,7+1):
    for j in range(1,7+1-i):
        print(j,end=" ")
    print()


print("-"*50)
"""
7 7 7 7 7 7 7 
7 7 7 7 7 7 
7 7 7 7 7 
7 7 7 7 
7 7 7 
7 7 
7 
"""
for i in range(7):
    for j in range(1,7+1-i):
        print(7,end=" ")
    print()


print("-"*60)
"""
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9 
11 11 11 11 11 11 
"""
for i in range(6+1):
    for j in range(1,i+1):
        print(i*2-1,end=" ")
    print()
print("-"*60)
"""
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
for i in range(6):
    for j in range(0,5-i+1):
        print(6-i,end=" ")
    print()