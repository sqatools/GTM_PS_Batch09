#print the below programe
"""
   *
 * * *
* * * * *
  * * *
    *
"""
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5:
            if j in [1,2,4,5]:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i==2 or i==4:
            if j==1 or j==5:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        elif i==3:
            print("*", end=" ")
    print()


#print "o"
"""
 * * *
*      *
*      *
*      *
*      *
 * * * 
"""
for i in range(1,7):
    for j in range(1,7):
        if i==1 or i==6:
            if j==1 or j==6:
                print (" ",end="")
            else:
                print("*",end="")
        if i in [2,3,4,5]:
            if j==1 or j==6:
                print("*",end="")
            else:
                print(" ",end="")
    print()

#print "A"
"""
  * * *    
*       *  
*       * 
* * * * *  
*       *   
*       *  
"""

for i in range(1,7):
    for j in range(1,5):
        if i==1:
            for j==1 or j==5:
                print("",end="")
            else:
                print("*",end="")
        if i in[2,3,5,6]:
            if j==1 or j==5:
                print("*",end="")
            else:
                print("",end="")
            