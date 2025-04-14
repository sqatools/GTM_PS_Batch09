for i in range(6, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()


print("_"*50)
for i in range(1, 5):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

print("_"*50)
"""
  * * *    # i = 1
*       *  # i = 2
*       *  # i = 3
* * * * *  # i = 4
*       *  # i = 5 
*       *  # i = 6
"""

for i in range(1, 7): # i = 1, 2
    for j in range(1, 6): # j= 1, 2, 3, 4, 5
        if i == 1:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2, 3, 5, 6]:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 4:
            print("*", end=" ")


    print()

print("_"*40)
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
        elif i in [2, 3, 4, 5]:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


# Home work
"""
    *
  * * *
* * * * *   
  * * *
    *  
"""

print("_"*50)

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
        elif i in [2, 3, 4, 5]:
            if j == 1 or j == 5:
                print(i, end=" ")
            else:
                print(" ", end=" ")
    print()