# Python If else Practice Programs, Exercises

# 1). Python program to check given number is divided by 3 or not.
x = 16
if x%3==0 and x%5==0:
    print('given no is divisible by 3 and 5')
else:
    print('given no is not divisible by 3 and 5')
# 2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1, 31):
    if i%3==0:
        print('No divisible by 3 are:', i)
    # else:
    #     print('No are not divisible by 3 are:', i)


# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
marks = int(input('Enter your marks (1-99): '))
if marks < 40:
    print("FAILED! - Parrent's Meeting organised at white house")
elif marks > 40 and marks <= 50:
    print('Grade: C')
elif marks > 50 and marks <= 60:
    print('Grade: B')
elif marks > 60 and marks <= 70:
    print('Grade: A')
elif marks > 70 and marks <= 80:
    print('Grade: A+')
elif marks > 80 and marks <= 90:
    print('Grade: A++')
elif marks > 90 and marks <= 99:
    print('Grade: Outstanding-Marvelous-fantastic--Party organised on the Mars')
else:
    print('Invalid marked')

# 4). Python program to check the given number divided by 3 and 5.
#
# Solution
# 5). Python program to print the square of the number if it is divided by 11.
#
# Solution
# 6). Python program to check given number is a prime number or not.
#
# Solution
# 7). Python program to check given number is odd or even.
#
# Solution
# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
#
# Solution
# 9). Python program to check authentication with the given username and password.
#
# Solution
# 10). Python program to validate user_id in the list of user_ids.
#
# Solution
#
#
# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
#
# Solution
# 12). Python program to describe the interview process.
#
# Solution
# 13). Python program to determine whether a given number is available in the list of numbers or not.
#
# Solution
# 14). Python program to find the largest number among three numbers.
#
# Solution
# 15). Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible
#
# Solution
# 16). Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome
#
# Solution
# 17). Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome
#
# Solution
# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
# Output = Pass
#
# Solution
# 19). Python program to check whether the given number is positive or not.
# Input = 20
# Output = True
#
# Solution
# 20). Python program to check whether the given number is negative or not.
# Input = -45
# Output = True
#
# Solution
#
# 21). Python program to check whether the given number is positive or negative and even or odd.
# Input = 26
# Output = The given number is positive and even
#
# Solution
# 22). Python program to print the largest number from two numbers.
# Input:
# 25, 63
# Output = 63
#
# Solution
# 23). Python program to check whether a given character is uppercase or not.
# Input = A
# Output = The given character is an Uppercase
#
# Solution
# 24). Python program to check whether the given character is lowercase or not.
# Input = c
# Output = True
#
# Solution
# 25). Python program to check whether the given number is an integer or not.
# Input = 54
# Output = True
#
# Solution
# 26). Python program to check whether the given number is float or not.
# Input = 12.6
# Output = True
#
# Solution
# 27). Python program to check whether the given input is a string or not.
# Input = ‘sqatools’
# Output = True
#
# Solution
# 28). Python program to print all the numbers from 10-15 except 13
# Output:
# 10
# 11
# 12
# 14
#
# Solution
# 29). Python program to find the electricity bill. According to the following conditions:
# Up to 50 units rs 0.50/unit
# Up to 100 units rs 0.75/unit
# Up to 250 units rs 1.25/unit
# above 250 rs 1.50/unit
# an additional surcharge of 17% is added to the bill
# Input = 350
# Output = 438.75
#
# Solution
# 30). Python program to check whether a given year is a leap or not.
# Input = 2000
# Output = The given year is a leap year
#
# Solution
# 31). Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.
# Input = 14
# Output = Fizz
# Input = 9
# Output = Buzz
# Input = 6
# Output = FizzBuzz
#
# Solution
# 32). Python program to check whether an alphabet is a vowel.
# Input = A
# Output = True
#
# Solution
# 33). Python program to check whether an alphabet is a consonant.
# Input = B
# Output = True
#
# Solution
# 34).  Python program to convert the month name to the number of days.
# Input = February
# Output = 28/29 days
#
# Solution
# 35). Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal.
# Input:
# Enter the length of the sides of the triangle
# A=10
# B=10
# C=10
# Output = True
#
# Solution
#
# 36). Python program to check whether a triangle is scalene or not. A scalene triangle is a triangle that has three unequal sides.
# Input:
# Enter the length of the sides of the triangle
# A=10
# B=15
# C=18
# Output = True
#
# Solution
# 37). Python program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides.
# Input:
# Enter the length of the sides of the triangle
# A=10
# B=15
# C=10
# Output = True
#
# Solution
# 38). Python program that reads month and returns season for that month.
# Input = February
# Output = Summer
#
# Solution
# 39). Python program to check whether the input number is a float or not if yes then round up the number to 2 decimal places.
# Input = 25.3614
# Output = 25.36
#
# Solution
# 40). Python program to check whether the input number is divisible by 12 or not.
# Input = 121
# Output = True
#
# Solution
#
# 41). Python program to check whether the input number is a square of 6 or not.
# Input = 37
# Output = False
#
# Solution
# 42). Python program to check whether the input number is a cube of 3 or not.
# Input = 27
# Output = True
#
# Solution
# 43). Python program to check whether two numbers are equal or not.
# Input:
# A=26,B=88
# Output = The given numbers are not equal
#
# Solution
# 44). Python program to check whether the given input is a complex type or not.
# Input:
# a=5+6j
# Output: True
#
# Solution
# 45). Python program to check whether the given input is Boolean type or not.
# Input:
# a=True
# Output = The given variable is Boolean
#
# Solution
# 46). Python program to check whether the given input is List or not.
# Input:
# a=[1,3,6,8]
# Output = True
#
# Solution
# 47). Python program to check whether the given input is a dictionary or not.
# Input:
# A={‘name’:’Virat’,’sport’:’cricket’}
# Output = True
#
# Solution
# 48). Python program to check the eligibility of a person to sit on a roller coaster ride or not. Eligible when age is greater than 12.
# Input = 15
# Output = You are eligible
#
# Solution
# 49). Python program to create 10 groups of numbers between 1-100 and find out given input belongs to which group using python nested if else statements.
# Input= 36
# Output = The given number belongs to 4th group
#
# Solution
# 50). Python program to find employees eligible for bonus. A company decided to give a bonus of 10% to employees. If the employee has served more than 4 years. Ask the user for years served and check whether an employee is eligible for a bonus or not.
# Input = Enter Years served: 5
# Output = You are eligible for a bonus
#
# Solution
# 51). Take values of the length and breadth of a rectangle from the user and check if it is square or not using the python if else statement.
# Input:
# Length= 4
# Breadth= 5
# Output = It is not a square
#
# Solution
# 52). A shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000. Using the python program Calculate the discount based on the bill.
# Input = 1500
# Output = Discount amount: 150
#
# Solution
#
# 53). Python program to print the absolute value of a number defined by the user.
# Input = -1
# Output = 1
#
# Solution
# 54). Python program to check the student’s eligibility to attend the exam based on his/her attendance. If attendance is greater than 75% eligible if less than 75% not eligible.
# Input = Enter attendance: 78
# Output = You are eligible
#
# Solution
# 55). Python program to check whether the last digit of a number defined by the user is divisible by 4 or not.
# Input = 58
# Output = The last digit is divisible by 4
#
# Solution
# 56). Python program to display 1/0 if the user gives Hello/Bye as output.
# Input = Enter your choice: Hello
# Output = 1
# Input = Enter your choice: Bye
# Output = 0
#
# Solution
# 57). Python program to accept the car price of a car and display the road tax to be paid according to the following criteria:
# Cost price<500000 –> tax:15000
# Cost price<1000000 –> tax:50000
# Cost price<1500000 –> tax:80000
# Input = Car Price: 1200000
# Output = Tax payable: 50000
#
# Solution
# 58). Using a python program take input from the user between 1 to 7 and print the day according to the number. 1 for Sunday 2 for Monday so on.
# Input = Enter number: 7
# Output = Saturday
#
# Solution
# 59). Python program to accept the city name and display its monuments (take Pune and Mumbai as cities).
# Input = Enter city name: Pune
# Output:
# Shaniwar vada
# Lal mahal
# Sinhgad fort
#
# Solution
# 60). Python program to check whether the citizen is a senior citizen or not. An age greater than 60 than the given citizen is a senior citizen.
# Input = Enter age: 70
# Output = The given citizen is a senior citizen
#
# Solution
# 61). Python program to find the lowest number between three numbers.
# Input:
# A=45
# B=23
# C=68
# Output = 23
#
# Solution
# 62). Python program to accept the temperature in Fahrenheit and check whether the water is boiling or not.
# Hint: The boiling temperature of water in Fahrenheit is 212 degrees
# Input = Enter temperature: 190
# Output = Water is not boiling
#
# Solution
# 63). Python program to accept two numbers and mathematical operations from users and perform mathematical operations according to it.
# Input:
# A=30
# B=45
# Operation = +
# Output = 75
#
# Solution
# 64). Python program to accept marks from the user allot the stream based on the following criteria.
# Marks>85: Science
# Marks>70: Commerce
# 35<Marks<70: Arts
# Marks<35: Fail
# Input = Marks: 88
# Output = Science
#
# Solution