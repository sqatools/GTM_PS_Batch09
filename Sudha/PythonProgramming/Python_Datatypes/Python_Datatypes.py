"""Python Data Types :

1.  Numbers
    i) Integer
    ii) Float
    iii) Complex Number

2.  Sequential
    i)   String
    ii)  List
    iii) Tuple


3.  Dictionary
4.  Set
5.  Boolean
"""

############ Integer #################
"""
# properties of integer
->  Integer is immutable data type, once it is defined we can not change it.
->  Integer can contains any position and negative value.
->  Only whole will be consider as int
->  There is no limit to defined data in int variable

"""
n1 = 0
n2 = 4
n3 = 100
n4 = 45435435434354545454222333333333
n5 = -5644545

print(n1, type(n1)) # 0 <class 'int'>
print(n2, type(n2)) # 4 <class 'int'>
print(n3, type(n3)) # 100 <class 'int'>
print(n4, type(n4)) # 45435435434354545454222333333333 <class 'int'>
print(n5, type(n5)) # -5644545 <class 'int'>

# when we multiply the string with a number then it will repeat the string with number of times
var1 = "Hello"
print(var1*5)

print("_"*50)
print("_"*50)
############ Float #################
"""
->  Float is immutable data type.
->  Float only contains pointer values. e.g 4.5, 5.6, 0.23
->  Any positive and negative values can be float data type
->  There is no limit for float data type
"""

f1 = 0.0
f2 = 12.34
f3 = 4543543543.776899
f4 = -45676.789
f5 = 0.45454545
f6 = 9.0

print("f1 :", f1, type(f1)) # 0.0 <class 'float'>
print("f2 :", f2, type(f2)) # 12.34 <class 'float'>
print("f3 :", f3, type(f3)) # 4543543543.776899 <class 'float'>
print("f4 :", f4, type(f4)) # -45676.789 <class 'float'>
print("f5 :", f5, type(f5)) # 0.45454545 <class 'float'>
print("f6 :", f6, type(f6)) # 9.0 <class 'float'>

print("_"*50)

##Complex Numbers
# var1 = x + yj
# x = real value
# y = imaginary value

var2 = 10 + 20j
print(var2, type(var2))#(10+20j) <class 'complex'>
print("value of real :", var2.real) # value of real : 10.0
print("value of imaginary :", var2.imag) #value of imaginary : 20.0

var3 = 0+50j
print(var3, type(var3)) # 50j <class 'complex'>

var5 = 50j + 70
print(var5, type(var5)) # (70+50j) <class 'complex'>

var6 = "40 + 60j"
print(var6, type(var6)) # 40 + 60j <class 'str'>

var4 = 40+0j
print(var4, type(var4)) # (40+0j) <class 'complex'>

print(70,'Hello', 80+90j) # 70 Hello (80+90j)

############ string data type #################
"""
# String Properties
1.  String is immutable data type, once it is defined can not update it.
2.  String follows positive and negative indexing.
3.  There is no limit for string to define.
4.  String value defined different types of quotes single quotes, double quotes, single triple quote, double triple quote.
5.  String can contains any data , numbers, special character
"""

s1 = 'h'
s2 = "Hello Python"
s3 = "We are learning Python Programming"
s4 = '''
1. Good Morning
2. Good Evening
3. Python Programming
'''
s5 = """
The STRING database contains information 
from numerous sources, including experimental\n
data, computational prediction methods and 
public text collections. It is freely accessible 
and it is regularly updated
"""

s6 = "My name is 'John' and live in mumbai"
s7 = 'My name is "John" and live in mumbai %^%RT&^%d45564654654e '

s8 = "1. The STRING database \t\t contains information from \n2. numerous sources, including \t\t experimental \n3. data, computational \t\t prediction methods and "

# \n = line break
# \t = line space


print(s1, type(s1))
print("_"*50)
print(s2, type(s2))
print("_"*50)
print(s3, type(s3))
print("_"*50)
print(s4, type(s4))
print("_"*50)
print(s5, type(s5))
print("_"*50)
print(s6, type(s6))
print("_"*50)
print(s7, type(s7))
print("_"*50)
print(s8, type(s8))



str_a  = "Python"

"""
 0  1  2  3  4   5   +ve
 P  y  t  h  o   n
-6 -5 -4 -3  -2  -1  -ve

"""

print("first char :", str_a[0])  # first char : P
print("third index char :", str_a[3])  # third index char : h
print("get h with -ve indexing :", str_a[-3]) # get h with -ve indexing : h


str9 = "My name is 'John' and live in mumbai"
print("get m with -ve index :", str9[-4]) #  m



print("_"*50)
print("_"*50)
############ List data type #################
"""
# Properties of List
->  List is mutable data type, we can modify the list content
->  List define with square bracket
->  List can contains all different types of values, int, float, sting, list, tuple, dictionary, set, boolean, complex number
->  List follows the positive and negative indexing as like string
->  There is no limit to defined values in the list
->  List values are comma seperated."""

#      0   1     2         3        4        5         6     7      8      9
list1=[2, 3.4, 'Hello', [4,5,6], (3,2,1), {'a':123}, {5,7}, True, 40+50j,None]
#    -10  -9    -8        -7       -6         -5       -4    -3     -2    -1

print(list1, type(list1))
print(list1[4])#(3, 2, 1)
print(list1[3][2])#6
#get the value using -ve indexing
print((list1[-4])) #{5, 7}

list2 = [5,6,7]
list2.append(100)
print(list2) #[5, 6, 7, 100]






