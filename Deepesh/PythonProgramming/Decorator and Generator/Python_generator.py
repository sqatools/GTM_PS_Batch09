# generator :  generator help us to manage the memory and load one value at a time in the memory..

def get_values(num):
    for i in range(num):
        print(i)
        if i == 5:
            return i**2
        elif i == 6:
             return i**3

result = get_values(100)
print("result :", result)

print("_"*50)
def greeting():
    return  "Good Morning"
    return  "Good Evening"
    return  "Hope you are good"

r1 = greeting()
print(r1)

r2 = greeting()
print(r2)

r3 = greeting()
print(r3)


print("_"*50)
def greeting_gen():
    yield "Good morning"
    yield "Good Evening"
    yield "Have a nice day"

data = greeting_gen()
# print(data)  # generator object greeting_gen at 0x000001FD22064880
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))

# get generator value with the help of loop.
for val in data:
    print(val)
