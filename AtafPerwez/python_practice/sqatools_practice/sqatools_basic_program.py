# My python practice.py file, question taken from https://sqatools.in/python-basic-programs/
################


# 1). Python Program to add two integer values.
# Solution
a = 50
b = 100
print('addition of two intezer:', a+b)

# 2). Python Program to subtract two integer values.
# Solution
a = 50
b = 100
print('Subtraction of two integer:', a-b)

# 3). Python program to multiply two numbers.
# Solution
a = 50
b = 100
print('Multiplication of two integer:', a*b)

# 4). Python program to repeat a given string 5 times.
# Input :
str1 = "SQATools"
# Output :
# “SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
#
print(str1*5) #SQAToolsSQAToolsSQAToolsSQAToolsSQATools

# Solution
# 5). Python program to get the Average of given numbers.
# Formula: sum of all the number/ total number
# Input:
a = 40
b = 50
c = 30
# Output : 40
Average = (a+b+c)/3
print('Averqge of the no. is:', Average) # Averqge of the no. is: 40.0
#
# 6). Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2
# n = Number of values
#  : [45, 60, 61, 66, 70, 77, 80]
# Output:  66
# Solution
# median = (n+1)/2
numbers = [45, 60, 61, 66, 70, 77, 80, 100,30]
n = len(numbers)

if n % 2 ==1:
    median = numbers[n//2]
    print(median)
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    print(median)

# 7). Python program to print the square and cube of a given number.
# Input :
num1 = 9
square= num1**2
cube = num1**3
print('square of the no.:', square)
print('cube of the no.:', cube)
# Output :
# Square = 81
# Cube =   729
#
# Solution
# 8). Python program to interchange values between variables.
# Input :
# a = 10
# b = 20
# Output :
# a = 20
# b = 10
# Solution
a= 10
b =20
a,b = b,a
print('value of a:', a)
print('value of b:',b)

# 9). Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
#
# Solution

a= 80
b= 60
c = a**2 + b**2
print('your hypotenuse is:', c)

# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
#
# Solution
# (a + b)2 = a^2 + b^2 + 2ab
a = 10
b= 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print(f' |(a + b)2| RHS = {rhs} and LHS={lhs}')


# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
#
# Solution
a = 15
b= 25
lhs = (a-b)**2
rhs = a**2 + b**2 - 2*a*b
print(f'RHS = {rhs} and LHS={lhs}')

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
#
# Solution
a = 55
b = 45
lhs = a**2 - b**2
rhs = (a-b)*(a+b)
print(f'|a2 – b2| RHS = {rhs} and LSH = {lhs}')


# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
#
# Solution
a = 90
b = 120
lhs = (a+b)**3
rhs = a**3 + 3*a*b * (a+b)+b**3
print(f'|(a + b)3| LHS={lhs} and RHS= {rhs}')

# 14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
#
# Solution

a = 130
b = 120
lhs = (a-b)**3
rhs = a**3 - 3*a**2*b + 3*a*b**2 - b**3
print(f'(a – b)3|| LHS={lhs} and RHS= {rhs}')

# 15). Python program to calculate the area of the square.
# Formula : area = a*a
#
# Solution
a = 150
print(f'Area of a square is = {a*a}')


# 16). Python program to calculate the area of a circle.
#
# r = radius
# PI = 3.14
# Formula = PI*r*r
# Solution
r = 450
PI = 3.14
area = PI*r*r
print(f'Area of a circle of radius- {r} = {area}')

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
#
# Solution
a= 200
area = 6*a**2
print(f'area of a cube of side {a} = {area}')

# 18). Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
#
# Solution
pi = 3.14
r = 40
h = 60
area = (2*pi*r*h) + (2*pi*r**2)
print(f'area of the cylinder is: {area}')



# 19). Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
#
# Solution
num = 159
armstrong_no= 1**3 + 5**3 + 3**3
if num == armstrong_no:
    print(f'The number:{num} is a Armstrong Number')
else:
    print(f'the given no. {num} is not a Armstrong number')

# 20). Python program to calculate simple interest.
# Formula = P+(P/r)*t
# P = Principle Amount
# r = Anual interest rate
# t = time
#
# Solution
p = 90000
r = 9
t = 2
si = p*r*t/100
print(f'simple interest = {si}')

# 21). Python program to print the current date in the given format
# Output: 2023 Jan 05
# Note: Use the DateTime library
#
# Solution



# 22). Python program to calculate days between 2 dates.
# Input date : (2023, 1, 5) (2023, 1, 22)
# Output: 17 days
#
# Solution
# 23). Python program to get the factorial of the given number.
#
# Solution
# 24). Python program to reverse a given number.
#
# Solution
# 25). Python program to get the Fibonacci series between 0 to 50.
#
# Solution
# 26). Python program to check given number is palindrome or not.
#
# Solution
# 27). Python program to calculate compound interest.
#
# Solution
# 28). Python program to check the prime number.
#
# Solution
# 29). Python program to check leap year.
#
# Solution
# 30). Python program to check for the anagram.
# Note: rearrangement of the letters of a word to another word, using all the original letters exactly once.
#
# Solution
# 31). Python program to generate random numbers.
#
# Solution
# 32). Python program to generate a random string with a specific length.
#
# Solution
# 33). Python program to get the current date.
#
# Solution
# 34). Python program to convert Decimal to Binary.
#
# Solution
# 35). Python program to find the sum of natural numbers.
#
# Solution
# 36). Python program to find HCF.
#
# Solution
# 37). Python program to find LCM.
#
# Solution
# 38). Python program to find the square root of a number.
# Note: Use the math library to get the square root.
#
# Solution
# 39). Python program to calculate the volume of a sphere.
# Formula = (4/3*pi*r^2)
# r = radius
# pi = 3
#
# Solution
# 40). Python program to perform mathematical operations on two numbers.
#
# Solution