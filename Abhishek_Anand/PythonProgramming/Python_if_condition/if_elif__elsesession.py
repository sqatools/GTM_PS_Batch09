############################ if-elif-else ################################
"""
if cond1:
    code1
elif cond2:
    code2:
elif cond3:
     code3
elif cond4:
    code4
else:
    code5
"""

print("_"*50)
# write a python program to find the greater number among three values
a = 30
b = 40
c = 30

if a > b and a > c:
    print("A has greater value:", a)
elif b > a and b > c:
    print("B has greater value:", b)
elif c > a and c > b:
    print("C has greater value:", c)
else:
    print("No one has greater value")


print("_"*50)
# write a program to provide grade to students as marks received.
marks = input("Please enter marks:")
print(marks, type(marks))
st_marks = int(marks)
print(st_marks, type(st_marks))

if st_marks > 40 and st_marks < 50:
    print("Passed with C grade")
elif 50 < st_marks < 60:
    print("Passed with B grade")
elif 60 < st_marks <= 70:
    print("Passed with A grade")
elif 70 < st_marks <= 80:
    print("Passed with A+ grade")
elif 80 < st_marks <= 100:
    print("Passed with A++ grade")
elif st_marks > 100:
    print("Invalid input, marks can not more than 100")
else:
    print("Failed in exam")


print("_"*50)
"""
# nested if condition
if cond1:
    code1
    if cond2:
       code2
       if cond3:
           code3
       else:
           code3
    else:
       code2
else:
    code1

"""

# write a python program to demonstrate the interview process.
round1 = "pass"
round2 = "pass"
round3 = "pass"


if round1 == "pass":
    print("congrats, 1st round is cleared.")
    if round2 == "pass":
        print("congrats, 2nd round is cleared.")
        if round3 == "pass":
            print("congrats, you are selected")
        else:
            print("Sorry, please try next time")
    else:
        print("Sorry, failed in 2nd round")

else:
    print("Sorry, failed in 1st round")


print("_"*50)
#######################################
# In operator: In operator we use for checking the value in target data type.

list1 = [5, 7, 9, 22]
val = 22

if val in list1:
    print("Value is present in the list")
else:
    print(" Value is not present in the list")


if 50 in (5, 7, 9, 50):
    print("50 is present in the tuple data")
else:
    print("This is not available")


print("_"*50)
# check given keys is not is dictionary
k1 = 'x'
dict1 = {'x': 345, 'y': 678, 'z': 111}

if k1 not in dict1:
    print("K1 is not available in dict1")
else:
    print("K1 is available in dict1")

print("_"*50)
##############################
# is operator :  is operator we use for comparison of data

v1 = False

if v1 is True:
    print("We are good to go further")
else:
    print("Value is not True")



print("_"*50)
# In below example program to will check the default value of v2 should be True
v2 = False
if v2:
    print("We are good to go further :", v2)
else:
    print("Value is not True :", v2)


print("_"*50)
# if variable holding other than boolean value
v3 = [4, 6, 7]
if v3:
    print("Variable is holding some value :", v3)
else:
    print("Variable is holding zero value :", v3)