from car_booking import CarBooking

class FlightBooking(CarBooking):
    def __init__(self, flight_src_city='Bangalore', flight_dest_city='Chennai', flight_depart_date='30/05/2025'):
        super().__init__()
        self.flight_src_city = flight_src_city
        self.flight_dest_city = flight_dest_city
        self.flight_depart_date = flight_depart_date

    def check_flight_booking(self):
        print(f"flight Booking confirm from :{self.flight_src_city} and {self.flight_dest_city} and date : {self.flight_depart_date}")
