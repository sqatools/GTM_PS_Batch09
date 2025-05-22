from pip._internal.metadata import importlib

importlib

"""
class : class is the blueprint of the object, where we defined all properties/attribute/parameter
        and functionality of the object.

object : Object is a physical entity, through which we can access all the feature function defined in
         the class.
method :  When define any function inside the class, then it became method.
          ->  instance method :  Anymethod with self as first parameter,
                                then it is called instance method.
                                ->  instance method we call with object of the class
                                ->  we can not call
          ->  class method : class method on deals with class variable.
                             -> we define the class method with the decorator @classmethod.
                             -> we can call the class method with class name
                             ->  we can call the class method with class object

          ->  static method :  static method is the normal function without any default parameter
                              ->  To call the static method, no need to create object of the class.
                              ->  static method, does not deal with any of the class variable or instance variable
                              ->  static method define with decorator @staticmethod

variables : When we defined any variable inside the class then it is called member variable.
            1. instance variable :  when we initialize any variable with self keyword, then
               it is called instance variable
               ->  instance are accessible across the class.

            2. class variable :  when we defined variable outside of the method and inside the class
                              then it is called class variable
               ->  we have to provide default value to the class variable

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

#### What is self ? #######
self is nothing but the object of the current class is being created.


"""


# Class
class Car:
    car_country = 'India'  # class variable
    # constructor/parametrize


def __init__(self, comp_name, car_price):
    print("Welcome to the car company")
    self.company_name = comp_name  # instance variable
    self.Car_Price = car_price  # instance Variable


def show_car_name(self, name):  # instance Method
    print("car name is ", name)


def show_company_name(self):  # instance Method
    print("Car Company name : ", self.company_name)


def show_car_price(self):  # instance Method
    print("Car Price : ", self.Car_Price)


def show_car_details(self):
    self.show_company_name()
    # # access class variable inside the instance method with self.
    # print("car country :", self.car_country)
    # we can access class method with self
    self.show_car_country_name()
    self.show_car_price()


@classmethod
def show_car_country_name(cls):
    """
    ->  class method only deal with class variable with cls
    ->  Can not access instance variable inside the class method
    ->  class method, directly connect with class name.
    ->  we can access class method with class as well.
    ->  we can access class method with object of the class

    :return:
    """
    print(f"Car Country Name : {cls.car_country}")


@staticmethod
def show_company_showroom_address(address):
    print("showroom address : ", address)

# create object
# while creating the object of the class, we have to provide value for constructor parameter.
#obj = Car('TATA', '20Lac')

obj.show_company_name()
obj.show_car_price()
#obj.show_car_name('Avinya Car')

print(obj.company_name) # TATA

