print(dir(str))
# String Methods
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
print("Upper result :", str1.upper()) # HELLO GOOD MORNING
print("Lower result :", str1.lower()) # hello good morning


##############################################
# isupper() and islower() method:
# isupper() :  This method check given string is in upper case or not.
# islower() :  This method check given string is in lower case or not.

str2 = "Python Programming"
str3 = "GOOD MORNING"
str4 = "learning python"

print("str2 is upper:", str2.isupper()) # False
print("str2 is lower:", str2.islower()) # False

print("str3 is upper:", str3.isupper()) # True
print("str4 is lower:", str4.islower()) # True

print("_"*50)
#########################################
#swapcase() method :  This method convert string characters upper to lower and lower to upper.

str5 = "Hello GoOd MoRnIng"
print(str5.swapcase())  # hELLO gOoD mOrNiNG


print("_"*50)
#########################################
# capatilize() method : This method change the first character of entire sentence into capital case

str6 = "we Are Learning Python"
print(str6.capitalize())
# We are learning python

print("_"*50)
#########################################
# title() method :  This method convert first letter of each word into capital case.

str7 = "india is besT cricket tEam"
print(str7.title())
# India Is Best Cricket Team

print("_"*50)
#########################################
# istitle() method:  This method check given string in following the rules of title or not.

str8 = "Virat is best cricketer"
str9 = "Sachin Is God Of Cricket"
print("str8 is title :", str8.istitle()) # False
print("str9 is title :", str9.istitle()) # True



print("_"*50)
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


print("_"*50)
#########################################
# split() method : This method break the string in list words with specifies delimeters.

str11 = "India will win world cup Wi India"

str12 = "We_Are_Learning_Python Programming"

word_list = str11.split(" ")
print(word_list) # ['India', 'will', 'win', 'world', 'cup', 'Wi', 'India']
print("count of words :", len(word_list)) # count of words : 7

word_list2 = str12.split("_")
print(word_list2) # ['We', 'Are', 'Learning', 'Python', 'Programming']

word_list3 = str12.split("P")
print("word_list3:", word_list3) # ['We_Are_Learning_', 'ython_', 'rogramming']

# use same method multiple times
str13 = "Very_good_morning Python_Programming"

print(str13.split(" ")) # ['Very_good_morning', 'Python_Programming']

print(str13.split(" ")[0].split("_")) # ['Very', 'good', 'morning']

print(str13.split(" ")[0].split("_")[1].upper()) # GOOD


print("_"*50)
#########################################
# replace() method : This method replace any word with target value.
# replace method accept three param
# replace(old, new, count)
# count is optional parameter, that replace number of occurrences
str14 = "Very good Python morning Python Programming"

# remove all spaces
result = str14.replace(" ", "")
print("result:", result)
print("only char count without space :", len(result)) # 32

# replace word Python with Java
result2 = str14.replace("Python", "Java")
print("result2 :", result2) # Very good morning Java Programming


result3 = str14.replace("Python", "C++", 1).replace("morning", "evening")
print("result3 :", result3)
# result3 : Very good C++ evening Python Programming

#str14.replace()
