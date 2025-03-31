a = 10
# a : variable
# = : assignment operator
# 10: value to store


# Address of Variable
print(id(a))  # 140726684158680
# print : in-built function :: print function shows the output on the console
# id : in-built function:: that return the memory address of the variable

print("the value of a: ", a)
print(a)

# if two variables with same value then their address are also same
x = 10
y = 10

print(id(x))
print(id(y))

# assign multiple value to multiple variable at a time
p, q, r = 40, 50, 60

print("the value of p :", p)
print("the value of q :", q)
print("the value of r =", r)


# assign one value to multiple variables

e = t = z = 100

print("the value of e:", e, id(e))
print("the value of t:", t, id(t))
print("the value of z:", z, id(z))





