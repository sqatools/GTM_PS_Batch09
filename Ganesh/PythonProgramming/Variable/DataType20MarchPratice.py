# Data type Interger data
# float is immutable data typ
# Float data type

a = 0.0
a1 = 23.30
b2 = 38.20
c3 = -23.30
d4 = 0.3232

print("data type :", a, type(a))
print("data type :", a1, type(a1))
print("data type :", b2, type(b2))
print("data type :", c3, type(c3))
print("data type :", d4, type(d4))
print("--" * 20);

# complex Data Type

# represent in 2 format#
# var= x+yj
# x-real,
# y-imaginary value

var = 10 + 0j
print(var, type(var))
print(type(var), ": real value", var.real, )
print(type(var), ": imaginary value", var.imag)
print("." * 200)

var2 = 100j + 23
print(" real =", var2.real, "\n", "imaginary =", var2.imag)

print("." * 20)

# String data type- sequence data type

# string is inmuttable data type once define it's cannot change
# define in different type of quates

s1 = 'Hello \t\t h2 we are learning data_type  2) data and symbol methods\n \t 3)multiple line'
print(s1)
s2 = '''
1)Hello h2 we are learning data_type  
2) data and symbol methods
3)multiple line'''
print(s2)
# \t= for single space
# \n - next line
print("." * 20)

#index sequence print

str_a = "GANESH"
'''
 0 1  2  3  4  4  (+ve)
 G A  N  E  S  H
-6 -5 -4 -3 -2 -1 (-ve)
'''

#print("Index Sequence :", str_a[-5])
#print(str_a)
for index, char in enumerate(str_a) :
    negative_index = index- len(str_a);
    print(f"Word: {char}, Index: {index}")
    print(f"word :{char},Negative Index:{negative_index}")

#for index, char in enumerate(str_a):
   # print(f"Character: {char}, Index: {index}")  # Correct indentation

