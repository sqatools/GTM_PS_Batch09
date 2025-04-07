#range(start, end, step difference)

# for val in range(1, 20, 2):
#     print(val)
#
# ########################################
#
# for i in range(5): # default value would starts from 0
#     print("Number :-",i)

################################################

#print output with negative step value

# for x in range(5, 100, 5):
#     print(x)

###############################################

#write a python program to print the table of given number number

# table = 4
#
# for i in range(1, 11, 1):
#     print(i,"*",table,"=", i*table)
#
#
# table = 12
#
# for t in range(1, 21, 1): #this programe will print 12 table till 20
#     print(t,"*",table,"=", t*table)
#####################################################################
# write a python program to get factorials of any given number
# 5 : 5*4*3*2*1
# n1 = 6
# fact = 1
#
# for i in range(n1, 0, - 1):
#     print(i) # 5, 4, 3, 2, 1
#     fact = fact*i # 5*1 =5, 5*4=20, 20*3 = 60, 60*2=120, 120*1 = 120
#
# print("factorials of :",n1,":", fact)

##################################################################

#write a python program to get sum of all the values from 1 to 10

# num = 0
# for n in range(1, 11):
#     num = num + n
# print(num)


# num1 = 0
#
# for i in range(1, 10):
#     num1 = num1 + i
# print(num1)

# write a python program to get values from list
# vlist = [2, 4, 10, 30, 9, 5, 3, 32]
# for i in vlist:
#     #print(i)
#     if i % 2 == 0 :
#         print(i)


# list1 = [10, 40, 39, "soon", 9.99]
# for l in range(1):
#     #print(l)
#     if "soon" in list1:
#         print("this is correct string",type(list1), list1)
#     else:
#         print("wrong string")
###########################################################################################
# write a python program to get all number which is divisible by 3 and 5 from given tuple

# tup = (10, 19, 30, 5, 4)
# for t in tup:
#     #print(t, type(tup))
#     if t% 3 == 0 and t%5 ==0:
#         print("this is the division number: -",t)
#     else:
#         ("wrong number try again")
#############################################################################
# write a python program to check given number is prime or not
# prime number is nothing but the number can be divide by 1

num = 10
count = 0
for i in range(2, num):
    if num%i == 0:
        count += 1
        print(i)
if count == 0:
    print("print this is the prime number", count)
else:
    print("this is not prime number")

#############################################################
# in below program with nested loop with each value of i entire inner loop will execute with













