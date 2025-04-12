#1). Python Dictionary program to add elements to the dictionary.
print("program 1")
d={}
d["name"]="basavaraja"
d["city"]="bangaluru"
print(d)
print("_"*50)
#2). Python Dictionary program to print the square of all values in a dictionary.
print("program 2")
d1={'a': 5, 'b':3, 'c': 6, 'd': 8}
for k,v in d1.items():
    print(k,v**2)

print()
print("-"*50)
#Python Dictionary program to move items from dict1 to dict2.
print("program 3")
dict1 = {'name':'john','city':'Landon','country':'UK'}
dict2 ={}
temp=dict1.copy()
for val in temp:
    val1=dict1.pop(val)
    dict2[val]=val1
print(dict1)
print(dict2)
print("-"*50)
#4). Python Dictionary program to concatenate two dictionaries.
print("program 4")
dict1 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict2 = {'Age':25,'salary': '$25k'}
dict1.update(dict2)              # method 1
print(dict1)
dict3=dict1|dict2                 # method 2
print(dict3)
print("-"*50)

#5). Python Dictionary program to get a list of odd and even keys from the dictionary.
print("program 5")
dict1 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
even_keys={}
odd_keys={}
for k,v in dict1.items():
    if k%2==0:
        even_keys[k]=v
    else:
        odd_keys[k]=v
print(even_keys)
print(odd_keys)
print("_"*50)

#6). Python Dictionary Program to create a dictionary from two lists.
print("program 6")
list1 = ['a','b','c','d','e']
list2 = [12,23,24,25,15,16]
dict1=dict(zip(list1,list2))
print(dict1)
print("-"*50)


#7Python Dictionary program to store squares of
#even and cubes of odd numbers in a dictionary using dictionary comprehension
        #Python Dictionary program to store
#squares of even and cubes of odd numbers in a dictionary using dictionary comprehension
print("program 7")
list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}

# iterate through the list of values
for val in list1:
    # val is divisible by 2, then value is even number
    if val % 2 == 0:
        # dict store value as square
        dict1[val] = val**2
    else:
        # dict store value as cube
        dict1[val] = val**3

print("result dictionary:", dict1)
print("-"*50)
#8). Python Dictionary program to clear all items from the dictionary.
print("program 8")
dict1 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
keys = list(dict1.keys())
print(keys)
for key in keys:
    del dict1[key]

print(dict1)
print("-"*50)

#9). Python Dictionary program to remove duplicate values from Dictionary.
print("program 9")
dict1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
d={}
for k,v in dict1.items():
    if v not in d.values():
        d[k]=v
    else:
        continue
print(d)
print("-"*50)

#10). Python Dictionary program to create a dictionary from the string.
string = "SQAToolss"
dict1 = {}

for char in string:
    dict1[char] = string.count(char)

print(dict1)

#11Python Dictionary program to sort a dictionary using keys.