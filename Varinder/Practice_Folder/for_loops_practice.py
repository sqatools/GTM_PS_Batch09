
# for i in range(1, 10):
#     if i <= 10:
#         i=i, i +1
#         print("print all values:-", i)

#
# # for i in range(1, 6):
# #     for j in range(1, i+1):
# #         print("*", end= " ")
# #
# #     print()
# ######################################
# for i in range(1, 6):
#     for j in range(1,i+1):
#         print(i,end= " ")
#     print()
#
# for i in range(6, 1, -1):
#     for j in range(i-1):
#         print("*", end= " ")
#     print()

##########################################
# Home work
"""
    *
  * * *
* * * * *   
  * * *
    *  
"""
for i in range(1, 6):
    for j in range(1,6):
        if i <= 1 and i >= 5:
            print()
        print("*", end= " ")
    print()
