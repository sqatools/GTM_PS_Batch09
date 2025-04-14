"""""

for condition
code

"""

#range (start , end , , step difference )

for val in range(1, 10, 2):
    print(val)

print("_"*50)

for i in range(5):
    print(i)

print("_" * 50)
    # print value with negative stepping

for i in range(5,0,-1):
    print(i)

print("_" * 50)

for i in range(10, 0 , -1):
    print(i)

print("_" * 50)

# python program to write table of numbers
# range works only with numbers
num = 5
for j in range (1, 11, 1):
    print(num, "*", j , "=", j*num)

print("_" * 50)
for k in range(11 ,3, -2):
    print(k)


# program to write factorial of a given number
#5 = 5*4*3*2*1

n1=5
fact = 1
for i in range(n1,0,-1):
    print(i)
    fact= fact*i

print("factorials of",i , "=", fact)

# program to get sum of all values 1 to 10

x=0
for i in range(11):
    x=x+i
    print(x)
print("_" *50)
print(x)

print("_" *50)
# Print fibonacci series
# 1,1,2,3,5,8,13,21,33

a=0
b=1
for i in range(10):
    a,b = b, a+b
    print(a,  b)