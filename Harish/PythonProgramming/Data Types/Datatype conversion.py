#######################intgerer#############
import json

from sqlalchemy.sql.operators import truediv

#int ------>flot
a= 23
print(a, type(a))
b=float(a)
print(b, type(b))

#int---->str
int1=2
c=str(int1)
print(c)

#Int to List is not possible
#Int to Tuple is not possible
#Int  to Dict is not possible
#Int to set is not possible

#int--------->bool

g=45
h=bool(g)
print(h, type(h))

m=0
n=bool(m)
print(n, type(n))


############Flost###########
#float----->int
float1=2.98
print(float1, type(float1))
float2=int(float1)
print(float2, type(float2))

#float--->str

f3=3.78
print(f3, type(f3))
f4=str(f3)
print(f4, type(f4))

#float to List is not possible
#float to Tuple is not possible
#float  to Dict is not possible
#float to set is not possible

#float---->bool

f5=5.89
print(f5, type(f5))
f6=bool(f5)
print(f6, type(f6))

f7=0.00
print(f7, type(f7))
f8=bool(f7)
print(f8, type(f8))


###########String##########

#String --------> int
a1= "133"
print(a1, type(a1))
a2=int(a1)
print(a2, type(a2))

#Srtring to Int conversion is not possible when the string in characters
#  it is possible only when the string is in numericals

#string ------> list

a2= "Harish"
print(a2, type(a2))
a3=list(a2)
print(a3, type(a3))

#string-------->tuple

a4= "Harish"
print(a4, type(a4))
a5=tuple(a4)
print(a5, type(a5))

#string-------->Dict
import json
str6 = '{"Name": "JOhn", "email":"john@gmail.com", "phone": 545435435}'
print(str6, type(str6))
# {"Name": "JOhn", "email":"john@gmail.com", "phone": 545435435} <class 'str'>
data = json.loads(str6)
print(data, type(data))
# {'Name': 'JOhn', 'email': 'john@gmail.com', 'phone': 545435435} <class 'dict'>
print(data['email']) # john@gmail.com

#string-----> set
a8='Harish'
print(a8, type(a8))
a9=set(a8)
print(a9, type(a9))

#String--->bool
a6="Harish Nani"
print(a6, type(a6))
a7=bool(a6)
print(a7, type(a7))

a10=" "
print(a10, type(a10))
a11=bool(a10)
print(a11, type(a11))

#######List####

#List  to int is not possible
#List to float is not possible

#list----> string

l1=[1, 4.8, (1,3,5), {1, 4, 8}]
print(l1, type(l1))
l2=str(l1)
print(l2, type(l2))

#list----> string

l2=[1, 4.8, (1,3,5), {1, 4, 8}]
print(l2, type(l2))
l3=tuple(l2)
print(l3, type(l3), l3[2])

#list----> Dict

l4 = ['a', 'b', 'c', 'd']
l5 = [33, 66, 89, 23]
result=dict(zip(l4,l5))
print(result, type(result))

l6 = ['a', 'b', 'c', 'd']
l7 = [55, 89, 32, 12]
result=dict(zip(l6,l7))
print(result, type(result))

#list-------->set
l8=[55, 89, 32, 12]
print(l8, type(l8))
l9=set(l8)
print(l9, type(l9))

#list-------->bool

l10=['a', 2, (1, 2, 4), 'Hellow']
print(l10, type(l10))
l11=bool(l10)
print(l11, type(l11))

l12=[]
print(l12, type(l12))
l13=bool(l12)
print(l13, type(l13))


#Tuple to int conversion is not possible
#Tuple to float conversion is not possible

#Tuple----->string

t1=('a', 2, (1, 2, 4), 'Hellow')
print(t1, type(t1))
t2=str(t1)
print(t2, type(t2), t2[4])

#tuple---->list

t3=('a', 2, (1, 2, 4), 'Hellow')
print(t3, type(t3))
t4=(list(t3))
print(t4, type(t4))

#tuple---->Dict

t4=('a','b','c','d')
t5=(1,4,5,6,7)
t6=dict(zip(t4,t5))
print(t6, type(t6))

#tuple---> Set

t7=('a', 2, (1, 2, 4), 'Hellow')
print(t7, type(t7))
t8=set(t7)
print(t8, type(t8))


#Tuple-------->bool

t9=('a', 2, (1, 2, 4), 'Hellow')
print(t9, type(t9))
t10=bool(t9)
print(t10, type(t10))

t11=()
print(t11, type(t11))
t12=bool(t11)
print(t12, type(t12))

#######Dictionary####


#Dict to int conversion is not possible
#Dict to float conversion is not possible

#dict---->string

d1={"a":'Name', "b":20, "c":8489954}
print(d1, type(d1))
d2=str(d1)
print(d2, type(d2),d2[2])

#dict---->List

d3={"a":'Name', "b":20, "c":8489954}
print(d3, type(d3))
d4=list(d3)
print(d4, type(d4))

#dict---->Set

d5={"a":'Name', "b":20, "c":8489954}
print(d5, type(d5))
d6=set(d5)
print(d6, type(d6))


#dict------>Bool
d7={"a":'Name', "b":20, "c":8489954}
print(d7, type(d7))
d8=bool(d7)
print(d8, type(d8))

d9={}
print(d9, type(d9))
d10=bool(d9)
print(d10, type(d10))


###########set#######
#set to int conversion is not possible
#set to float conversion is not possible

#set---> string
s1= {"a",'Name',20, 8489954}
print(s1, type(s1))
s2=str(s1)
print(s2, type(s2), s2[0])

#set---> List

s3= {"a",'Name',20, 8489954}
print(s3, type(s3))
s4=list(s3)
print(s4, type(s4))

#set---> Tuple

s5= {"a",'Name',20, 8489954}
print(s5, type(s5))
s6=tuple(s5)
print(s6, type(s6))

#set to dictonary conversion is not possible

s9= {"a",'Name',20, 8489954}
print(s9, type(s9))
s10=bool(s9)
print(s10, type(s10))


s7= set()
print(s7, type(s7))
s8=bool(s7)
print(s8, type(s8))


#####bool####

#boo------> int
b1=True
print(b1, type(b1))
b2=int(b1)
print(b2, type(b2))

#boo------> float

b3=False
print(b3, type(b3))
b4=float(b3)
print(b4, type(b4))

#boo------> str

b5=False
print(b5, type(b5))
b6=str(b5)
print(b6, type(b6))

#bool to list conversion is not possible
#bool to tuple conversion is not possible
#bool to dict conversion is not possible
#bool to set conversion is not possible











