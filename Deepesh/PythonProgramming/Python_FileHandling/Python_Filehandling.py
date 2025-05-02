"""
for file handling there are three mode of file to open
read mode (r) :
write mode (w) :
Append mode (a) :
"""

def read_file(file_path):
    file = open(file_path, 'r')
    data = file.read()
    print(data)
    file.close()

# read file from current location
# read_file("read_data.txt")

# Read file from specific location
#read_file(r"E:\Filesdata\count_name.txt")


# open file in write mode and update the content
def write_file_content(filepath, content):
    file = open(filepath, "w")
    file.write(content)
    file.close()


# 1. write to non-existing file:  It will create new file and add content to the file.
new_content = """ Unadkat to Shivam Dube, out Caught by 
Abhishek Sharma!! Shivam Dube goes for the
big hit and perishes. Was fullish on off, 
he gets forward to loft and does not get the
"""
#write_file_content("write_file.txt", new_content)  # create file on same location
# write_file_content(r"E:\Filesdata\write_file_new.txt", new_content) # create file on specified path.

# 1. write to existing file: It will overwrite the previous content and write new content
#msg = "Hello, we are learning file handling"
#write_file_content("write_file_update.txt", msg)




##########################################
# open file in append mode and update the content
def append_file_content(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()


#1. append to non-existing file : It will create file and add content.
append_content = """Unadkat to Shivam Dube, out Caught by 
Abhishek Sharma!! Shivam Dube goes for the
big hit and perishes. Was fullish on off, 
he gets forward to loft and does not get the
Good morning, good evening
"""
#append_file_content("append_file.txt", append_content)


#2. append to existing file : It will add content at end of the file after previous content.
msg = """i). Unadkat to Shivam Dube, out Caught by 
ii) Abhishek Sharma!! Shivam Dube goes for the
iii) big hit and perishes. Was fullish on off, 
iv) he gets forward to loft and does not get the
v) Good morning, good evening
"""
#append_file_content("append_file_update.txt", "Python Programming is easy to learn\n")
#append_file_content("append_file_update.txt", msg)


print("_"*50)
###################################################
# context manager :  context manager has its own enter and exit method, it automatically close the file
# once we come out from context manager session.

def read_file_content(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(data)
        print("is file closed : in context manger:", file.closed) # False

    print("is file closed : outside of context manger:", file.closed) # True

#read_file_content("read_data.txt")


print("_"*50)
###################################################
# 1. read number of bytes : file.read(10)
# 2. read line from file : file.readline()
# 3. read list of lines :  file.readlines()

# 1. read number of bytes : file.read(10)
def read_byte_data(filepath, no_bytes):
    with open(filepath, "r") as file:
        data = file.read(no_bytes)
        print(data)


# read_byte_data("read_data.txt", 20)
# Harshal Patel to Bre

print("_"*50)
# 2. read  line from file : file.readline():  readline method return one single line output
def read_line_data(filepath, no_lines):
    with open(filepath, "r") as file:
        for _ in range(no_lines):
            print(file.readline(), end="")

#read_line_data("read_data.txt", 4)


print("_"*50)
##########################################################
# 3. read list of lines :  file.readlines() :
# readlines method return list of all lines in the target file.


def read_lines_list(filepath):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)

        # print all lines one by one
        for val in lines_list:
            print(val)


#read_lines_list("read_data.txt")

def read_specific_no_lines(filepath, lines_no):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)

    # read lines from positive index
    if lines_no > 0:
        for i in range(lines_no):
            print(lines_list[i], end="")
    else:
    # read lines from negative index
        for i in range(lines_no, 0, 1):
            print(lines_list[i], end="")

# This will print first 5 lines
read_specific_no_lines("read_data.txt", 5)
"""
1.Harshal Patel to Brevis, SIX, that is an extraordinary shot.
2.Was a slower-ball off-cutter dug in short outside off,
3.Brevis generates so much power on the cut,12.3
4.Harshal Patel to Brevis, no run, wide of the crease and
5.short of length outside off, Brevis whiplashes the cut but

"""

print("_"*50)
# This will print last three lines from file
read_specific_no_lines("read_data.txt", -3)

"""
9.Harshal Patel to Brevis, no run, wide of the crease and
10.short of length outside off, Brevis whiplashes the cut but
11.straight to the fielder at backward point, either side and was four
"""

print("_"*50)
####################################
# tell() method : This method return the current position of the cursor
def read_byte_data_with_tell(filepath, no_bytes):
    with open(filepath, "r") as file:
        print("initial cursor position :", file.tell())
        data = file.read(no_bytes)
        print(data)
        print("after reading value cursor position :", file.tell())

#read_byte_data_with_tell("read_data.txt", 25)


print("_"*50)
# seek(bytes, offset) method :  seek method helps to set the cursor position.
# 0 :  from begining of the file :  we can read normal file content
# 1:  from current position :  we have to open file in binary mode
# 2:  end of the file. :  we have to open file in binary mode.
def read_byte_data_with_seek(filepath):
    with open(filepath, "r") as file:
        print("initial cursor position :", file.tell())  # 0
        file.seek(30, 0)
        print("current cursor position :", file.tell())  # 30
        #data_40 = file.read(40)
        #print(data_40)
        file.seek(40, 1)
        print("new cursor position :", file.tell()) # 70

        # set cursor position from end of the file

        file.seek(-50, 2)
        print(file.read())

read_byte_data_with_seek("read_data.txt")
