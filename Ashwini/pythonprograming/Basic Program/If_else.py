# compair two number
n1 = 20
n2 = 20
# print(n1 == n2)
if n1 == n2:
    print("both number are equal")
else:
    print("number are not equal")

print("-" * 50)
# write program to check even number and odd numbers
num1 = 57
if num1 % 2 == 0:
    print("This is even number:", num1)
else:
    print("This is odd number:", num1)

print("-" * 50)
# Python program to check given number is divided by 3 or not.
num2 = 13
if num2 % 3 == 0:
    print("this number is divided by 3:", num2)
else:
    print("this number is not divided by 3:", num2)
print("-" * 50)
# If else program to get all the numbers divided by 3 from 1 to 30.

# wap to print squre value if it is even else print cube of the value
p = 6
Result = p ** 2 if p % 2 == 0 else p ** 3
print("Result:", Result)

print("-" * 50)

### Logical Operator #########
"""AND Operator
cond1 and cond2
true and false = false
false and true = false
true and true = true
false and false = false

OR Operator
cond1 or cond2
True or False = True
False or True = True
True or True = True
False or False = False
"""
# Python program to check the given number divided by 3 and 5.
n1 = 15
if n1 % 3 == 0 and n1 % 5 == 0:
    print("this number is divided by 3 and 5:", n1)
else:
    print("this number is not divided by 3 and 5:", n1)
print("-" * 50)

# Python program to check the given number divided by 3 or 5.
x = 9
if x % 3 == 0 or x % 5 == 0:
    print("This number is divide by 3 or 5:", x)
else:
    print("This number is not divide by 3 or 5:", x)
print("-" * 50)

# Python program to check whether the given number is positive or not.
# Input = 20
# Output = True
# num = int(input("Enter a number: "))
num = 20
if num > 0:
    print("True")
else:
    print("False")
print("-" * 50)
# Python program to check whether the given number is negative or not.
# Input = -45
# Output = True
y = -45
if y < 0:
    print("True")
else:
    print("False")
print("-" * 50)
"""Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
Input = Enter marks: 45
Output = Pass"""
User = int(input("Enter the marks:"))
if User > 35:
    print("pass")
else:
    print("Fail")
print("-" * 50)
""" Python program to check whether the given number is positive or negative and even or odd."""

num = int(input("Enter a number:"))
if num > 0:
    if num % 2 == 0:
        print("The given number is positive and even")
    else:
        print("The given number is positive and odd")
else:

    if num % 2 == 0:
        print("The given number is negative and even")
    if num % 2 == 0:
        print("The given number is negative and even")
    else:
        print("The given number is negative and odd")
# Python program to print the square of the number if it is divided by 11.
User = int(input("Enter the number:"))
if User % 11 == 0:
    print("the squer of number is:", User ** 2)
else:
    print("the number is not divided by 11:")

print("-" * 50)
# Python program to check authentication with the given username and password.
name = input("Enter the Name:")
password = input("Enter The password:")
if name == password:
    print("User is valid")
else:
    print("User is invalid")
print("-" * 50)
"""If else program to get all the numbers divided by 3 from 1 to 30.
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
if y % 3 == 0:
    print("all the number divided by 3:", y)
else:
    print("all the number not divided by 3:", y)"""
# Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
num = int(input("enter the number:"))
if num % 2 == 0:
    print("squre of number:", num ** 2)
else:
    print("cube of number:", num ** 3)