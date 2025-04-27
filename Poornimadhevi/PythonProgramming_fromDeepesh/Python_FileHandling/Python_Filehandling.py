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
append_file_content("append_file_update.txt", msg)
