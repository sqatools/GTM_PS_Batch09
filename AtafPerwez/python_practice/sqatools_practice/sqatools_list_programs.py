# Python List Programs
# 1). Python program to calculate the square of each number from the given list.
list1 = [2, 4, 5, 98, 34]
for i in list1:
    print(f'Square of {i} is: {i ** 2}')
# 2). Python program to combine two lists.
list2 = [4, 5, 8, 23, 76]
list3 = [2, 5, 7, 45, 65, 2]
print(list2 + list3)

# 3). Python program to calculate the sum of all elements from a list.
sum = 0
for value in list3:
    sum = sum + value
print(f'sum of all value in list3 is: {sum}')

# 4). Python program to find a product of all elements from a given list.
list4 = [1, 5, 43, 98, 2]
product = 1
for value in list4:
    product *= value
print(f'product of all element: {product}')
print(1 * 5 * 43 * 98 * 2)

# 5). Python program to find the minimum and maximum elements from the list.
list5 = list4
print(f'maxumum element is: {max(list5)} and min element is: {min(list5)}')

# 6). Python program to differentiate even and odd elements from the given list.
list6 = [2, 5, 6, 7, 8, 24, 44, 75]
odd = []
even = []
for i in list6:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f'odd is: {odd} \neven is: {even}')

# 7). Python program to remove all duplicate elements from the list.
list7 = [2, 5, 2, 6, 7, 8, 8, 24, 44, 3, 75, 75]
temp = []
for i in list7:
    if i not in temp:
        temp.append(i)
print(f'list without duplicate value: {temp} ')

# 8). Python program to print a combination of 2 elements from the list whose sum is 10.
print('------------8--------------')
list8 = [2, 8, 10, 1, 9, 8, 6, 4, 24, 44, 3, 78]
result = []
len_list8 = len(list8)
for i in range(len_list8):
    for j in range(i + 1, len_list8):
        if list8[i] + list8[j] == 10:
            print([list8[i], list8[j]])

# 9). Python program to print squares of all even numbers in a list.
list9 = [2, 4, 5, 7, 9, 6]
for i in list9:
    if i % 2 == 0:
        print([i ** 2], end=" ")

# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
# Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
# Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
print('------------10-----------')
list10 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even = []
odd = []
for i in list10:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
output = odd + even
print(output)

# 11).  Python program to get common elements from two lists.
# Input =
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# Outputt : [4, 5, 7, 2]
print('----------11-----------')
list11 = [4, 5, 7, 9, 2, 1]
listt = [2, 5, 8, 3, 4, 7]
output = []
for i in list11:
    if i in listt:
        output.append(i)
    else:
        continue
print(output)

# 12). Python program to reverse a list with for loop.
print('---------------------12')
list12 = [1, 3, 5, 4, 6, 9, 7, 8, 4]
for i in range(len(list12) - 1, 1, -1):
    print(list12[i], end=" ")

# 13). Python program to reverse a list with a while loop.
print('\n\n13--------------------')
list12 = [1, 3, 5, 4, 6, 9, 7, 8, 4]
count = len(list12)
print(list12[count:1:-1])

print('\n---------------------')
while count <= 0:
    print(value[count], end=" ")
    count -= 1

# 14). Python program to reverse a list using index slicing.
print('\n=========14=========')
list14 = [1, 3, 5, 4, 6, 9, 7, 8, 4]
print(list14[::-1])

# 15). Python program to reverse a list with reversed and reverse methods.
print('\n=========15=========')

list15 = [1, 3, 5, 7, 6, 9, 17, 28, 19]
list15.reverse()
print(f'Reversed list using reverse method: {list15}')

# 16). Python program to copy or clone one list to another list.
print('\n=========16=========')
list16 = [1, 3, 5, 7, 6, 9, 17, 28, 19]
print(dir(list16))
clone_list = list16.copy()
print(clone_list)

# 17). Python program to return True if two lists have any common member.
print('\n=========17=========')
list17 = [1, 3, 5, 7, 6, 9, 17, 28, 19]
list_17 = [21, 33, 35, 7, 6, 9, 17, 328, 219]
for i in list_17:
    if i in list17:
        print(i, ":", True)
    else:
        print(i, ":", False)

# 18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
print('\n ==========18==========')
list19 = [1, 3, 5, 6, 8, 9, 0, 1, 2, 21, 54, 76, 89]
del list19[0]
del list19[4]
del list19[6]

print(list19)

# 19). Python program to remove negative values from the list.
list20 = [1, 3, 5, 6, 8, 9, -3, -5, -1]
for num in list20:
    if num >= 0:
        print(num, end=", ")
    else:
        continue

# 20). Python program to get a list of all elements which are divided by 3 and 7.
print('\n ==============20==============')
list20 = [1, 3, 5, 21, 6, 8, 14, 9, 42, -3, -5, -1, 12, 28]
output = []
for num in list20:
    if num % 3 == 0 and num % 7 == 0:
        output.append(num)
    else:
        continue
print(output)

# 21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
#
# Solution
# 22). Python Program to get a list of words which has vowels in the given string.
# Input: “www Student ppp are qqqq learning Python vvv”
# Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
# Solution
# 23). Python program to add 2 lists with extend method.
#
# Solution
# 24). Python program to sort list data, with the sort and sorted method.
#
# Solution
# 25). Python program to remove data from the list from a specific index using the pop method.
#


#
# str1 = " hello we are learning python program"
#
# words = str1.split()
#
#
# result = [(word, len(word)) for word in words]
# print(result)
#
# #############
#
# str1 = " hello we are learning python program"
# words = str1.split()
# result = []
# for word in words:
#     pair = (word, len(word))
#     result.append(pair)
#
# print(result)
