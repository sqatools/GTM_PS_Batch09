""" slicing Home work
 str1 = "Hello good Morning"

 output1 = "HHello good Morningg"

 output2 = "HHelloo ggoodd MMorningg"

 output3 = "olleH doog gninroM"
 """
str1 = "Hello good Morning"
# output1
print(f"{str1[0]}{str1}{str1[-1]}")
# output2
word1 = str1[:5]
word2 = str1[6:10]
word3 = str1[11:]
print(f"{word1[0]}{word1}{word1[-1]} {word2[0]}{word2}{word2[-1]} {word3[0]}{word3}{word3[-1]}")
# output3
print(f"{word1[::-1]} {word2[::-1]} {word3[::-1]}")
print("-" * 60)
str1 = "Hello good Morning"
print(str1[:2], str1[-3])
print("-" * 60)
for i in str1:
    print(i)

print("-" * 50)
str_len = len(str1)
print("length of the string is:", str_len)
for i in range(str_len):
    print(i, str1[i])

print("-" * 60)
print(str1[3:8])  # lo go
# default start index is 0
print(str1[:6])  # Hello
# default end index will end of string.
print(str1[7:])  # ood Morning

# start : +ve and end : -ve
print(str1[7:-5])  # ood Mo

print("-" * 50)
# get left to right output
print(str1[4:8:1])  # o go
print(str1[1:10:2])  # el od
print(str1[1:12:])  # ello good M
print("-" * 60)
# get right to left output
print(str1[-5:-16:-1])  # roM doog ol
print(str1[-7:-18:-2])  # mdo le
print("-" * 60)
# default end index will be start of string when step value is -ve e.g. [start index:: -ve step value]
str_d = "Python Programming"
print(str_d[-3::-1])  # immargorP nohtyP
print(str_d[-1::-2])  # gimroPnhy
print("-" * 50)
# default end index will be end of string when step value is +ve e.g. [start index::+ve step value]
print(str_d[::])  # Python Programming
print(str_d[1::1])  # Python Programming
print("-" * 50)
# default start index will be -1, when step value is -ve. e.g str[: end index: -ve step value]
print(str_d[:5:-1])  # gnimmargorP
print("-" * 60)
# reverse of the string
print(str_d[::-1])  # gnimmargorP nohtyP
print("-" * 60)

############################# STRING METHOD ########################################
# upper() and lower() methods
# upper() method convert string into upper case.
# lower() method convert string into lower case.

str2 = "Hello World"
str3 = "GOOD MORNING"
str4 = "hello"
print(f"{str2} is:", str2.upper())
print(f"{str2} is:", str2.lower())

##############################################
# isupper() and islower() method:
# isupper() :  This method check given string is in upper case or not.
# islower() :  This method check given string is in lower case or not.

print(f"{str3}:", str3.isupper())
print(f"{str2} is:", str2.islower())
print(f"{str4} is:", str4.islower())

print("-" * 60)
################ replace method #################
my_string = "Python is fun. Python is awesome."
new_string = my_string.replace("   Python", "Java")

print("Original string:", my_string)
print("New string:", new_string)
print("-" * 50)

######### title method #######
str5 = "i have good in python Programming"
print(f"{str5} is :", str5.title())
# I Have Good In Python Programming
# title() method :  This method convert first letter of each word into capital case.

str7 = "india is besT cricket tEam"
print(str7.title())
# India Is Best Cricket Team

print("_" * 50)
#########################################
# swapcase() method :  This method convert string characters upper to lower and lower to upper.

str5 = "Hello GoOd MoRnIng"
print(str5.swapcase())  # hELLO gOoD mOrNiNG

print("_" * 50)
#########################################
# capatilize() method : This method change the first character of entire sentence into capital case

str6 = "we Are Learning Python"
print(str6.capitalize())
# We are learning python


print("_" * 50)
#########################################
# istitle() method:  This method check given string in following the rules of title or not.

str8 = "Virat is best cricketer"
str9 = "Sachin Is God Of Cricket"
print("str8 is title :", str8.istitle())  # False
print("str9 is title :", str9.istitle())  # True

print("_" * 50)
#########################################
# count() method : This method count the occurrences of any particular character/substring

str10 = "India will win world cup Wi India"
print("count of w :", str10.count('w'))
# count of w : 3

print("count of substring wi :", str10.count('wi'))
# count of substring wi : 2

print("count of substring India :", str10.count('India'))
# count of substring India : 2

print("all character count :", len(str10))
# all character count : 33


print("_" * 50)
#########################################
# split() method : This method break the string in list words with specifies delimeters.

str11 = "India will win world cup Wi India"

str12 = "We_Are_Learning_Python Programming"

word_list = str11.split(" ")
print(word_list)  # ['India', 'will', 'win', 'world', 'cup', 'Wi', 'India']
print("count of words :", len(word_list))  # count of words : 7

word_list2 = str12.split("_")
print(word_list2)  # ['We', 'Are', 'Learning', 'Python', 'Programming']

word_list3 = str12.split("p  ")
print("word_list3:", word_list3)  # ['We_Are_Learning_', 'ython_', 'rogramming']

# use same method multiple times
str13 = "Very_good_morning Python_Programming"

print(str13.split(" "))  # ['Very_good_morning', 'Python_Programming']

print(str13.split(" ")[0].split("_"))  # ['Very', 'good', 'morning']

print(str13.split(" ")[0].split("_")[1].upper())  # GOOD

print("_" * 50)
#########################################
str11 = "Hello we are learning python program"
list = str11.split()
result = []
for word in list:
    result.append((word, len(word)))
print(result)