#write a program to get all odd no of lines from the given file.
def read_file_line(filepath):
    with open(filepath,'r') as file:
        line_list = file.readlines()
        #print(line_list)
        length_lines = len(line_list)
        for i in range(0,length_lines,2):
            print(line_list[i])


read_file_line("read_data.txt")
