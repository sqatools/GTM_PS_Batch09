#1 write a python program to create a dictionary with given string.

str1 = "Hello We Are Learning Python"
#output = {'HO': 'olleH', 'WE': 'eW', 'AE': 'erA', 'LG': 'gninraeL', 'PN': 'nohtyP'}

result = {}
word_list = str1.split()
for word in word_list:
    key = f"{word[0]}{word[-1]}"
    val = word[::-1]
    result[key.upper()] = val

print("output :", result)
# {'HO': 'olleH', 'WE': 'eW', 'AE': 'erA', 'LG': 'gninraeL', 'PN': 'nohtyP'}


print("_"*50)
##############################
# 2 : write a python program to calculate total bill as per purchase items.
# part1 :  calculate bill
# part2 :  update inventory

fruit_inventory = {'Apple': 500, 'Mango': 200, 'Banana': 300, 'Lichi': 1000}
fruit_price = {'Apple': 50, 'Mango': 30, 'Banana': 20, 'Lichi': 70}
fruit_purchased = {'Apple': 10, 'Mango': 50, 'Banana': 12, 'Lichi': 100}

total_bill = 0

print("Fruit Name|Fruit Price|Fruit No|Fruit Bill")
for fruit, price in fruit_price.items():
    fruit_name = fruit
    fruit_price = price
    fruit_no = fruit_purchased[fruit]
    fruit_bill = fruit_price*fruit_no
    print(fruit_name, "\t\t", fruit_price, "\t\t", fruit_no, "\t\t", fruit_bill)
    total_bill = total_bill + fruit_bill


print("_"*40)
print("Total bill :", total_bill)


# Home work:
# write a python program to provide salary hike to employee on the basis there exp.
# - if exp is greater 5 and less than equal to 10 :  7%
# - if exp is greater 10 and less than equal to 15 :  10%
# - if exp is less than equal to 5, then 20% increment.

employee_list = [
    {'Name': 'john', 'exp': 5, 'age': 30, 'salary': 300000},
    {'Name': 'Jenny', 'exp': 10, 'age': 45, 'salary': 1000000},
    {'Name': 'rahul', 'exp': 15, 'age': 30, 'salary': 500000}
]


for data in employee_list:
    print(data)
    user_experience = data['exp']
    if user_experience <= 5:
        cur_salary = data['salary']
        update_salary = cur_salary*(20/100) + cur_salary
        print(update_salary)
        data['salary'] = int(update_salary)

    elif user_experience >5 and user_experience <= 10:
        cur_salary = data['salary']
        update_salary = cur_salary*(7/100) + cur_salary
        print(update_salary)
        data['salary'] = int(update_salary)

    elif user_experience >= 10 and user_experience <= 15:
        cur_salary = data['salary']
        update_salary = cur_salary*(10/100) + cur_salary
        print(update_salary)
        data['salary'] = int(update_salary)

    else:
        continue

    print("Updated data :", data)


print(employee_list)


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

input = 'IT_02'
print("IT_02")
