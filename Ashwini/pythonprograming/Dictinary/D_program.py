# 1 Python Dictionary program to concatenate two dictionaries.

dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}
#Output :dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
dict1.update(dict2)
print(dict1)

# 2 Python Dictionary program to get a list of odd and even keys from the dictionary.
#output:Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
#       Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
dict3={1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
list1=[[v,dict3[v]] for v in dict3 if v%2==0]
list2=[[v,dict3[v]] for v in dict3 if v%2!=0]
print("Even key:",list1)
print("Odd Key:",list2)
print("-"*60)
# 3 Python Dictionary Program to create a dictionary from two lists.
#output={‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15,16]
result = dict(zip(list1, list2))
print("result:", result)

print("-"*50)
# 4 Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
#output={4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
list4=[4, 5, 6, 2, 1, 7, 11]
dict_1={}
for val in list4:
    if val%2==0:
        dict_1[val]=val**2
    else:
        dict_1[val]=val**3
print(dict_1)
print("-"*50)
# 5 Python Dictionary program to remove duplicate values from Dictionary.
dict4={'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
d={}
for key,val in dict4.items():
    if val not in d.values():
          d[key]=val
print(d)

print("-"*50)
# 6 Python Dictionary program to create a dictionary from the string.
#Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
str="SQATools"
d1={}
for char in str:
    d1[char]=str.count(char)
print(d1)

# 7 Python Dictionary program to sort a dictionary using keys.
#Output =(‘a’, 13)(‘b’, 53)(‘c’, 41)(‘d’, 21)
dict5 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
for key in sorted(dict5):
      print((key,dict5[key]),end="")
print("-"*50)
# 8 Python Dictionary program to sort a dictionary in python using values.
dict6 = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }




# 9 Python Dictionary program to find the sum of all items in the dictionary.
dict7= { 'a' : 2, 'b' : 4, 'c' : 5}

total=0
for val in dict7.values():
        total +=val

print(total)
print("-"*50)
#10 Python Dictionary program to find the product of all items in the dictionary.
dict8={'x':4,'y':6,'z':2}
total=1
for val in dict8.values():
    total *= val
print(total)

print("-"*50)
# 11 Python Dictionary program to group the same items into a dictionary value

list = [1,3,4,4,2,5,3,1,5,5,2,]
#  12 write a python program to calculate total bill as per purchase items.
# part1 :  calculate bill
# part2 :  update inventory

fruit_inventory = {'Apple': 500, 'Mango': 200, 'Banana': 300, 'Lichi': 1000}
fruit_price = {'Apple': 50, 'Mango': 30, 'Banana': 20, 'Lichi': 70}
fruit_purchased = {'Apple': 10, 'Mango': 50, 'Banana': 12, 'Lichi': 100}

total_bill = 0

print("Fruit Name|fruit total|Fruit Price|Fruit No|Fruit Bill|update inventry")
for fruit,total_f in fruit_inventory.items():
    fruit_name = fruit
    fruit_total = total_f
    fruit_no = fruit_purchased[fruit]
    t_price=fruit_price[fruit]
    fruit_bill =t_price*fruit_no
    update_fruit=total_f-fruit_no
    print(fruit_name, "\t\t",fruit_total,"\t\t", t_price, "\t\t", fruit_no, "\t\t", fruit_bill,"\t\t",update_fruit)
    total_bill = total_bill + fruit_bill


print("_"*40)
print("Total bill :", total_bill)

# 13 Python Dictionary program to remove duplicate values from dictionary values.
#Output= { ‘marks1’ : [28, 69], ‘marks2’ : [14,19] }
Dict1 = { 'marks1' : [23,28,23,69], 'marks2' : [ 25, 14,25] }

for key,val in Dict1.items():
    for ele in val:
        if ele in val:
            val.remove(ele)


print(Dict1)
print("-"*50)
# 14 Python Dictionary program to remove a word from the string if it is a key in a dictionary.
String = 'sqatools is best for learning python'
Dict = { 'best' : 2, 'learning' : 6}
#Output = “sqatools is for python”
str=" "
for word in String.split():
    if word not in Dict:
        str+=word+" "
print(str)

print("-"*50)
# 15 Python Dictionary program to replace words in a string using a dictionary.
#Output = ‘learning python is fun’
String1 = "learning python at sqa-tools"
Dict = { 'at' : 'is', 'sqa-tools' : 'fun'}
#result=String1.replace("at","is").replace("sqa-tools","fun")
#print(result)
for key,val in Dict.items():
    String1=String1.replace(key,val)
print(String1)
print("-"*50)
# 16 Python Dictionary program to map two lists into a dictionary.
l_a = [ 'name', 'sport', 'rank', 'age']
l_b = ['Virat', 'cricket', 1,  32]
new_d=dict(zip(l_a,l_b))
print(new_d)
print("-"*50)
# 17 Python program to iterate over a dictionary.
#Output :food : burger type : fast food
dict1 ={'food':'burger', 'type':'fast food'}
for val in dict1:
    print(val,dict1[val])

print("-"*50)
# 18 Python program to print a dictionary line by line.
#Output=ViratSport : cricket Team : india Messi Sport : football Team : argentina
D= {'virat': {'sport':'cricket', 'team':'india'}, 'messi': {'sport':'football', 'team':'argentina'}}
for key,val in D.items():
    print(key)
    for k,v in val.items():
        print(k,"",v)

# Home work:
# 19 write a python program to provide salary hike to employee on the basis there exp.
# - if exp is greater 5 and less than equal to 10 :  7%
# - if exp is greater 10 and less than equal to 15 :  10%
# - if exp is less than equal to 5, then 20% increment.

employee_list = [
    {'Name': 'john', 'exp': 5, 'age': 30, 'salary': 300000},
    {'Name': 'Jenny', 'exp': 10, 'age': 45, 'salary': 1000000},
    {'Name': 'rahul', 'exp': 15, 'age': 30, 'salary': 500000}
]
for data in employee_list:
    if data['exp'] <= 5:
        cur_salary = data['salary']
        update_salary = cur_salary*(20/100) + cur_salary
        print(update_salary)
        data['salary'] = update_salary

    elif data['exp'] >=5 and data['exp'] <=10:
        cur_salary=data['salary']
        update_salary1=cur_salary*(7/100)+cur_salary
        print(update_salary1)
        data['salary']=update_salary1
    elif data['exp'] >=10 and data['exp']<=15:
        cur_salary=data['salary']
        update_salary2=cur_salary*(10/100)+cur_salary
        print(update_salary2)
        data['salary']=update_salary2
    else:
        continue

print(employee_list)

print("-"*50)
# 20 write a python program to show employee details from given dictionary
emp_dict = {
    'IT': [
        {'emp_id': 'IT_01', 'name': 'john', 'surname': 'doe', 'mobile': 5434545, 'email': 'john@gmail.com'},
        {'emp_id': 'IT_02', 'name': 'Rahul', 'surname': 'gupta', 'mobile': 542432423, 'email': 'rahul@gmail.com'}
    ],
    'ADMIN' : [
        {'emp_id': 'ADMIN_01', 'name': 'mohan', 'surname': 'doe', 'mobile': 5434545, 'email': 'mohan@gmail.com'},
        {'emp_id': 'ADMIN_02', 'name': 'shyam', 'surname': 'gupta', 'mobile': 542432423, 'email': 'shyam@gmail.com'}

    ],
    'Sells' : [],
    'Marketing' : [],
    'Engineering' : []
}

#input = 'IT_02'
#print("IT_02")
emp_id="ADMIN_01"
for k1, v1 in emp_dict.items():
    #print(k1,"|||",v1)
    for data in v1:
        #print(data)
        for k2,v2 in data.items():
            if emp_id==v2:
                print(data)

