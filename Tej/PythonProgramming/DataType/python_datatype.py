##types of datatype-->python is object based programming language

# 1)numbers
#     a)integer
#     b)float
#     c)complex numbers
#
# 2)sequential
#     a)string
#     b)list
#     c)tuple
# 3)dictionary
# 4)set
# 5)boolean
print("********************************************************************************************")
###to find types of data which function
#   Type is used

#integrer

#properties ofinteger
    # -->integer is immutable datatype (once defined we cannot change)
    # -->integer can contains and positive and negative value
    # -->only whole number will be consider (2.3, 0.3 its wrong)
    # -->there is no limit to define data in variables

n1=0
n2=4
n3=100
n4=734834635475475437478485886



print (n1, type(n1))    #0 <class 'int'>
print (n2, type(n2))    #4 <class 'int'>
print (n3, type(n3))    #100 <class 'int'>
print (n4, type(n4))    #734834635475475437478485886 <class 'int'>

var1="hello"
print(var1*5) #hellohellohellohellohello

print("_"*50)  #__________________________________________________
print("********************************************************************************************")
#float

#properties of float
    # -->float is immutable datatype (once defined we cannot change)
    # -->float only  contains pointer value(2.3, 0.3 it can be alloweded)
    # -->positive and negative value can be consider
    # -->there is no limit to define data in float


f1 = 0.0
f2 = 12.45
f3 = 423234.317346
f4 = 8384774.78788
f5=0.647384

print (f1, type(f1))    #0.0 <class 'float'>
print (f2, type(f2))    #12.45 <class 'float'>
print (f3, type(f3))    #423234.317346 <class 'float'>
print (f4, type(f4))    #8384774.78788 <class 'float'>
print (f5, type(f5))    #0.647384 <class 'float'>

print("********************************************************************************************")
#complex-->jikde pan j ahe tikde imaginary gintihonar

#va1=x+yj
#x=realvalue
#y=imaginary value

var2=10+20j
print(var2, type(var2))
print("real valaue:", var2.real)    #real valaue: 10.0
print("imaginary value", var2.imag) #imaginary value 20.0



#zhol(anything print under ""is considered as string)
print("20+3j")  #20+3j


print("********************************************************************************************")
#string--->

#properties of string
    # -->string is immutable datatype (once defined we cannot change)
    # -->string follows positive and negative indexing
    # -->there is no limit for string to define
    # -->string value defined differnet typesof qyotes single, double, single triple,double triple.
    #string can contain any data, number, spcial charchter

s1='s'
s2="hello"
s3="we are learning"

print(s1, type(s1))  #s <class 'str'>
print(s2, type(s2)) #hello <class 'str'>
print(s3, type(s3))  #we are learning <class 'str'>

s5="my name is 'tejas' i stay in mumbai"
print(s5, type(s5))   #my name is 'tejas' i stay in mumbai <class 'str'>

s6='my name is "tejas" i stay in mumbai'
print(s6, type(s6)) #my name is "tejas" i stay in mumbai <class 'str'>

# \n =line break           ajun \t = space sati

a="my name is tejas  \n i stay in mumbai"
print(a)   #my name is tejas
            #i stay in mumbai

#indexing in string (spaces la pan considered in index)

#0 1 2 3 4 5 =positive indexing start from zero
#p y t h o n
#-6 -5 -4 -3 -2 -1 = negative indexing from -1

str_a="Python"
print("first char:", str_a[0])  #first char: P
print("third index char:", str_a[3])  #third index char: h
print("negative index char:", str_a[-3])  #negative index char: h

print("********************************************************************************************")
#List--->

#properties of list
    # -->list is mutable datatype (we can change and modify)
    # -->list defined with square bracket
    # -->list can contain all different types of value, int, float, string, list, tuple, dic, set, boolean, complexnumber
    # -->listfollows the positve and negative indexing like string
    #-->thereis no limit to defined values in list
    #-->list values are comma separted.

list1=[2, 3.4, "hello", [4,5,7], (2,7,9), {'a':123},{5,7}, True, 40+5j, None]
print(list1,type(list1))  #[2, 3.4, 'hello', [4, 5, 7], (2, 7, 9), {'a': 123}, {5, 7}, True, (40+5j), None] <class 'list'>
print(list1[3])    #[4.5.7]

