"""
Polymorphism :  polymorphism stands for one particular person is doing multiple task.
Method Overriding : When two class are connected via inheritance and both class have method with
                    same with different parameter, and if we create object child class, then
                    child class method will override the parent class method.
                    ->  child class method will get priority.

Method Overloading : Method overloading is not possible in Python
                   ->  When one class have two method with same and different parameter, then it
                       is called method overloading, but python does not support this feature.

                   -> In python if defined two method with same name in same class, and try to access
                      the method will class object, then latest defined method will get priority

Operator Overloading :
"""

# Single Inheritance
# Base/parent class

class Father:
    def __init__(self, f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_father_name(self):
        print("Father name :", self.father_name)

    def show_father_business(self):
        print("Father business :", self.father_business)

    def show_father_car(self):
        print("Father car :", self.father_car)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

    def show_greeting(self):
        print("From Father Class : Very good morning")

class Son(Father):   # setup single inheritance between father and son class.
    """
    When we setup inheritance between 2 classes then parent class constructor has to
    initialize in the child class constructor with the help of super() keyword.

    """
    def __init__(self, s_name, f_name, f_business, f_car):
        super().__init__(f_name, f_business, f_car)
        self.son_name = s_name

    def show_son_name(self):
        print("Son name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()

    def show_greeting(self):
        print("From Son Class : Very good morning")


    def Addition(self, v1, v2):
        print(f"addition of {v1}, {v2} :", v1+v2)

    def Addition(self, n1, n2, n3):
        print(f"addition of {n1}, {n2}, {n3}:", n1+n2+n3)




obj = Son('Mohit', 'Narendra', 'Builder', 'Safari')
obj.show_family_details()

# son class method will get priority
obj.show_greeting() # From Son Class : Very good morning

# call overloaded method : latest
obj.Addition(30, 50, 60)
# addition of 30, 50, 60: 140


print("_"*50)
##################################
# operator overloading :  when operator perform multiple task, then it is called operator overloading.
#                          e.g. + plus operator.

# plus operator
n1 = 40
n2 = 50
print('Add values :', n1+n2)
print('Add values with __add__ :', n1.__add__(n2))
print(dir(int))

s1 = 'Hello'
s2 = 'Good Morning'
print("Concatenate string :", s1+s2)
print("Concatenate string with __add__:", s1.__add__(s2))
print(dir(str))


# multiplication operator : * : __mul__
# equal operator == : __eq__
# greater equal >= : __ge__
# greter operator > : __gt__
