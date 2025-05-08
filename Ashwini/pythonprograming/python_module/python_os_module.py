import os
import shutil
#get current working directory

#1). Write a Python Program To Get The Current Working Directory.
print(os.curdir)
print(os.getcwd())
#2). Write a Python Program To Get The Environment Variable
print(os.environ)
#get the environment
print(os.getenv('Browser2'))
print(os.getenv('LANGUAGE'))

##### Create a directory ############
# create directory on current path
#os.mkdir("folder1")

# create directory at specific path
#os.mkdir(r"D:\batch09")

# create nested level of directories
#os.makedirs(r"D:\batch09\fold1\fold2\fold3\fold4\fold5")

####### remove directory ########
#os.rmdir('folder1')  # remove from current location

#os.rmdir(r"D:\batch09")  # remove from specific path

# remove non-empty directories from given path structure.
#os.removedirs(r"D:\batch09\fold1\fold2\fold3\fold4\fold5")

#3). Write a Python Program To Set The Environment Variable
#4). Write a Python Program To Get a List Of All Environment Variable Using os.environ.

#5). Write a Python Program To Create a Directory Using os.mkdir()
#os.mkdir(r"D:\Filesdata\batch09")
#6). Write a Python Program To Create 10 DirecTories With a Random Name."""
#os.makedirs(r"D:\Filesdata1\stud1\stud2\stud3\stud4\stud5\stud6\stud7\stud8\stud9\stud10")
############# Get list of all files and folder ##################

# list of file/folders
target_path = r"D:\RBL project"
files_data = os.listdir(target_path)
print(files_data)
print("Total files/folder :", len(files_data)) #  19

# join two paths
str_path = r'D:\StudentProject'
filename = 'count_name.txt'
files_path = os.path.join(str_path, filename)
print("filepath :", files_path)
# filepath : D:\StudentProject\count_name.txt


print("_"*50)
# Check given path is file or folder
path1 = r"D:\count_name.txt"
path2 = r"D:\batch08"
path3 = r"D:\batch09"

print("check for file :", os.path.isfile(path1)) # True
print("check for file :", os.path.isfile(path3)) # False

print("check directory file :", os.path.isdir(path2)) # false
print("check directory file :", os.path.isdir(path3))  # true

print("_"*50)
# write a python program to get count of files and folder in target path
tar_path = r"D:\RBL project"

files_list = []
folder_list = []
data_list = os.listdir(tar_path) # get files/folder list
for data in data_list:
    #(data)
    data_path = os.path.join(tar_path, data)
    if os.path.isfile(data_path):
        files_list.append(data)
    else:
        folder_list.append(data)

print("files count :", len(files_list))
print(files_list)

print("folder count :", len(folder_list))
print(folder_list)
# Copy content from one location to another.

file1 = r"D:\Filesdata\count_name.txt"
tar_path = r"D:\Filesdata\batch09\count_name.txt"

tar_path2 = r"D:\Filesdata\batch09\count_name_copy.txt"

# copy with file same file name
shutil.copy(file1, tar_path)

# copy with updated file name
shutil.copy(file1, tar_path2)


print("_"*50)
######################### get size of the file ################
filepath = r"D:\Filesdata\batch09\count_name.txt"
# get size of file
filesize = os.path.getsize(filepath)
print("file size in byte :", filesize)

############# file creation time ####
print("creation time of file:",os.path.getctime(filepath))
# 1746605522.8771577

####### get cpu_count of your system ########
print("current CPU count :", os.cpu_count()) # 4


print("_"*50)
############ Run windows command throught python #####
os.system("control")  # open control panel
os.system("appwiz.cpl")  # open program features.
os.system("notepad")   # open notepad.

# run python file with os.system.
os.system("python sample_script.py")























