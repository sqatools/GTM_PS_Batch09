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
