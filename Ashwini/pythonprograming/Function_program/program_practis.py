# function without parameter
def function1():
    print("Hello")

# def : def is the keyword, that is required to initiate the definition of the function


function1()


print("_"*50)
#######################################
# create function with parameter.
def greeting(msg):
    print(msg)

# There are 2 ways to provide value to parameters
# 1. Pass by value
greeting("Very Good evening")

# 2. Pass by reference
var1 = "Have a nice day"
greeting(var1)

x = "Hope you are doing good"
greeting(x)
def mathoperation(n1,n2):
    add=n1+n2+n2
    sub=n1-n1-n2
    print("addition of three number is:",add)

# *args parameter in the function
# *args parameter accepts multiple value inform tuple.
def get_all_even_number(*args):
    print("args values :", args, type(args))
    for val in args:
        if val % 2 == 0:
            print(val)
        else:
            continue


# get_all_even_number(3, 5, 6, 8)
get_all_even_number(3, 5, 6, 8, 7, 99, 12, 34, 77)


def get_diff_values(*args):
    for val in args:
        print(val)


get_diff_values(3, 'Hello', [5, 6, 7], (3, 5, 6), {'a': 123}, True)

print("_" * 50)


print("_"*50)
#################################
# **kwargs Parameter: This parameter accepts the values in key value format while calling the function.
#                     It stores the values in form of dictionary.

def get_employee_details(**kwargs):
    print("kwargs values :", kwargs)
    for k, v in kwargs.items():
        print(k, ":", v)

get_employee_details(name='Rahul', surname='Gupta', email='rahul@gmail.com', phone=4545435455)


print("_"*50)
############ Function with doc ###################

def calculator(n1: int, n2: int, op: str) ->  int:
    """
    This is calculator of different math operation
    :param n1: int value for operation
    :param n2: int value for operation
    :param op: string value as per the operation.
    :return: int
    """
    if op == 'add':
        return n1+n2
    elif op == 'sub':
        return n1-n2
    elif op == 'divide':
        return n1//n2
    elif op == 'mul':
        return n1*n2


output = calculator(30, 40, "add")
print(output)


print("_"*50)
#################### Call function inside a function ###############

def add_Values(n1, n2):
    return n1+n2

def multiplication_values(n1, n2, n3):
    output = add_Values(n1, n2)
    print("multiplication :", output*n3)


multiplication_values(30, 40, 5)

#function with multiple parameters
#1 Python function program to add three numbers.
def addition(a,b,c):
    print("a :", a)
    print("b :", b)
    print("c :", c)
    add = a + b + c

    print("addition of two numbers is:", add)
addition(30,40,50)
print("-"*50)
#2 Python function program to print a table of a given number.
def table(n):
    count=0
    for i in range(1,11):
        count=i*n

        print(i, "*", n, "=", count)
#n = int(input("Enter a number: "))
table(5)
print("-"*50)
#3 Python function program to find the sum of all the numbers in a list.
def sum_list(list1):
    count=0
    for val in list1:
        count+=val
    print("sum of given list:", count)
list=[6,9,4,5,3]
sum_list(list)

print("-"*50)
#4 Python function program to multiply all the numbers in a list.
#Input : [-8, 6, 1, 9, 2]
def mul_list(l):
    count=1
    for val in l:
        count*=val
    print("multiply of all list is:",count)
l1=[-8,6,1,9,2]
mul_list(l1)
#5 write a python function to add value from 1 to 100 and return it
# return statement break the execution of the function
def get_sum_of_value(num):
    sum = 0
    for i in range(1, num):
        if i == 10:
            return sum, 'b'
        sum += i

    return sum, 'a'

output1 = get_sum_of_value(5)
print(output1)  # return sum, 'a'


output2 = get_sum_of_value(50)
print(output2)



 #Home work
# Q6 write a python function to get factorial any given number with return statement
def factrorial(n):
     fact=1
     for x in range(1,n+1):

         fact=fact*x
     return fact

num=int(input("Enter the number:"))
if num < 0:
    print("Factorial of negative number can not calculated")
else:
    print("Factorial of number is:",factrorial(num))

print("-"*50)
 # Q7 write a python function to get list of all the prime number from 1 to 100
