dict1={'Name':'sonali','CLASS':'PYTHON','Age':12}
print(dict1,type(dict1))

print(dict1['Name'])
print("*"*50)

list1=['A','b','c','d']
list2=[1,2,3,4]
result=dict(zip(list1,list2))
print(result)

print("*"*50)
print("*"* 60)
#Add data to dictionary
dict1['Number']=456
print(dict1)
dict1['python']='python'  #single data
print(dict1)

dict1['a','b','c']=[1,2,3]  #multiple values
print(dict1)
print("_" * 50)
print("*"* 60)
#loop in dictionary
for k1,v1 in dict1.items():
    print(k1,':',v1) # it will print both key and value
print("*"* 60)
#ADDing  1 dictionary data to another using update()

dict_y = {'a': 123, 'b': 456, 'c': 556}
dict_z = {'P': 444, 'Q': 555, 'R': 879}

dict_y.update(dict_z)
print(dict_y)
print("*"* 60)
#setdeafault()

result=dict_z.setdefault('z',900)
print(result) #return the new value
print(dict_z)
r2=dict_y.setdefault('a',88888888888888)
print(r2) #return the existing value
print("*"* 60)
#dict comprehension
#normal square printing
dict_B = {'a': 5, 'b': 6, 'c': 7}
result3={k:v**2 for k,v in dict_B.items() }
print(result3)

print("*"* 60)
#if even then square
dict_c = {'a': 5, 'b': 6, 'c': 7, 'd': 23, 'e': 14, 'f': 8}
result4={k:v**2 for k,v in dict_c.items() if v%2==0}
print(result4)

print("*"* 60)
#if even square else cube
dict_d = {'a': 5, 'b': 6, 'c': 7, 'd': 23, 'e': 14, 'f': 8}
result5=dict([(k,v**2) if v%2==0 else (k,v**3) for k,v in dict_d.items()]) #list converted to dictionary
print(result5)


#1 write a python program to create a dictionary with given string.

str1 = "Hello We Are Learning Python"
#output = {'HO': 'olleH', 'WE': 'eW', 'AE': 'erA', 'LG': 'gninraeL', 'PN': 'nohtyP'}

result={}
word_list=str1.split()
for word in word_list:
    key=f"{word[0]}{word[-1]}"
    val= word[::-1]
    result[key.upper()]=val
print("result:", result)

#calculate total bill and inventory update after sell
fruit_inventory = {'Apple': 500, 'Mango': 200, 'Banana': 300, 'Lichi': 1000}
fruit_price = {'Apple': 50, 'Mango': 30, 'Banana': 20, 'Lichi': 70}
fruit_purchased = {'Apple': 10, 'Mango': 50, 'Banana': 12, 'Lichi': 100}
#total bill will be calculated on the basis of fruit price and fruit purchased
total_bill=0

print("fruit name" ,"|","fruit no","|","fruit price","|","total bill")
for fruit,price in fruit_price.items():
    fruit_name=fruit
    fruit_price=price
    fruit_no=fruit_purchased[fruit]
    fruit_bill=fruit_no*fruit_price
    print(fruit_name, "\t\t", fruit_price, "\t\t", fruit_no, "\t\t", fruit_bill)
    total_bill+=fruit_bill
print("Total bill:",total_bill)
for fruit in fruit_purchased:
    fruit_name = fruit
    fruit_no = fruit_purchased[fruit]
    fruit_quantity=fruit_inventory[fruit]
    fruit_remaining =fruit_quantity-fruit_no
    print("fruit_name","\t","fruit_no","\t","fruit_quantity","\t","fruit_remaining")
    print(fruit_name, "\t\t", fruit_no, "\t\t", fruit_quantity,"\t\t\t\t",fruit_remaining)

# write a python program to provide salary hike to employee on the basis there exp.
# - if exp is greater 5 and less than equal to 10 :  7%
# - if exp is greater 10 and less than equal to 15 :  10%
# - if exp is less than equal to 5, then 20% increment.

employee_list = [
    {'Name': 'john', 'exp': 5, 'age': 30, 'salary': 300000},
    {'Name': 'Jenny', 'exp': 10, 'age': 45, 'salary': 1000000},
    {'Name': 'rahul', 'exp': 15, 'age': 30, 'salary': 500000}
]

