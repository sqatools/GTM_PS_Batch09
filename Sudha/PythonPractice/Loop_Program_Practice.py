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
"""

"""
21). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even
"""

n = 26
if n >= 0:
    if n % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is Positive and odd")
else:
    if n % 2 == 0:
        print("The number is negative and even")
    else:
        print("The number is negative and odd")