def prime_value(n1,n2):

    for num in range(n1,n2+1):
        count=0
        for i in range(2,num):
          if (num%i)==0:
             count+=1
             break
          else:
              continue
        if count==0:
            print(num,end=" ")

prime_value(1,100)

print("-"*50)
#8 Python function program to reverse a string.
#Input: Python1234
def reverse_string(str):
    r=str[::-1]
    print("Reverse of the given string: ", r)
reverse_string("Python1234")

print("-"*50)
#9 Python function program that takes a list and returns a new list with unique elements of the first list.
#Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
#Output : [2, 3, 1, 4, 6 ]
def unique_ele(l):
    l1=[]
    for val in l:
        if val not in l1:
            l1.append(val)
    print(l1)
l=[2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
unique_ele(l)

#10 Python function program to find the maximum of three numbers.
def find_max_value(l1):
    max_val = 0
    for val in l1:
        if val > max_val:
            max_val = val
        else:
            continue

    return max_val


result = find_max_value([5, 23, 4])
print("max value result :", result)
#11 Python function program to find the even numbers from a given list.
def even(list1):
    even_list = []
    for val in list1:
        if val%2 == 0:
            even_list.append(val)
    print(even_list)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even(l)
#12 Python function program to create and print a list where the values are squares of numbers between 1 to 10.
def square():

    for i in range(1,11):
       print(i,":" ,i**2)

square()

#13Python function program to create a function with *args as parameters.
#Input: 5, 6, 8, 7
def square_list(*args):
    print("args value:",args,type(args))
    for val in args:
        print(val**3,end=" ")

square_list(5,6,8,7)
#Output: 125 216 512 343

print("-"*50)
#14 Python function program to get the Fibonacci series up to the given number.
def fibonacci_series():
    n1=0
    n2=1
    count=0
    while count < 10:
        print(n1, end=" ")
        num = n1 + n2
        n1 = n2
        n2 = num
        count += 1
fibonacci_series()

print("-"*50)
"""15 Python function program to get the duplicate characters from the string.
Input: Programming
Output: {‘g’,’m’,’r’}"""
def duplicate(str):
    list=[]

    for char in str:
        if str.count(char)>1:

           list.append(char)


    print(set(list))
duplicate("Programming")
print("-"*50)
"""16 Python function program to get the square of all values in the given dictionary.
Input = {‘a’: 4, ‘b’ :3, ‘c’ : 12, ‘d’: 6}
Output = {‘a’: 16, ‘b’ : 9, ‘c’: 144, ‘d’, 36}"""
def square(D):
     dict={}
     for key,val in D.items():
        dict[key]= val**2
     print(dict)
square({'a': 4, 'b' :3, 'c' : 12, 'd': 6})
print("-"*50)
"""17 Python function program to create dictionary output from the given string.
Note: Combination of the first and last character from each word should be
key and the same word will the value in the dictionary.
Input = “Python is easy to Learn”
Output = {‘Pn’: ‘Python’, ‘is’: ‘is’, ‘ey’: ‘easy’, ‘to’: ‘to’, ‘Ln’: ‘Learn’}"""
def function(string):
    d={}
    list=string.split(" ")
    for word in list:
        d[word[0]+word[-1]]=word
    print(d)
function("Python is easy to learn")

#18 Python function program to print and accept login credentials.
def login():
    name = input("Enter name: ")
    password = input("Enter password")
    print("Credential accepted")
login()
print("-"*50)
#19  Python function program to check whether the given year is a leap year.
def leap_year(num):
    if (num%400 == 0 or num%100 != 0) and num%4 == 0:
       print("the given year is leap year")
    else:
        print("the given year is not leap year")
leap_year(2025)

print("-"*50)
#20 Python function program to get a valid mobile number.
def mobile_number(n):
    if len(str(n))==10:
        print("This is valid mobile number")
    else:
        print("This is not valid mobile number")
mobile_number("2345555880")
print("-"*50)
#21  Python function program to create a function with **kwargs as parameters.
def emp_details(**kwargs):
    print("kwargs value:",kwargs)
    for key,val in kwargs.items():
        print(key,":",val)
emp_details(name='Rahul', surname='Gupta', email='rahul@gmail.com', phone=4545435455)
