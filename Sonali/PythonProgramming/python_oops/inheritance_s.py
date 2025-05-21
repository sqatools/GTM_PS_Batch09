#inheritance is of 4 types
#when one class aquires the properties of the other class
"""
1.single inheritance: class A-->class B......................here class B will access all the properties of class A.
2.multilevel inheritance:classA-->class B-->class C---------here class B will acess the properties of class A and class c will acess properties of both A and B
3.multiple inheritance:--> class A-->class B , class C-->class B.........here class A and class C have no links but class B will get the properties of both
4.Hierarchical Inheritance:-->
"""

#single inheritance

class Father:
    def __init__(self,f_name,f_add,f_business):
        self.father_name=f_name
        self.father_address=f_add
        self.father_business=f_business

    def show_father_details(self):
        print("father name is:",self.father_name)
        print("father address is:",self.father_address)
        print("father business is:",self.father_business)

class son(Father):
    def __init__(self, s_name, f_name, f_add, f_business):
        super().__init__(f_name, f_add, f_business)
        self.son_name=s_name

    def show_son_details(self):
        self.show_father_details()
        print("son name is:",self.son_name)

obj1=son('mohit','narendra','banglore','teacher')
obj1.show_son_details()

