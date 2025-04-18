#square of each number from given list
list1=[1,2,3]
for i in list1:
    print(i**2)
print("-"*50)
#combine 2 lists----------------(+ operator only)

list2=[2,3,4,'sona','python']
list3=[5,6,7,8,'mishra','program']
#list2.append(list3)
#print(list2)
output=list2+list3
print(output)


print("-"*50)

#SUM OF ALL ELEMENTS FROM LIST
list4=[1,2,3,4,5,6,7,78]
print(sum(list4))#----------------method1
var=0
for i in list4:#---------------method2
    var += i
print(var)

    #method3--------------while loop
list4=[1,2,3,4,5,6,7,78]
#declaring 2 varibles
c =0 #index here
t=0 # value will be stored
while c < len(list4): #0 <8
     t+=list4[c]      #t=0+1
     c += 1           #c will increment to 1

print(t)               #end print total

print("*"*50)

#product of all elements
list5=[2,3,4,5,6]
count=1
for i in list5:  # method1
    count=count*i
print(count)

    #method2-while loop
list5=[2,3,4,5,6]
#declaring variables
a=0 # for index
b=1 # for total
while a< len(list5):
    b=b*list5[a]
    a=a+1
print(b)



print("*"*40)

#max and min of the list
list6=[12,23,808080808080,1,56,435,77]
max_value=max(list6) # list should pass as argument not list.max()
min_value=min(list6)
print(max_value,min_value)

#even odd from the given list
list7=[2,3,4,5,6,7,8,9,90]
result=[('even',x) if x%2==0 else ('odd',x) for x in list7] #method1-list comprehesion
print(result)

print("*"*40)
even=[]
odd=[]
for i in list7: #method2---------------for loop

    if i%2==0:
        print("val is even",i)
        even.append(i)
    else:
        print("val is odd",i)
        odd.append(i)
print("val is :",even)
print("val is :",odd)

print("*"*40)

#remove all the duplicate elements from the list
list7=[2,2,2,2,2,2,4,5,6,78,8,4,4,4,4,]
list8=[]
for val1 in list7:
    if val1 not in list8:
        list8.append(val1)


print(list8)


#combination of 2 elements from the list whose sum is 10.

list8=[3,7,4,6,8,9,2,4]
list_len=len(list8)
for val2 in range(list_len):

    for val3 in range(val2+1,list_len):
        if list8[val2]+list8[val3]==10:
            print(list8[val2],list8[val3])
        else:
            continue






