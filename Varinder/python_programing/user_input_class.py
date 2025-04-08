#write a program to provide grade to students as marks received.
#multiple elif conditions

grade = int(input("Enter Your Grade Here :-"))
#grade = 50
if grade == 70:
    print("Retake your test")
elif grade < 70:
    print("you failed your test")
elif grade > 80:
    print(" greate job you passed your test ")
else:
    print("you need to focus on study")
