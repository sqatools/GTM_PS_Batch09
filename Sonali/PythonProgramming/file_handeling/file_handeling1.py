'''
File handeling has 3 way to handel
1.read mode
2.write mode
3.appened mode
'''

#Read mode

#method-1(with function)
def file_read(file_path):
     file=open(file_path,'r')
     data=file.read()
     print(data)
     file.close()
file_read('read_data.txt')


print("*"*60)

#method-2 (without function)
file=open('read_data.txt','r') #open the file
data=file.read()               #read the file
print(data)                    #print data
file.close()                   #close the file

#u can take the file or file_path


#Write mode
#method-1:(without function)
data="This is new line"

file=open('read_data.txt','w')
file.write(data)
print(file)
file.close()

#it will ovedrride the existing data... meansa old values will be removed and only new data will be there

#method-2:(with function)
data1="This is india"
def file_write(filepath,data1):
     file1 = open(filepath, 'w')
     file1.write(data1)
     print(file)
     file1.close()
file_write('read_data1.txt', data1)   #new file will be craeted at same location

#The above one will create the file at same location


#appened()- it can create as well as can add the content at the end of the lines of file
#it will create and add

content1="This is banglore"
file=open("fileapnd.txt","a")
file.write(content1)
file.close()

#add the lines at the end of the file

new_content = """ Unadkat to Shivam Dube, out Caught by 
Abhishek Sharma!! Shivam Dube goes for the
big hit and perishes. Was fullish on off, 
he gets forward to loft and does not get the
"""

def file_apend(filepath,new_content):
     file = open(filepath, "a")
     file.write(new_content)
     file.close()
file_apend('fileapnd.txt',new_content)




