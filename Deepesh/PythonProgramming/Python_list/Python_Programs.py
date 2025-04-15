#q1 :  write a Python Program to remove duplicate value from given list

list1 = [5, 7, 9, 3, 5, 8, 2, 7]
# output = [5, 7, 9, 3, 8, 2]

output = []
for val in list1:
    if val not in output:
        output.append(val)
    else:
        continue

print("output :", output)
# [5, 7, 9, 3, 8, 2]


print("_"*50)
#q2 : write a program to find the common values between two lists

list2 = [4, 67, 8, 2, 7, 12]
list3 = [4, 77, 88, 2, 13, 7]

#output = [4, 2, 7]
output = []

for val in list2:
    if val in list3:
        output.append(val)
    else:
        continue

print("output :", output)
# [4, 2, 7]


print("_"*50)
#Q3 :  write python program to find list of word with len is even.

str1 = "Hello we are Learning Python Programming, Its easy to learn"
output = []

word_list = str1.split(" ")
for word in word_list:
    if len(word)%2 == 0:
        output.append(word)
    else:
        continue

# ['we', 'Learning', 'Python', 'Programming,', 'easy', 'to']

print("OUTPUT :", output)

print("_"*50)
#Q4 : write a program to get sublist with 2 values whose sum is 10 from given list
#         i
list_a = [4, 6, 7, 3, 1, 9, 8, 2, 5]
#            j
lista_len = len(list_a)
for i in range(lista_len): # i = 0
    for j in range(i+1, lista_len): # j= 1
        if list_a[i] + list_a[j] == 10:
            print([list_a[i], list_a[j]])
        else:
            continue


"""
[4, 6]
[7, 3]
[1, 9]
[8, 2]


"""

print("_"*50)
# Q5 : write a python to calculate the total bill of fruit purchased.
fruit_list_price = [['Apple', 200], ['Mango', 50], ['Banana', 25], ['Lichi', 40]]
fruit_purchase_list = [['Apple', 5], ['Mango', 2], ['Banana', 2], ['Lichi', 5]]
total_bill = 0

for data in fruit_list_price:
    print(data)
    fruit_name = data[0]
    fruit_price = data[1]
    print(fruit_name, fruit_price)
    for pr_data in fruit_purchase_list:
        pr_fruit_name = pr_data[0]
        pr_fruit_no = pr_data[1]
        if fruit_name == pr_fruit_name:
            fruit_bill = fruit_price*pr_fruit_no
            total_bill = total_bill + fruit_bill

        else:
            continue


print("Total bill amount :", total_bill)
