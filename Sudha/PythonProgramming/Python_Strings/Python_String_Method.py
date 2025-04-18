print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

# str() # class
# str.upper() # method
# for :  keyword
# dir() : function
"""
########
# upper() and lower() methods
# upper() method convert string into upper case.
# lower() method convert string into lower case.

str1 = "Hello Good Morning"
print("Upper result = ", str1.upper())
print("Lower result = ", str1.lower())

##############################################
# isupper() and islower() method:
# isupper() :  This method check given string is in upper case or not.
# islower() :  This method check given string is in lower case or not.

str2 = "Python Programming"
str3 = "GOOD MORNING"
str4 = "learning python"

print(str2.isupper())  # False
print(str2.islower())  # False
print(str3.isupper())  # True
print(str4.islower())  # True

print("_" * 50)
#########################################
# swapcase() method :  This method convert string characters upper to lower and lower to upper.

str5 = "Hello GoOd MoRnIng"
print(str5.swapcase())  # hELLO gOoD mOrNiNG

print("_" * 50)
#########################################
# capatilize() method : This method change the first character of entire sentence into capital case

str6 = "we are learning python"
print(str6.capitalize())  # We are learning python

print("_" * 50)
#########################################
# title() method :  This method convert first letter of each word into capital case.

str7 = "india is besT cricket tEam"
print(str7.title())  # India Is Best Cricket Team

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
print("Count of w : ", str10.count('w'))  # Count of w :  3

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
print(word_list)
# ['India', 'will', 'win', 'world', 'cup', 'Wi', 'India']
print("Count of words = ", len(word_list))  # Count of words =  7

word_list2 = str12.split("_")
print(word_list2)  # ['We', 'Are', 'Learning', 'Python', 'Programming']

word_list3 = str12.split("P")
print("word_list3:", word_list3)  # ['We_Are_Learning_', 'ython_', 'rogramming']

# use same method multiple times
str13 = "Very_good_morning Python_Programming"

print(str13.split(" "))
# ['Very_good_morning', 'Python_Programming']
print(str13.split(" ")[0].split("_"))
# ['Very', 'good', 'morning']
print(str13.split(" ")[0].split("_")[1].upper())
# GOOD

print("_" * 50)
#########################################
# replace() method : This method replace any word with target value.
# replace method accept three param
# replace(old, new, count)
# count is optional parameter, that replace number of occurrences
str14 = "Very good Python morning Python Programming"

# remove all spaces
result = str14.replace(" ", "")
print("result2 : ", result)
print("char count without space in given string : ", len(result))

# replace word Python with Java
result2 = str14.replace("Python", "Java")
print("Result 2 after replacing : ", result2)
# Result 2 after replacing :  Very good Java morning Java Programming

result3 = str14.replace("Python", "C++", 1).replace("morning", "evening")
print("Result3 : ", result3)
# Result3 :  Very good C++ evening Python Programming,
# only first occurrence of Python was replaced with c++

print("_" * 50)
# #########################################
# index() method:  This method return index position of any character or substring
str_a = "Good MorningM"

# if any character/substring is repeated multiple times, then index method will only
# return the index position first occurrence of character/sub-string
print("Index of M :", str_a.index("M"))

# if given character/substring is not available then it will throw error
# print("Index of P :", str_a.index("P"))
# ValueError: substring not found

print("_" * 50)
# #########################################
# find() method: find method also return the index position of given character/substring in given
# string, but if char/sub-string does not exist in given , then it return

str_b = "We are Learning Python"
print("find are : ", str_b.find("are"))  # find are :  3

# sub-string does not exist
print("find 'pro' in given string :", str_b.find("pro"))
# find 'pro' in given string : -1

print("_" * 50)
# #########################################
# strip() method: This remove trailing spaces from given string, trailing spaces means space
# in prefix and postfix position of the entire string.

str_c = "  Python Programming  "
print(str_c)

result = str_c.strip()
print("--------- result after strip -------")
print(result)

# lstrip():  Remove left side spaces from given string.
print(str_c.lstrip())
# Python Programming


# rstrip() :  This method remove right side spaces from given string.
print(str_c.rstrip())
#   Python Programming

print("_" * 50)
# #########################################
# join() method :  This method connect each character of the string with specific value

str1 = "Learning"

result = "_".join(str1)
print("Result : ", result)
# Result :  L_e_a_r_n_i_n_g

str_d = "Python Programming"
result2 = "123".join(str_d)
print(result2)  # P@y@t@h@o@n@ @P@r@o@g@r@a@m@m@i@n@g

print("@".join(str_d[:4]))  # P@y@t@h

print("_" * 50)
##########################################
# isdigit() method: this method check the given string only contains numbers.

n1 = "2345 678"
print(n1.isdigit())  # False, false because it has space between 5 6

n2 = "54353454"
print(n2.isdigit())  # True

n3 = "Hello123"
print(n3.isdigit())  # False

# get all the numbers from given string
str_q = "We 18 are 23 4 67 b 12 learning Python"
word_list = str_q.split()
print(word_list)
for word in word_list:
    if word.isdigit():
        print(word)
    else:
        continue
"""
18
23
4
67
12
"""

print("_"*50)
##########################################
# isalpha() method:  This method check the given string only cotains alphabates.

str_x = "Hello"
print(str_x.isalpha()) # True
str_y = " Python "

print(str_y.isalpha()) #False

print("_"*50)
##########################################
# isalnum() method:This method check the given string only contains alpha numeric values
str_z = "Python 123"
print("str_z:", str_z.isalnum())  # str_z: True