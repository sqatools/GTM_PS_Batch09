# write a python program to read content from 2 files and
# store in 3rd file.

def merge_two_files_content(f1, f2, f3):
    with open(f1, 'r') as file1:
        file1_data = file1.read()

    with open(f2, 'r') as file2:
        file2_data = file2.read()

    file3_data = file1_data + file2_data
    with open(f3, "w") as file3:
        file3.write(file3_data)


merge_two_files_content("read_data_file1.txt",
                        "read_data_file2.txt",
                        "write_data_file3.txt")


#Q : write python program to get list emails and phones
# numbers from given file.

def get_email_phone(file_path):
    email_list = []
    phone_list = []
    with open(file_path, "r") as file:
        data = file.read()

    # get word list with split method.
    word_list = data.split(" ")

    for word in word_list:
        # check @ in the given word
        if '@' in word:
            email_list.append(word)
        # check if word length is 10 and only contains number.
        elif len(word) == 10 and word.isdigit():
            phone_list.append(word)


    print("email list :", email_list)
    print("phone list :", phone_list)


#get_email_phone("read_email_phone.txt")


# write a python program to get all odd lines from
# given file.

def get_odd_lines(filepath):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        for i in range(len(lines_list)):
            line_no = i+1
            if line_no%2 != 0:
                print(lines_list[i], end="")
            else:
                continue


get_odd_lines("read_data.txt")




