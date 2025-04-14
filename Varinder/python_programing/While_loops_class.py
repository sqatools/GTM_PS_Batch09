# print 1 to 10 with while loop
#
# num = 1
# while num <= 10:
#     print(num)
#     num += 1


####### Break and continue statement ######
# continue statement : when ever we met with continue condition, then code will move to next
# without executing the remaining code.

# num1 = 1
# while(num1 <= 15):
#     if num1 <= 3 or num1 == 8:
#         num1 += 1
#         continue
#     else:
#         print(num1)
#         num1 += 1


########And Oprator with countinue statement ########
#
# num2 = 1
# while(num2 <= 15):
#     if num2 <= 5 and num2 == 5:
#         num2 += 1
#         continue
#     else:
#         print(num2)
#         num2 += 1
# Break  statement: whenever the conde met with break condition, then loop will break imidiately
# won't go for next value

# num3 = 1
# while(num3 <= 10):
#     if num3 == 6:
#         num3 += 1
#         break
#     else:
#         print(num3)
#         num3 += 1

##### for loops with continue statement ####

# for i in range(1, 20):
#     if i <= 6:
#         i += 1
#         continue
#     print(i)

# while loop program
# write a program to reverse a integer number.

num1 = 12334
rev_val = 0
count = 0
while num1 > 0:
    temp = num1%10
    rev_val = rev_val*10 + temp
    num1 = num1//10
    count += 1

print("reverse value :", rev_val)
print("total digits :", count)



