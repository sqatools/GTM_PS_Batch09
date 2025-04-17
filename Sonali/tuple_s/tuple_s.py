######### write tuple comprehension ##########

# write a program to get square of all the values from given tuple with tuple comprehension.
# Note :  tuple comprehension return the generator object instead of tuple values directly
#         if want to get value in tuple
tup_x = (5, 7, 9, 2, 4)
square = tuple(x**2 for x in tup_x)
print(square) # (25, 49, 81, 4, 16)

# for val in square:
#     print(val)

# (25, 49, 81, 4, 16)

# Home work
# tuple comprehension: need to practice.py.
# 1. tuple comp with if condition
# 2. tuple comp with if and else condition.
# 3  tuple comp with nested loop.
#tuple comprehesion if conndition

tup_y=(2,4,6,7,5,3)
even=tuple(x for x in tup_y if x%2==0)
print(even)

#tuple comp with if and else condition
tup_z=(2,4,3,5,6,7)
eo=tuple(('even',val)if val%2==0 else ('odd',val) for val in tup_z)
print(eo)

#tuple comp with nested loop
result=tuple((x,y) for x in ('a','b','c') for y in ('p','q'))
print(result)

