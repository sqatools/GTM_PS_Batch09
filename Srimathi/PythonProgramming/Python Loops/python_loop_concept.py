# write a python program to get values from list

l1 = [4, 13, 16, 8, 11, 2, 6, 12, 3]
for val in l1:
    # print(val)
    if val % 2 == 0:
        print(val)

print("_" * 50)
# write a python program to get all number which is divisible by 3 and 5 from given tuple
t1 = (3, 5, 7, 15, 20, 25, 30)

for num in t1:
    if num % 3 == 0 and num % 5 == 0:
        print(num)

"""
15
30
"""

print("_" * 50)
# write a python program to check given number is prime or not
num = 12

count = 0
for i in range(2, num):  # 2, 3, 4, 5, 6
    if num % i == 0:  # 12%6 == 0
        count += 1  # 1, 2, 3, 4

print("counter :", count)
if count == 0:
    print("This is prime number:", num)
else:
    print("This is not prime number:", num)

print("_" * 50)
#################################################
############## Nested loop condition ##########
# in below program with nested loop with each value of i entire inner loop will execute with
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
for num in range(2, 50): # num=2, 3, 4, 5
    count = 0 # 0
    for i in range(2, num): # (2, 5)  #2, 3, 4
        if num % i == 0: # 5%4 == 0
            count += 1 #

    #print(num,":", count)
    if count == 0:
        print(num, end=" ")
        prime_count += 1
    else:
        non_prime_count += 1


print()
print("Prime count :", prime_count)
print("Non prime count :", non_prime_count)


print("_"*50)
################################################
# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6): # i=1, 2, 3, 4
    for j in range(1, i+1): # (1,5)
        print("*", end=" ")

    print()


# HW: write a pattern with nested loop
"""

* * * * * 
* * * *
* * *
* *
*
"""

print("-"*50)

for i in range(6, 0, -1):# i = 6, 5
    for _ in range(1, i): # (1, 5)
        print("*", end=" ")

    print()



#####################################
# write a python program to print A letter with * pattern.

"""
  * * *    # i = 1
*       *  # i = 2
*       *  # i = 3
* * * * *  # i = 4
*       *  # i = 5 
*       *  # i = 6
"""

for i in range(1, 7): # i = 1, 2
    for j in range(1, 6): # j= 1, 2, 3, 4, 5
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


print("_"*40)
########################################
# write a python program to print O pattern with nested loop

"""
  * * *    # i = 1
*       *  # i = 2
*       *  # i = 3
*       *  # i = 4
*       *  # i = 5
  * * *    # i = 6
"""

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2, 3, 4, 5]:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


# Home work
"""
    *
  * * *
* * * * *   
  * * *
    *  
"""

print("_"*50)

"""
  1 1 1    # i = 1
2       2  # i = 2
3       3  # i = 3
4       4  # i = 4
5       5  # i = 5
  6 6 6    # i = 6
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
    print()