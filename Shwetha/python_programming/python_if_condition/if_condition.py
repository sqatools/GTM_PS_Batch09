#value = int(input("enter a value:"))
value = 123
if value >= 1000:
    print("yes")
else:
    print("no")

print("-"*25)

#value1 = int(input("enter a value1:"))
#value2 = int(input("enter a value2:"))
value1 = 10
value2 = 12
if value1 == value2:
    print("both are equal")
else:
    print("not equal")

print("-"*25)
'''
stu_mark = int(input("enter a marks:"))
if 40<=stu_mark<=50:
    print("c grade")
elif 50<=stu_mark<=65:
    print("b grade")
elif 65<=stu_mark<=75:
    print("a grade")
elif 75<=stu_mark<=100:
    print("distinction")
else:
    print("fail")

print("-"*25)

stu_mark = int(input("Enter marks (between 1 and 100): "))

if 1 <= stu_mark <= 100:  # Check if input is within the valid range
    if 40 <= stu_mark <= 50:
        print("C Grade")
    elif 50 <= stu_mark <= 65:
        print("B Grade")
    elif 65 <= stu_mark <= 75:
        print("A Grade")
    elif 75 <= stu_mark <= 100:
        print("A+ grade")
    else:
        print("Fail")
else:
    print("Invalid input! Please enter a number between 1 and 100.")
'''
print("-"*25)

'''
Problem Statement:

Write a program to determine if a given year is a leap year.
Conditions for a Leap Year:
The year must be divisible by 4.
If the year is divisible by 100, it must also be divisible by 400.
'''

leap_year = 1900 #2024,2000

if ((leap_year%4==0 and leap_year%100 !=0) or leap_year%400==0):
    print("leap year")
else:
    print("not a leap year")

print("-"*25)

#check the positive or negative numbers

num=0
if num > 0:
    print("pos")
elif num<0:
    print("neg")
else:
   print("zeo")

print("-"*25)

#check the number is even or odd

num=10
if num % 2 == 0:
    print("even")
else:
    print("odd")

print("-"*25)

#find the largest of 3 numbers

a,b,c = 30,40,40

if a>=b and a>=c:
   print("a is greater")
elif b>=a and b>=c:
    print("b is greater")
elif c>=a and c>=b:
    print("c is greater")
else:
    print("No one has greater")

print("-" * 25)
a = 30
b = 40
c = 40

if a > b and a > c:
    print("A has greater value :", a)
elif b > a and b > c :
    print("B has greater value :", b)
elif c > a and c > b :
    print("C has greater value :", c)
else:
    print("No one has greater")

print("-" * 25)

temperature = 3

if temperature > 25:
    print("It's a hot day!")
print("Enjoy your day.")

print("-" * 25)

temperature = 45

if temperature > 85:
    print("It's really hot outside.")
elif temperature > 70:
    print("It's warm outside.")
elif temperature > 55:
    print("It's cool outside.")
elif temperature > 32:
    print("It's cold outside.")
else:
    print("It's freezing outside!")

print("-" * 25)
#Program to get all numbers divided by 3 between 1 to 30

for i in range(1,31):
    if i%3 == 0:
        print(i,end=" ")
print()

print("-" * 25)



num =  50
# Check for division
if num%3 == 0  and num%5 == 0:
    # Print output
    print("Given number can divide by both 3 and 5")
else:
    # Print output
    print("Given number can not divide by 3 and 5")
