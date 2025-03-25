# 1). Python Program to add two integer values.

a = 10
b = 20
print(a+b)

#2). Python Program to subtract two integer values.

a=50
b=10
print(b-a)

#3). Python program to multiply two numbers.
a=5
b=2
print(a*b)

"""
4). Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
 """
str1 = 'SQATools'
print(str1*5)

"""
5). Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40
"""
a = 40
b = 50
c = 30
avg= (a+b+c)/3
print(avg)

"""
7). Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729
"""
num1 = 9
square = num1**2
cube = num1**3
print("square of num1 is:", square)
print("cube of num1 is:", cube)

"""
8). Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10
"""
a = 10
b = 20

a,b = b,a
print(a)
print(b)

"""9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)
"""
a=3
b=4
c=5
lhs = (a**2) + (b**2)
rhs = c**2
print("lhs is:",lhs)
print("RHS is:", rhs)

"""
10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab
"""
a=5
b=6
LHS = (a+b)**2
RHS = a**2 + b**2 + 2*a*b
print(LHS)
print(RHS)

"""
11). Python program to solve the given math formula.
Formula : (a – b)2 = a^2 + b^2 – 2ab
"""
a = 5
b = 3
LHS = (a-b)**2
RHS = a**2 + b**2 -2*a*b

print("LHS of 11th ques is:", LHS)
print("RHS of 11th ques is:", RHS)
print("--"* 50)
"""
12). Python program to solve the given math formula.
Formula : a2 – b2 = (a-b)(a+b)
"""
a= 2
b = 3
LHS = a**2 - b**2
RHS = (a-b)*(a+b)
print(LHS)
print("RHS ==: ", RHS)

print("--"* 50)

"""
13). Python program to solve the given math formula.
Formula : (a + b)3 = a3 + 3ab(a+b) + b3 
"""
a= 3
b=5
LHS = (a+b)**3
RHS = a**3 + 3*a*b*(a+b) + b**3

print(LHS)
print(RHS)

print("*"* 50)
"""
14). Python program to solve the given math formula.
Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
"""
a= 6
b= 3
LHS = (a-b)**3
RHS = a**3 - 3*a**2*b + 3*a*b**2 - b**3
print(LHS)
print(RHS)

print("*"* 50)

"""
15). Python program to calculate the area of the square.
Formula : area = a*a
"""
a = 25
area = a*a
print(area)
print("%"* 50)
"""
16). Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14
"""
r= 5
PI = 3.14
radius = PI * r*r
print(radius)

"""
17). Python program to calculate the area of a cube.
Formula = 6*side*side
"""

side = 4
area = 6*side*side
print(area)

print("$"*100)
"""
18). Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r
"""
PI =3.14
r= 5
h= 20
area= 2*PI*r*h + 2*PI*r*r

print(int(area))

"""
20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Annual interest rate
t = time
"""
P = 1000
r =2
t = 6
SI = P+(P/r)*t
print(SI)

"""
27). Python program to calculate compound interest.
p = int(input("Enter principle amount: "))
r = float(input("Enter interest rate: "))
n = int(input("Enter number of years: "))

amount = p*((1+r/100)**n)
"""
p = 1000
r =2
n = 1
amount = p*((1+r/100)**n)
print(amount)


"""

21). Python program to print the current date in the given format
Output: 2023 Jan 05
Note: Use the DateTime library

22). Python program to calculate days between 2 dates.
Input date : (2023, 1, 5) (2023, 1, 22)
Output: 17 days


23). Python program to get the factorial of the given number.

24). Python program to reverse a given number.

25). Python program to get the Fibonacci series between 0 to 50.

26). Python program to check given number is palindrome or not.

27). Python program to calculate compound interest.

28). Python program to check the prime number.


29). Python program to check leap year.

30). Python program to check for the anagram.
Note: rearrangement of the letters of a word to another word, using all the original letters exactly once.


31). Python program to generate random numbers.


32). Python program to generate a random string with a specific length.

33). Python program to get the current date.
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
40). Python program to perform mathematical operations on two numbers.
"""

"""
6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
"""

"""
a = input()
b = input()
if (a+b)**2 == a**2 + b**2 + 2*a*b:
    print("Lhs=RHS")
else:
    print("LHS!=RHS")"""


"""
19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
"""