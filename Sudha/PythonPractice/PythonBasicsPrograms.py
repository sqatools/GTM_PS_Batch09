#Python Basic Programs, Exercises

#1). Python Program to add two integer values.
a = 10
b= 20
print("Solution 1 : Addition of two integer values :", a+b)

#2). Python Program to subtract two integer values.
print("Solution 2 : subtraction of two integer values :", b-a)

#3). Python program to multiply two numbers.
print("Solution 3 : Multiplication of two integer values :", a*b)



'''4). Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools” '''
str1 = "SQATools"
print("Solution 4 :", str1*5)

'''5). Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40'''

a = 40
b= 50
c= 30
Average1 = (40+50+30)/3 #Average =  40.0
Average2 = (40+50+30)//3 #Average =  40
print("Solution 5 : Average = ", Average1)
print("Solution 5 : Average = ", Average2)

"""6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66"""
print("Solution 6")
l1 = [45, 60, 61, 66, 70, 77, 80]
l1.sort()
n = len(l1)


"""

7). Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729
"""
print("Solution 7")
num1 = 9
print("Square = ",num1*2)
print("Cube = ",num1**3)

"""

Solution
8). Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10

"""
print("solution 8")
a = 10
b = 20
c = a
a = b
b = c
print("a = ", a)
print("b = ", b)
"""

Solution
9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)

Solution
10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab

"""
print(("_"*50))
a = 2
b = 3
LHS = (a+b)**2
x = a**2
y = b**2
z = 2*a*b
RHS = x+y+z
print(" Solution 10 \nLHS = ", LHS)
print("RHS = ", RHS)
print("LHS = RHS")

"""

Solution
11). Python program to solve the given math formula.
Formula : (a – b)2 = a^2 + b^2 – 2ab
"""
print(("_"*50))
a = 8
b = 4
LHS = (a-b)**2
x = a**2
y = b**2
z = 2*a*b
RHS = x+y-z
print(" Solution 11 \nLHS = ", LHS)
print("RHS = ", RHS)
print("LHS = RHS")
"""

Solution
12). Python program to solve the given math formula.
Formula : a2 – b2 = (a-b)(a+b)

"""
print(("_"*50))
a = 5
b = 2
x = a**2
y = b**2
LHS = x-y
z = (a-b)
M = (a+b)
RHS = z*M
print(" Solution 12 \nLHS = ", LHS)
print("RHS = ", RHS)
print("LHS = RHS")
"""


Solution
13). Python program to solve the given math formula.
Formula : (a + b)3 = a3 + 3ab(a+b) + b3 
"""
print(("_"*50))
a = 6
b = 4
sum = a+b
LHS = sum**3
x = a**3
y = b**3
z = 3*a*b*sum
RHS = x + z + y
print(" Solution 13 \nLHS = ", LHS)
print("RHS = ", RHS)
print("LHS = RHS")
"""

Solution
14). Python program to solve the given math formula.
Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

"""
print(("_"*50))
a = 6
b = 4
sum = a-b
LHS = sum**3
a3 = a**3
b3 = b**3
a2 = a**2
b2 = b**2
z = 3*a2*b
M = 3*a*b2
RHS = a3 - z + M - b3
print(" Solution 14 \nLHS = ", LHS)
print("RHS = ", RHS)
print("LHS = RHS")
"""
Solution
15). Python program to calculate the area of the square.
Formula : area = a*a
"""
print(("_"*50))
print("Solution 15")
side = int(input("Enter the side of a Square ="))
print("Area of Square = ", side**2)
"""

Solution
16). Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14

"""
print(("_"*50))
print("Solution 16")
radius = int(input("Enter the radius of a Circle = "))
Area = 3.14*radius*radius
print("Area of a Circle = ", Area)
"""

Solution
17). Python program to calculate the area of a cube.
Formula = 6*a*a

"""
print(("_"*50))
print("Solution 17")
side = int(input("Enter the side of a Cube = "))
print("Area of a Cube = ", 6*side*side)
"""
Solution
18). Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r

"""
print(("_"*50))
print("Solution 18")
r = int(input("Enter the Radius of the Cylinder = "))
h = int(input("Enter the Height of the Cylinder = "))
Area = (2*3.14*r*h) + (2*3.14*r*r)
print("Area of a Cylinder = ", Area)
"""

Solution
19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

Solution
20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time

"""
print(("_"*50))
print("Solution 20")
P = int(input("Enter the Principle Amount = "))
R = int(input("Enter Anual Interest Rate = "))
T = int(input("Time = "))
print("Simple Interest = ", P + ((P/R)*T))
"""

Solution
21). Python program to print the current date in the given format
Output: 2023 Jan 05
Note: Use the DateTime library

Solution
22). Python program to calculate days between 2 dates.
Input date : (2023, 1, 5) (2023, 1, 22)
Output: 17 days

Solution
23). Python program to get the factorial of the given number.

Solution
24). Python program to reverse a given number.

Solution
25). Python program to get the Fibonacci series between 0 to 50.

Solution
26). Python program to check given number is palindrome or not.

Solution
27). Python program to calculate compound interest.

Solution
28). Python program to check the prime number.

Solution
29). Python program to check leap year.

Solution
30). Python program to check for the anagram.
Note: rearrangement of the letters of a word to another word, using all the original letters exactly once.

Solution
31). Python program to generate random numbers.

Solution
32). Python program to generate a random string with a specific length.

Solution
33). Python program to get the current date.

Solution
34). Python program to convert Decimal to Binary.

Solution
35). Python program to find the sum of natural numbers.

Solution
36). Python program to find HCF.

Solution
37). Python program to find LCM.

Solution
38). Python program to find the square root of a number.
Note: Use the math library to get the square root.

Solution
39). Python program to calculate the volume of a sphere.
Formula = (4/3*pi*r^2)
r = radius
pi = 3

Solution
40). Python program to perform mathematical operations on two numbers
"""