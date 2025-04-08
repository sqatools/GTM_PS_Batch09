


# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# Input1:1500
# Input2:2700
print('Q1')
for i in range(1500, 2700, 1):
    if i%7==0 and i%5==0:
        # print(f'No. divisible by 7 and 5 in this range are: {i}')
        print(i, end=" | ")

# Solution
# 2). Python Loops program to construct the following pattern, using a nested for loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
print('Q2')

for i in range(0, 6, 1):
    print(i*"*")
for i in range(6, 0, -1):
    print(i*"*")
#
# 3). Python Loops program that will add the word from the user to the empty string using python.
# Input: “python”
# # Output : “python”
# Take a word as input from the user.
# Create an empty string.
# Add each character from the input word to the empty string using for loop with the range function.
# Print the output.
#
# user_input= input(str('please enter any word: '))
print('----Q3------')
user_input= "Time Stone"
word = ""
for i in range(len(user_input)):
    word += user_input[i]
print(word)


# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Output :
# Number of even numbers: 4
# Number of odd numbers: 5
print('------Q4------')
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in numbers:
    if i%2 ==0:
        even += 1
    else:
        odd +=1
print(f'No of even: {even}')
print(f'No of odd: {odd}')


# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
print('------Q5------')
# for i in range(1,7,3):
#     print(i)
for i in range(1,7):
    if i!=3 and i!=6:
        print(i)

#
# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
# Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
print('------Q6------')

# Solution
# 7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.
print('------Q7------')
for i in range(1, 31):
    if i % 3 ==0:
        print('Fizz')

    elif i % 5 ==0:
        print('Buzz')

# 8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
# Input : “SqaTOOlS”
# Output : “sqatools”
print('------Q8------')
word = "UPPER roller, LOWER roller"
print(word.lower())

for l in word:
    if l.isupper():
        print(l.lower(), end="")
    else:
        print(l, end="")


# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
# Input : “python1234”
# Output :
# Letters 6
# Digits 4
print('\n------Q9------')
word = 'python1234'
digits= 0
char= 0

for e in word:
    if e.isalpha():
        char+=1
    elif e.isnumeric():
        digits+=1

print(f'Digits: {digits} and Characters: {char}')



# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# Output:
#   ***
# *      *
# *      *
# *      *
# *      *
# *      *
#    ***
print('------Q10------')
for i in range(1, 8):
    for j in range(1,8):
        if i ==1 or i == 7:
            print('*', end=" ")
        elif j ==1 or j == 7:
                print('*', end=" ")
        else:
            print(" ", end=" ")
    print()

# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
print('------Q11------')
n = 21
count = 0
while count<= n:
    print(count, end=" ")
    count+=1
# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
print('\n------Q12------')
n = 30
count = n
while count !=0:
    print(count, end=" ")
    count -=1



# 13). Python Loops program to print all alphabets from a to z using for loop
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’
#         A-Z ASCII Range  65-90
#         a-z ASCII Range  97-122
print('------Q3------')
import string
for letter in string.ascii_lowercase:
    print(letter, end=" ")
print()
for letter in string.ascii_uppercase:
    print(letter, end=" ")
# 14). Python Loops program to print all even numbers between 1 to 100 in python.
print('\n------Q4------')
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")
# 15). Python Loops program to print all odd numbers between 1 to 100 using python.
print('------Q5------')
for i in range(1,101):
    if i%2 !=0:
        print(i, end=" ")
# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
print('\n------Q16-----')
n = 15
total = 0
for i in range(1, n+1):
    total +=i
    print(total, end=" ")

# 17). Python program to find the sum of all even numbers between 1 to n using python.
print('\n------Q17------')
n = 20
total = 0

for i in range(1,n+1):
    if i%2 == 0:
        total += i

print(total)

# 18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
print('\n------Q18------')

# 19). Write a program to count the number of digits in a number using python.
print('------Q19------')

# 20). Write a program to find the first and last digits of a number using python.
print('------Q20------')

