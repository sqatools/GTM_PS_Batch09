# Print the numbers from 1 to 10 using while loop ##
x=1
while x<=10:
    print(x)
    x+=1

# print the numbers using infinite while loop:
"""
num1=1
while True:
    print(num1)
    num1+=1
"""
 # Break and Continue Statement #
# Continue#
x=1
while x<=10:
    if x==4 or x==5:
         x+=1
         continue
    print(x)
    x+=1

# Break #
y=1
while y<=10:
    if y==5:
        break
    print(y)
    y+=1

for i in range(1, 11): #i=1, 2, 3, 7, 8, 9, 10
    if i > 3 and i < 7:
        continue
    print(i)

rev=0
a=int(input("Enter the number"))
while a>0:
    dig=a%10
    rev=rev*10+dig
    a=a//10
print(rev)

count=65
for i in range(1,6):
    for j in range(1, i+1):
        print(chr(count), end="")
        count+=1
    else:
        print(" ", end="")
    print()


for i in range(65, 91):
    print(chr(i), end=" ")
print()

for i in range(97, 123):
    print(chr(i), end=" ")
print()

for i in range(1, 65):
    print(chr(i), end=" ")
print()

