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
        print('No. divisible by 3 are:', i)
    # else:
    #     print('No are not divisible by 3 are:', i)

# 2). Python program to check the given number divided by 3 and 5.
print('# 3)')
x = 60
if x%3==0 and x%5==0:
    print('given no is divisible by 3 and 5')
else:
    print('given no is not divisible by 3 and 5')


# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
# marks = int(input('Enter your marks (1-99): '))
marks = 99
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
    print('Grade: Outstanding-Marvelous-fantastic--Party organised on Mars')
else:
    print('Invalid marked')



# 4). If else program to get all the numbers divided by 3 from 1 to 30.
print('#4')
for i in range(31):
    if i%3==0:
        print(f'No. divided by 3 is: {i}')
    else:
        print(f'No. not diivided by 3 is: {i}')




# 5). Python program to print the square of the number if it is divided by 11.
print('#5')
num = 88
if num %11 ==0:
    print(f'{num} is divisible by 11, square = {num**2}')
else:
    print(f'{num} is not divisible by 11')



# 6). Python program to check given number is a prime number or not. #doubt
print('#6')

num = 11
if num > 1:
    for i in range(2, num):
        print(i)
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# 7). Python program to check given number is odd or even.
print(f'#7 {">"*20}')
num = 9
if num%2 ==0:
    print(f'the no. {num} is a even number')
else:
    print(f'The number {num} is Odd Number')


# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
# Fibonacci series
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Take input through the user
# num = int(input("Enter a number: "))
num = 13
# Check for number in fibonacci series
if num in fib:
# Print output
    print("It is a part of the Fibonacci series")
else:
# Print output
    print("It is not a part of the series")


# 9). Python program to check authentication with the given username and password.
usr_name = 'perwez'
pas= 12345
input_id= 'perwez'
input_pas= 12345
if input_id == usr_name and input_pas == pas:
    print(f'Success! you have entered valid username and password')
else:
    print(f'Failed! Enter valid user name and password')



# 10). Python program to validate user_id in the list of user_ids.
print('#10#')
id_list = [111, 222, 333, 444, 555, 666]

# input_id = int(input("Enter ID number: "))
input_id = 33

if input_id in id_list:
    print("Valid ID")
else:
    print("Invalid ID")



# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
print('# 11 #')
num = 789
if num%2 == 0:
    print("Sqaure: ",num**2)

elif num%3 == 0:
    print("Cube: ",num**3)

# Solution
# 12). Python program to describe the interview process.
print('#12')
round1 = 'passed'
round2 = 'passed'
round3 = 'passed'

if round1 == "passed":
    print("Congrats your 1st round is clear")
    if round2 == "passed":
        print("Congrats 2nd round is clear")
        if round3 == 'passed':
            print('Congratulation! you are placed')
        else:
            print('Failed in the 3rd round')
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")




# 13). Python program to determine whether a given number is available in the list of numbers or not.
print('#13')
list1 = [22,33,49,34,65,67,12,25]
num = 25

if num in list1:
    print(f"{num} is available in the list")
else:
    print(f"{num} is not available in the list")

# 14). Python program to find the largest number among three numbers.
print('#14')
num1 = 19
num2 = 51
num3 = 93

if num1 > num2:
    if num1 > num3:
        print(f'{num1} is the greatest')
    else:
        print(f'{num3} is the greatest')
else:
    if num2>num3:
        print(f'{num2} is the greatest')
    else:
        print(f'{num3} is the greatest')


# 15). Python program to check any person eligible to vote or not
print('#15')
age = 2

if age >= 18:
    print("You are eligible to VOte")
else:
    print("You are not eligible to vote")


# 16). Python program to check whether any given number is a palindrome.
print('#16')
num1 = 121
num2 = str(num1)

if num1 == int(num2[::-1]):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")


# 17). Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome
print('#17')
name = 'LuL'
if name == name[::-1]:
    print(f'Given name |{name}| is Palindrome')
else:
    print(f'Given name |{name}| is not a palindrome')

#
# Solution
# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
print('#18')
input_marks= 99

if input_marks >=35:
    print('passed')
else:
    print('failed')

# 19). Python program to check whether the given number is positive or not.
print('#19')
input_num= -65
if input_num > 0:
    print(f' Number is positive')
else:
    print(f'Number is negetive')


# 20). Python program to check whether the given number is negative or not.
print('#20')
input_num= 3
if input_num < 0:
    print(f'Negative: True')
else:
    print(f'Negative: False')




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