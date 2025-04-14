# Class of 20/03/2025

## Integer Data Type ##

n1=0
n2=4
n3=100
n4=432123567829837647382
n5=-5678765678768787876565656
print("n1:", n1, type(n1))
print("n2:", n2, type(n2))
print("n3:", n3, type(n3))
print("n4:", n4, type(n4))
print("n5:", n5, type(n5))

## Float Data Type ##

f1=0.0
f2=12.32
f3= 4543234567.77900
f4=-45678767.789
f5=0.044545
f6=9.0
print("f1:", f1, type(f1))
print("f2:", f2, type(f2))
print("f3:", f3, type(f3))
print("f4:", f4, type(f4))
print("f5:", f5, type(f5))
print("f6:", f6, type(f6))

## Complex Number Data Type ##
"""
var1=X+Yj
X= Real Value
Y= Imaginary Value

"""
var2=10+20j
print(var2, type(var2))
print("Real value:", var2.real)
print("Imaginary Value", var2.imag)

var3=0+50j
var4=40+0j
var5=50j+70
var6="40+60j"
print(var3, type(var3))
print(var4, type(var4))
print(var5, type(var5))
print(var6, type(var6))

## String Data Type ##

s1 = 'Hi'
s2 = "Hello"
s3 = "Hello Sweetie, we are playing. Wanna join with us"
s4 = """"
1. I am Rameez
2. I am a Software Test Engineer
3. Now, learning Python Automation Testing
"""
s5 = '''
Impossible is just an opinion

'''

s6= "1. Be stronger than your excuses. — Unknown\n\t2. Be so good they can’t ignore you. — Steve Martin\n\t3.Lead from the heart, not the head. — Princess Diana\n\t4. Let the beauty of what you love be what you do. — Rumi\n\t5. Be yourself; everyone else is already taken. — Oscar Wilde"
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))
print(s6, type(s6))

str_a="python"
print("The 4th character of python word is", str_a[3])
print("The 5th character of python word is", str_a[-2])


## List Data Type ##

List1=[2,3.5,"Hello",[4,6,7],(3,7,9),{'a':123},{5,7},True,(40+50j),None]
print(List1, type(List1))
print(List1[3])
print(List1[3][2])
print(List1[-4])

List2=[5,7,8]
List2.append(100)
print(List2)

## Tuple Date Type ##
tuple1=(1,3.4,"Hello",[4,5,6],(3,6),{"a":123},{4,6,8},True)
print(tuple1, type(tuple1))

# Dictionary Data Type ##
dict2={"a":123, "b":456}
print(dict2)
dict2["c"]=500
print(dict2)

dict3={"a":123, "b":456, "c":600, "e":456}
print(dict3)

"""
dict4= {
    34:4.5,
    55.6:"Hello",
    "Name": "Rameez",
    ("a","b"):[4,6,7,8],
    True:{"p":345,"q":789, "R":3456},
    [1,2,3]:{4,6,8,1}
}
print(dict4)
"""
dict4= {
    34:4.5,
    55.6:"Hello",
    "Name": "Rameez",
    ("a","b"):[4,6,7,8],
    True:{"p":345,"q":789, "R":3456},
    (1,2,3):{4,6,8,1} # Changed the list to a tuple
}
print(dict4)
result=dict4.popitem()
print(result)
print(dict4)

# Set Data type#
set1={3,"c",7,"a","b",8,2,7,"a",9,3}
print(set1)

set2={3,5,7,"a","b",3}
print(set2, type(set2))
set2.add(100)
print(set2)

set3={3,5,7,"a","b",3,(3,5,7)}
print(set3)