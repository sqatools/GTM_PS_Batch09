# exception handling : through exception handling we can handle programming/user specific errors with
#  the help custom messages and does not fail the program.

def create_exception_handling():
    try:
        var1 = 45
        var2 = 300
        add = var1 + var2
        print("Adding value :", add)
    except Exception as e:
        print(e)
        print("Addition of the number and string is not allowed")

#create_exception_handling()
#print("Good Morning")


# raise the exception as per our requirement.
def raise_exception_handling():
    try:
        var1 = 45
        var2 = '50'
        add = var1 + var2
        print("Adding value :", add)
    except Exception as e:
        print("Addition of the number and string is not allowed")
        raise e

# create_exception_handling()
# print("Good Morning")
# raise_exception_handling()
# print("Good Morning")


print("_"*50)
################################################
# try-except-else condition :
# else condition only executes, when there is no exception in the program.


def try_except_else_handling(v1, v2):
    try:
        var1 = v1
        var2 = v2
        add = var1 + var2
        print("Adding value :", add)
    except Exception as e:
        print(e)
        print("Addition of the number and string is not allowed")
    else:
        # else section only executes, when there is no exception
        print("Code executed successfully")

#try_except_else_handling(40, 100) #  else condition will execute
#try_except_else_handling(40, 'Hello') # else condition will not execute with exception.



print("_"*50)
################################################
# try-except-else-finally condition : finally section will execute always even there is exception or
# no exception in the code.

def try_except_else_finally_handling(v1, v2, v3):
    try:
        var1 = v1
        var2 = v2
        add = var1 + var2
        print("Adding value :", add)
    except Exception as e:
        print(e)
        print("Addition of the number and string is not allowed")
    else:
        # else section only executes, when there is no exception
        print("Code executed successfully")

    finally:
        # Finally section will execute the code even there is exception or no exception.
        fact = 1
        for i in range(v3, 0, -1):
            fact = fact*i

        print("Factorial value :", fact)

# execute code without exception
#try_except_else_finally_handling(20, 50, 6)
"""
Adding value : 70
Code executed successfully
Factorial value : 720
"""

# execute code with exception
try_except_else_finally_handling(20, 's', 6)
"""
unsupported operand type(s) for +: 'int' and 'str'
Addition of the number and string is not allowed
Factorial value : 720
"""
