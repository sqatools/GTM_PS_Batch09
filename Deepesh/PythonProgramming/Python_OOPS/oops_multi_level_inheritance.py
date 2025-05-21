"""
When one class the aquire the property of another class, then it is called inheritance.
1. Single Inheritance :  class A (Father) ->  Class B (Son)
2. Multi level inheritance : Class A (GrandFather) -> Class B (Father) -> Class C (Son)
3. Multiple Inheritance :  Class A (Father) ->  Class B (Son),  Class C (Mother) ->  Class B (Son)
4. Hierarchical Inheritance : Class A (Father) -> Class B (Son1),
                              Class A (Father) -> Class C (Son2)
"""

# multilevel Inheritance
# Base/parent class

class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.grand_father_name = gf_name
        self.grand_father_property = gf_property

    def show_grand_father_details(self):
        print("Grand Father Name :", self.grand_father_name)
        print("Grand Father Property :", self.grand_father_property)

class Father(GrandFather):
    def __init__(self, f_name, f_business, f_car, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
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

class Son(Father):   # setup single inheritance between father and son class.
    """
    When we setup inheritance between 2 classes then parent class constructor has to
    initialize in the child class constructor with the help of super() keyword.

    """
    def __init__(self, s_name, f_name, f_business, f_car, gf_name, gf_property):
        super().__init__(f_name, f_business, f_car, gf_name, gf_property)
        self.son_name = s_name

    def show_son_name(self):
        print("Son name :", self.son_name)

    def show_family_details(self):
        self.show_grand_father_details()
        self.show_father_details()
        self.show_son_name()



obj = Son('Mohit', 'Narendra', 'Builder', 'Audi', 'Ram Dayal', '200Acr')
obj.show_family_details()




# obj1= Father()
# obj1.show_father_details()
