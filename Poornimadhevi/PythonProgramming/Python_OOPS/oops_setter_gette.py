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

# setter and getter help to assign new value the class parameter and print its value.
obj = Father('Mr. Rohan', 'Transport', 'Audi')

print("Father Name :", obj.__getattribute__('father_name'))

# set value to parameter
obj.__setattr__('father_car', 'Fortuner')

print("Father car :", obj.father_car)
