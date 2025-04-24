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










