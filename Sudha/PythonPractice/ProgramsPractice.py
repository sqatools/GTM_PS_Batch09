#Q1 write a python program to check given is ready to vote or not.
"""
age = int(input("Please enter the age = "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")
    """

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

"""
item1 = int(input("Enter Price of item 1 = "))
item2 = int(input("Enter Price of item 2 = "))
item3 = int(input("Enter Price of item 3 = "))
total = item1+item2+item3
if total > 1000:
    discount = total*(20/100)
    total_amount = total - discount
    print("Total Amount = ", total_amount)
else:
    print("Total Amount = ", total)
"""

num1 = int(input("Enter number 1 = "))
num2 = int(input("Enter number 2 = "))
operator = input("Please enter the operator to perform = ")
if operator == "*":
    print(num1*num2)
elif operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)





