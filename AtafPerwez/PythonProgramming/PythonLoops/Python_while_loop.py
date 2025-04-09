"""
while condition:
    code
"""


# print 1 to 10 with while loop
n=1
while n<=10:
    print(n)
    n += 1

print("_"*50)
# infinite loop
"""
num1 = 1
while True:
    print(num1)
    num1 += 1

"""


####### Break and continue statement ######
# continue statement : when ever we met with continue condition, then code will move to next
# without executing the remaining code.

x = 1
while x<=10:
    if x == 4 or x == 5:
        x += 1
        continue
    print(x)
    x +=1

"""
1
2
3
6
7
8
9
10
"""

# Break  statement: whenever the conde met with break condition, then loop will break imidiately
# won't go for next value

y = 1
while y <=100:
    if y == 5:
        break

    print(y)
    y += 1

"""
1
2
3
4

"""

print("_"*50)
# for loop with continue

for i in range(1, 11): #i=1, 2, 3, 7, 8, 9, 10
    if i > 3 and i < 7:
        continue
    print(i)


print("_"*40)
# while loop program
# write a program to reverse a integer number.

num1 = 123
#num1 = 35789
rev_val = 0
count = 0
while num1 > 0: # 12 > 0| 1 > 0 | 0 > 0
    temp = num1%10 # 3, 2, 1
    rev_val = rev_val*10 + temp # 3, 32
    # 0*10 + 3=3
    # 3*10 + 2 = 32
    # 32*10 + 1 = 321
    num1 = num1//10 # 12, 1, 0
    count += 1

print("reverse value :", rev_val)
print("total digits :", count)


