# Variables
a=10
print(a)
# Single variables with single value
p=10
q=20
r=30
print(p,id(p))
print(q,id(q))
print(r,id(r))

# Multiple variables with multiple values
x,y,z = 10, 20, 30
print((x,id(x)), (y,id(y)), (z,id(z)))

# Multiple variables with single value
a=b=c = 100
print(a,id(a))
print(b,id(b))
print(c,id(c))

# single variable with multiple values
a= 10, 20, 30
print(a,id(a))

d=20
d=30
print(d)

