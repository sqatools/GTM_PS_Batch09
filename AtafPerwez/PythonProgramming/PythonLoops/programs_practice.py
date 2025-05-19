# ord :  ord in this function that return the ASCII value with the help of  character
# chr : chr function returns the letter name with the help of ASCII value.
# ASCII :
# Capital letters :  65-90
# Small letters : 97-122
print(ord("A")) # 65

print(chr(97)) # a


for i in range(65, 91):
    print(chr(i), end=" ")

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
print()

for i in range(97, 123):
    print(chr(i), end=" ")

# a b c d e f g h i j k l m n o p q r s t u v w x y z

print()
for i in range(1, 65):
    print(chr(i), end=" ")

# ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @

print()
print("_"*50)
"""
A
B C
D E F
G H I J
K L M N O  
"""
count = 65
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(count), end=" ")
        count += 1
    else:
        print(" ", end=" ")
    print()
