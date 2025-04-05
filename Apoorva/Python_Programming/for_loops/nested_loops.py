# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):  # i=1, 2, 3, 4
    for j in range(1, i + 1):  # (1,5)
        print("*", end=" ")

    print()

print("-"*50 )

# HW: write a pattern with nested loop

"""
* * * * *
* * * *
* * *
* *
*
"""
print("class home work")
for i in range(1,6):
    for j in range(5-i,-1,-1):
        print("*",end=" ")
    print()

