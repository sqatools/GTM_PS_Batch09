import os

# get current working directory
print(os.curdir) # .
print(os.getcwd()) #
# E:\Trainings\GTM_PS_Batch09_7Mar25\GTM_PS_Batch09\Deepesh\PythonProgramming\Python_Modules


### Get environment variable value ###
print(os.getenv('Browser2'))  # Mozilla
print(os.getenv('LANGUAGE'))  # Python

# GET LIST of All Environment variables
print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Deepesh Yadav\\AppData\\Roaming', 'BROWSER2': 'Mozilla', 'CHROME_PATH': 'C:\\drivers\\chromedriver_win32\\chromedriver.exe', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPOSE_CONVERT_WINDOWS_PATHS': 'true', 'COMPUTERNAME': 'LAPTOP-H6M50F6C', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DOCKER_CERT_PATH': 'C:\\Users\\Deepesh Yadav\\.docker\\machine\\machines\\default', 'DOCKER_HOST': 'tcp://192.168.99.100:2376', 'DOCKER_MACHINE_NAME': 'default', 'DOCKER_TLS_VERIFY': '1', 'DOCKER_TOOLBOX_INSTALL_PATH': 'C:\\Program Files\\Docker Toolbox', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EFC_6176_1592913036': '1', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Deepesh Yadav', 'IDEA_INITIAL_DIRECTORY': 'C:\\Program Files\\JetBrains\\PyCharm Edu 2022.2.2\\bin', 'INTELLIJ IDEA COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.3.2\\bin;', 'LANGUAGE': 'Python', 'LOCALAPPDATA': 'C:\\Users\\Deepesh Yadav\\AppData\\Local', 'LOGONSERVER': '\\\\LAPTOP-H6M50F6C', 'NO_PROXY': '192.168.99.100', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\Deepesh Yadav\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\Deepesh Yadav\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\Deepesh Yadav\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\Deepesh Yadav\\AppData\\Local\\Programs\\Python\\Python38\\;C:\\Program Files\\Python38\\Scripts\\;C:\\Program Files\\Python38\\;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;E:\\driver;C:\\sqalite3\\;C:\\Program Files (x86)\\dotnet\\;E:\\Trainings\\PythonRobotTavet14Feb2023\\RobotframeworkProject\\chromedriver_win32\\chromedriver.exe;c:\\users\\deepesh yadav\\appdata\\roaming\\python\\python312\\;c:\\users\\deepesh yadav\\appdata\\roaming\\python\\python312\\Scripts\\;C:\\Program Files\\Git\\cmd;C:\\Python312\\;C:\\Python312\\Scripts\\;C:\\Program Files\\PuTTY\\;C:\\Users\\Deepesh Yadav\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.2\\bin;;E:\\chromedriver_win32;C:\\Program Files\\Docker Toolbox;C:\\Users\\Deepesh Yadav\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.3.2\\bin;;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 126 Stepping 5, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '7e05', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files (x86)\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.2\\bin;', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'E:\\Trainings\\GTM_PS_Batch09_7Mar25\\GTM_PS_Batch09', 'PYTHONUNBUFFERED': '1', 'PYTHONVERSION': '3.12', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\DEEPES~1\\AppData\\Local\\Temp', 'TEST_ENV': 'TEST', 'TMP': 'C:\\Users\\DEEPES~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-H6M50F6C', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-H6M50F6C', 'USERNAME': 'Deepesh Yadav', 'USERPROFILE': 'C:\\Users\\Deepesh Yadav', 'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1'})


##### Create a directory ############
# create directory on current path
# os.mkdir("folder1")

# create directory at specific path
# os.mkdir(r"E:\Filesdata\batch09")

# create nested level of directories
# os.makedirs(r"E:\Filesdata\batch09\fold1\fold2\fold3\fold4\fold5")

####### remove directory ########
#os.rmdir('folder1')  # remove from current location

# os.rmdir(r"E:\Filesdata\batch09")  # remove from specific path

# remove non-empty directories from given path structure.
# os.removedirs(r"E:\Filesdata\batch09\fold1\fold2\fold3\fold4\fold5")


############# Get list of all files and folder ##################

# list of file/folders
target_path = r"E:\Filesdata"
files_data = os.listdir(target_path)
print(files_data)
print("Total files/folder :", len(files_data)) #  58

# join two paths
str_path = r'E:\Filesdata'
filename = 'count_name.txt'
files_path = os.path.join(str_path, filename)
print("filepath :", files_path)
# filepath : E:\Filesdata\count_name.txt


print("_"*50)
# Check given path is file or folder
path1 = r"E:\Filesdata\count_name.txt"
path2 = r"E:\Filesdata\batch08"
path3 = r"E:\Filesdata\batch09"

print("check for file :", os.path.isfile(path1)) # True
print("check for file :", os.path.isfile(path3)) # False

print("check directory file :", os.path.isdir(path2)) # True
print("check directory file :", os.path.isdir(path3))  # False

print("_"*50)
# write a python program to get count of files and folder in target path
tar_path = r"E:\Filesdata"

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


