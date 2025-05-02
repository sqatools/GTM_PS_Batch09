#context manager has its own entry and exit point. no need to write code for exit.. it will automatic exit

#1.read no of bytes(charchter)
#without function

with open('read_data.txt','r') as file:
    data=file.read(10)
 #   print(data)

#with function
def read_byte_data(filepath,no_bytes):
    with open(filepath, 'r') as file:
        data = file.read(no_bytes)
       # print(data)
#read_byte_data('read_data.txt',30)

#2.Read line from file(single line need to be read)------it will give output as a single line
#without function
print("*"*70)
with open('read_data.txt','r') as file:
    data1 = file.readline()
    print(data1)



#without function
#def read_line_data(filepath, no_lines):
    #with open(filepath, "r") as file:
        #for _ in range(no_lines):
            #print(file.readline())


#read_line_data("read_data.txt", 4)

#3.read the lines from the list
print("*"*79)
def read_lines_list(filepath):
    with open(filepath,'r') as file:
        data=file.readlines()
        print(data) # it will print all the lines of the list in a single line
        for val in data:   # it will print lines one by one
            print(val)

#read_lines_list("read_data.txt")










