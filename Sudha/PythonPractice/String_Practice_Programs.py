# 1). Write a Python program to get a string made of the first and the last
# 2 chars from a given string. If the string length is less than 2, return
# instead of the empty string
"""
solution1
string1 = "sqatools"
if len(string1)<2:
    print(True)
else:
    print(string1[:2]+string1[-2:])
output
sqls
"""
# 2). Python string program that takes a list of strings and returns
# the length of the longest string.
"""
solution2
string = ["i", "am", "learning", "python"]
temp = 0

for word in string:
    a = len(word)
    if a > temp:
        temp = a
    else:
        continue

print(temp)

"""

# 3). Python string program to get a string made of 4 copies of the
# last two characters of a specified string (length must be at least 2).
"""string = "sqatools"
print(string[-2:] * 4)

# 4). Python string program to reverse a string if it’s length is a multiple of 4.
input = "sqatools"
if len(input) % 4 == 0:
    print(input[::-1])

# 5). Python string program to count occurrences of a substring in a string.
input2 = "we are learning python programming python is a language"
print("no of python occurrence in a given string : ", input2.count("python"))
# no of python occurrence in a given string :  2

# 6). Python string program to test whether a passed letter is a vowel or consonant.
input3 = "aiorvnbf"
vowels = "aeiouAEIOU"

for char in input3:
    if char in vowels:
        print("char is vowel", char)
    else:
        print("char is consonant", char)

# 7). Find the longest and smallest word in the input string.
input4 = "hi are going learns a programming"
word_len = 0
min_len = 0
wordlist = input4.split(" ")
for word in wordlist:
    if len(word) > word_len:
        word_len = len(word)
    else:
        min_len = len(word)
        continue
print(word_len)
print(min_len)

print("------second solution for 7 ")

# Input string
string = "we are learning python"
list1 = string.split(" ")

# printing output
print("Longest word: ", max(list1, key=len))
print("Smallest word: ", min(list1, key=len))

# 9). Write a Python program to calculate the length of a string
# with loop logic.

input_string = "welcomehere"
count = 0
for char in input_string:
    count = count + 1
print("length of the string : ", count)

# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”
Input_s = "Programming"
result = ""
for char in Input_s:
    if char in result:
        result = result + "$"
    else:
        result = result + char
print("Result : ", result)
# Result :  Prog$am$in$

# 11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”

string_1 = "SqaTool"
print(string_1[-1] + string_1[1:-1] + string_1[0])

# 12). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
# Output = “stI enlino gearninL”
Input21 = "Its Online Learning"
result_String = ""
word_list = Input21.split(" ")
for word in word_list:
    st = word[-1] + word[1:-1] + word[0]
    result_String = result_String + st + " "
print(result_String)
#output : stI enlinO gearninL


13). Write a python to count vowels from each word in the given 
string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

in_str = "We are Learning Python Codding"
vowel = "aeiou"
output = {}

list_word = in_str.split(" ")
for word in list_word:
    v_count = 0
    for char in word:
        if char in vowel:
            v_count += 1
            output[word] = v_count
        else:
            continue


print(output)
#output {'We': 1, 'are': 2, 'Learning': 3, 'Python': 1, 'Codding': 2}"""

"""14). Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg” 

str_in = "Sqa Tools Learning"
vowel = "aeiou"
result = ""
for char in str_in:
    if char in vowel:
        result = result + char*3
    else:
        result = result + char*2

print(result)
# output: SSqqaaa  TToooooollss  LLeeeaaarrnniiinngg"""

"""
15). Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”

String = "Cricket Plays Virat"
list = String.split(" ")
list.reverse()

print(" ".join(list))"""

"""
16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]
"""
input_string = "Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s 5324 success or failure is based on 555 leadership excellence and not managerialacumen"









