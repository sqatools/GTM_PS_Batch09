#write down the logic inside try block

# try.............except..... block
def try_except_exception():
    try:
        v1=5
        v2='6'
        addition=v1+v2
        print(addition)
    except Exception as e:
        print(e)
        print("numbers can not be added as not same data type")

#try_except_exception()
print("*"*90)

#raise................. block
#here raise will stop further execution .. so what ever u want to execute that need to write before calling that raise function
#we have to cretae according to our wish, where we know the further execution is not possible
#for example whatsapp or face book where without login we can not use that app. login id and password is not correct then that will trough exception.
#there we can use Raise exception
def raise_exception():
    try:
        v1=7
        v2='hello'
        print("addition is:",v1+v2)
    except Exception as e:
        print("numbers can not be added for different data type")
        raise e
#print("good morning")
#try_except_exception()
#raise_exception()

#try_except_else() method
#error will handel by try except and else part will execute if there is no exception

def try_except_else(v5,v6):
    try:
        var1=v5
        var2=v6
        print("addition:",var1+var2)
    except Exception as e:
        print(e)
        print("2 different data type cannot be added")
    else:
        print("code addition is succesful")
#try_except_else(4,'hello')
#try_except_else(4,6)

#finally() method----------where whatever issue ,if exception is there or not finally will be excecuted

# for example -cleaning of memory or data mostly we use.
#even if exception is there or not cleaning is mandetory, so in finally: block we mostly use the cleaning activity

def try_except_else_finally(v51,v61,v3):
    try:
        var1 = v51
        var2 = v61
        print("addition:", var1 + var2)
    except Exception as e:
        print(e)
        print("2 different data type cannot be added")
    else:
        print("code addition is succesful")
    finally:
        for i in range(v3):
            print(i)
#try_except_else_finally(2,3,6)
#try_except_else_finally(2,'hello',6)

print("_"*50)
################################################
# multiple exception handling:
#within try block write down all the codes like multiple codes, that exception will be handeled by next exception statements

def multiple_exception_handeling(v1,v2,v3):
    try:
        add=v1+v2
        print("addition is:",add)
        div=v1//v3
        print("mul is :",div)
        assert v1+v2==v3
    except TypeError:
        print("addition of the string is not allowed")
    except ZeroDivisionError:
        print("division by zero is not allowed")
    except AssertionError:
        print("addition of value is not equal to 3rd value")
    except Exception as e:
        raise e
#multiple_exception_handeling(2,80,5)
#multiple_exception_handeling(2,80,"hello")

#nested level exception_handeling

#outer exception handeling and inner exception handelling will be there
#try inside try except then outer except will be there

def nested_exception_handeling(n1,n2,n3):
    #outer exception
    try:
        add=n1+n2
        print(add)
        try:
            div=n2//n3
            print(div)
        except Exception as f:
            print(f)
            print("division can not be done to zero ")
    except Exception as e:
        print(e)
        print("addition of different data type is not required")

#nested_exception_handeling(2,5)
#nested_exception_handeling(2,4,0)












