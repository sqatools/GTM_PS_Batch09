# write a pattern for nested loop

for i in range(6,1,-1):
    for j in range(1,i):
       print("*",end=" ")
    print()
print("_"*40)
############################
# Python to print letter A with * pattern

for i in range(1,7):
    for j in range(1,6):
        if i==1:
            if j==1 or j==5:
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

# write a python program to print O pattern with nested loop

for i in range(1,7):
    for j in range(1,6):
        if i==1 or i==6:
            if j==1 or j==5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i in [2, 3, 4, 5]:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


print("_"*40)


for i in range (1,6):
    for j in range (1,6):

        if j==3:
            print("*",end=" ")
        else:
            print(" ", end= " ")

        print("_" * 40)

    rows = 3

    for i in range(rows):
        print(' ' * (rows - i - 1), end='')
        print('* ' * (2 * i + 1))

            # Bottom half of the pattern
    for i in range(rows - 2, -1, -1):
        print(' ' * (rows - i - 1), end='')
        print('* ' * (2 * i + 1))

print("_"*40)

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5:
            if j==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        elif(i==2 or i==4):




