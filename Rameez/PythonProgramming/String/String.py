# HomeWork #
#1. Print the output as "HHello good morningg" for the input "Hello good morning"
str1="Hello good morning"
s1="H"
s2="g"
s3="m"
result1=f"{s1}Hello good morning{s2}"
print(result1)

#2. Print the output as "HHelloo ggoodd mmorningg" for the input "Hello good morning"
str2="Hello good morning"
s1="H"
s2="g"
s3="m"
s4="o"
s5="d"
result2=f"{s1}Hello{s4} g{s2}ood{s5} {s3}morning{s2}"
print(result2)

#3. Print "oellH doog gninrom"
a="Hello"
b="good"
c="morning"
print(a[::-1],b[::-1],c[::-1])

# Apply loop without indexing
a="Python"
for i in a:
    print(i)

# Apply loop with loop

b="Programming"
word_len=len(b)
for i in range(word_len):
    print(i, b[i])

# String Formatting #
s1="My name is john and my age is 25, living in mumbai"
Name="Rahul"
Age=20
City="Bengaluru"

# 1. String concatenation
result1="My name is "+Name+" and my age is "+str(Age)+", living in "+City+""
print(result1)

# 2. String format method
result2="My name is {} and my age is {}, living in {}".format(Name, Age, City)
print(result2)

# 3. f string formating
result3=f"My name is {Name} and my age is {Age}, living in {City}"
print(result3)

# Convert string to raw string
result4=r"My name is Rameez\t\t, and my age is 20\n, living in {City}\t\t"
print(result4)

# String Slicing

# Rule 1

str_a="Programming"
# Default start index is zero
print(str_a[:8])

# Default end index will end of string
print(str_a[3:])

# -Ve and +ve
print(str_a[-3:10])

# +ve and -ve
print(str_a[1:-7])

# -ve and -ve
print(str_a[-7:])
print(str_a[-7:-1])

# Rule 2

# Default step value is 1
# Get left to right output

str_c="Hello World"
print(str_c[2:8:1])
print(str_c[1:10:2])

# Get right to left output
print(str_c[-1:-9:-1])

# Default end index will be end of string when step value is +ve
print(str_c[::])
print(str_c[1::1])

# Default start index will be -1, when step value is -ve.
print(str_c[:5:-1])

# Reverse of the string
print(str_c[::-1])