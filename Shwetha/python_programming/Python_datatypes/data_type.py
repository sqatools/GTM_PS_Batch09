
# string data type

str1="python"
#print(str1[-7]) #IndexError: string index out of range

#str[0]=4 #TypeError: 'type' object does not support item assignment


'''
 0   1  2  3  4  5 
 p   y  t  h  o  n
-6  -5 -4 -3 -2 -1 
'''
'''
: : -3
'''
print(str1[::-5]) # np
print(str1[::-4]) #ny
print(str1[::-3])# nt
print(str1[::-2]) #nhy
print(str1[::-1]) #nohtyp
print("@"*30)

print(str1[::5]) # pn
print(str1[::4]) # po
print(str1[::3])# ph
print(str1[::2]) # pto
print(str1[::1]) #python

print("@"*30)
str2 ="Hi my name is 'shwetha'nice to meet you"
print("get m with -ve index :", str2[-3]) #  m
print(str2[15:22]) #shwetha

print("@"*30)
print("It's alright")
print("He is called 'Johnny'") #He is called 'Johnny'
print('He is called "Johnny"') # He is called "Johnny"

print("@"*30)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("@"*30)
# range
b = "Hello, World!"
print(b[2:5]) # llo
print(b[:5]) # Hello
print(b[2:]) #llo, World!
print(b[-5:-2]) #orl
print("@"*30)
# apply loop without indexing
for char in str1:
    print(char,end=" ") #p y t h o n
print()

print("@"*30)

for char in str1:
    print(str1[::-1],end=" ") #nohtyp nohtyp nohtyp nohtyp nohtyp nohtyp
print()

# apply loop with indexing
print("@"*30)
str2="Chitradurga"

str_len = len(str2)
print("string length :", str_len, str2) #11 ,Chitradurga
for i in range(str_len):
    print(i, str2[i],end=" ") # 0 C 1 h 2 i 3 t 4 r 5 a 6 d 7 u 8 r 9 g 10 a
print()

print("@"*30)
##################### String formating ##############
str3 = "My name is john and my age is 25, living in Mumbai"

Name = "Rahul"
Age = 20
City = "Bangalore"

# 1. string concatenation
result1 = "My name is "+Name+" and my age is "+str(Age)+", living in "+City

print("result1:", result1)

# 2. string format method.
result2 = "My name is {} and my age is {}, living in {}".format(Name, Age, City)
print("result2:", result2)

# 3. f string formatting.
result3 = f"My name is {Name} and my age is {Age}, living in {City}"
print("result3:", result3)

######## convert string to raw string #############
# \t :  add spaces in string
# \n :  add next line in the string.
str4 = r"Hello good morning \t \t \t, hope you are doing good \n \h $%$#@ , we are learning Python"
print(str4)


# Rule 1: str[start index: end index]

str_a = "Programming"
#str_a = "P r o g r a m m i n g"
#         0 1 2 3 4 5 6 7 8 9 10
print(str_a[3:8])  # gramm

# default start index is 0
print(str_a[:8])  # Programm

# default end index will end of string.
print(str_a[3:]) # gramming

# start : -ve and end : +ve
print(str_a[-6:10])  # ammin

# start : +ve and end : -ve
print(str_a[1:-1]) # rogrammin
print("_"*50)

print(str_a[1:-9]) #
print("_"*50)

str_b = "Good Morning"
# start : -ve and end : -ve
print(str_b[-7:-1]) # Mornin
print(str_b[-7:]) # Morning
print(str_b[-12:-8]) # Good
print(str_b[:4])# Good
print("_"*50)


# Rule 2: str[start index: end index: step value]

str_c = "Hello world"

# get left to right output
print(str_c[2:8:1]) #llo wo
print(str_c[1:10:2]) # el ol
print(str_c[2:11:]) # llo world

str_c = "Helloworld"
print("_"*50)
# get right to left output
print(str_c[-1:-9:-1]) #dlrowoll

print("_"*50)

print(str_c[-5:-2:]) #wor

print("_"*50)
print(str_c[-4:-10:-2]) #ool
print(str_c[-10:-4:2]) #Hlo

print(str_c[-4:-10:2])#no o/p
print(str_c[-10:-4:-2]) #no o/p

# slicing Home work
str1 = "Hello good Morning"

print("u"*40)
output1 = "HHello good Morningg"
print(f"{str1[0]}{str1}{str1[-1]}")

print("_"*40)
output2 = "HHelloo ggoodd MMorningg"
# solution2
word1 = str1[:5]
word2 = str1[6:10]
word3 = str1[11:]

print(f"{word1[0]}{word1}{word1[-1]} {word2[0]}{word2}{word2[-1]}  {word3[0]}{word3}{word3[-1]}")
# HHelloo ggoodd  MMorningg

###
print("_"*40)
output3 = "olleH doog gninroM"
# solution
print(f"{word1[::-1]} {word2[::-1]} {word3[::-1]}") # olleH doog gninroM

