
#write a python function to get factorial any given number with return statement
def fact(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print(fact)
n=int(input("enter number:"))
fact(n)

#write a python function to get list of all the prime number from 1 to 100
n1=int(input("enter starting value:"))
n2=int(input("enter ending value:"))
def prime(n1,n2):
    for num in range(n1,n2+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
                else:
                    print(num)

prime(1,100)





