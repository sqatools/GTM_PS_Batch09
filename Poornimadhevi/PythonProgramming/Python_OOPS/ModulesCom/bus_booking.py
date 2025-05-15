

class BusBooking:
    def __init__(self, src_city='Mumbai', dest_city='Delhi', depart_date='20/05/2025'):
        self.src_city = src_city
        self.dest_city = dest_city
        self.depart_date = depart_date

    def check_bus_booking(self):
        print(f"Booking confirm from :{self.src_city} and {self.dest_city} and date : {self.depart_date}")
