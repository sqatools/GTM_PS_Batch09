## If Condition ##

# Compare two numbers
"""
n1=float(input("enter the number"))
n2=float(input("Enter the number"))
if n1==n2:
    print("Both the numbers are equal")
else:
    print("Both the numbers are not equal")
"""
'''
# Check given number is even or odd
n1=float(input("Enter the number"))
if n1%2==0:
    print("It is an even number")
else:
    print("It is an odd number")
'''

# Check the given number is divisible by 3
# Write a if condition without else condition
'''
n1= float(input("Enter the number"))
if n1%3==0:
    print("The number is divisible by 3")
'''

#Get if condition output in one single line
# Write a program to print square of value if it is even else print cube of the value
'''
n=float(input("Enter the number"))
result=n**2 if n%2==0 else n**3
print(result)
'''
# Write a program to check the given number is divisible by 3 and 5 using "and" operator.
"""
n1=float(input("Enter the number"))
if (n1%3==0) and (n1%5==0):
    print(n1,": is divisible by 3 & 5")
else:
    print(n1, ": is not divisible by 3 & 5")
"""
# Write a program to check the given number is divisible by 3 and 5 using "or" operator.
"""
n1=float(input("Enter the number"))
if (n1%3==0) or (n1%5==0):
    print(n1,": is divisible by 3 or 5")
else:
    print(n1, ": is not divisible by 3 or 5")
"""
## if-elif-else condition ##

# Write a python program to find the greater number among three values
"""
a=float(input("Enter the number"))
b=float(input("Enter the number"))
c=float(input("Enter the number"))
if a>b and a>c:
    print("a is grater than b & c")
elif b>a and b>c:
    print("b is greater than a & c")
elif c>a and c>b:
    print("c is greater than a & b")
else:
    print("no one has greater value")
"""
# write a program to provide grade to students as marks received.
"""
marks=int(input("Enter the marks"))
if marks < 35:
    print("Sorry, you failed in the examination")
elif 35 <= marks < 40:
    print("Nice, you passed the examination with C grade")
elif 40 < marks < 60:
    print("Nice, you passed the examination with B grade")
elif 60 < marks < 80:
    print("Nice, you passed the examination with A grade")
elif 80 < marks <= 100:
    print("Congratulation, you passed the examination with A++ grade")
else:
    print("Invalid marks entry")
"""
## nested if condition ##
# write a python program to demonstrate the interview process
"""
round1= str(input("Enter the result of round 1"))
round2= str(input("Enter the result of round 2"))
round3= str(input("Enter the result of round 3"))
if round1 == "Pass":
    print("Congrats 1st round is cleared")
    if round2 == "Pass":
        print("Congrats 2nd round is cleared")
        if round3 == "Pass":
            print("Congrats you are selected")
        else:
            print("Sorry you are not selected")
    else:
        print("Sorry failed in second round")
else:
    print("Sorry failed in 1st round")
"""
# In operator
"""
list1=[5,7,9,22]
v=22
if v in list1:
    print("v is present in list1")
else:
    print("v is not present in list1")
"""

"""
tuple2=(5, 7, 9, 50)
t=50
if t in tuple2:
    print("t is present in tuple2")
else:
    print("t is not present in tuple2")
"""
"""
k1="P"
dict1={"X":345, "Y":567, "Z":890}
if k1 in dict1:
    print("k1 is present in dict1")
else:
    print("k1 is not present in dict1")
"""
"""
v1=True
if v1 is True:
    print("We are good to go further")
else:
    print("Value is not true")
"""
"""
v3=False
if v3:
    print("Variable is holding some value:", v3)
else:
    print("Variable is holding zero")
"""



