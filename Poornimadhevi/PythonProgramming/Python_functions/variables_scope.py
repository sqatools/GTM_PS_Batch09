"""
local variable :  The variable that we declare inside of the function, then it is called local variable.
                ->  scope of local variable is limited to function only.

global variable : The variable that we declare outside of the function, then it is called global variable.
                  ->  global variable is globally available for the functions.
non local variable :  when defined variable inside the outer function and then it become nonlocal variable for
                      all the inner function. nonlocal variable is not accessible outside of the outer function.


Notes:  If we want to change the value of global and nonlocal variable inside the function, then we have use
        global and nonlocal keyword explicitly.
"""
# global variable
var_p = 500

def function1():
    print("________________Function1____________________")
    global var_p
    var_p = 1500
    var_q = 300  # local variable
    print("local variable var_q :", var_q)
    print("global variable var_p :", var_p)


def function2():
    print("________________Function2____________________")
    var_r = 200  # local variable
    print("local variable var_r :", var_r)
    print("global variable var_p :", var_p)


function1()
print("_"*50)
function2()



var_x = 1000 # global
def outer_function():
    var_y = 900  #non local variable
    print(var_y)

    def inner_fun1():
        print("______innerfun1______")
        nonlocal var_y
        var_z = 800 # local variable
        var_y = 200
        print("global variable var_x:", var_x)
        print("nonlocal variable var_y:", var_y)
        print("local variable var_z:", var_z)


    def inner_fun2():
        print("______innerfun2______")
        var_w = 700 # local variable
        print("global variable var_x:", var_x)
        print("nonlocal variable var_y:", var_y)
        print("local variable var_w:", var_w)


    inner_fun1()
    inner_fun2()

#outer_function()
#print(var_y)
