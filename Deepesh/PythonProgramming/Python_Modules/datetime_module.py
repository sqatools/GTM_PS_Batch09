from datetime import datetime, timedelta

print("current date :", datetime.now())
#  2025-05-05 20:40:49.851047

print("current date", datetime.now().date()) # 2025-05-05
print("current day", datetime.now().day) # 5
print("current month", datetime.now().month) # 5
print("current year", datetime.now().year) # 2025

print("current day name", datetime.now().strftime("%A")) # Monday

# regenerate a dynamic name with current date and time.
result = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
# %d :  get today's day
# %m :  get current month
# %y or %Y : 25 or 2025
# %H :  Hours
# %M : Minutes
# %S : seconds
print("new name :", result) # 05_05_2025_20_48_02


# date before 2 days
last_2_date = datetime.now() - timedelta(2)
print("date before 2 days:", last_2_date)   # 2025-05-03 20:52:54.305030


# date after 2 days
date_after_2days = datetime.now() + timedelta(2)
print("date after 2 days :", date_after_2days)  # 2025-05-07 20:54:31.391389
