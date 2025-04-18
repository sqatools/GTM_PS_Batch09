############## string slicing ####################
# Rule 1: str[start index: end index]
"""
->  Output will contains result from left to right.
->  Output value will include start index and exclude the end index.
->  if we don't defined the start index, then default start index is 0 e.g. str[:end index]
->   if we don't defined the end index, then default end index would be end of the string.
     e.g. str[start index:]
->
"""
city = "WashigtonDC"
print(city[3:11])# this will print higton Means start from the 3rd index till 11 index

print(city[:4])# this will print wash means start from 0 till 4 index

print(city[4:])# this will print igtonDC

print(city[-2:])

print(city[-2:5])



