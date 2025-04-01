"""
 if condition:
     code
 else:
     code
 """

n1 = 30
n2 = 35
print(n1 == n2)
# = :  assignment operator
# == : equal to operator


# compare two numbers
if n1 == n2:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

print("_" * 50)
# check given is even or odd
v1 = 51

print(v1 % 2 == 0)

if v1 % 2 == 0:
    print("This is even number :", v1)
else:
    print("This is odd number :", v1)

print("_" * 50)
# write if condition without else
# check given number is divisible by 3
num1 = 15

if num1 % 3 == 0:
    print("Operation successful")

print("Good Morning")

print("_" * 50)
#######################
# get if condition output in one single line
# write a program to print square of value if it is even else print cube of the value
p = 6

result = p ** 2 if p % 2 == 0 else p ** 3
print("result :", result)  # result : 36

print(p ** 2 if p % 2 == 0 else p ** 3)  # 36

# Logical operators
"""
# AND logical operator
cond1 and cond2
True and False :  False
False and True :  False
False and False :  False
True and True :  True


# OR Logical operator:
cond1 or cond2 

True or True :  True
False or True :  True
True or False :  True
False or False :  False

# Other operators
> :  greater than
< :  less than
>= :  greater than equal
<= : less than equal
== :  equal to
!= : not equal to
in :  operator
is : operator
not : not operator
"""

print("_" * 50)

# write a python program to check the given number is divisible by 3 and 5
x = 26

if (x % 3 == 0) and (x % 5 == 0):
    print("The number is divisible by 3 and 5 :", x)
else:
    print("The number is not divisible by 3 and 5:", x)

print("_" * 50)

# write a python program to check the given number is divisible by 3 or 5
y = 16

if (y % 3 == 0) or (y % 5 == 0):
    print("The number is divisible by 3 or 5 :", y)
else:
    print("The number is not divisible by 3 or 5:", y)

print("_" * 50)
############################ if-elif-else ################################
"""
if cond1:
    code1
elif cond2:
    code2:
elif cond3:
     code3
elif cond4:
    code4
else:
    code5
"""