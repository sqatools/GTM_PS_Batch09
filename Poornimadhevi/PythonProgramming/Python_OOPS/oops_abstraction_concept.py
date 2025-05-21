"""
Abstraction :  When user provide the overview information of the application and hiding the
               internal architecture of the code, then it is called abstraction.

->  Abstraction can be achieved in OOPs when we defined method in parent class and impliment the
   method in child class, this is called abstract method.

->  The class contains the abstract method, then it is called abstract class.


"""

from abc import abstractmethod

class Animal:

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def breed(self):
        pass

    @abstractmethod
    def location(self):
        pass

class Lion(Animal):
    def name(self):
        print('Name of lion : African Lion')

    def voice(self):
        print("Roar")

    def breed(self):
        print("White Lion")

    def location(self):
        print("Africa Forest")


class Dog(Animal):
    def name(self):
        print('Tommy')

    def voice(self):
        print("Bark")

    def breed(self):
        print("German Shepherd")

    def location(self):
        print("USA")


obj1 = Lion()
obj1.name()

obj2 = Dog()
obj2.name()
