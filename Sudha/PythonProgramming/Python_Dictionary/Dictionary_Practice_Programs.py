#1 write a python program to create a dictionary with given string.

str1 = "Hello We Are Learning Python"
#output = {'HO': 'olleH', 'WE': 'eW', 'AE': 'erA', 'LG': 'gninraeL', 'PN': 'nohtyP'}

result = {}
wordlist = str1.split(" ")
for word in wordlist:
    key = f"{word[0]}{word[-1]}"
    val = word[::-1]
    result[key.upper()] = val

print("Output : ", result)

print("_"*50)
##############################
# 2 : write a python program to calculate total bill as per purchase items.
# part1 :  calculate bill
# part2 :  update inventory

fruit_inventory = {'Apple': 500, 'Mango': 200, 'Banana': 300, 'Lichi': 1000}
fruit_price = {'Apple': 50, 'Mango': 30, 'Banana': 20, 'Lichi': 70}
fruit_purchased = {'Apple': 10, 'Mango': 50, 'Banana': 12, 'Lichi': 100}

totalbill = 0
print("Fruit Name|Fruit Price|Fruit No|Fruit Bill")
for fruit, price in fruit_price.items():
    fruit_name = fruit
    fruit_price = price
    fruit_no = fruit_purchased[fruit]
    result_bill = price*fruit_no
    print(fruit_name, "\t\t", fruit_price, "\t\t", fruit_no, "\t\t", result_bill)
    totalbill = totalbill+result_bill
    fruit_update = fruit_inventory[fruit_name] - fruit_no
    fruit_inventory[fruit_name] = fruit_update

print("_"*50)
print("Total Bill = ",totalbill)
print("Final Inventory : ", fruit_inventory)

"""
output
__________________________________________________
Fruit Name|Fruit Price|Fruit No|Fruit Bill
Apple 		 50 		 10 		 500
Mango 		 30 		 50 		 1500
Banana 		 20 		 12 		 240
Lichi 		 70 		 100 		 7000
__________________________________________________
Total Bill =  9240
Final Inventory :  {'Apple': 490, 'Mango': 150, 'Banana': 288, 'Lichi': 900}
"""



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

for employee in employee_list:
    if employee['exp'] <= 5:
        cur_salary = employee['salary']
        upd_salary = cur_salary*(20/100)+cur_salary
        employee['salary'] = upd_salary
    elif employee['exp'] <= 10:
        cur_salary = employee['salary']
        upd_salary = cur_salary*(10/100)+cur_salary
        employee['salary'] = upd_salary
    elif employee['exp'] <= 15:
        cur_salary = employee['salary']
        upd_salary = cur_salary * (7 / 100) + cur_salary
        employee['salary'] = upd_salary

print("Final Employee List : ",employee_list)
"""
output
Final Employee List :  [{'Name': 'john', 'exp': 5, 'age': 30, 'salary': 360000.0}, {'Name': 'Jenny', 'exp': 10, 'age': 45, 'salary': 1100000.0}, {'Name': 'rahul', 'exp': 15, 'age': 30, 'salary': 535000.0}]
"""







