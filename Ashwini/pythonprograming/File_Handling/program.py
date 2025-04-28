"""for file handlin tere are tree type of file open
read_data.txt mode(r):
write mode(w):
append mode(a):

"""
#read_data.txt the file mode
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