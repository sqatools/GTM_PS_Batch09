"""for file handlin tere are tree type of file open
read_data1.txt mode(r):
write mode(w):
append mode(a):

"""
#read_data1.txt the file mode
def read_file(file_path):
    file=open(file_path,'r')
    data=file.read()
    print(data)
#read file from current location
read_file("read_data.txt")

#read file from specific location
read_file(r"D:\RBL project\serviceDetail.txt")
#open file in write mode and update the content
def write_file_content(filepathe,content):
    file=open(filepathe,"w")
    file.write(content)
    file.close()


# write to non-existing file:it wil create new file and add content to the file.
new_content=""" hi good morning python is lanvage for learning  
it is to easy for coding purpose i am good knowelde of coding
he gets forward to loft and not get the ball"""
#write_file_content("write_file.txt",new_content)# create file on same location
#write_file_content(r"write_file_new.txt",new_content)# create file on specific path

#write to existing file: it will overwrite the previous content and write new content
msg="""hello modify the perivious file """
write_file_content("write_file_update.txt",msg)
#open file in append mode and update the content
def append_file_content(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()


#1. append to non-existing file : It will create file and add content.
append_content = """python is lanvage learning is easy way to write a code
Abhishek Sharma!! rahul patel goes for the
big hit and perishes. Was fullish on off, 
Good morning, good evening
"""
#append_file_content("append_file.txt", append_content)


#2. append to existing file : It will add content at end of the file after previous content.
msg = """i). ashwini to sonal patel, out Caught by 
ii) Abhilas rathod!! mona Dube goes for the
iii) big hit and perishes. Was fullish on off, 
iv) he gets forward to loft and does not get the
v) Good morning, good evening
"""
#append_file_content("append_file_update.txt", "Python Programming is easy to learn\n")
#append_file_content("append_file_update.txt", msg)

###### Context Manager#############
#context manager: its own enter aand exit method it automatically close the file
#once we come out  from context manager session
def read_file_content(filepath):
    with open(filepath,'r') as file:
        data=file.read()
        print(data)
        print("is file closed:in context manager:",file.close())
    print("is file closed: outside of context manager:",file.close())

read_file_content("read_data.txt")

print("_"*50)
#1.read number from file:file.read()
#2. read line from file:file.readline()
#3.read list of lines: file.readlines()

def read_byte_data(filepath,no_bytes):
    with open(filepath,'r') as file:
        data=file.read(no_bytes)
        print(data)

read_byte_data("read_data.txt",10)
#2.read line from file:file.readline():this method return one single line output
def read_byte_data(filepath,no_lines):
    with open(filepath,'r') as file:
         print(file.readline())

read_byte_data("read_data.txt",2)

print("-"*50)
#3.read list of line: file.readlines() :this method return  all line in target file
def read_byte_data(filepath):
    with open(filepath,'r') as file:
        lines_list=file.readlines()
        print(lines_list)


read_byte_data("read_data.txt")

# tell() method : This method return the current position of the cursor
def read_byte_data_with_tell(filepath, no_bytes):
    with open(filepath, "r") as file:
        print("initial cursor position :", file.tell())
        data = file.read(no_bytes)
        print(data)
        print("after reading value cursor position :", file.tell())

read_byte_data_with_tell("read_data.txt", 25)


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

#read_byte_data_with_seek("read_data.txt")