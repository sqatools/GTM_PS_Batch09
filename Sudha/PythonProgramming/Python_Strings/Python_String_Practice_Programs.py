# 1. write a python to get longgest word from given string.

str1 = "We are Learning Python Programming Hello good Morning"
long_word = ''
long_len = 0

word_list = str1.split(" ")
print(word_list)
for word in word_list:
    word_len = len(word)
    print(word,word_len)
    if word_len > long_len:
        long_len = word_len
        long_word = word
    else:
        continue

print(long_word, long_len)

print("_"*50)
# write a python program to remove duplicate names from given string

str2 = "RAM SHYAM MOHAN SHYAM RAM RAHUL"
result = ""

word_list1 = str2.split(" ")
print(word_list1)

for word1 in word_list1:
    if word1 not in result:
        #result = result.__add__(word1).__add__(" ") any one of the statement will work
        result = result + word1 + " "
    else:
        continue
print("Result after deleting duplicate names : ",result)
"""
['RAM', 'SHYAM', 'MOHAN', 'SHYAM', 'RAM', 'RAHUL']
Result after deleting duplicate names :  RAM SHYAM MOHAN RAHUL 
"""

print("_"*50)
#3. write a python program to count total vowels in given string.
str3= "Sachin is best cricketer HEllO"
vowels = "aeiouAEIOU"
vcount = 0

for char in str3:
    if char in vowels:
        vcount = vcount+1
    else:
        continue
print("vowels count in an given string : ", vcount)

"""
print("_"*50)
stringa = "I Love Java"
print(stringa)
#output Java Love I
list1 = stringa.split(" ")
word1 = list1[0]
word2 = list1[1]
word3 = list1[2]
print(word3,word2,word1)
#avaJ evoL I
print(stringa[::-1])
#output avaJ evoL I

"""




