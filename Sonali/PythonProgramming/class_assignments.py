
str1= "Hello we are learning python program"
#output=[('Hello',5) ('we',2)]

list2=str1.split()
result=[]
for word in list2:
    result.append((word,len(word)))
print(result)


#2nd way(list comprehesion)
r=[(word,len(word)) for word in list2]
print(r)





