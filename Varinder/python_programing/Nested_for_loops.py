# in below program with nested loop with each value of i entire inner loop will execute with

# for i in range(1,5):# i is outer loop
#     print("this is I :-", i)
#     #j is the inner loop
#     for j in range(2,7):
#         print("this is whole J statement:- ",j)

## write a python program to get list of all prime number from 1 to 50

# for num in range(2, 50):
#     count = 0
#     for i in range(2, num):
#         if num % i == 0:
#             count += 1
#
#     if count == 0:
#         print(num)
##############################################################
# write a python program to print below pattern

# for i in range(1, 6):
#     for j in range(1, i +1):
#         print("*", end = " ")
#     print()
# print()

# for i in range(6, 1, -1):
#     for j in range(1, i):
#         print("*", end=" ")
#
#
#     print()
# print()
########################################################3
# write a python program to print A letter with * pattern.
for i in range(1, 7):
    for j in range(1, 6):
        if i == 1:
            if j == 1 or j == 5:
                print(" ",end= " ")
            else:
                print("*", end=" ")
    print()




