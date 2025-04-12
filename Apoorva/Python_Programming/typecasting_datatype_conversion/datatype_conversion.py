### string -> list ####
str3 = "Python"
l3 = list(str3)
print(l3, type(l3))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

print(l3[0],l3[1])

print("_"*50)


### List -> tuple ###
l3 = [5, 7, 9, 2, 5]
t3 = tuple(l3)
print(t3, type(t3))
# (5, 7, 9, 2, 5) <class 'tuple'>

print(t3[0],t3[1])

######### list -> dict #########

list_a = ['a','b', 'c']
list_b = [1, 2, 3, 4]

dict1 = dict(zip(list_a,list_b))
print(dict1)