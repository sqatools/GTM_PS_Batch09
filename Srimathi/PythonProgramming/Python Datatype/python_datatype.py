n1 = 0
n2 = 4
n3 = 100
n4 = 45435435434354545454222333333333
n5 = -5644545

print(n1, type(n1)) # 0 <class 'int'>
print(n4, type(n4)) # 45435435434354545454222333333333 <class 'int'>


var1='Sri'
print(var1*5) #SriSriSriSriSri

s1="Sumanth"
print(s1, type(s1)) #Sumanth <class 'str'>

# Python program to repeat a given string 5 times
s2="Python"
n1=5
print(s2, type(s2))
print("Result :", s2*n1) #Result PythonPythonPythonPythonPython

# Python program to get the Average of given numbers.
a = 40
b = 50
c = 30
print("Average=", (a+b+c)/3) #Average = 40

#Python program to get the median of given numbers.
# Formula : (n+1)/2
# n = Number of values
values= [45, 60, 61, 66, 70, 77, 80]
values.sort()
n=len(values)
median_value = (values[n // 2 - 1] + values[n // 2]) / 2
print("Median:",median_value )


# Python program to print the square and cube of a given number.
n1 = 9
print("Square:", n1*n1) #Square = 81
print("Cube:", n1*n1*n1) #Cube =   729

#Python program to interchange values between variables.
a = 10
b = 20

print("Value of a", b)
print("value of b", a)





#Problem to get product of all elements in a list
list1=[2,3,4,5]
var =1
for value in list1:
    var *= value;
print(list1)
print(var)


# Python program to find the minimum and maximum elements from the list.
list1 = [23,56,12,89]
list1.sort()
print("smallest:", list1[0])
print("Largest:", list1[-1])

# Python program to remove all duplicate elements from the list.
list1 = [5,7,8,2,5,0,7,2]
list2 = []

for value in list1:
    if value not in list2:
        list2.append(value)
print(list2)

#Python program to get common elements from two lists.
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]

common_list = []
for value in list1:
    if value in list2:
        common_list.append(value)

#Printing output
print(common_list)


# Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
list1=[2,3,4,5,6]
list1 = [element for (value,element) in enumerate(list1)
    if value not in (1,3,6)]
print(list1)


tup2=(6,9,10,('a','b','c'), 13)
print(tup2[2])
print(tup2[-2])

# Python tuple program to create a tuple with 2 lists of data.
tup1 = [4, 6, 8]
tup2 = [7, 1, 4]
tup=tuple(zip(tup1, tup2))
print(tup)

#Python tuple program to find the maximum value from a tuple.
tup1 = (41, 15, 69, 55)
print("Maximum value", max(tup1))


#Python tuple program to create a tuple and find an element from it by its index no.
tup1 = (4, 8, 9, 1)
print(tup1[2])

#Python tuple program to assign values of tuples to several variables and print them.
tup1 = (6,7,3)
a,b,c = tup1
print("a:",tup1[0])
print("b:",tup1[1])
print("c:",tup1[2])






