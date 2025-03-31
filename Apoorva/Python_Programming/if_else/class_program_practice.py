# writa a program to check if person age is ready to vote or not

"""age = int(input("Enter the age of the person :"))

if age<18:
    print("Person is less than 18 years and cannot vote", age)
elif age>=18 and age<=100:
    print("Age is greater than or equal to 18 and is eligible to vote:", age)
else:
    print("please enter valid age")
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

item1_cost = int(input("please enter item1 cost:"))
item2_cost = int(input("please enter item2 cost:"))
item3_cost = int(input("please enter item3 cost:"))

sum = (item1_cost + item2_cost + item3_cost)
print("sum is:" ,sum)

if sum >= 1000:
    discount = sum * (20/100)
    total = sum - discount
    print("total after discount is:", total)
else:
    total = sum
    print( "total without discount is:" , total )


#Q3: write a python to create calculator
"""
->  Accept three values 1 for operation 2 for calculation.
"""

value1 = int(input("please enter value1 :"))
value2 = int(input("please enter value2 :"))
value3 = int(input("please enter value3 :"))

