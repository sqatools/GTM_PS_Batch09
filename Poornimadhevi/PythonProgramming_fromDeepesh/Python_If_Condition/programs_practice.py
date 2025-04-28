"""

user_input = input("Please enter value :")
if int(user_input) >= 0:
    print("This is positive number")
else:
    print("Invalid input")
"""

#Q1 write a python program to check given is ready to vote or not.

#Q2 write a python program to calculate the bill amount and provide 20% discount to user if bill
# amount is greater than 1000
"""
customer purchase 3 items.
we have to provide price of 3 items and calculate bill by adding three prices.
if total bill is greater than 1000, then provide 20% discount
total bill would be -20%
discount = total_bi*(20/100)
total_bill = total_bill - discount
"""

#Q3: write a python to create calculator
"""
->  Accept three values 1 value for operation 2 values for calculation.
val1 = input()
val2 = int(input()) # number
val3 = int(input()) # number
if input is + and add 2 values
if input is * then multiply the values
if input is / then devide values
if input is - then subtract the values
"""


n1 = 6
fact = 1

for i in range(6, 0, -1):
    print(i) # 5, 4, 3, 2, 1
    fact = fact*i # 5*1 =5, 5*4=20, 20*3 = 60, 60*2=120, 120*1 = 120

print("factorials of :",n1,":", fact)

# factorials of : 6 : 720