#zhol varhce madhe madhe
print(list1[3][2])   #7
print(list1[-4])   #{5,7}

###########
list2=[5,7,8,9]
list2.append(100)
print(list2)     #[5, 7, 8, 9, 100]



print("********************************************************************************************")

#tuple =itis similar like a list it is immutable datatype (we cannot change), it can contain any type of data,tuple defined with () round brackwt

tuple1= (1,2,4, 'hello', [4,5,6], (3,6),{'a':123},{4,6,8},True)
print(tuple1, type(tuple1)) #(1, 2, 4, 'hello', [4, 5, 6], (3, 6), {'a': 123}, {8, 4, 6}, True) <class 'tuple'>

#properties of list
    # -->tuple is immutable,once it is defined we cannot change the value
    # -->tuplecotains all type of data like int, float, complex, str, list, tuple, dict, boolean
    # -->tuple follows positive negative indexing as like string string and lis
    # -->tuple store data in with round brackets
    #-->in terms of performance, tuple is faster than list
    #it can also have duplicate value, set datatype shivay duplicate sarvan madhe use karu shakto

tuple2 =(4,7,9, 4,('a', 'b', 'c'), 'hello',14)

print(tuple2[2])   #9
print(tuple2[-3]) #('a', 'b', 'c')
print(tuple2[-3][-3])   #a
print(tuple2[5][1])    #e


print("********************************************************************************************")

#dictionary-->curly brackecs used{}, it is having in key and value format

#dict1={'key':'value'}

dict1={'name':'rahul gupta', 'age':28, 'email':'rahul@gmail.com', 'phone':6745234512}
print(dict1, type(dict1))  #{'name': 'rahul gupta', 'age': 28, 'email': 'rahul@gmail.com', 'phone': 6745234512} <class 'dict'>

#to get data we need to mention key
print(dict1['name']) #rahul gupta

#properties of dict
    # -->dict  is mutable,we can change data anypoint oftime
    # -->dict store data in key value format eg{'a':123}
    # -->dict store datawith unique key, duplicate keys are not allowed
    # -->dict value can contain duplicate data
    #-->if we will duplicate keys, then latest defined key data will be considered
    #-->only immutable data type can be key in dictionary, int, float, string, tuples, boolean.
    #-->all types of data can be value in the dictionary
    #-->dictionary does not followpositve negative index
    #-->dic store the data in lifo(last in first out)


dict2={'a':123, 'b':456}
print(dict2)
dict2['c']=500   #{'a': 123, 'b': 456}
print(dict2)  #{'a': 123, 'b': 456, 'c': 500}

#if we define duplicate keyin the dic then latest value will be considered
dict3={'a':123, 'b':456, 'c':600, 'a':500, 'e':456}
print(dict3)   #{'a': 500, 'b': 456, 'c': 600, 'e': 456}


dict4={34:4.5, 55.6:'hello', 'name':'john', ('a','b'):[4.6,8,9], True: {'P':345, 'Q':789, 'R':3456}}
print(dict4)  #{34: 4.5, 55.6: 'hello', 'name': 'john', ('a', 'b'): [4.6, 8, 9], True: {'P': 345, 'Q': 789, 'R': 3456}}

#mutable data type is not allowed as key (list,dict,set)(zhol)


#remove data from dict
z={34:4.5, 55.6:'hello', 'name':'john', ('a','b'):[4.6,8,9], True: {'P':345, 'Q':789, 'R':3456}}
result=z.popitem()  # it will remove last data entered in the dict
print(result)  #(True, {'P': 345, 'Q': 789, 'R': 3456})



print("********************************************************************************************")
#set-->it uses {], curly bracket,  it store unique value, set is a mutable data type, mage pude kase pan yete number
set1={3,'c',7,'a', 'b', 8,2,7, 'a', 9,3}
print(set1) #{2, 3, 'c', 'a', 7, 'b', 8, 9}

#properties of set
    # -->set  is mutable data type,we modify it
    # -->set storeunique data,duplicate values are not allowed
    # -->set store data in random order.
    # -->set can contains onlyimmutable data type like int, float,string, tuple, boolean, complex number
    #-->set doe not follow indexing


set2={3,5,7,'a', 'b'}
print(set2,type(set2))  #{3, 7, 5, 'b', 'a'} <class 'set'>

set2.add(100)
print(set2)  #{3, 100, 5, 'a', 7, 'b'}






