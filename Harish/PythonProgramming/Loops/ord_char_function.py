#ord
#chr
#ASCII
#Capital Letters: 65-90
#Small Letter: 97-122
from Deepesh.PythonProgramming.PythonLoops.Python_loops_concept import count

print(ord("A"))

print(chr(97))

"""
A
B C
D E F
G H I J
K L M N O
"""
count=65
for i in range(1,6):
    for j in range(1, i+1):
        print(chr(count), eng="'")
        count+=1
    else:
        print(" ", end="")
    print()














