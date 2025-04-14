"""# get if condition output in one single line
# write a program to print square of value if it is even else print cube of the value
p = 6
result = p**2 if p%2 ==0 else p**3
print("result :", result) # result : 36

print(p**2 if p%2 ==0 else p**3)  # 36 , printing if condition in single line
"""

# write a python program to check the given number is divisible by 3 and 5

"""num1 = 16

if num1%3 ==0 and num1%5 ==0:
    print("num1 is divisible by both 3 and 5:", num1)
else:
    print("num1 is not divisible by both:", num1)
"""

print("_"*50)

"""# write a python program to check the given number is divisible by 3 or 5
y = int(input("Enter number:"))

if y%3 == 0 or y%5 == 0:
    print("The number is divisible by 3 or 5 :", y)
else:
    print("The number is not divisible by 3 or 5:", y)

    print("_" * 50)
"""
############################ if-elif-else ################################
"""
marks= int(input("Please enter marks:"))

if  30<=marks<=40:
    print("Grade D")
elif 40<marks<=50:
    print("Grade C")
elif 50<marks<=60:
    print("Grade B")
elif 60<marks<=70:
    print("Grade A")
elif marks>70 and marks<=100:
    print("Distinction")
elif marks>100:
    print("Please provide valid marks <=100")
elif marks<30:
    print("Fail")


print("_"*50)
"""

############################ nested-if ################################

# write a python program to demonstrate the interview process.

round1 = "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("Round one: cleared")
    if round2 == "pass":
        print("round two : cleared")
        if round3 == "pass":
            print("You are selected: congrats")
        else:
            print("Sorry, Try after 6 months")
    else:
        print("round two : failed")
else:
    print("Round one: Failed")

a = 'hello'
print(a,type(a))


import json
a = '{"name" : "apoorva", "mobile": 8296936484}'
print(a, type(a))

dict4 = json.loads(a)
print(dict4,type(dict4))





