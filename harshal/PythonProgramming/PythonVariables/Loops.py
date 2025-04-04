for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

print("_"*50)

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(" *",end="")
    print()

print("_"*50)
"""
*****   i1
  *     i2
  *     i3
***     i4

"""


for i in range(1,5,1):
    for j in range(1,6,1):
        print("*", end="")
        if i==2:
            if j==1:
                print(" ", end="")
            else:
                print("*", end="*")
    print()
