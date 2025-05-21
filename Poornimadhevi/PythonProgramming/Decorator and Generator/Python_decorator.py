# decorator is external code that enhance the exiting functionali of feature without changing exiting code.

def FunDecorate(func):
    def inner(*args):
        print("*"*50)
        func(*args)
        print("*"*50)
    return inner

@FunDecorate
def greeting(msg):
    print(msg)


#greeting("Good Morning")


@FunDecorate
def addition(n1, n2, n3):
    print("addition of values :", n1+n2+n3)

addition(20, 30, 40)
