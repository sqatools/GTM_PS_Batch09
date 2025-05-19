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
#raise_exception_handling()
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
#try_except_else_finally_handling(20, 's', 6)
"""
unsupported operand type(s) for +: 'int' and 'str'
Addition of the number and string is not allowed
Factorial value : 720
"""

print("_"*50)
################################################
# multiple exception handling:


def try_except_multiple_exception_handling(v1, v2, v3):
    try:

        add = v1 + v2
        print("Adding value :", add)

        divide = v1//v3
        print("divide value :", divide)

        assert v1+v2 == v3
    except TypeError:
        print("Addition of string and int is not allowed")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except AssertionError:
        print("addition of value are not equal to third value")
    except Exception as e:
        raise e


#try_except_multiple_exception_handling(20, 30 , 70)


def nested_level_exception(n1, n2, n3):
    # Outer exception handling
    try:
        add = n1+n2
        print("addition :", add)
        # Inner exception handling
        try :
            divide = n2//n3
            print("division output :", divide)

        except Exception as f:
            print(f)
            print("Inner exception :Can not divide number with zero")

    except Exception as e:
        print(e)
        print("Outer exception : both the values should be integer")

# code without exception
# nested_level_exception(30,20,2)
"""
addition : 50
division output : 10
"""

# code outer exception
nested_level_exception(30,'Hello',2)
"""
unsupported operand type(s) for +: 'int' and 'str'
Outer exception : both the values should be integer
"""


# inner outer exception
nested_level_exception(30,10,0)
"""
addition : 40
integer division or modulo by zero
Inner exception :Can not divide number with zero
"""

print("_"*50)
#####################################
# create custom exception class and use it is program.

class MyCustomException(Exception):
    """
        Exception raise with custom exception class
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def use_custom_exception():
    for i in range(12):
        if i> 10:
            raise MyCustomException("More than 10 values are not allowed")
        else:
            print(i)


###########################################################
#use_custom_exception()
def use_custom_exception_with_try_except(num1, num2):
    try:
        value = num1+num2
        print(value)
    except:
        raise MyCustomException('Not a valid values')


#use_custom_exception_with_try_except(10, 30)
use_custom_exception_with_try_except(10, 'Hello')
