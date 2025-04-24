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

print("*"*60)
list1 = [4, 6, 8]
list2 = [7, 1, 4]
#Output= ((4, 7), (6, 1), (8, 4))
tup=tuple(zip(list1,list2))
print(tup)

print("*"*60)
tup1 = (41, 15, 69, 55)
print(max(tup1))
print(min(tup1))

print("*"*60)
rel = [4,6,3,8]
res=[]
#Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
for i in rel:
    res.append((i,i**2))
print(res)


#method-2
tup3=[(i,i**2) for i in rel]
print(tup3)


print("*"*60)
#val from index
tup4 = (4, 8, 9, 1)
print(tup4[2])

print("*"*60)
tupp1= (6,7,3)
tupp2= ('a','b','c')
tupp3=tuple(zip(tupp2,tupp1))
print(tupp3)

tupp5= ( 18, 65, 3, 45)
#Output=(18, 65, 3, 45, 15)
#add 15 to tuple
#list and tuple conversion and viseversa
tupp5=list(tupp5)
tupp5.append(15)
tupp5=tuple(tupp5)
print(tupp5)

print("*"*60)
# Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
tupp6 =('s','q','a','t','o','o','l','s')
print(tupp6[1])
print(tupp6[-3])

print("*"*60)
tupp7=('p','y','t','h','o','n')
for i in range (len(tupp7)):
    if i==tupp7[i]:
        print(true)
    else:
        continue




















