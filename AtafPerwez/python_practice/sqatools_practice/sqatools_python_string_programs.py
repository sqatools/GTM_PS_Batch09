# Python string programs
print("-----------solution-2--------")
# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
str1= 'PYthn is fun'
print(str1[:2], str1[-1:-3:-1])

# 2). Python string program that takes a list of strings and returns the length of the longest string.
print("-----------solution-2--------")
str2 = "A quick brown fox jump over the intelligent dog"
words = str2.split()
print(words)
temp =0
for word in words:
    length = len(word)
    if length > temp:
        temp= length

print(f'longest word is: {temp}')


# 3). Python string program to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).
print("--------solution-3--------")# Solution
str3 = 'python'
temp = str3[4:]
print(temp)
print(list(4*temp))



# 4). Python string program to reverse a string if it’s length is a multiple of 4.
print("--------solution-4--------")# Solution
str4= 'reversey'
for i in str4:
    l = len(str4)
    if l%4==0:
        print(str4[-1::-1])
    else:
        print(f'length of string is not divisible by 4')


# 5). Python string program to count occurrences of a substring in a string.
print("--------solution-5--------")# Solution
str5 = 'I am a disco dancer'
substr= 'dis'
print(str5.count(substr))

# 6). Python string program to test whether a passed letter is a vowel or consonant.
print("--------solution-6--------")# Solution
letter = 'o'
for l in letter:
    if l == 'a' or 'e' or 'i' or 'o' or 'u':
        print(f'letter is vowel:{letter}')
    else:
        print(f'letter is consonant: {letter}')



# 7). Find the longest and smallest word in the input string.
print("--------solution-7--------")# Solution
str6 = 'learinig python is fun a'
list = str6.split()
print(f'Longest word: {max(list, key=len)}')
print(f'smallest word: {min(list, key=len)}')



# 8). Print most simultaneously repeated characters in the input string.



# 9). Write a Python program to calculate the length of a string with loop logic.
str =  "we are learning python"
temp = 0
for i in str:
    length = len(i)
    temp +=1
print(f'length of string is: {temp}')


# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”
inp = 'Programming'
result = ''
for char in inp:
    if char in result:
        result = result + "$"
    else:
        result = result + char
print(result)

# 11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”

str11 = "PythoN"
print(str11[-1]+str11[1:-1] + str11[0])


# 12). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
# Output = “stI enlino gearninL”

str12 = 'Its Online Learning'
print(str12[-1] + str12[1:-1] + str12[0])

# 13). Write a python to count vowels from each word in the given string show as dictionary output.
# Input = “We are Learning Python Codding”
# output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
print('------13------')
str13 = 'We are Learning Python Codding'
vowels = 'AEIOUaeiou'
dict= ()
for char in str13:
    for v in vowels:
        if v in char:
            result = v
            print(result, end=" ")


# 14). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

print('\n------14-----')
str14= 'Sqa Tools Learning'
vowels = ["a","e","i","o","u","A","E","I","O","U"]
result = ''
for char in str14:
    if char in vowels:
        result = result+char*3
    else:
        result = result+char*2
print(result)


# 15). Write a python program to re-arrange the string.
# Input = “Cricket Plays Virat”
# Output = “Virat Plays Cricket”
print('\n------14-----')
str15 = "cricket play MSD"
words= str15.split()
print(words[-1::-1])



# 16). Write a python program to get all the digits from the given string.
print("---------16--------")
str16 = 'Sinaks 1112 aim is to 1773 create a new generation of people who understand 444 that an organizations 5324 success or failure is based on 555 leadership excellence and not managerial acumen'
# Output = [1112, 5324, 1773, 5324, 555]

digit = []
char = []
words =str16.split()
# print(words)
for word in words:
    if word.isalpha():
        char.append(word)
    else:
        digit.append(word)
print(f'char= {char}')
print(f'digit= {digit}')



# 17). Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”
print('-------17-------')
str17 = " JAVA is the best programming language in the market"
str17= str17.replace('JAVA', 'Python')
print(str17)



# 18). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]
print('-----------18----------')
str18= 'Python efe language aakaa hellolleh'
words= str18.split(" ")
palindrome= []
for word in words:
    if word[::-1] == word:
        palindrome.append(word)
    else:
        continue
print(palindrome)


# 19). Write a Python program to create a string with a given list of words.
# Input = [“There”, “are”, “Many”, “Programming”, “Language”]
# Output = There are many programming languages.
list19 = ['there', 'are', 'many', 'programming', 'language']
str19 = " ".join(list19)
print(str19)

# 20). Write a Python program to remove duplicate words from the string.
# Input = “John jany sabi row john sabi”
# output = “John jany sabi row”
str20 = 'John jany sabi row John sabi'
words = str20.split(" ")
temp = []
for wor in words:
    if wor not in temp:
        temp.append(wor)

print(temp)



# 21). Write a Python to remove unwanted characters from the given string.
# Input = “Prog^ra*m#ming”
# Output = “Programming”
print('-----------21--------')
str21 = 'Prog^ra*m#ming'
result = ''.join(letter for letter in str21 if letter.isalnum())
print(result)
# Input = “Py(th)#@&on Pro$*#gram”
# Output = “PythonProgram”
str22 = 'PythonProgram'
result = ''.join(letter for letter in str22 if letter.isalnum())
print(result)
# Solution
# 22). Write a Python program to find the longest capital letter word from the string.
# Input = “Learning PYTHON programming is FUN”
# Output = “PYTHON”
#
# Solution
# 23). Write a Python program to get common words from strings.
# Input String1 = “Very Good Morning, How are You”
# Input String1 = “You are a Good student, keep it up”
# Output = “You Good are”
#
# Solution
# 24). Write a Python program to find the smallest and largest word in a given string.
# Input = “Learning is a part of life and we strive”
# Output = “a”, “Learning”
#
# Solution
# 25). Check whether the given string is a palindrome (similar) or not.
# Input= sqatoolssqatools
# Output= Given string is not a palindrome
#
# Solution
# 26). Write a program using python to reverse the words in a string.
# Input= sqatools python
# Output= slootaqs
#
# Solution
# 27). Write a program to calculate the length of a string.
# Input= “python”
# Output = 6
#
# Solution
# 28). Write a program to calculate the frequency of each character in a string.
# Input = “sqatools”
# Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}
#
# Solution
# 29). Write a program to combine two strings into one.
# Input:
# A = ’abc’
# B = ’def’
# Output = abcdef
#
# Solution
# 30). Write a program to print characters at even places in a string.
# Input = ‘sqatools’
# Output = saol
#
# Solution
# 31). Write a program to check if a string has a number or not.
# Input = ‘python1’
# Output = ‘Given string have a number’
#
# Solution
# 32). Write a python program to count the number of vowels in a string.
# Input= ‘I am learning python’
# Output= 6
#
# Solution
# 33). Write a python program to count the number of consonants in a string.
# Input= ‘sqltools’
# Output= 6
#
# Solution
