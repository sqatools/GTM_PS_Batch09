from bus_booking import BusBooking

class CarBooking(BusBooking):
    def __init__(self, car_src_city='Pune', car_dest_city='Mumbai', car_depart_date='25/05/2025'):
        super().__init__()
        self.car_src_city = car_src_city
        self.car_dest_city = car_dest_city
        self.car_depart_date = car_depart_date

    def check_car_booking(self):
        print(f"Car Booking confirm from :{self.car_src_city} and {self.car_dest_city} and date : {self.car_depart_date}")
