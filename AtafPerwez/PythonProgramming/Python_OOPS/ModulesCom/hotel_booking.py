from flight_booking import FlightBooking

class HotelBooking(FlightBooking):
    def __init__(self, hotel_city_name='Ladakh', hotel_name='Taj Hotel', hotel_booking_date='30/05/2025'):
        super().__init__()
        self.hotel_city_name = hotel_city_name
        self.hotel_name = hotel_name
        self.hotel_booking_date = hotel_booking_date

    def check_hotel_booking(self):
        print(f"hotel Booking confirm from :{self.hotel_city_name} and {self.hotel_name} and booking date : {self.hotel_booking_date}")
