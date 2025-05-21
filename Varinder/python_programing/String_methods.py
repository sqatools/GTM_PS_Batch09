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
# string1 = "today_is_good_day to_learn_python"
# print(string1.split(" "))
# print(string1.split(" ")[0].split("_"))
# print(string1.split(" ")[0].split("_")[1].upper())
#
# # replace() method : This method replace any word with target value.
# # replace method accept three param
# # replace(old, new, count)
# # count is optional parameter, that replace number of occurrences
#
# house = "living and bathroom"
# print(len(house))
# print(house.replace("living", "Family room"),len(house))

# #########################################
# index() method:  This method return index position of any character or substring
home = "home sweet home"
print(len(home))
print(home.index(home))
print(home.index("h"))

# if any character/substring is repeated multiple times, then index method will only
# return the index position first occurrence of character/sub-string
# if given character/substring is not available then it will throw error
# print("Index of P :", str_a.index("P"))
# ValueError: substring not found

# #########################################
# find() method: find method also return the index position of given character/substring in given
# string, but if char/sub-string does not exist in given , then it return -1

country = "United states of America"
print(country.find("states"))

# #########################################
# strip() method: This remove trailing spaces from given string, trailing spaces means space
# in prefix and postfix position of the entire string.

city = "  Ashburn  "
print(city)
print(city.strip())


# lstrip():  Remove left side spaces from given string.
print(city.lstrip())



# rstrip() :  This method remove right side spaces from given string.
print(city.rstrip())


# join() method :  This method connect each character of the string with specific value

car = "honda"
print("_".join(car))

print(car)

print("**".join(car[:3]))


# isdigit() method: this method check the given string only contains numbers.

house_no  = "21945 ashburn 20146"
print(house_no.isdigit())

# get all the numbers from given string
my_str = "harveer 27 yaad 17 jas 21"
# your_str = my_str.split()
# print(your_str)
# for i in your_str:
#     if i.isdigit():
#         print(i)
#     else:
#         continue

for i in my_str.split():
    if i.isdigit():
        print(i)
    else:
        continue

# isalpha() method:  This method check the given string only cotains alphabates.

country = "America"
print(country.isalpha())

print("_"*50)
##########################################
# isalnum() method:This method check the given string only contains alpha numeric values

user_name = "watch123"
print(user_name.isalnum())









