from datetime import datetime,timedelta
print("Current Date:",datetime.now())
# Current Date: 2025-05-07 13:50:40.263547

print("current date", datetime.now().date()) #current date 2025-05-07
print("current day", datetime.now().day) #current day 7
print("current month", datetime.now().month) # current month 5
print("current year", datetime.now().year) # current year 2025

print("current day name", datetime.now().strftime("%A")) #current day name Wednesday

# regenerate a dynamic name with current date and time.
result = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
# %d :  get today's day
# %m :  get current month
# %y or %Y : 25 or 2025
# %H :  Hours
# %M : Minutes
# %S : seconds
print("new name :", result)
#new name : 07_05_2025_13_52_41

# date before 2 days
last_2_date = datetime.now() - timedelta(2)
print("date before 2 days:", last_2_date)
#date before 2 days: 2025-05-05 13:52:41.486208

# date after 2 days
date_after_2days = datetime.now() + timedelta(2)
print("date after 2 days :", date_after_2days)
#date after 2 days : 2025-05-09 13:52:41.486504