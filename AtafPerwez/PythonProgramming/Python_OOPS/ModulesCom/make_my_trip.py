from hotel_booking import HotelBooking

class MakeMyTGrip(HotelBooking):
    def __init__(self):

        super().__init__()

    def greeting_msg(self):
        print("Welcome to Make My Trip")


obj = MakeMyTGrip()

obj.check_hotel_booking()
obj.hotel_city_name = 'Mumbai'
obj.hotel_name = 'Banana Leaf'
obj.hotel_booking_date = "1/06/2025"

obj.check_hotel_booking()
obj.check_car_booking()
obj.check_flight_booking()
obj.check_bus_booking()

