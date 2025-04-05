#while loop concept
# print 1 to 10 with while loop
'''
n=1
while n<=10:
    print(n)
    n +=1
print()

print("_"*20)
# Infinite Loop
num1=1
while True:
    print(num1)
    num1 +=1
'''


#>>>>> Break and continue statement
#Continue statement : When ever we met with continue condition, then code will move to next
#without executing the remanining code

x = 1
while x <=10:
    if x == 4 or x == 5:
        x +=1
        continue

        print(x)
        x += 4

#print("-"*20)

#break statement : whenever the code met twith beak condition, then loop will break immedeatley
# won't go for next value

'''
y = 1
while y <=10:
    if y == 1500:
        break

    print(y)
    y +=1
'''
