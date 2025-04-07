"""
# for loop
for <condition>:
    code

"""
# range(start, end, step difference)
# range(1, 10, 1)
# in range output, will consider the start and exclude the end value

for val in range(1, 10, 1):
    print(val)

"""
1
2
3
4
5
6
7
8
9

"""
print("_"*50)
# print values with 2 difference

for val in range(1, 10, 2):
    print(val)

"""
1
3
5
7
9
"""

print("_"*50)
# get output with default start value (0) and default step value (1)


for i in range(5):
    print(i)

"""
0
1
2
3
4
"""

print("_"*50)
# print output with negative step value

for i in range(5, 0, -1):
    print(i)

"""
5
4
3
2
1
"""

print("_"*50)
# print output with all negative

for i in range(-1, -11, -1):
    print(i)

"""
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
"""

print("_"*50)
#######
# write a python program to print the table of given number number
num = 7

for j in range(1, 11, 1):
    print(j, "*", num, "=", j*num)

"""
1 * 7 = 7
2 * 7 = 14
3 * 7 = 21
4 * 7 = 28
5 * 7 = 35
6 * 7 = 42
7 * 7 = 49
8 * 7 = 56
9 * 7 = 63
10 * 7 = 70
"""

print("_"*50)
######################################
# write a python program to get factorials of any given number
# 5 : 5*4*3*2*1
n1 = 6
fact = 1

for i in range(n1, 0, 1):
    print(i) # 5, 4, 3, 2, 1
    fact = fact*i # 5*1 =5, 5*4=20, 20*3 = 60, 60*2=120, 120*1 = 120

print("factorials of :",n1,":", fact)
# factorials of : 6 : 720

print("_"*50)
####################################################
# write a python program to get sum of all the values from 1 to 10
output = 0

for i in range(1, 11):
    output = output + i # 0 + 1 = 1, 1+2 = 3, 3+3 = 6, 6+4=10,
    # 10+5 = 15 , 15+6 = 21, 21+7 = 28, 28+8 = 36, 36+9=45, 45+10 = 55

    print("Output :", output)
    # Output : 55


"""
Output : 1
Output : 3
Output : 6
Output : 10
Output : 15
Output : 21
Output : 28
Output : 36
Output : 45
Output : 55

"""

print("_"*50)
# write a python program to print the fabonacci series
#     a   b   a+b
# 1,  2,  3,  5,  8, 13, 21, 33
# a,  b,  a+b


a = 0
b = 1
for _ in range(10):

    a, b = b, a+b
    #print("a:", a, "b:", b)
    print(b, end=" ")

# 1 2 3 5 8 13 21 34 55 89
