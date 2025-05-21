import random
list1 = [5, 7, 9, 10, 23]
# get random value from list of values
val1 = random.choices(list1)
print(val1)

# shuffle list values and modify the original list
random.shuffle(list1)
print("shuffle result :",list1)
# [10, 7, 5, 9, 23]

# get random int value from given range
val2 = random.randint(1, 20)
print("random number :", val2) # 14

# random with specific range and difference
val3 = random.randrange(1, 10, 2)
print(val3) # 5