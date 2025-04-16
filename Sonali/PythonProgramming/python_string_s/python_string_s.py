#slicing concept
str1="python"
for i in (str1):
    print(i)

# howmany letters in a word and print every letter with its index value
str_len=len(str1)
print(str1,str_len)
for i in range (str_len):
    print(i, str1[i])

print("-"*50)
#slicing concept
str1 = "Hello good Morning"
print("_"*40)
output1 = "HHello good Morningg"
#solution:
print(f"{str1[0]}{str1}{str1[-1]}")
print("_"*40)
str1 = "Hello good Morning"
output2="HHelloo ggoodd MMorningg"
#solution:
word1=str1[:5] #consider space so that it will print till o in hello
word2=str1[6:10] #from g to space in good and space
word3=str1[11:]  #from m to g in morning

print(f"{word1[0]}{word1}{word1[-1]} {word2[0]}{word2}{word2[-1]} {word3[0]}{word3}{word3[-1]}")

print("_"*40)
str1 = "Hello good Morning"
output3 = "olleH doog gninroM"
# solution:

word1=str1[:5] #consider space so that it will print till o in hello
word2=str1[6:10] #from g to space in good and space
word3=str1[11:]  #from m to g in morning

print(f"{word1[-1:-6:-1]} {word2[::-1]} {word3[::-1]}") # between hello and good and morning the space is defined if we give space between {}


#get all the numbers from a given string
str1="i am 23 learing python 34 56 78 90"
w_li=str1.split()
print(w_li)
for word in w_li:
    if word.isdigit():
        print(word)
    else:
        continue



print("-"*50)
n="I am learning python programming"
long_len=0
long_word=''
word_list=n.split()
for word in word_list:
    word_len=len(word)
    if word_len>long_len:
        long_len=word_len    #word length assigned to long_len
        long_word=word
    else:
        continue
print(long_word,long_len)

print("-"*50)
#====================================


#There should not be any duplicate in the string

str3="sonali ram shyam RAM SONALI"
result=" "
word_list2=str3.split()
print(word_list2)
for word in word_list2:
    if word not in result:
        result=result+word+" "
    else:
        continue
print(result)     # it will print the words as case sensitive

#









