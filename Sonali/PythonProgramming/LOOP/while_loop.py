# print the numbers between 1 to 10 without 4 and 5

x = 1
while (x <= 10):
    if x == 4 or x == 5:
        x += 1
        continue
    else:
        print(x)
        x += 1



print("-"*50)
#---------------------------------
y=1
while y<10:
    if y==5:
        break
    print(y)
    y+=1


print("-"*50)
#---------------------------------
#print a number in reverse order
#Here count is not mandetory .. only for own purpose
num1=2345
rev_val=0
count=0
while num1>0:
    temp=num1%10
    rev_val=rev_val*10+temp
    num1=num1//10
    count +=1
print ("rev_value is:",rev_val)
print("count is :", count)






