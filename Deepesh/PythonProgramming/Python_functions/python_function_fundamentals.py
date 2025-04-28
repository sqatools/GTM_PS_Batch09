# function without parameter
def function1():
    print("Good Morning")


# def : def is the keyword, that is required to initiate the definition of the function


function1()
function1()

print("_" * 50)


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

print("_" * 50)


#####################################
# function with multiple parameters
def addition(n1, n2, n3):
    print("n1 :", n1)
    print("n2 :", n2)
    print("n3 :", n3)
    add = n1 + n2 + n3
    print("Addition output :", add)


# parameter value read in same sequence as we defined in the function.
addition(30, 40, 50)
"""
n1 : 30
n2 : 40
n3 : 50
Addition output : 120

"""

print("_" * 50)
# change parameter sequence during function calling
addition(n2=500, n3=700, n1=100)
"""
n1 : 100
n2 : 500
n3 : 700
Addition output : 1300
"""

addition('Python', 'Programming', 'Language')
"""
n1 : Python
n2 : Programming
n3 : Language
Addition output : PythonProgrammingLanguage

"""

print("_" * 50)
# Pass by reference of other variable
x = 50
y = 80
z = 90
addition(x, y, z)

"""
n1 : 50
n2 : 80
n3 : 90
Addition output : 220
"""

print("_" * 50)


def multiplication(n1, n2):
    print("multiply :", n1 * n2)


# multiplication(40, 5)
# multiply : 200


print("_" * 50)


##################### function with default parameter value #######################
# Note :  Default parameters always comes at right side of the parameter list.
#         default parameter has to follow non default parameter.
def division_value(v1, v2=5):
    print("v1 :", v1)
    print("v2 :", v2)
    print("division :", v1 // v2)


# when dont define value for default parameter, then it will consider default value
division_value(20)
# v1 : 20
# v2 : 5
# division : 4


# when defined another value for default parameter, then it will overwrite the default value
division_value(500, 10)
# v1 : 500
# v2 : 10
# division : 50


list1 = [40, 50, 60]
v1 = sum(list1)
print("return value:", v1)
# return value: 150

print("_" * 50)


###################### Create function with return statement ################

def find_max_value(l1):
    max_val = 0
    for val in l1:
        if val > max_val:
            max_val = val
        else:
            continue

    return max_val


result = find_max_value([5, 7, 9, 23, 4])
print("max value result :", result)


# max value result : 23


# function with multiple return value
def math_operation(n1, n2):
    add = n1 + n2
    mul = n1 * n2
    sub = n1 - n2
    return add, mul, sub


output = math_operation(50, 20)
print("output :", output)  # output : (70, 1000, 30)

a, b, c = math_operation(70, 20)
print("addition :", a)  # 90
print("multiplication :", b)  # 1400
print("subtraction :", c)  # 50

print("_" * 40)


# write a python function to add value from 1 to 100 and return it
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

# Home work
# Q1 write a python function to get factorial any given number with return statement
# Q2 write a python function to get list of all the prime number from 1 to 100

print("_" * 50)


#################################
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
