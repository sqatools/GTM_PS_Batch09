################################################
# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")

    print()
print()

print("_" * 50)
for i in range(1, 6):
    for j in range(5 - i, -1, -1):
        print("*", end=" ")
    print()

print("_" * 50)
#####################################
# write a python program to print A letter with * pattern.

"""
here i is number of lines = 6, j is number of characters(*, including spaces) = 5
  * * *    # i = 1
*       *  # i = 2
*       *  # i = 3
* * * * *  # i = 4
*       *  # i = 5 
*       *  # i = 6
"""
for i in range(1, 7, 1):
    for j in range(1, 6, 1):
        if i == 1:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i == 2 or i == 3 or i == 5 or i == 6:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
print()
print("_" * 50)
########################################
# write a python program to print O pattern with nested loop

"""
  * * *    # i = 1
*       *  # i = 2
*       *  # i = 3
*       *  # i = 4
*       *  # i = 5
  * * *    # i = 6
"""

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i == 2 or i == 3 or i == 4 or i == 5:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

print("_" * 50)
# Home work
"""
    *      i=1, j=3
  * * *    i=2, j=2,3,4
* * * * *  i=3, j=1,2,3,4,5
  * * *    i=4, j=2,3,4
    *      i=5, j=3
"""
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5:
            if j == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 2 or i == 4:
            if j == 2 or j == 3 or j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

print("_" * 50)

"""
  1 1 1    # i = 1
2       2  # i = 2
3       3  # i = 3
4       4  # i = 4
5       5  # i = 5
  6 6 6    # i = 6
"""

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 or i == 6:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print(i, end=" ")
        elif i == 2 or i == 3 or i == 4 or i == 5:
            if j == 1 or j == 5:
                print(i, end=" ")
            else:
                print(" ", end=" ")

    print()
