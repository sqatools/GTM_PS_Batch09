#function is of 3 types
# without parameter
# passing value by parameter
# passing value by reference

#without parameter
def fun1():   #def is the keyword defining the function
    print("good morning") #good morning is the value printed which will be called while fun1() will be called
fun1()        #calling function......... here howmany times u call the function that much time it will print the value

print("*"*60)
#passing value by parameter
def fun2(msg): #msg is any random name we need to pass as a parameter
    print(msg)
fun2("good morning")  #while calling function whatever parameter will pass that will print at end

print("*"*60)
#passing value as reference

def fun3(n1):
    print("n1:",n1)
fun3(90)

def fun4(n1,n2):
    print("add is",n1+n2)
fun4(20,30) #by default the values are taken in the sequential format means 1st position is n1 and 2nd position is n2

def fun5(n1,n2,n3):
    print(n1,n2,n3)
fun5(n2=200,n1=90,n3=400) # if you want to change the sequence then you have to mention both ref and value


#whatever functions we are defining here that we can call at any time and multiple times

list1=[30,40,50]
v1=sum(list1)
print("return value:", v1)

def fun7(n1,n2=9):
    print(n1,n2)
fun7(5) #bydefault it will aasign to n1

fun7(200,300) #this value will ovverride




#return value

def find_max_value(l1):
    max_val=0
    for val in l1:
        if val>max_val:
            max_val=val
        else:
            continue
    return max_val
result=find_max_value([2,3,4,5,6,7,8,9])
print(result)

#math_operation
def math_operation(n1,n2):
    add=n1+n2
    mul=n1*n2
    div=n1//n2
    sub=n1-n2
    return add,sub,mul,div
output=math_operation(30,40)
print(output)

#sum of number from 1 to 100
def print_sum_num(num):

    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
res1=print_sum_num(50)
print(res1)


#*args
#differenece between parameter and *args value is
#one parameter represents 1 value
#one *args represents multiple values


def print_val(*args): # args will accept multiple values
    print(args,type(args))
print_val(20,3,56 )

#**kwargs ---------it will accpet the value in dictionary format and store in the dictionary format(key and value format


def new_val(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k ,":" ,v)

new_val (name='Rahul', surname='Gupta', email='rahul@gmail.com', phone=4545435455)







