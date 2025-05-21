"""for Loop
 for <condition>:
      code

  """
# range(start,end,step difference)
# range(1, 10, 1)
# in range output, will consider the start and exclude the the end value
for val in range(1, 10, 2):
    print(val)
print("-" * 50)

# WAP to print the table of given number
n = 5
for i in range(1, 11, 1):
    print(i, "*", n, "=", i * n)
print("-" * 60)
# print output wit negative step value
for i in range(5, 0, -1):
    print(i)

print("-" * 60)
"""Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700"""
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

"""Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5"""

even = 0
odd = 0
for i in range(1, 10, 1):

    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("count number of even number:", even)
print("count number of odd number:", odd)

print("-" * 60)
# WAP to get factorials of any number.
n1 = 5
fact = 1
for i in range(n1, 0, -1):
    fact = fact * i
print("Factorials of:", n1, ":", fact)
print("-" * 60)
# Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for j in range(0, 7):
    if j != 3 or j != 6:
        print(j)

print("-" * 60)
for n2 in range(0, 11):
    if n2 != 3 or n2 != 6:
        print(n2)
# get sum of all the value from 1 to 10.
output = 0
for i in range(1, 11):
    output = output + i
print("output :", output)

"""for Loop


for < condition >:
    code
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


# range(start,end,step difference)
# range(1, 10, 1)
# in range output, will consider the start and exclude the the end value
for val in range(1, 10, 2):
    print(val)
print("-" * 50)

# WAP to print the table of given number
n = 5
for i in range(1, 11, 1):
    print(i, "*", n, "=", i * n)
print("-" * 60)
# print output wit negative step value

1
3
5
7
9


print("_" * 50)
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

print("_" * 50)
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

print("_" * 50)
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

print("_" * 50)
#######
# write a python program to print the table of given number number
num = 7

for j in range(1, 11, 1):
    print(j, "*", num, "=", j * num)

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

print("_" * 50)
######################################
# write a python program to get factorials of any given number
# 5 : 5*4*3*2*1
n1 = 6
fact = 1

for i in range(n1, 0, 1):
    print(i)  # 5, 4, 3, 2, 1
    fact = fact * i  # 5*1 =5, 5*4=20, 20*3 = 60, 60*2=120, 120*1 = 120

print("factorials of :", n1, ":", fact)
# factorials of : 6 : 720

print("_" * 50)
####################################################
# write a python program to get sum of all the values from 1 to 10
output = 0

for i in range(1, 11):
    output = output + i  # 0 + 1 = 1, 1+2 = 3, 3+3 = 6, 6+4=10,
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

print("_" * 50)
# write a python program to print the fabonacci series
#     a   b   a+b
# 1,  2,  3,  5,  8, 13, 21, 33
# a,  b,  a+b


a = 0
b = 1
for _ in range(10):
    a, b = b, a + b
    # print("a:", a, "b:", b)
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

print("-" * 60)

#python Loops program to find the sum of all natural numbers between 1 to n using python.
n= int(input("Enter the last number: "))
total =0
for i in range(1, n+1):
  total += i
  print(total)
print("-"*50)
#Python program to find the sum of all even numbers between 1 to n using python.
n1= int(input("Enter the last number: "))
count = 0
for x in range(1, n+1):
     if x%2 == 0:
       count += x

print(count)

print("-"*50)
#Python loops program to enter a number and print it in words.
num = int(input("Enter a number: "))
count=0
for i in str(num):
     if i == "1":
         count += 1
         print("one", end="")
     elif i == "2":
         print("Two",end="")
     elif i == "3":
         print("Three",end="")
     elif i == "4":
         print("Four",end="")
     elif i == "5":
         print("Five",end="")
     elif i == "6":
         print("Six",end="")
     elif i == "7":
         print("Seven",end="")
     elif i == "8":
         print("Eight",end="")
     elif i == "9":
         print("Nine",end="")

print("-"*50)
# Write a program to count the number of digits in a number using python
num = "1234590"
count = 0
for _ in num:
 count += 1
 print("total number of digit is: ", count)

print("-"*50)
#write a python program to check given number is prime or not
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
