for i in range(5,0,-1): # i=5 ,4,3,2,1
    for j in range(1, i+1): # (1,6)
        print("*", end=" ")

    print()

'''
* * * * * 
* * * * 
* * * 
* * 
*
'''
print("_"*50)

# Take input through the user
num =  int(input("Enter a number: "))
# Create count variable
count = 0
# Iterate over numbers
for i in range(2,num):
# Check for division
    if num%i == 0:
    # Add 1 to the count variable
        count += 1
# Check for prime number
if count > 0:
# Print output
    print("It is not a prime number")
else:
#Print output
    print("It is a prime number")
