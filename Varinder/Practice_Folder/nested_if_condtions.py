#write a python program to demostrade the interview process

first_interview = "10:00 am"
second_interview = "10:00 am"
third_interview = "11:00 am"

if first_interview == second_interview:
    print("congratulations you cleared your interview!")
    if second_interview != third_interview:
        print("your second interview is at 10:00 am")
        if third_interview == first_interview:
            print("your interview is at 11:00 am")
        else:
            print("we will schedule another interview round")
    else:
        print("schedule your interview at different time")
else:
    print("get ready for first interview")




