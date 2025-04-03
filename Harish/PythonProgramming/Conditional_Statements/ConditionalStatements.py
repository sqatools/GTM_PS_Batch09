######if Condition#####
"""
if condition:
code
else:
code
"""
from basavraj.Python_Programming.Programs.if_conditions import marks

#To find the number is even or odd
a= 20
if a%2==0:
    print("a is an even number", a)
else:
    print("a is an odd number", a)

b=12
if b%2==0 and b%8==0:
    print("b is divided by 2 and 8", b)
else:
    print("b is divided by only 2", b)


# 1). Python program to check given number is divided by 3 or not.

a= 12
if a%3==0:
    print("The value is divided by a",a )
else:
    print("The value is not divided by a",a )

# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
marks=int(input("Enter marks"))
if marks<40:
    print("failed")
elif marks>=40 and marks<=50:
    print("c grade")
elif marks>=50 and marks<=60:
    print("B grade")
elif marks>=60 and marks<=70:
    print("A")
elif marks >= 70 and marks <=80:
    print("A+")
elif marks>=80 and marks<=90:
    print("A++")
elif marks>=90 and marks<=100:
    print("Excellent")
else:
    print("Invalid")

# 4). Python program to check the given number divided by 3 and 5.

c=int(input("Enter the value"))
if c%3==0 and c%5==0:
    print("The value is divided by 5 and 3",c)
else:
    print("The value is not divided by 5 and 3", c)

# 5). Python program to print the square of the number if it is divided by 11.

d=int(input("Enter Value"))
if d%11==0:
    print(d**2)
else:
    print("Not divided by 11")

 # 7. Python program to check given number is odd or even.

 e=int(input("Enter value"))









