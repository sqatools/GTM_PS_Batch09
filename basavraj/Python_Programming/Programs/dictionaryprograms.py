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
print("program 10")
string = "SQAAToolss"
dict1 = {}

for char in string:
    dict1[char] = string.count(char)

print(dict1)
print("-"*50)

#11Python Dictionary program to sort a dictionary using keys.
print("program 11 doubt")
print("_"*50)
#12). Python Dictionary program to sort a dictionary in python using values.
print("program 12 doubt")
print("_"*50)
#13). Python Dictionary program to add a key in a dictionary.
print("program 13")
dict1 = {1:'a',2:'b'}
dict1[3]="c"
print(dict1)
print("-"*50)

#14). Python Dictionary program to concatenate two dictionaries.
print("program 14")
dict1 = {'name':'yash','city':'pune'}
dict2 =  {'course':'python','institute':'sqatools'}

dict3=dict1|dict2
print(dict3)

dict1.update(dict2)
print(dict1)
print("-"*50)
#15). Python Dictionary program to swap the values of the keys in the dictionary.
print("program 15")
D1 = {'name':'yash','city':'pune'}
d2={v:k for k,v in D1.items()}
print(d2)
print("-"*50)

#16). Python Dictionary program to get the sum of all the items in a dictionary.
print("program 16")
d1={'x':23,'y':10,'z':7}
s=0
for val in d1.values():
    s=s+val
print(s)
print("-"*50)

#17). Python program to get the size of a dictionary in python
print("program 17 doubt")
print("-"*50)

#18). Python Dictionary program to check whether a key exists in the dictionary or not.
print("program 18")
d1={"name":"basava","city":"gadag","state":"karnataka"}
c=0
for key in d1.keys():
    if key=="city":
        c=c+1
if c==1:
    print("the key is exists")
else:
    print("the entered key is not exits")
print("-"*50)
#19). Python program to iterate over a dictionary
print("program 19")
d1={"name":"basava","city":"gadag","state":"karnataka"}
for key,value in d1.items():
    print(key,value)
print("_"*50)
#20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
print("program 20")
n = 4
D1=dict((i,i**3) for i in range(1,n+1))
print(D1)

print("_"*50)
