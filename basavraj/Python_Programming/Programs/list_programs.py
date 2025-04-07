#1). Python program to calculate the square of each number from the given list.
print("program 1")
l1=[2,3,4,5]
for i in l1:
    print(i**2,end=" ")
print()
print("-"*50)
#2). Python program to combine two lists.
print("program 2")
l1=[1,2,3,4]
l2=[5,6,7,8]
print()
print(l1+l2)
print("-"*50)
#3). Python program to calculate the sum of all elements from a list.
print("prpgram 3")

l1=[1,2,3,4,5]
s=0
for i in l1:
    s=s+i

print(s)
print("-"*50)
#4). Python program to find a product of all elements from a given list.
print("prpgram 4")

l1=[1,2,3,4,5]
prod=1
for i in l1:
    prod=prod*i
print(prod)
print("-"*50)
#5). Python program to find the minimum and maximum elements from the list.
print("program 5")
l2=[10,12,99,123,44,66]
print(max(l2))
print(min(l2))
l3=0
for i in l2:
    if i>l3:
        l3=i
print(l3)
print("-"*50)

for i in l2:
    if i<l3:
        l3=i
print(l3)
print("-"*50)

#6). Python program to differentiate even and odd elements from the given list.
print("program 6")

l1=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
print("-"*50)
#7). Python program to remove all duplicate elements from the list.
print("program 7")
lst=[1,2,3,3,3,2,2,5,6,7,8,8,8]
#print(set(lst))
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)

print(lst2)
print("-"*50)
#8). Python program to print a combination of 2 elements from the list whose sum is 10.
print("program 8")
def targets(lst,target_sum):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target_sum:
                print(lst[i],lst[j])

lst=[1, 2, 3, 7, 8, 5, 6, 4]
target_sum=10
targets(lst,target_sum)
print("-"*50)
#9). Python program to print squares of all even numbers in a list.
print("program 9")

lst=[1, 2, 3, 7, 8, 5, 6, 4]
for i in lst:
    if i%2==0:
        print(i**2,end=" ")
print()
print("-"*50)
#10). Python program to split the list into two-part, the left side all odd values and the
print("program 10")
l1=[5, 7, 2, 8, 11, 12, 17, 19, 22]
even=[]
odd=[]
for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

odd.extend(even)
print(odd)
print("-"*50)
#11).  Python program to get common elements from two lists.
print("program 11")

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
list3=[]
#print(set(list1)&set(list2))
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print(list3)
print("-"*50)

#12). Python program to reverse a list with for loop.
print("program 12")
list1 = [4, 5, 7, 9, 2, 1]
for i in range(len(list1)-1,-1,-1):
    print(list1[i],end=" ")
print()
print("-"*50)
#13). Python program to reverse a list with a while loop.
print("program 13")

list1 = [4, 5, 7, 9, 2, 1]
c=len(list1)-1
while c>=0:
    print(list1[c],end=" ")
    c=c-1
print()
print("-"*50)
#14). Python program to reverse a list using index slicing.
print("program 14")
list1 = [4, 5, 7, 9, 2, 1]
print(list1[::-1])

print("-"*50)
#15). Python program to reverse a list with reversed and reverse methods.
print("program 15")
list1 = [4, 5, 7, 9, 2, 1]
list1.reverse()
print(list1)
print("-"*50)
#16). Python program to copy or clone one list to another list.
print("program 16")
list1 = [4, 5, 7, 9, 2, 1]
#list2=list1[:]
#print(list2)
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)
print("-"*50)


#17). Python program to return True if two lists have any common member.
print("program 17")

#Input list
list1 = [2,4,7,8,3]
list2 = [4,5,0]

for value in list1:
    if value in list2:
        #Printing output
        print("True")

print("-"*50)


#18). Python program to print a specific list after
# removing the 1st, 3rd, and 6th elements from the list.
print("program 18")
l1=[1,2,3,4,5,6,7,8,9]
l1.pop(0)
l1.pop(2)
l1.pop(5)
print(l1)

print("-"*50)
#method 2
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
modified_list = [my_list[i] for i in range(len(my_list)) if i not in [0, 2, 5]]
print(modified_list)

print("-"*50)

#19). Python program to remove negative values from the list.
print("program 19")

lst=[1,-3,4,-9,5,-6,-9,11]
for i in lst:
    if i>0:
        print(i,end=" ")
print()
print("-"*50)

#20). Python program to get a list of all elements which are divided by 3 and 7.
print("program 20")

lst=[3,7,0,2,6,14,88,21]

for i in lst:
    if i%3==0 or i%7==0:
        print(i,end=" ")

print()
print("-"*50)


