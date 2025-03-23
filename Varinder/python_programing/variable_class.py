#diffrent values
# a = 10
# b = 20
# print(id(a))
# print(id(b))

# same values to different variable

# a = 10
# b = 10
# print("this is first location :", (id(a)))
# print("this is the second location :", (id(b)))

# assign multiple values to multiple variables

# a, b, c = 10, 20, 30
# print("this is a value of a:", a)
# print("this is a value of b:", b)
# print("this is a value of c:", c)

#############################################
# Assign one value to multiple variables

d = 20
e = 20
f = 20

print("this is d value :",d, id(d))
print("this is e value :", e)
print("this is f value :", f)

###############################################
"""
Math operation on variables

+ :  plus operator
- :  subtraction
* :  multiplication
/ and // : division
== :  equal to operator
!= : not equal to
** : power operator
%  : remainder operator
"""

# plus Operator
# a = 30
# b = 25
# print(" this is my total :" , a+b)
#
#
# # subtraction operator
#
# a = 30
# b = 40
# print(" this is my total after subtraction :", b-a)

# multiplication operator
a = 10*30

print("welcome to pyhon programing" *10)
print("this is my multiplication total =", a)