"""
# for loop
for <condition>:
    code

"""
# range(start, end, step difference)
# range(1, 10, 1)
# in range output, will consider the start and exclude the end value

for val in range(1, 10, 1):
    print(val)

"""
1
2
3
4
5
6
7
8
9

"""
print("_"*50)
# print values with 2 difference

for val in range(1, 10, 2):
    print(val)

"""
1
3
5
7
9
"""

print("_"*50)
# get output with default start value (0) and default step value (1)


for i in range(5):
    print(i)

"""
0
1
2
3
4
"""

print("_"*50)
# print output with negative step value

for i in range(5, 0, -1):
    print(i)

"""
5
4
3
2
1
"""

print("_"*50)
# print output with all negative

for i in range(-1, -11, -1):
    print(i)

"""
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
"""

print("_"*50)
#######
# write a python program to print the table of given number number
num = 7

for j in range(1, 11, 1):
    print(j, "*", num, "=", j*num)

"""
1 * 7 = 7
2 * 7 = 14
3 * 7 = 21
4 * 7 = 28
5 * 7 = 35
6 * 7 = 42
7 * 7 = 49
8 * 7 = 56
9 * 7 = 63
10 * 7 = 70
"""

print("_"*50)
######################################
# write a python program to get factorials of any given number
# 5 : 5*4*3*2*1
n1 = 6
fact = 1

for i in range(n1, 0, 1):
    print(i) # 5, 4, 3, 2, 1
    fact = fact*i # 5*1 =5, 5*4=20, 20*3 = 60, 60*2=120, 120*1 = 120

print("factorials of :",n1,":", fact)
# factorials of : 6 : 720

print("_"*50)
####################################################
# write a python program to get sum of all the values from 1 to 10
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

print("_"*50)
# write a python program to print the fabonacci series
#     a   b   a+b
# 1,  2,  3,  5,  8, 13, 21, 33
# a,  b,  a+b


a = 0
b = 1
for _ in range(10):

    a, b = b, a+b
    #print("a:", a, "b:", b)
    print(b, end=" ")

# 1 2 3 5 8 13 21 34 55 89

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


