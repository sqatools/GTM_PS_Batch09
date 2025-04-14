#1). Python program to create a set with some elements.
s1={1,2,3,4}
print(s1)
#2). Python program to add an element to a set.
s2={1,2,3}
s2.add(5)
print(s2)
#3). Python program to remove an element from a set.
s3={1,2,3}
s3.remove(2)
print(s3)
#4). Python program to find the length of a set.
s4={1,2,3}
#print(len(s4))
s=0
for i in s4:
    s=s+1
print(s)
#5). Python program to check if an element is present in a set.
s4={1,2,3,4,5,6}
if 5 in {1,2,3,4,5,6}:
    print("exits")
else:
    print("not exits")

#6). Python program to find the union of two sets.
a = {1,2,4,5}
b = {7,8,9,1}
c=a|b
print(c)
#7). Python program to find the intersection of two sets.
s5={1,2,3,4,5}
s6={6,7,1,2,3}
s7=s5&s6
print(s7)
#8). Python program to find the difference of two sets.
s5={1,2,3,4,5}
s6={6,7,1,2,3}
s7=s5-s6
print(s7)
#9). Python program to find the symmetric difference of two sets.
s5={1,2,3,4,5}
s6={6,7,1,2,3}
s7=s5^s6
print(s7)
#10). Python program to show if one set is a subset of another set.
#11). Python program to check if two sets are disjoint.
#13). Python program to convert a set to a list.
s5={1,2,3,4,5}
print(list(s5))
#12). Python program to convert a list to a set.
s4=[1, 2, 3, 4, 5]
print(set(s4))
#14). Python program to find the maximum element in a set.
s4=[1, 2, 3, 4, 5]
#print(max(s4))
m=0
for i in s4:
    if i>m:
        m=i
print(m)
#15). Python program to find the minimum element in a set.
s4=[1, 2, 3, 4, 5]
#print(min(s4))
minn=s4[0]
for i in s4:
    if i<m:
        m=i
print(minn)
#16). Python program to find the sum of elements in a set.
s4=[1, 2, 3, 4, 5]
s=0
for i in s4:
    s=s+i
print(s)
#17). Python program to find the average of elements in a set.
s8=[1, 2, 3, 4, 5]
s9=len(s4)
sm=0
for i in s8:
    sm=sm+i
print("average",sm/s9)
#18). Python program to check if all elements in a set are even.
s8=[1, 2, 3, 4, 5]
s=len(s8)
c=0
for i in s8:
    if i%2==0:
        c=c+1
if c==s:
    print("all elements are  even")
else:
    print("all elements are not even")
#19). Python program to check if all elements in a set are odd.
s8=[1, 7, 3, 11, 5]
s=len(s8)
c=0
for i in s8:
    if i%2==1:
        c=c+1
if c==s:
    print("all elements are  odd")
else:
    print("all elements are not odd")
#20). Python program to check if all elements in a set are prime.
s8=[17, 7, 3, 11, 5]
s1=len(s8)
for n in s8:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print(n,end=" ")
print("half done and doubt")
#