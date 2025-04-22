
#21). Python program to print the current date in the given format
#Output: 2023 Jan 05
#Note: Use the DateTime library

from datetime import date
from datetime import datetime
today = date.today()
print("Today's date is : ",today)

formatteddate = today.strftime("%Y %b %d")
print("Today's date ins tring format: ",formatteddate)

#22). Python program to calculate days
# between 2 dates.
#Input date : (2023, 1, 5) (2023, 1, 22)
#Output: 17 days
date1 = date(2023,1,5)
date2 = date(2023,1,22)

difference = (date2-date1).days
print("The difference between days ",date1, " and ", date2 ," is :" , difference)

#23). Python program to get the factorial of the given number.
num1  = 5
sum1 = 1
# For loop
for i in range(1, (num1+1)):
    sum1 = sum1 * i
print("Factorial of given number ", num1 , "is :", sum1)
#while loop
sum1 = 1
i= 1
while(i <= num1):
    sum1 = sum1 * i
    i+=1

print("While Loop Factorial of given number ", num1 , "is :", sum1)


#24). Python program to reverse a given number.

num1 = 1234
reverse = 0
while (num1 > 0):
    rem = num1 % 10
    print(rem)
    num1 = num1 // 10
    print("Remaining num : ", num1)
    reverse = rem + reverse * 10

print("Reverse is ", reverse)


#25). Python program to get the Fibonacci series between 0 to 50.

num1 = 0
num2 = 1
print("Fibbonaci Series is : ",num1, " ", num2, end=" ")
while (num2 < 50):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print( num3, end = " ")



#26). Python program to check given number is palindrome or not.
num1 = 234542
original = num1
reverse = 0
while (num1 > 0):
    rem = num1 % 10
    print(rem)
    num1 = num1 // 10
    print("Remaining num : ", num1)
    reverse = rem + reverse * 10

print("Reverse number is : ", reverse)

if (reverse == original):
    print("Given number is palindrome ")
else:
    print("Not a palindrome")

#27). Python program to calculate compound interest.


#28). Python program to check the prime number.
num1 = 2
flag = 0
for i in range(2, int(num1/2)):
    if((num1 != 2) and ((num1%i) == 0)):
        flag+=1
        print("i ", i , " flag = ", flag)

if (flag > 0):
    print("Give number ", num1, " is not a prime")
else:
    print("Given number ", num1 , " is Prime")



#29). Python program to check leap year.
year = 2008 #2024 #1990 2012 2016 2020 2024
if( ((year % 4 ==0 ) and (year % 100 !=0 )) or (year % 400 ==0) ):
    print("This year ,",year ," is a leap year")
else:
    print("Given year ", year ," is not a leap year")

#30). Python program to check for the anagram.
#Note: rearrangement of the letters of a word to another word, using all the original letters exactly once.


#31). Python program to generate random numbers.


#32). Python program to generate a random string with a specific length.


#33). Python program to get the current date.


#34). Python program to convert Decimal to Binary.


#35). Python program to find the sum of natural numbers.


#36). Python program to find HCF.


#37). Python program to find LCM.


#38). Python program to find the square root of a number.
#Note: Use the math library to get the square root.


#39). Python program to calculate the volume of a sphere.
#Formula = (4/3*pi*r^2)
#r = radius
#pi = 3


#40). Python program to perform mathematical operations on two numbers.