#1 Python Program How to read a file in reading mode.
def read_file(filepath):
    file=open(filepath,"r")
    data=file.read()

    print(data)
read_file("read1_data.txt")


#2 Python file program to overwrite the existing file content.
content="""
1.Explaine oobs concept user1@gmail.com
2.What is microservices
3.What is container ram@yahoo.com
4.Differenace bet hasmap hashtable and conccurent hashmap
5.Difference between @restcontroller and @controller
6.Explaine archetechure of microservics sonali12@facebook.com
7.What is methodoverloading and methodoverriding
8.What is use of @springapplication
9.Object method in java
10.Class loader
11.What is conccurenthasmap
12.How to skip finally block
"""

def write_file_content(filepathe,content):
    file=open(filepathe,"w")
    file.write(content)
    file.close()
write_file_content("read1_data.txt",content)
print("-"*50)

#3 Python file program to append data to an existing file.
file=open("read1_data.txt","a")
file.write("13. what is python")
file.close()


#4 Python file program to get the file’s first three and last three lines
# Open file with read mode
file=open("read1_data.txt.","r")
# Read file lines in the list
linesList= file.readlines()
# Print first three lines
for i in (linesList[:3]):
    print(i)

# Print last three lines
for i in (linesList[-3:]):
    print(i)

print("-"*50)
def get_even_no_lines(filepath):
    with open(filepath, "r") as file:
        lines_list = file.readlines()

        for i in range(len(lines_list)):
            line_no=i+1
            if line_no%2!=0:
                print(lines_list[i], end="")

            else:
                continue
get_even_no_lines("read1_data.txt")


print("-"*50)
#5 Python file program to get a specific line from the file.
"""def read_specific_no_lines(filepath, lines_no):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        for i in range(lines_no):
            print(lines_list[i], end="")

read_specific_no_lines("read1_data.txt",4)"""
# Open the file
file = open("read1_data.txt","r")
# Read lines of the file
data = file.readlines()
# Print 1st line

print(data[3])
# Close the file
file.close()

print("-"*50)
#6
def get_email(filepath):
    email_list=[]
    with open(filepath,"r") as file:
       data=file.read()
       word_list=data.split()
       for word in word_list:
           if '@' in  word:
               email_list.append(word)
       print(email_list)
get_email("read1_data.txt")


print("-"*50)
#7 Python file program to get odd lines from files and append them to separate files.
# Open 1st file in read mode
file = open("read1_data.txt", 'r')
# Open 2nd file in write mode
file1 = open('writecontent.txt', 'w')
# Read lines of the file
lines_list = file.readlines()

for i in range(0, len(lines_list)):

    if((i+1) % 2 == 0):

        file1.write(lines_list[i])
    else:
        pass
# Close the file
file.close()
file1.close()

print("-"*50)
#8 Python file program to count all the words from a file.
def count_all_word(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        word_list = data.split()
        count=0
        for word in word_list:
            count+=1
        print("count all the words in file is:",count)
count_all_word("read1_data.txt")
print("-"*50)
#9 Python file program to find the longest word in a file.
def find_longest_word(filepate):
    with open(filepate,"r") as file:
        data=file.read()
        word_list=data.split()
        max_len=0
        max_word=""
        for word in word_list:
            if len(word)> max_len:
                max_len=len(word)
                max_word=word
            else:
                continue
        print("longest word in file is:",max_word)
find_longest_word("read1_data.txt")

#10 Python file program to copy the file’s contents to another file after converting it to lowercase.

with open('read1_data.txt', 'r') as data_file:
        # Open another file in append mode
        with open('writecontent.txt', 'a') as output_file:

            for line in data_file:

                output_file.write(line.lower())


#11 Python file program to copy the file’s contents to another file after converting it to uppercase.
with open("read1_data.txt","r")as data_file:
    with open("writecontent.txt","a") as output_file:
        for line in data_file:
            output_file.write(line.upper())


#12 Python file program to count the number of lines in a file.
with open("read1_data.txt","r") as data_file:
    count=0
    for line in data_file:
        count+=1
    print("count number of line is:",count)

#13 Python file program to get a list of all domains from a file. e.g. .com, .au, .in
with open("read1_data.txt","r") as data_file:
    list=[]
    for word in data_file:
        if ".com" in word:
            list.append(word)
    print(list)


#14 Python file program to count the total number of characters in a file.\
with open("read1_data.txt","r") as file:
    word_list=file.read().split()
    count=0
    for word in word_list:
        for char in word:
            if char.isalpha():
               count+=1

    print("count the total number of characters in a file:",count)

#15 Python file program to count the total number of Uppercase characters in a file.
with open("read1_data.txt","r") as file:
    word_list=file.read().split()
    count=0
    for word in word_list:
        for char in word:
            if char.isupper():
                count+=1
    print("count the total number of Uppercase characters in a file:",count)
print("-"*50)
#16 Python file program to count the total number of Lowercase characters in a file.
with open("read1_data.txt","r") as file:
    word_list=file.read().split()
    count=0
    for word in word_list:
        for char in word:
            if char.islower():
                count+=1
    print("count the total number of Lowercase characters in a file:",count)
print("-"*50)
#17 Python file program to count the total number of digits in a file.
with open("read1_data.txt","r") as file:
    word_list=file.read().split()
    count=0
    for word in word_list:
        for char in word:
            if char.isnumeric():
                count+=1
    print("count the total number of digit in a file:",count)
print("-"*50)
#18 Python file program to count the total number of special characters in a file.
with open("read1_data.txt","r") as file:
    special = ['!', '@', '#', '$', '%', '^', '&', '*',
               '~', '`', '?', ':', ';']
    word_list=file.read().split()
    count=0
    for word in word_list:
        for char in word:
            if char in special:
               count+=1
    print("count the total number of special characters in a file:",count)
print("-"*50)
#19 Python file program to find the cursor position in a file.
"""def read_byte_data_with_tell(filepath, no_bytes):
    with open(filepath, "r") as file:
        print("initial cursor position :", file.tell())
        data = file.read(no_bytes)
        print(data)
        print("after reading value cursor position :", file.tell())

read_byte_data_with_tell("read1_data.txt", 2)"""
# Open the file
file = open("read1_data.txt","r")
file.readline()

print("Position of a cursor in the file: ",file.tell())
print("-"*50)
#20 Python file program to move the cursor to a specific position in a file.

file=open("read1_data.txt","r")
file.readline()
print("position of a cursor in the file:",file.tell())
file.seek(20,0)
print("specific position of the cursor is:",file.tell())

#21 Python file program to read the content of the file in reverse order.
file=open("read1_data.txt")
data=file.readlines()
list=[]
for line in reversed(data):
    list.append(line)
print(list)

print("-"*50)
#22 Python file program to count the total number of vowels in a file.
file=open("read1_data.txt")

word_list=file.read().split()
vowel = ["a", "e", "i", "o", "u","A","E","I","O","U"]
count = 0
for word in word_list:
    for char in word:
         if char in vowel:
                count+=1
print("Total number of vowel in file is:",count)
print("-"*50)
#23 Python file program to count the total number of consonants in a file.

file=open("read1_data.txt")

word_list=file.read().split()
vowel = ["a", "e", "i", "o", "u","A","E","I","O","U"]
count = 0
for word in word_list:
    for char in word:
         if char not in vowel:
                count+=1
print("Total number of constant in file is:",count)
print("-"*50)
#24 Python file program to display words from a file that has less than 5 characters.
file=open("read1_data.txt")
word_list=file.read().split()
for word in word_list:
        if len(word) <5:
            print(word,end=" ")
