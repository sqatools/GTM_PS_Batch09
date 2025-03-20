a=10
print(a)  # it will print the value of a
print(id(a)) #it will print the addres "a" value
##############################
a=10
b=10
print(a,b)
print(id(a),id(b)) # here a and b are sharing the same memory bcz both variable having the same value

###############################
a,b=10,20  # here 10 value assigning to the a and 20 assigning to b
print("value of a is =",a)
print("value of b is =",b)
print(id(a),id(b))  # here both a and b sharing the different memory

###############################
a=b=c=10     # here a,b and c having the same value
print(a,b,c)
print(id(a),id(b),id(c)) # whenever we are assinging same value to the multiple variables address will be same

#################################

x=10
print(id(x))
x=30
print(x) # here latest x value will print
print(id(x)) # latest x value address will print

########################################

# Rules to defined variable name
# 1 variable name should not cantain space in between thr variable name ex = xx yy
# 2 variable should not the numbers ex= 1var
# 3 variable should not cantain the special characters
# 4 variable name are case sensitive ex = name, NAME,Name,nAmE,NAme all are same