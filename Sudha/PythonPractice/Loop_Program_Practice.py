"""
1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700
"""
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

print("_" * 50)
"""
2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
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
for i in range(1, 10):
    for j in range(1, 6):
        if i == 1 or i == 9:
            if j == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 2 or i == 8:
            if j == 1 or j == 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 3 or i == 7:
            if j == 1 or j == 2 or j == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 4 or i == 6:
            if j == 1 or j == 2 or j == 3 or j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

print("_" * 50)
"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
"""
print("_" * 50)

"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""
even = 0
odd = 0

for i in range(1, 10):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)

"""
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""
for i in range(0, 7):
    if i % 3 != 0:
        print(i)

"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
"""
a = 1
b = 0, 1
n = 20
for i in range(n):
    print(a)
    a, b = b, a + b
    """
print("_" * 50)
a, b = 0, 1

n = 20

for i in range(n):
    print(a)

    a, b = b, a + b

"""
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 
"""

print("_" * 50)
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")

"""
8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”

print("_" * 50)
string = input("Please enter the string = ")

for char in string:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char, end="")

8.OUTPUT
Please enter the string = sqaTOOLS
sqatools
"""

"""
9). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4

print("_" * 50)
character = 0
digits = 0
input1 = input("enter the string =")
for char in input1:
    if char.isalpha():
        character = character+1
    elif char.isnumeric():
        digits = digits+1

print("Characters = ", character)
print("Digits = ", digits)

9.output
enter the string =python1234
Characters =  6
Digits =  4
"""

"""
10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  


for i in range(0, 8):
    for j in range(0, 6):
        if i == 1 or i == 7:
            if j == 2 or j == 3 or j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
"""
"""
4). Python Loops program to print all even numbers between 1 to 100 in python.

print("-" * 50)
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
print()
"""
"""
15). Python Loops program to print all odd numbers between 1 to 100 using python.

print("_" * 50)


for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")

"""

"""
17). Python program to find the sum of all even numbers between 1 to n using python.
print("_"*50)
n = 5
sum1 = 0
for i in range(n):
    if i % 2 == 0:
        sum1 = sum1+i
print(sum1)

"""

"""
18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

n = int(input("Enter the last number = "))
total1 = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total1 = total1 + i
print("sum of all odd numbers from 1 to ", n, " = ", total1)
18.output
Enter the last number = 3
sum of all odd numbers from 1 to  3  =  4
"""

"""
19). Write a program to count the number of digits in a number using python.

num1 = '1234'
count1 = 0
for i in num1:
    count1 = count1+1
print("Total number of digits in given number = ", count1)

19.output
Total number of digits in given number =  4
"""

"""
20). Write a program to find the first and last digits of a number using python.

Solution 20
num1 = input("please enter the number = ")
length = int(len(num1))
print(length)
print(num1[0], num1[length-1])

20.output
please enter the number = 1234567
7
1 7

"""
"""
21). Write a program to find the sum of the first and last digits of a number using python.

21.Solution method 1

num1 = input("please enter the number = ")
length = int(len(num1))
print("First digit of the number = ", num1[0], " \n Second digit of the number = ", num1[length - 1], "\n Sum of "
                                                                                                      "those two "
                                                                                                      "number = ",
      int(num1[0]) + int(num1[length - 1]))

21.output
please enter the number = 123
First digit of the number =  1  
 Second digit of the number =  3 
 Sum of those two number =  4
"""
"""
21. solution method 2
num1 = int(input("Please enter the number = "))
str1 = str(num1)
total = 0
for i in range(len(str1)):
    if i == 0:
        total += int(str1[i])
    elif i == len(str1)-1:
        total += int(str1[i])

print("Sum of two number = ", total)
21.output
Please enter the number = 123456
Sum of two number =  7

"""

"""
22). Write a program to calculate the sum of digits of a number using python.

num1 = int(input("Please enter the number = "))
str1 = str(num1)
total = 0
for i in range(len(str1)):
    total = total+int(str1[i])

print(total)

22.output
Please enter the number = 256
13
"""
"""
23). Write a program to calculate the product of digits of a number using python.

num1 = int(input("Please enter the number = "))
str1 = str(num1)
total = 1
for i in range(len(str1)):
    total = total * int(str1[i])

print(total)
23.output
Please enter the number = 34
12
"""
"""
23.solution method two
num1 = int(input("Please enter the number = "))
product = 1
while num1 > 0:
    rem = num1 % 10
    product = product * rem
    num1 = num1 // 10

print(product)

output
Please enter the number = 34
12
"""

"""
24).Python loops program to enter a number and print its reverse using python.
"""
num1 = int(input("Please enter the number = "))
rev_Val = 0
while num1 > 0:
    temp = num1 % 10
    rev_Val = rev_Val*10 + temp

