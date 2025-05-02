#tell() method identify the cursor position
#seek() method set the cursor position

#tell()  Method

#with function

def tell_file_method(filepath,no_bytes):
    with open(filepath,'r') as file:
        print("current position of cursor:",file.tell())
        data=file.read(no_bytes)
        print(data)
        print("current position of cursor:", file.tell())
tell_file_method('read_data1.txt', 40)


print("*"*777)
with open ('read_data1.txt','r') as file:
    print("initial curson pos:",file.tell())
    data=file.read(70)
    print(data)
    print("cursor pos is:",file.tell())


print("*"*90)
#seek()==== it will set the cursor position
with open ('read_data1.txt','r') as file:
    print("current cursor position:", file.tell())
    print("cursor position set to: ", file.seek(30, 0))
    #data=file.read()
    #print(data)
    print("current cursor position:",file.tell())
    print("cursor position set to: ", file.seek(40, 1))
    print("current cursor position is :", file.tell())



