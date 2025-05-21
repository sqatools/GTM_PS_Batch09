#variables are 3 typres
'''
1.local varibales : (defined inside function)(inner function also we can say)
                    scope of this local varibale is limited within function
2.Nonlocal varibales:(defined inside outer funtion outside for inner function)
                     scope of this varibale is within outer function and inner function.
                     not accesable by outside of the outer function
3.Global function  :  (defined outside of functions)
                      globally available for all the functions

#here inner function and outer function means when we defined function inside function(function loop can say))

'''

var_g=100 #global variable
def function1():
    print("-------------------Function1---------------------")
    var_nl=200   #nonlocal variables
  #  print(var_l)   it will not acess as local variable by outside function
    print(var_nl)
    print(var_g)
    def function2():
        print("--------------------function2---------------------")
        var_l=500
        print(var_l)
        print(var_nl)
        print(var_g)
    function2()
function1()

# inside function if you change the v aribal evalue it will take that new value while calling the function