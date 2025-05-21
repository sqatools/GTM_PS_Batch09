# write a python program to show employee details from given dictionary
emp_dict = {
    'IT': [
        {'emp_id': 'IT_01', 'name': 'john', 'surname': 'doe', 'mobile': 5434545, 'email': 'john@gmail.com'},
        {'emp_id': 'IT_02', 'name': 'Rahul', 'surname': 'gupta', 'mobile': 542432423, 'email': 'rahul@gmail.com'}
    ],
    'ADMIN': [
        {'emp_id': 'ADMIN_01', 'name': 'mohan', 'surname': 'doe', 'mobile': 5434545, 'email': 'mohan@gmail.com'},
        {'emp_id': 'ADMIN_02', 'name': 'shyam', 'surname': 'gupta', 'mobile': 542432423, 'email': 'shyam@gmail.com'}

    ],
    'Sells': [],
    'Marketing': [],
    'Engineering': []
}

input = 'ADMIN_02'
# print("IT_02")
# here we have emp_dict is a dictionary, and key as it, admin,
# and values as list of dictionary


"""dict2 = {'a': [{'Pune': {
    'Fav_Food': 'misal pav', 'historic place': 'shanirwada'
}}, {'Mumbai': {
    'Fav_Food': 'Vada Pav', 'historic place': 'Gateway of India'
}}],
    'b': ['India', 'China', 'USA'],
    'c': {'name': 'john', 'phone': 2342343, 'email': 'john123@gmail.com'}
}

for k1 , v1 in dict2.items():
    key = k1
    value = v1
    for val in v1:
        print(val)
    #print(key)
    #print(value)"""

for k1, v1 in emp_dict.items():#spliting key k1, value v1 from emp_dict
    for v2 in v1:# here v1 is a list of dictionary
        if v2['emp_id'] == input:# calling and checking employee id in each list items
            print(v2['emp_id'], v2['name'], v2['surname'], v2['mobile'], v2['email'])
        else:
            continue
