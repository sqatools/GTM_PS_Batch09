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