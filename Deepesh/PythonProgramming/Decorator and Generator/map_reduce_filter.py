# lambda function : lambda function anonymous function without function body

result = lambda x, y: x+y
print("result :", result(50, 70))

print("")
# Map :  map function help to use list of values as parameter for the function.

list1 = [2, 5, 7, 9, 8]
result = tuple(map(lambda x:x**2, list1))
print(result)  # (4, 25, 49, 81, 64)

# filter function : filter return the output with the help lambda function and list of values.
#                   ->  It only return the output when condition is true
list2 = [2, 5, 6, 9, 8, 11, 15, 17, 18]
even_value = list(filter(lambda x:x%2 == 0, list2))
print("even values :", even_value)  # [2, 6, 8, 18]
# Reduce function


from functools import reduce
# reduce :  reduce help us to generate a combine values
list3 = [2, 5, 6, 9, 8, 11, 15, 17, 18]
result = reduce(lambda x, y:x+y, list3)
print("result :", result)
