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

#function with multiple parameters
#Python function program to add three numbers.
def addition(a,b,c):
    print("a :", a)
    print("b :", b)
    print("c :", c)
    add = a + b + c

    print("addition of two numbers is:", add)
addition(30,40,50)
print("-"*50)
# Python function program to print a table of a given number.
def table(n):
    count=0
    for i in range(1,11):
        count=i*n

        print(i, "*", n, "=", count)
#n = int(input("Enter a number: "))
table(5)
print("-"*50)
# Python function program to find the sum of all the numbers in a list.
def sum_list(list1):
    count=0
    for val in list1:
        count+=val
    print("sum of given list:", count)
list=[6,9,4,5,3]
sum_list(list)

print("-"*50)
#Python function program to multiply all the numbers in a list.
#Input : [-8, 6, 1, 9, 2]
def mul_list(l):
    count=1
    for val in l:
        count*=val
    print("multiply of all list is:",count)
l1=[-8,6,1,9,2]
mul_list(l1)
#write a python function to add value from 1 to 100 and return it
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
# Q1 write a python function to get factorial any given number with return statement
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
 # Q2 write a python function to get list of all the prime number from 1 to 100
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
            print(num)

prime_value(1,100)