# 21). Write a program to find the sum of the first and last digits of a number using python.
#
# Solution
# 22). Write a program to calculate the sum of digits of a number using python.
#
# Solution
# 23). Write a program to calculate the product of digits of a number using python.
#
# Solution
# 24).Python loops program to enter a number and print its reverse using python.
#
# Solution
# 25). Write a program to check whether a number is a palindrome or not using python loops.
#
# Solution
# 26). Program to find the frequency of each digit in a given integer using Python Loops.
#
# Solution
# 27). Python loops program to enter a number and print it in words.
#
# Solution
# 28). Python loops program to find the power of a number using Python for loop. Take values as an input base number and power, and get the total value using a loop.
#
# Solution
# 29). Python loops program to find all factors of a number using Python. Get all the numbers that can divide this number from 1 to n.
#
# Solution
# 30). Write a program to calculate the factorial of a number using Python Loops.
#
# Solution
# 31). Write a program to check whether a number is a Prime number or not using Python Loops.
#
# Solution
# 32). Write a program to print all Prime numbers between 1 to n using Python Loops.
#
# Solution
# 33). Python loops program to find the sum of all prime numbers between 1 to n using Python.
#
# Solution
#
# 34). Python loops program to find all prime factors of a number using Python Loops.
#
# Solution
# 35). Python loops program to check whether a number is an Armstrong number or not using Python Loops.
#
# Armstrong Example : 153 = 1*1*1 + 5*5*5 + 3*3*3
# Solution
# 36). Python loops program to print all Armstrong numbers between 1 to n using Python Loops.
#
# Armstrong Example : 153 = 1*1*1 + 5*5*5 + 3*3*3
# Solution
# 37). Write a program to check whether a number is a Perfect number or not using Python.
# Get factors of any number and the sum of those factors should be equal to the given number. The factor of 28: 1, 2, 4, 7, 14, and their sum is 28.
# Solution
# 38). Python loops program to print all Perfect numbers between 1 to n using Python. The factor of 28: 1, 2, 4, 7, 14, and their sum is 28.
# Solution
# 39). Python loops program to print the Fibonacci series up to n terms using Python Loops.
# 0, 1, 1, 2, 3, 5, 8, 13, 21 …..n
# Solution
# 40). Python loops program to print the multiplication table of any number using Python Loops.
#
# Solution
# 41).  Python loops program to print the pattern T using Python Loops.
#
#        Output :
#
#        * * * * * * * * *
#        * * * * * * * * *
#                * * *
#                * * *
#                * * *
#                * * *
#                * * *
# Solution
# 42).  Write a program to print number patterns using Python Loops.
#
#      Output:
#
#      1
#      2   3
#      4   5   6
#      7   8   9   10
#      11  12  13  14  15
#      14  13  12  11
#      10  9   8
#      7   6
#      5
# Solution
#
# 43). Write a program to print the pattern A using Python Loops.
#
#     Output :
#
#        *  *  *
#     * * * * * *
#     * *      * *
#     * *      * *
#     * * * * * *
#     * * * * * *
#     * *      * *
#     * *      * *
#     * *      * *
# Solution
# 44). Write a program to print the pyramid structure using Python Loops.
#
#     Output:
#
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# Solution
# 45). Write a program to count total numbers of even numbers between 1-100 using Python Loops.
# Output = 50
#
# Solution
# 46). Write a program to count the total numbers of odd numbers between 1-100 using Python Loops.
# Output = 50
#
# Solution
# 47). Write a program to get input from the user if it is a number insert it into an empty list using Python Loops.
# Input :
# L=[]
# 125python
# Output = [1,2,5]
#
# Solution
# 48). Write a program to get input from the user if it is a string insert it into an empty list using Python Loops.
# Input :
# L=[]
# ‘sqatools007’
# Output = [‘s’,’q’,’a’,’t’,’o’,’o’,’l’,’s’]
#
# Solution
# 49). Write a program to accept the kilometers covered and calculate the bill according to the following using Python Loops.
# First 5 km- 15rs/km
# Next 20 km- 12rs/km
# After that- 10rs/km
#
# Solution
# 50). Write a program to input electricity unit charges and calculate the total electricity bill according to the given condition using Python Loops.
# For the first 50 units Rs. 0.50/unit.
# For the next 100 units Rs. 0.75/unit.
# For the next 100 units Rs. 1.25/unit.
# For units above 250 Rs. 1.50/unit.
# An additional surcharge of 17% is added to the bill.
# Input = 350
# Output = 438.75
#
# Solution
#
# 51). Write a program to calculate the sum of all odd numbers between 1-100 using Python Loops.
# Output = 2500
#
# Solution
# 52). Find the numbers which are divisible by 5 in 0-100 using Python Loops.
#
# Solution
# 53). Write a program to construct the following pattern, using a for loop in Python.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
#
# Solution
# 54). Write a program to construct the following pattern, using a for loop in Python.
# Output :
# * * * * *
# * * * *
# * * *
# * *
# *
#
# Solution
# 55). Write a program to construct the following pattern, using a nested for loop in Python.
# Output :
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
#
# Solution
# 56). Write a program to get the Fibonacci series between 0 to 10 using Python Loops.
# Output = 0 1 1 2 3 5 8 13 21 34 55
#
# Solution
# 57). Write a program to check the validity of password input by users using Python Loops.
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 5 characters.
# Maximum length 15 characters.
# Input = Abc@1234
# Output = Valid password
#
# Solution
# 58). Write a program to check whether a string contains an integer or not using Python Loops.
# Input = Python123
# Output = True
#
# Solution
# 59). Write a program to print the following pattern using Python Loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# Solution
#
# 60). Write a program to print a table of 5 using for loop using Python Loops.
# Output :
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
#
# Solution
# 61). Write a program to print the first 20 natural numbers using for loop in Python.
# Output = 1,2,3,….,20
#
# Solution
# 62). Write a program to display numbers from a list using Python Loops.
# Input = [1,5,8,0,4]
# Output = 1,5,8,0,4
#
# Solution
# 63). Write a program to print each word in a string on a new line using Python Loops.
# Input = Sqatools
# Output :
# S
# q
# a
# t
# o
# o
# l
# s
#
# Solution
# 64). Write a program to create an empty list and add even numbers from 1-10 in it including 10 using Python Loops.
# Input = []
# Output :
# [2,4,6,8,10]
#
# Solution
# 65). Write a program to create an empty list and add odd numbers from 1-10 in it including 1 using Python.
# Input = []
# Output : [1,3,5,7,9]
#
# Solution
# 66). Write a program to print the keys of a dictionary using Python Loops.
# Input = {‘name’:’virat’,’sports’:’cricket’}
# Output :
# name
# cricket
#
# Solution
# 67). Write a program to print the values of the keys of a dictionary using Python.
# Input = {name’:’virat’,’sports’:’cricket’}
# Output :
# Virat
# Cricket
#
# Solution
# 68). Write a program to print the keys and values of a dictionary using Python Loops
# Input = {name’:’virat’,’sports’:’cricket’}
# Output :
# name Virat
# sports cricket
#
# Solution
# 69). Write a program to print the first 20 natural numbers using a while loop in Python.
#
# Solution
#
# 70). Write a program to print a table of 2 using a while loop in Python.
# Output :
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
#
# Solution
# 71). Find the sum of the first 10 natural numbers using the while loop in Python Loops.
# Output = 55
#
# Solution
# 72). Find the multiplication of the first 10 natural numbers using Python Loops.
# Output = 3628800
#
# Solution
# 73). Print numbers from 1-10 except 5,6 using a while loop in Python.
# Output :
# 1
# 2
# 3
# 4
# 7
# 8
# 9
# 10
#
# Solution
# 74). Write a program to print the days in a week except Sunday using a while loop in Python.
# Output :
# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
#
# Solution
# 75). Write a program to find the total number of special characters in a string using Python Loops.
# Input = ‘@sqa#tools!!’
# Output = 4
#
# Solution
# 76). Write a program to add even numbers in an empty list from a given list using Python Loops.
# Input :
# A=[2,3,5,76,9,0,16], B=[]
# Output = [2,76,0,16]
#
# Solution
# 77). Write a program to add odd numbers in an empty list from a given list using Python Loops.
# Input :
# A=[3,8,5,0,2,7], B=[]
# Output = [3,5,7]
#
# Solution
# 78). Write a program to add special characters in an empty list from a given list using Python Loops.
# Input :
# A=[s,2,4,6,a,@,!,%,#], B=[]
# Output = [@,!,%,#]
#
# Solution
# 79). Write a program to print the last element of a list using a while loop using Python Loops.
# Input :
# C=[s,q,a,t,o,o,l,s]
# Output = s
#
# Solution
#
# 80). Write a program to print 1-10 natural numbers but it should stop when the number is 6 using a while loop in Python.
# Output :
# 1
# 2
# 3
# 4
# 5
#
# Solution
# 81). Write a program to print 1-10 natural numbers but it should stop when the number is 6 using Python Loops
# Output :
# 1
# 2
# 3
# 4
# 5
#
# Solution
# 82). Write a program to count the total number of characters in a file using Python Loops.
# Input :
# (file.txt
# Content= I’m learning python
# At
# Sqatools)
# Output = 26
#
# Solution
# 83). Write a program to find the total number of digits in a file using Python Loops.
# Input :
# (file.txt – file name
# Content-
# Virat Kohli scored 100 in the last match)
# Output = 3
#
# Solution
# 84). Write a program to find the total number of Uppercase letters in a file using Python Loops.
# Input :
# (file.txt – file name
# Content-
# Virat Kohli scored 100 in the last match)
# Output = 2
#
# Solution
# 85). Write a program to find the total number of special characters in a file using Python Loops.
# Input :
# (file.txt – file name
# Content-
# student@gmail.com
# ##comment)
# Output = 3
#
# Solution
# 86). Write a program to sort a list using for loop in Python Loops.
# Input = [6,8,2,3,1,0,5]
# Output = [0,1,2,3,5,6,8]
#
# Solution
# 87). Write a program to add elements from one list to another list and print It in descending order using Python Loops.
# Input :
# A=[2,5,8,0,1,4], B=[]
# Output = [8,5,4,2,1,0]
#
# Solution
# 88). Write a program to find the maximum number from the list using Python Loops
# Input : [12,14,45,88,63,97,88]
# Output : Maximum number: 97
#
# Solution
# 89). Print the following camel letter pattern using Python Loops.
# Output =
# A
# B C
# D E F
# G H I J
# K L M N O
# P Q R S
# T U V
# W X
# Y
#
# Solution
# 90). Print the following small alphabet letter pattern using Python Loops.
# Output =
#            a
#        b c d
#      e f g h i
#    j k l m n o p
#      q r s t u
#        v w x
#           y
#
