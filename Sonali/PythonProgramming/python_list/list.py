list1=[1,2.3,"hello","sonali",2456,8989]
print(list1,type(list1))

print("-"*50)

for i in list1:
    print(i*2)

print("-"*60)
list2=[2,4,6,8,5,7,3,1]
for j in list2:
    if j%2==0:
        print([j],end=" ")

print("-"*60)

print(dir(list))

#Add data to the list
#append()------add data to the last position
list_1=[56,"hello","kite",67,8888888]
list_1.append(34444444444444444)
print(list_1)

#insert()-------------insert at specific index point
list_1.insert(1,"sonali")
print(list_1)

#extend()-----------------add data from 1 list to another list
list_2=["python","koooooooooop"]
list_1.extend(list_2)
print(list_1)

#concartination

list_g = [55, 77, 88, 'Hello']
list_h = [11, 12, 13, 4.5]
result=list_g+list_h
print(result)

#list multiplication
list_i=[5,6,'a','k']
result2=list_i*2
print(result2)

#Remove the data with vaient way
#remove()---------------------remove the data
list_k=[1,4,3,23,'a','b','sonali',9087,678]
list_k.remove('b')
print(list_k)

#pop()-------------------remove last data if no argument passed,removed according to index
list_p=[1,234,543,34,23,'a','sonali','you']
list_p.pop()
print(list_p)
list_p.pop(1)
print(list_p)

#clear()----------------------remove all the data from the list. empty list will be there
list_p.clear()
print(list_p)
#delete---------------------it will delete full list .. no empty list also pending
list_j=[1,234,543,34,23,'a','sonali','you']
del list_j

#slicing concept also we can use for delete some portion of the list  by index and slicing concept
list_n = [4, 6, 8, 22, 55, 11, 45]
del list_n[1:4]
print(list_n)

del list_n[-3]
print(list_n)

#replace data from list-----------------it will be done by index no keyword for replace
list_r=[12,13,14,234,456,567,789,900,'a','b']
list_r[0]=400
print(list_r)

list_r[2:5]=[300,350,260]
print(list_r)

#index of a element from list----------if duplicate then 1st occarnce will be considered
list_l=[12,34,23,89589854,'a','g','sona','g',12,34,34,34,'sona']
print(list_l.index('g'))
print(list_l.count(34))
print(len(list_r))

#sort() method------------- -both asecending and descending order-it will modify the list
#ascending order------sort()
#descending order------------sort(reverse=True)

list_w=[1,68,23,67,0,5,54,1000000,7777,564]
list_w.sort()
print(list_w)
list_w.sort(reverse=True)
print(list_w)

#sorted function-----------------------both ascending and descending order ----it will not modify the list

list_a=[1,68,23,67,0,5,54,1000000,7777,564]
print(sorted(list_a))
print(sorted(list_a,reverse=True))

list_x = ['hello', 'Python', 'Apple', 'Mango']
print(sorted(list_x))
print(sorted(list_x,reverse=True))

#list comprehesion
result10=[x for x in list_w if x%2==0]
print(result10)


list99 = [5, 7, 9, 12, 6]
#output = [(5, 'odd'), (7, 'odd'), (9, 'odd'), (12, 'even'), (6, 'even')]

result9=[(val,'even')  if val%2==0 else (val,'odd') for val in list99]
print(result9)

#nested loop condition

result11=[(x,y) for x in ['a','b','c'] for y in ['p','q']]
print(result11)









