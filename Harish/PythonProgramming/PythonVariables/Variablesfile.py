
                                #Variables
# single variable having single value
x=20
y=30
z=50
print("x value is :", x)
print("y value is :", y)
print("z value is :", z)
#address
print("x value is :", x, id(x))
print("y value is :", y, id(y))
print("z value is :", z, id(z))

#Multiple variables with multiple values
x, y, z = 10, 20, 30
print("x value is :", x)
print("y value is :", y)
print("z value is :", z)
#Address
print("x value is :", x, id(x))
print("y value is :", y, id(y))
print("z value is :", z, id(z))

#multiple variables with only one value
x=y=z=50
print("x value is :", x)
print("y value is :", y)
print("z value is :", z)
#Address
print("x value is :", x, id(x))
print("y value is :", y, id(y))
print("z value is :", z, id(z))

# Single variable with multiple values
x=10,12,30
print(x,id(x))

#Same variables with different values
x=10
x=20
x=30
print(x,id(x))

print("Hello World")
