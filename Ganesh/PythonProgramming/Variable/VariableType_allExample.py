#additional operators
num=1
num2=2
a=num + num2
print("additinal:", a)
print('-'*200)
#multiplication
num=1
num2=2
a=num * num2
print("multiplication:", a)
print('-'*200)
#subtraction
num1=3
num2=7
a=num1 - num2
print("subtraction:", a)
print('-'*200)
#division
v1=50
v2=3
print("Division:",v1/v2) #when we divide number with single '/' then it's give pointer output
print("Division:",v1//v2) #'//' use to give whole value without pointer
print('-'*200)
#get square and cube of given value
n=5
print("square & Cube :", n**2,n**3)
#get remider value
a=20
a2=3
print("remider value :", a%a2)
print('-'*200)
#cmpare 2 value
n1=40
p2=50
p3=40
print(n1 == p2)
print(n1 == p3)
print(n1 !=p2) # value is not equal to '! ='
print(id(p3)== id(n1))
print('-'*200)
# (a-b)^2=a^2 +b^2 +2ab
a=4
b=7
LHS=(a-b)**2
RHS=a**2 + b**2 - 2*a*b
print("print LHS",LHS,"Print RHS :",RHS)
print(LHS == RHS),print( RHS !=LHS)
print('-'*200)
# calculate simle interest
#a=principle outstanding
#b=rate of interest
#c=days
#d=tenure
a=2000
b=10
c=30
d=24
T=d/12
Interest = (a*b*T)/100
print(Interest)
perdayInterst= (a*b) / (100*365)
print("perdayInterst :", perdayInterst)





