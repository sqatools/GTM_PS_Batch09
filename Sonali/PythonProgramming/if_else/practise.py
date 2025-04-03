user=int(input("enter the age:"))
if user>=18:
    print("Ready to do voting")
else:
    print("Not ready for voting")




item1=345
item2=500
item3=600
Tbill=item1+item2+item3
print(Tbill)
if Tbill>1000:
    discount=Tbill*(20/100)
    final_bill=Tbill-discount
    print("amount to be given:",final_bill)
else:
    print("no discount")


n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
input=input("enter input of your choice:")
if input=="+":
    print("addition is:",n1+n2)
elif input=="-":
    print("substraction is:",n1-n2)
elif input=="*":
    print("multiplication is:",n1*n2)
elif input=="/":
    print("division id:",n1/n2)
else:
    print("invalid number")