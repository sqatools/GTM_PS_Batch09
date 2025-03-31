# writa a program to check if person age is ready to vote or not

age = int(input("Enter the age of the person :"))

if age<18:
    print("Person is less than 18 years and cannot vote", age)
elif age>=18 and age<=100:
    print("Age is greater than or equal to 18 and is eligible to vote:", age)
else:
    print("please enter valid age")




