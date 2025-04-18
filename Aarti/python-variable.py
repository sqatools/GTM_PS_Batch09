a = 10
b = 20
print("Hello Word")
# 1 . Python Program to add two integer values
print("Addtion of 2 numbers ", a+b)

# 2. Python Program to subtract two integer values.
print ("Subtraction of ", a , " and" , b, " is ",b - a)

# 3 . Python program to multiply two numbers.
print ("Multiplication of ", a , " and", b," is ", b * a)

# 4.  Python program to repeat a given string 5 times.
string1 = "AbcD "
print("Repeating String ", string1*5)
# 5. Python program to get the Average of given numbers.
a = 10
b = 20
c = 30
print("Average Number: ", (a+b+c)/3)
# 6. Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order

ls1 = [45, 60, 61, 66, 40, 70, 77, 80,90]
ls2 = ls1.sort()
lenth = len(ls1)
print("Median Value of given list is :  ", ls1 , " \n", ls1[int((lenth)/2)])

# 7. Python program to print the square and cube of a given number.
num1 = 7
print(" Square of number 7 : ", num1**2 )
print(" Square of number 7 : ", num1**3 )

# 8. Python program to interchange values between variables
num1 = 25
num2 = 20
print("    Num1 :  ", num1 , " Num2 : ", num2)
num3 = num1
num1 = num2
num2 = num3
print("After exchange : \n   Num1 :  ", num1 , " Num2 : ", num2)
# 9. Python program to solve this Pythagorous theorem.
a = 2
b = 3
c = a**2 + b**2

print("Pythagorun Output:  ", c)

# 10. Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
c = a**2 + b**2 + 2*a*b
d = (a+b)**2
print("Formula: (a + b)2 = a^2 + b^2 + 2ab ")
print("(a+b)2 :", d , " a^2 + b^2 + 2ab: ", c)
# 11. Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab

c = a**2 + b**2 - 2*a*b
d = (a-b)**2
print("Formula: (a - b)2 = a^2 + b^2 - 2ab ")
print("(a+b)2 :", d , " a^2 + b^2 - 2ab: ", c)

# 12. Python program to solve the given math formula.
# a2 – b2 = (a-b)(a+b)
c= a**2 - b**2
d = (a-b)*(a+b)
print("check if right is same as left")
if (c == d):
    print("a^2 - b^2" ,c ," = (a-b)(a+b) ",d)
# 13. Python program to solve the given math formula.
# (a + b)3 = a3 + 3ab(a+b) + b3
c = (a+b)**3
d = a**3 + b**3 + 3*(a*b)*(a+b)
if (c == d):
    print ("(a + b)3 :", c ," a3 + 3ab(a+b) + b3 : ",d)
# 14. Python program to solve the given math formula.
#  (a – b)3 = a3 – 3a2b + 3ab2 – b3
c =  (a-b)*3
d = a**3 - 3*(a**2)*b + 3*a*(b**2) - b**3
if (c == d):
    print ("(a - b)3 :", c ," a3 - 3a2b +3ab2 + b3 : ",d)

# 15. Python program to calculate the area of the square.
line =  15
area = line**2
print("Area of Square : ", area)
# 16.  Python program to calculate the area of a circle.
pi = 3.14
radius =  15
area = pi* radius**2
print("Area of Circle : ", area)
# 17.  Python program to calculate the area of a cube.
a = 10
print("Area of Cube : ", 6*a*a)
# 18. Python program to calculate the area of the cylinder.
r = 10
h= 18

print("Area of cylinder  :  ", 2*pi*r*h + 2*pi*r**2)
# 19.  Python program to check whether the given number is an Armstrong number or not
num = a = 153
rev = 0
while a > 0:
    rem = a%10
    print("rem: ",rem)
    rev = rev + rem**3
    print("rev:", rev)
    a = a//10
    print("a again : ",a)

if(rev == num):
    print("It is Armstrong number")
else:
    print("Not a palindrom")

# 20. Python program to calculate simple interest.

p = 1000
r = 10
t = 2

amount = p+(p/r)*t

print("Amount payable: ",amount)