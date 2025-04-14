# ord :  ord in this function that return the ASCII value with the help of  character
# chr : chr function returns the letter name with the help of ASCII value.

# print(ord("A"))
# print(chr(65))
#
# for i in range(65, 91):
#     print(chr(i), end= "")
#
# for i in range(97, 123):
#     print(chr(i), end= "")

letter = 65
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(letter), end= "")
        letter +=1
    else:
        print(" ", end= " ")
    print()





