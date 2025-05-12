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
obj=School('Orchid','Banglore')
obj.school_Name()
obj.school_Address()

#NOTE:   method name and varibale name should be different otherwise it will through error



