# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *
"""
"""
for i in range(1, 7):  # i=1, 2, 3, 4
    for j in range(1, i + 1):
        # (1,5)
        print("*", end=" ")

    print()


print("&"* 50)

for i in range(5):   # 0,
    for j in range(i+1):  # 0

        print("*", end=" ")

    print()"""

# HW: write a pattern with nested loop
"""

* * * * * 
* * * *
* * *
* *
*
"""


for i in range(6,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()

print("*"* 50)

for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5:
            if j == 3:
                print("*",end =" ")
            else:
                print(" ", end=" ")
        elif i == 2 or i == 4:
            if j == 2 or j == 4:
                print("*",end =" ")
            else:
                print(" ", end=" ")
        else:
            print("*",end =" ")
    print()



print("*"* 50)

str1 = "Hi hello good morning"

output1 = f"{str1[-1]}{ str1[1:-1]}{ str1[0]}"


print(output1)

for i in str1:
    s = list(i)
    s[0],s[-1]=s[-1],s[0]
print(s)

