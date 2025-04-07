# write a pattern for nested loop

for i in range(6,1,-1):
    for j in range(1,i):
       print("*",end=" ")
    print()

############################
# Python to print letter A with * pattern

for i in range(1,7):
    for j in range(1,6):
        if i==1:
            if j==1 or j==5:
                print(" ", end=" ")
            else:
                print("*", end=" ")


    print()


