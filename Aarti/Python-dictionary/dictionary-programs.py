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
# Calculate Bill
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

#update inventory
print("Fruit Inventory : ", fruit_inventory)
print("Fruit Name|Fruit Purchased|Fruit Inventory")

for fruit, quantity in fruit_purchased.items():
    fruit_name = fruit
    fruit_inventory[fruit] = fruit_inventory[fruit] - quantity
    print(fruit, "\t\t\t", quantity, "\t\t\t", fruit_inventory[fruit])

print("Updated Inventory ", fruit_inventory)
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
print("Name |\t Exp |\t Age |\t Salary")
for listitem in employee_list:
    name = listitem['Name']
    exp = listitem['exp']
    age = listitem['age']
    salary = listitem['salary']
    increment = 0
    if(exp > 5 and exp <= 10):
         increment = (salary * 7/ 100) + salary
    elif(exp > 10 and exp <= 15):
        increment = (salary * 10/100) + salary
    elif(exp <= 5):
        increment = (salary *20/100) + salary

    print(name, "\t",exp , "\t",age, "\t", salary,"\t", increment)
