"""
Data hiding or Encapsulation can be achieved with single underscore and double under as prefix
in the variable and method name.


"""

class School:
    school_name = 'Emerald International School'
    _school_address = 'Mumbai Boriwali'
    __school_principle = 'Mr Jagan Mohan'

    def __init__(self, fee, board, branch_no):
        self.sch_fee = fee
        self._school_board = board
        self.__school_branch = branch_no

    def show_school_name_fee(self):
        print("School Name :", self.school_name)
        print("School Fee :", self.sch_fee)

    def _show_school_board_address(self):
        print("School board :", self._school_board)
        print("School Address :", self._school_address)

    def __show_school_branch_and_principle(self):
        print("School Principle :", self.__school_principle)
        print("School Branch :", self.__school_branch)


obj = School('2 Lac', 'CBSC', 2345)

# -> If we defined any method/variable with single or double underscore as prefix, then
# all those variables/methods will not show in suggestion list
obj.show_school_name_fee()


# ->  If we want to access method/variable with single underscore as prefix
#     We can access directly without any issue.
obj._show_school_board_address()



# ->  If can not access method/variable with double underscore as prefix
#     if we want to access it, then we have to follow the pattern
#     obj._classname__variable/method
#    when we try to access, it will give you warning, that attribute is not available

obj._School__show_school_branch_and_principle()
