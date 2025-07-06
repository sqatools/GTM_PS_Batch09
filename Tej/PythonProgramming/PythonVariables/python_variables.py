a=10

#a : variables
#= :assignement operator
#10: value to store


#to find the address  of variables

print(id(a))    #140717193501400
print(a)       #10
print("this is value:", a)   #this is value: 10

###########inbuilt function

#1)print
#2)id

# eg

p=1
q=2
r=3

print(p)  #1
print(q)  #2
print(r)  #3

#eg

w=1.2,3
print(w)  #1,2,3


#eg ---->if two variables with same value then their address is also same

x=10
y=10

print("the value of x,y:",x,y, "the address of x,y:",id(x), id(y))   #the value of x,y: 10 10 the address of x,y: 140717193501400 140717193501400


#eg-->assign multiple value  tomultiple variable at a time

p,q,r=40,50,60
print(p)  #40
print(q)  #50
print(r) #60


#eg--> assign one value to multiple variables

x=y=z=100

print(x,id(x))#100 140717193504280
print(x,id(y))#100 140717193504280
print(x,id(z))#100 140717193504280

###############################
#rules to defined variables names

#1)variable name shouldnot contain space in the name (a b c=50 invalid)
#2)varibale name  cannot start with number (1_var=60 invalid)
#3)there is no limit for variable name lenghth (abc_xuz_hello =40)
#4) cannot contains special charchter in variable name except underscore (var% =700 invalid)
#5)variable name is  casesenitive (a, A) both are different



#math operators on variables


# + :plus
# - :minus
# * :multiplication
# / and // :division
# == :equal to
# != : not equal to
# **: power operator
# %: reminder operator

#addition

num1=40
num2=50
num3= num1+num2

print(num3)   #90
print("addition of num1, num2:", num1+num2)  #90

#multiplication

var1=num1 *num2
print(var1)   #2000

#subtraction

print("subtraction", 500-num1)  #460

#divsion

v1=50
v2=3

print('divsion with single /:', v1/v2)   #divsion with single /: 16.666666666666668
print('divsion with double //:', v1//v2)   #divsion with double //: 16


#get square and cube of any number


n1=5
print(n1**2) #25
print(n1**3)  #125


#reminder value

v2=20
v3=3

print("remainder value :", v2%v3) #2

#equal operator/ not equal)

p1=40
p2=50
p3=40

print(p1==p2) #false
print(p1 != p2)#true

print(p1==p3)   #true



##################################################
# (a+b)^2 = a^2+b^2 +2ab

#(a-b)^2 = a^2+b^2-2ab


a=4
b=7

lhs=(a-b)**2
print(lhs)  #9

rhs=a**2+b**2-2*a*b
print(rhs)  #9


##########################################################
#calculate simple interest
p=2000
r=8
t=5
#p=principle amount
#r= rate of interest
#t=time  in a year

a=(p*t*r)/100

print ("simple interest:",a)#8000.0