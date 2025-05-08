"""
class : class is the blueprint of the object, where we defined all properties/attribute/parameter
        and functionality of the object.

object : Object is a physical entity, through which we can access all the feature function defined in
         the class.
method :  When define any function inside the class, then it became method.

variables : When we defined any variable inside the class then it is called member variable.
            1. instance variable :  when we initialize any variable with self keyword, then
               it is called instance variable
               ->  instance are accessible across the class.

constructor : constructor initialize the memory for object of the class.
              1.  default constructor: This constructor with can define with inbuilt name __init__
                  and constructor call automatically whenever we create object of the class

                  def __init__():
                      code

              2.  parametrize constructor: When we pass parameters to the constructor, then it become
                                           parametrize constructor.
                  ->  we have to provide value for constructor parameter during the creation of class
                      object.

                def __init__(var1, var2):
                   self.v1 = var1
                   self.v2 = var2


"""

# class
class Car:

    # constructor/parametrize
    def __init__(self, comp_name):
        print("---- Welcome to Car company ----")
        # instance variable
        self.company_name = comp_name

    # method
    def show_car_name(self, name):
        print("Car name is :", name)

    def show_company_name(self):
        print("Car company name :", self.company_name)


# create object
obj = Car('TATA')
obj.show_company_name()
obj.show_car_name('Avinya Car')


# HW
# create a class for school institute with school_name and school_Address as parameter.

