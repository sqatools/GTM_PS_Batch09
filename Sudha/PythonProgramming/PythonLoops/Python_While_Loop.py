"""
while condition:
    code
"""

n = 1
while n <= 10:
    print(n)
    n = n + 1

print("_" * 50)
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
while x <= 10:
    if x == 4 or x == 5:
        x += 1
        continue
    print(x)
    x += 1
"""
leaving the condition if x = 4, 5 and then continue of the rest of numbers
1
2
3
6
7
8
9
10
"""
print("_"*50)
# Break  statement: whenever the conde met with break condition, then loop will break imidiately
# won't go for next value

y = 1
while y <=100:
    if y == 5:
        break

    print(y)
    y += 1

"""
if it meets the condition and break the condition it will not continue to next
1
2
3
4

"""