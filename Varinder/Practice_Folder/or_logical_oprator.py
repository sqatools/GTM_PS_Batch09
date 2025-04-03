# OR Logical operator:
# cond1 or cond2 if one condition is true
#
# True or True :  True
# False or True :  True
# True or False :  True
# False or False :  False

sim = 20

if sim%2 == 0 or sim%3 == 0:
    print("This will print because it is true value ", sim)
else:
    print("not true, so it won't print", sim)

#######################################################
# both false

sim2 = 20
if sim2%4 == 0 or sim2%5 == 0:
    print(" this will print it true one ", sim2)
else:
    print("this wont print because first value match", sim2)