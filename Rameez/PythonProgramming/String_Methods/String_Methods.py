# Upper() and Lower() method #
from itertools import count

from pandas._libs.writers import word_len

str1= "Hello Good Morning"
print("Upper result:", str1.upper())
print("Lower result:", str1.lower())

# is_upper() and is_lower() method #
str2="Python Programming"
str3="GOOD MORNING"
str4="learning python"
print("str2 is upper:", str2.isupper())
print("str2 is lower:", str2.islower())
print("str3 is upper:", str3.isupper())
print("str4 is lower:", str4.islower())

# swapcase() method #

str5="Hello GoOd Morning"
print(str5.swapcase())

# capitalize() method

str6="we Are Learning python"
print(str6.capitalize())

#Title() method
str7="india is besT cricket tEam"
print(str7.title())

# istitle() method
str8="virat is best cricketer"
str9="Sachin Is God Of Cricket"
print(str8.istitle())
print(str9.istitle())

# count() method
str10="India will win world cup wi"
print("count of i:", str10.count('i'))

# split() Method

str11="India will win world cup wi india"
print(str11.split(" "))

str12="we_Are_Learning_Python_programming"
wordlist1=str12.split("_")
print(wordlist1, len(wordlist1))
wordlist2=str12.split("P")
print(wordlist2)

str13="Very_good_morning_Python_programming"
print(str13.split("_")[1].upper())

# replace() method

str14="Hello Rameez, How are you doing?"
result1=(str14.replace(" ",""))
print(result1, len(result1))

str15="Hey babe, Good Morning.... Shall we go for a coffee date?"
result2=str15.replace("Morning", "Evening").replace("coffee", "movie")
print(result2, len(result2))

# index() Method
str16="Hello Rameez"
print(str16.index("l"))

# find() Method
str17="How are you doing?"
print(str17.find("are"))
print(str17.find("cow"))

#strip() Method

str18=" I am software test engineer "
print(str18.strip())
print(str18.lstrip())
print(str18.rstrip())

#join() method:
str19="Rameez"
print("@".join(str19))
print("_".join(str19[:4]))

#isdigit() method:
str20="43562 789"
str21="987654567.987654"
str22="123456"
print(str20.isdigit())
print(str21.isdigit())
print(str22.isdigit())

# get all the numbers from given string#

str23=" we are all happy family 12 13 15 16 176"
str_word=str23.split()
print(str_word)
for word in str_word:
    if word.isdigit():
        print(word)
    else:
        continue


# isalpha() method
a="alpha123"
b="beta"
print(a.isalpha())
print(b.isalpha())

# isalnum() method
d="a1fh38888"
v="happy"
print(v.isalnum())
print(d.isalnum())










