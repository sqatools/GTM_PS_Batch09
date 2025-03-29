n=int(input("enter the value :"))
if n%3 == 0:
    print("n devisible by 3:",n)
else:
    print("n is not devisible by 3")

print("-"*50)
for i in range(1,31):
    if i % 3 == 0:
        print(i)
print("-"*50)

mark=int(input("enter the mark:"))
if mark < 40:
    print("FAIL")
elif 40<= mark <= 50:
    print("c grade")
elif 50<mark<=60:
    print("grade B")
elif 60<mark<=70:
    print("grade A")
elif 70<mark<=80:
    print("grade A+")
elif 80<mark<=90:
    print("grade is A++")
elif 90<mark<=100:
    print("EXCELLENT")
elif mark>100:
    print("INVALID")



num=int(input("enter number"))
if num%3==0 and num%5==0:
    print("number is ok")
else:
    print("not a good number")


num1=int(input("enter number"))
if num1%11==0:
    num2=num1**2
    print(num2)
else:
    print("num is not devided by 11")

num4=int(input("enter number"))
for i in range(2,)


