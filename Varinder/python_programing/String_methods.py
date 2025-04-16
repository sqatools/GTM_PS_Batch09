# print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
#  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
#  'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

# str() # class
# str.upper() # method
# for :  keyword
# dir() : function

# name1 = "varinder batth"
# name2 = "YADLEEN KAUR"
#
# print(name1.upper())
# print(name2.lower())
#
# # isupper() and islower() method:
# # isupper() :  This method check given string is in upper case or not.
# # islower() :  This method check given string is in lower case or not.
# print(name1.upper().isupper())
# print(name2.lower().islower())
#
# #swapcase() method :  This method convert string characters upper to lower and lower to upper.
#
# city = "AmriTsaR"
# print(city.swapcase())
#
# # capatilize() method : This method change the first character of entire sentence into capital case
# name3 = "varinder"
# print(name3.capitalize())
#
# # title() method :  This method convert first letter of each word into capital case.
#
# name4 = "varinder batth"
# print(name4.title())
#
# # istitle() method:  This method check given string in following the rules of title or not.
# print(name4.istitle())
# print(name4.title().istitle())
#
# # count() method : This method count the occurrences of any particular character/substring
#
# fruits = "apple orange grapes mango"
# print(len(fruits)) # this will count the length of the string
#
# print(fruits.count("g")) # this will print the specific character (g 3 times)


# split() method : This method break the string in list words with specifies delimeters.

# word = "this is the python programing class"
# print(word.split(" "))

# use same method multiple times
string1 = "today_is_good_day to_learn_python"
print(string1.split(" "))
print(string1.split(" ")[0].split("_"))
print(string1.split(" ")[0].split("_")[1].upper())

# replace() method : This method replace any word with target value.
# replace method accept three param
# replace(old, new, count)
# count is optional parameter, that replace number of occurrences

house = "living and bathroom"
print(len(house))
print(house.replace("living", "Family room"),len(house))
