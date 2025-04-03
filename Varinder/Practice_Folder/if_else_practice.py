# user input

# num = input("enter your value :-")
# if int(num) >= 10:
#     print(" this is true value",num)
# else:
#     print("this value is less then 10")

######################################

# age = int(input("enetr the age:- "))
# if age >= 30:
#     print("you can drive safely!")
# elif age == 30:
#     print("you can Drive but, focus on the Rode ")
# else:
#     print("you are too young to drive")
###############################################
#write a python program to check given is ready to vote or not

# vote_age = 50
#
# if vote_age >= 20:
#     print("you are eligible to vote")
# else:
#     print("Not eligibale you are under age")
# ##############################################
# # check given is even or odd
#
# num = 19
#
# if num%2 == 0:
#     print(" This is even number :-", num)
# else:
#     print("this is odd value :-")

##################################################
"""
# Other operators
> :  greater than
< :  less than
>= :  greater than equal
<= : less than equal
== :  equal to
!= : not equal to
in :  operator
is : operator
not : not operator
"""
######################################################
# write a python program to find the greater number among three values
age1 = 20
age2 = 30
age3 = 10

if age1 <= age2 and age1 > age3:
    print("you are adult ")
elif age2 < age3 and age1 > age3:
    print("you are Teenager ")
elif age2 > age1 and age3 < age1:
    print("this is true ")
else:
    print("you are taldor ")
#######################################################
# nested if condition

#write a python program to demostrade the interview process.

first_interview = "try again"
seconed_interview = "pass"
third_interview = "not passed "
forth_interview = "pass"

if first_interview == "not passed":
    print("prepare for next interview ")
    if seconed_interview == "pass":
        print("you cleared your interview")
        if third_interview == "not passe":
            print("Sorry try again")
elif seconed_interview ==  forth_interview:
    print("congratulations! you got selected ")
else:
    print("we will contact you soon")










