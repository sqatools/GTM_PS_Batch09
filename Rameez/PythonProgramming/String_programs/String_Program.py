# write a python program to get word from given string
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

str2="Happy birthday rameez"
long_word=""
long_len=0

word_list=str2.split()
print(word_list)
for word in word_list:
    word_len=len(word)
    print(word_len)
    if word_len>long_len:
        long_len=word_len
        long_word=word
    else:
        continue
print(long_word, long_len)

# Write a python program to remove duplicate names from given string
str3= " Abdul Mudassir Hamza Abdul Rameez Hamza Abdul Hameed Hamza"
result=""
word_list=str3.split(" ")
print(word_list)
for word in word_list:
    if word not in result:
        result= result + word
    else:
        continue
print(result)
# write a python program to calculate the count of total vowels in given string
str4= "I Am Working As Software Test Engineer"
vowels="aeiouAEIOU"
count=0
for char in str4:
    if char in vowels:
        count=count+1
    else:
        continue
print(count)