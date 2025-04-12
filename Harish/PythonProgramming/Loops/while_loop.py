#print 1 to 10 with while loop
n=1
while n<=10:
    print(n)
    n+=1

print("_"*100)

# break and continue statement
#when ever we met with continue condition, then code will move to next
#without executing the remaining code
x=1
while x<=10:
    if x==4 or x==5:
        x+=1
        continue
    print(x)
    x+=1

print("_"*100)
#break statement
#when ever the code met the break condition then loop will break immediately and wont go for next value
y=1
while y<=100:
    if y==5:
        break
    print(y)
    y+=1

print("_"*100)
#for loop with continue

for i in range(1,11):
    if i>3 and i<7:
        continue
    print(i)

print("_"*100)

#write a py program to reverse a integer number
rev=0
n=int(input("Enter the number"))
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)

rev=0
x=int(input("Enter Vale:"))
while x>0:
    dig=x%10
    rev=rev*10+dig
    x=x//10
print(rev)






