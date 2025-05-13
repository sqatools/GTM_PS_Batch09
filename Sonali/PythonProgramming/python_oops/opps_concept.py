# create a class for school institute with school_name and school_Address as parameter

class School:
    def __init__(self,name,address):
        print("-----------welcome to school------------")
        self.schoolname=name
        self.schooladdress=address
    def school_Name(self):
        print("school name is :", self.schoolname)
    def school_Address(self):
        print("school adress is :", self.schooladdress)
#obj=School('Orchid','Banglore')
#obj.school_Name()
#obj.school_Address()

#NOTE:   method name and varibale name should be different otherwise it will through error


#Description of a code

class car:     #car is a class
    country_origine="INDIA"       #class varibale
    def __init__(self,company_name,car_price):   #constructer with parameter
        print("**********welcome to car world*******")
        self.company1_name=company_name
        self.car_price1=car_price
#here when you define any constructor, the parameter what we pass for that varibale need to defineinside constructor
#for the variable defined inside constructor need to define the method.but method name variable name should not be same

#different types of method
    def show_company(self):                               #instance method
        print("company name is:",self.company1_name)
    def show_price(self):
        print("company price is:",self.car_price1)
    def car_name(self ,name):
        print("car name is:",name )
#method inside method
    def show_car_details(self):
        self.show_price()        #instance method calling with self object
        self.show_car_country_name() #cllass method calling with self object
        self.show_adress("mysore")            #static method calling with self object
        print(self.country_origine)    #class varibale calling with self object



    @classmethod    #class method will define here
    def show_car_country_name(cls):      #as class method defined so cls will come automatically
        print("car country name:",cls.country_origine)  #class method will access class variable , it canot acess instance variable

    @staticmethod  #static method doesnot have any parameter, like a normal function we can call it
    def show_adress(address):
        print("adress is:",address)



ob1=car("car","20lkh")  #pass parameter to class name so that it will directly pass to the constructor
ob1.show_company()      #company name
ob1.show_price()        #instance method can be called using object
car.show_price(ob1)     #instance method can be called by using class name and as passing object as parameter
ob1.car_name("maruti")  #car name it will show
ob1.show_car_country_name() #classmethod can be called by using object as well as class name
car.show_car_country_name()
ob1.show_adress("bengaluru")
print("*"*50)
ob1.show_car_details()

