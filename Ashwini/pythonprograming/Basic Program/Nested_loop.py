for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")

    print()

print("-" * 50)

for x in range(0, 5):
    for y in range(0, 5 - x):
        print(' * ', end='')

    print('')

print("-" * 50)