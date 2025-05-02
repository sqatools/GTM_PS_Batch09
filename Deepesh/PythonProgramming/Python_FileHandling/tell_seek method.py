#tell() method identify the cursor position
#seek() method set the cursor position

#tell()  Method

#with function

def tell_file_method(filepath,no_bytes):
    with open(filepath,'r') as file:
        print("current position of cursor:",file.tell())