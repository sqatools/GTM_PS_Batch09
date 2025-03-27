############ Integer #################
"""
# properties of integer
->  Integer is immutable data type, once it is defined we can not change it.
->  Integer can contains any position and negative value.
->  Only whole will be consider as int
->  There is no limit to defined data in int variable

"""
# int1 = 100
# int2 = 120
# int3 = 40
# int4 = int1 + int2 + int3
# print(int4, type(int2))

############################################
# Sting datatype
# name = "varinder"
# Add = "123 you got it"
# phone = "703-450-6043"
#
# print("this is my name : " ,name, type(name))
# print("this is VA. Sam's\n coming to Washington tomorrow")
#
# print("this will print v and that is my 0 index :", name[0])# positive index

# in the below print statement I pulled Location of the element, type of the datatype and the negtive index
# print("this will print the last charcher, which is r :", name[-1], id(name),type(name))



# float1 = 28.001
# float2 = 2.94
# print("this is float:/" ,float1, type(float1))
# print("this is floate valve2 :" ,float2, type(float2))

###################################################
# List holds all types of data type example - int, string, boolean, float etc.

list = [2, 4, 6, "varinder", "harveer",[2, 4, 7],{"h", "j",9},(10, 6,"Roop",)]

tup = (20, 30, {"hello", "yup", 6, 7},("this is tuple", 7, 20),[20, 10, "yad"])

dict1 = {"name" :"Varinder", "age" : 27, "address" :"21 merion dr"}


print(list[5])
print(list[5][2])
print(tup[3],type(tup))
print(tup[3][0])
print(dict1["name"],type(dict1))
print(dict1["address"])
"""
##############Set ###########################################
Properties :
->  Set is mutable data type, we modify it.
->  Set store unique data, duplicate values are not allowed.
->  Set store data in random order.
->  Set can contain only immutable data type, int, float, string, tuple, boolean, complex number.
->  Set does not follow indexing.
"""
setdatatype = {10, 3, "varinder", 5, ("v", 6, 10.0,)}
print(setdatatype)

######################################
#   True and False
name = "varinder"
age = 25
houseNo = 25
print("this is :",name == age)
print("this is :",age == houseNo)