print("*"*60)
#increment=0
for data in employee_list:

    if 5 <data['exp']<= 10:
        cur_salary = data['salary']
        update_salary = cur_salary * (7 / 100) + cur_salary
        print(update_salary)
        data['salary'] = update_salary

    elif 10 < data['exp'] <= 15:
        cur_salary = data['salary']
        update_salary = cur_salary * (10 / 100) + cur_salary
        print(update_salary)
        data['salary'] = update_salary
    elif data['exp'] <= 5:
        cur_salary = data['salary']
        update_salary = cur_salary*(20/100) + cur_salary
        print(update_salary)
        data['salary'] = update_salary

    else:
        print("NO hike")
print(employee_list)
print("*"*60)

# write a python program to show employee details from given dictionary
emp_dict = {
    'IT': [
        {'emp_id': 'IT_01', 'name': 'john', 'surname': 'doe', 'mobile': 5434545, 'email': 'john@gmail.com'},
        {'emp_id': 'IT_02', 'name': 'Rahul', 'surname': 'gupta', 'mobile': 542432423, 'email': 'rahul@gmail.com'}
    ],
    'ADMIN' : [
        {'emp_id': 'ADMIN_01', 'name': 'mohan', 'surname': 'doe', 'mobile': 5434545, 'email': 'mohan@gmail.com'},
        {'emp_id': 'ADMIN_02', 'name': 'shyam', 'surname': 'gupta', 'mobile': 542432423, 'email': 'shyam@gmail.com'}

    ],
    'Sells' : [
        {'emp_id': 'Sells_01', 'name': 'mohan1', 'surname': 'doe', 'mobile': 5434545, 'email': 'mohan@gmail.com'},
        {'emp_id': 'Sells_02', 'name': 'shyam1', 'surname': 'gupta', 'mobile': 542432423, 'email': 'shyam@gmail.com'}
    ],
}

#method-1----------------single line printing
print(emp_dict['IT'][1]['emp_id'])
'''
Explanation:
emp_dict=dict[list{dict}]
it is in this format
emp_dict['IT']----------IT WILL print the full dictionary
then inside it list is there. so print the list by its indexing so [0]
then again inside list again dictionary is there
then we will get the value by keys

'''
print("*"*60)
#method-2-----------use the loop
emp_id='IT_02'
for k1,v1 in emp_dict.items():    # here key and value in dictionary
    for data in v1:               #here it is list means data which is dictionary in v1 which is list
        for k2,v2 in data.items(): # here key and value in data which is dictionary
            if emp_id==v2:      #if emp_id is defined value then print
                print(data)




print("*"*60)
#python programm to add data to dictionary
dict1={}
dict1["name"]="ramesh"
dict1["age"]=98
print(dict1)
print("*"*60)
#Python Dictionary program to print the square of all values in a dictionary.
dict2 = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
for k in dict2:
    print(k, ":", dict2[k] ** 2)

print("*"*60)
#move value of 1 dictionary to another dictionary
dict77 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict70 = {}
dict70=dict77.copy()
print(dict70)
print("*"*60)
#update value
dict11 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict22 = {'Age':25,'salary': '$25k'}
dict22.update(dict11)
print(dict22)

print("*"*60)
# Python Dictionary program to get a list of odd and even keys from the dictionary.
dict67 ={1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
list1=[]
list2=[]
for k in dict67:
    if k%2==0:
        list1=[k, dict67[k]]
        print("even is:",list1)

    elif k%2!=0:
        list2=[k,dict67[k]]
        print("odd is:", list2)


#above need to chk as it is not printing in single line

'''
Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
'''
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
dict999={}
dict999=dict(zip(list1,list2))
print(dict999)

#Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}
for i in list1:
    if i%2==0:
        dict1[i]=i**2
    elif i%2!=0:
        dict1[i]=i**3
print(dict1)



#Python Dictionary program to create a dictionary from the string.
input1 = 'SQATools'
#Output = {'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 1}
dict45={}
for char in input1:
    dict45[char]= input1.count(char) #count is used to count the number of char
print(dict45)















