"""for Loop
for <condition>:
     code

 """
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


print("-"*60)
"""Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700"""
for i in range(1500, 2701):
        if i%7 == 0 and i%5 == 0:
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

print("-"*60)
#WAP to get factorials of any number.
n1 = 5
fact = 1
for i in range(n1, 0, -1):

    fact = fact*i
print("Factorials of:", n1, ":", fact)
print("-"*60)
#Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for j in range(0, 7):
    if j != 3 or j != 6:
        print(j)

print("-"*60)
for n2 in range(0, 11):
    if n2 != 3 or n2 != 6:
        print(n2)
#get sum of all the value from 1 to 10.
output = 0
for i in range(1,11):
    output = output+i
print("output :", output)