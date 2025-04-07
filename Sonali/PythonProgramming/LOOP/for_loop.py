for i in range(10):
    print(i)

print("-"*50)

for j in range(1,10,2):
    print(j)

print("-"*50)
for k in range(10,0,-1):
    print(k)
print("-"*50)
for val in range(-1,-11,-2):
    print(val)
print("-"*50)
for val1 in range(-15,-1,1):
    print(val1)

print("-"*50)

#print(1*2=2 ..........................1*10=10) this format

num=int(input("enter the number for u want the multiplication table:"))
for val3 in range(1,11,1):
    print(val3 ,"*" ,num ,"=" , val3*num)



#factorial of a given number

n1=int(input("enter the number u want the factorial of:"))
fact=1
for l in range(1,n1+1,1):
    fact=fact*l
print("factorial of the number is:",fact)

print("_"*50)

#fibonacci series
a=0
b=1
for _ in range(10):
    a, b = b, a+b
    print(b,  end="  ") #"" inbetween space matters...

#print the below format
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(5 , 0):
    for j in range(5, i-1):
        print("*", end=" ")

    print()


