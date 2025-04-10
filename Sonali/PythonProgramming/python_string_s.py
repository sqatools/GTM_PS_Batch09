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



