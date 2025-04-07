# AND logical operator
# cond1 and cond2
# True and False :  False
# False and True :  False
# False and False :  False
# True and True :  True

# # write a python program to check the given number is divisible by 3 and 5
#(if both of the conditions match only then it will become true)
div = 12

if (div%3 == 0) and (div%5 == 0):
    print("this is divisible value:-", div) #true
else:
    print("this is not divisible :-", div)  #false

#####################################################

math = 12

if math%2 == 0 and math%4 == 0:
    print("both conditions are true ", math) #true
else:
    print("this won't print", math)# true
