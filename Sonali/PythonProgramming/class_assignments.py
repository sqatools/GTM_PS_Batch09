
str1= "Hello we are learning python program"
#output=[('Hello',5) ('we',2)]

list2=str1.split()
result=[]
for word in list2:
    result.append((word,len(word)))
print(result)


#2nd way(list comprehesion)
r=[(word,len(word)) for word in list2]
print(r)

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
    'Sells' : [],
    'Marketing' : [],
    'Engineering' : []
}

#input = 'IT_02'
#print("IT_0
#


for data in emp_dict:
    for key,val in emp_dict.items():

        if key=={'emp_id'}:
            val='A'['emp_id': 'IT_02']
            print(val)
        else:
            continue

print(emp_dict)







