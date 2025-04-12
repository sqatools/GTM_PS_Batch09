
# 1. write a python to get longgest word from given string.

str1 = "We are Learning Python Programming Hello good Morning"
long_word = ''
long_len = 0

word_list = str1.split()
print(word_list)
for word in word_list: # We, are, Learning, Python, Programming
    word_len = len(word) # 2, 3, 8, 6, 11
    #print(word, word_len)
    if word_len >  long_len: # 2 > 0 | 3 > 2 | 8> 3 | 6> 8 | 11> 8
        long_len = word_len # 2, 3, 8, 11
        long_word = word # We, Are, Learning, Programming
    else:
        continue


print(long_word, long_len)


print("_"*50)
# write a python program to remove duplicate names from given string

str2 = "RAM SHYAM MOHAN SHYAM RAM RAHUL"
result = ""
word_list = str2.split()
for word in word_list: # RAM SHYAM MOHAN SHYAM RAM RAHUL
    if word not in result:
        result = result + word + " " # RAM SHYAM MOHAN RAHUL
    else:
        continue

print("result :", result)
# result : RAM SHYAM MOHAN RAHUL


print("_"*50)
#3. write a python program to count total vowels in given string.
str3= "Sachin is best cricketer HEllO"
vowels = "aeiouAEIOU"
vcount = 0

for char in str3:
    if char in vowels:
        vcount += 1
    else:
        continue


print("vowels count :", vcount)




