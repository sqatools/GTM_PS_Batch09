from facebook_file import Facebook

obj = Facebook('User2@gmail.com', 'Admin@12345')
print("module name :", obj.__module__)  #facebook_file

"""
Notes:
->  By default each file module name is __main__ module.
->  When import file in some other file, the filename will become module name.
    facebook_file.
"""
