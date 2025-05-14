import os
print(os.curdir)  #. is the ans.. as it represents the current dir
print(os.getcwd())

print(os.environ)
#os.mkdir("folder1")
#os.mkdir(r"C:\Users\SM2977\OneDrive - Zebra Technologies\Pictures\batch08") #.................single folder/file creation
#os.rmdir(r"C:\Users\SM2977\OneDrive - Zebra Technologies\Pictures\batch08") #------------single file/folder removal
#os.makedirs(r"C:\Users\SM2977\OneDrive - Zebra Technologies\Pictures\batch09\fold1\fold2\fold3\fold4\fold5")  #------nested file/folder created
#os.removedirs(r"C:\Users\SM2977\OneDrive - Zebra Technologies\Pictures\batch09\fold1\fold2\fold3\fold4\fold5") #-------nested file/folder removal



##########list of all files and folders##########

target_file=r"C:\AutomationCode"
file_data=os.listdir(target_file)
print(file_data)
print("total files and folders:",len(file_data))


