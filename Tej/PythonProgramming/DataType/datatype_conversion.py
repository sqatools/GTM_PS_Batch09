####integer #####

#int-->float

n1=55
f1=float(n1)
print(f1, type(f1))  #55.0 <class 'float'>

#int-->string
n2=456567
s2=str(n2)
print(s2, type(s2), s2[2]) #456567 <class 'str'> 6

#int -->list(conversion is not possible)  ####he kadun check kar
####n3=8956948
####l1=list(n3)
####print(l1)  #TypeError: 'int' object is not iterable
#the data type which accept multiple types of data isn called iterable only, iterable to iterable is possible

#int-->boolean
v1=0
print(v1,type(v1))  #0 <class 'int'>

b1=bool(v1)
print(b1, type(b1)) #False <class 'bool'>

v2=503
print(v2,type(v2))  #503 <class 'int'>

b2=bool(v2)
print(b2, type(b2)) #True <class 'bool'>

#int -->tuple(conversion is not possible)

##int -->dict(conversion is not possible)

###int -->set(conversion is not possible)


print("********************************************************************************************")
#float

#float-->int

f1=56.78
n1=int(f1)
print(n1,type(n1))  #56 <class 'int'>

#float-->string

f2=678.293
print(f2, type(f2))

s2=str(f2)
print(s2, type(s2), s2[-2]) #678.293 <class 'str'> 9

#float-->list  #conversion is not possible

#float-->dict  #conversion is not possible

#float-->set  #conversion is not possible


#float-->bool

x1=0.0
b1=bool(x1)
print(b1, type(b1)) #False <class 'bool'>

x2=45.67
b2=bool(x2)
print(b2, type(b2))  #True <class 'bool'>


print("********************************************************************************************")
#string

#string-->int

####s1="Hello"
####n1=int(s1)
####print(n1,type(n1))

#cannot convert string into integer when it contains charcter as value
#ValueError: invalid literal for int() with base 10: 'Hello'

#string to int conversion is possible when string contains only number
#
s2="987654"
print(s2, type(s2))  #987654 <class 'str'>

n2=int(s2)
print(n2, type(n2))  #987654 <class 'int'
print(n2*2)#1975308


##string-->float


s3="567.89"
f3=float(s3)
print(f3, type(f3), f3*10) #567.89 <class 'float'> 5678.9

##string to lists

str3="python"
l3=list(str3)
print(l3, type(l3))    #['p', 'y', 't', 'h', 'o', 'n'] <class 'list'>


##string to tuple

str4="python"
t3=tuple(str4)
print(t3, type(t3))    #('p', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

#string to dict

####str5="good morning"
#### d1=dict(str5)
#### print(d1)   #he run nahi honar

str6="{'name':'john', 'email':'john@gmail.com','phone':9807564321}"
print(str6, type(str6)) #{'name':'john', 'email':'john@gmail.com','phone':9807564321} <class 'str'>

#we cannot direct convert string to dict so we can use library (json)
#when string follows the dic pattern and all values are defined in json key value
#format then wwe can convert into dict with help of json module

import json

str7 = '{"name": "john", "email": "john@gmail.com", "phone": 9807564321}'
print(str7, type(str7))

data = json.loads(str7)
print(data, type(data))  #{'name': 'john', 'email': 'john@gmail.com', 'phone': 9807564321} <class 'dict'>
print(data['email']) #john@gmail.com

#string to set  -->will remove duplicate values from here
str8="python programming"
s1=set(str8)
print(s1, type(s1))#{'t', 'a', 'n', 'i', 'p', 'm', 'h', 'o', 'y', ' ', 'r', 'g'} <class 'set'>

#string to boolean
s9=""
b1=bool(s9)
print(b1, type(b1))  #False <class 'bool'>

s10="hello"
b2=bool(s10)
print(b2, type(b2)) #True <class 'bool'>


print("********************************************************************************************")

#list


#list to int
####l1=[4,5,6]
####n1=int(l1)
####print(n1, type(n1))  #nahihonar conversion

#list to string

l2=[5,7,8,9]
s2=str(l2)
print(s2, type(s2))  #[5, 7, 8, 9] <class 'str'>
print(s2[1], s2[-2])  #5 9

#list to tuple

l3=[5,7,9,2,5]
t3=tuple(l3)
print(t3, type(t3))  #(5, 7, 9, 2, 5) <class 'tuple'>

#list to dict --->it isnotpossible
#list to dict conversion is  possible but khali bag

#if we have 2 list amdconvert into dict,then wecan do it with help of zip function

l1=['a', 'b', 'c', 'd']
l2=[33, 66, 89, 23]
print(list(zip(l1,l2)))   #[('a', 33), ('b', 66), ('c', 89), ('d', 23)]

result=dict(zip(l1, l2))
print(result, type(result)) #{'a': 33, 'b': 66, 'c': 89, 'd': 23} <class 'dict'>

