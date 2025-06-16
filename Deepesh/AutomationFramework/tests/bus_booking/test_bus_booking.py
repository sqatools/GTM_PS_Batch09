import time

import pytest
from modules.bus_page.bus_booking_page_class import BusBooking
from modules.bus_page.bus_booking_page_data import *

@pytest.mark.usefixtures("get_driver")
class TestBusBooking():

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bus = BusBooking(self.driver)

    def test_search_bus(self):
        self.bus.goto_bus_booking_page()
        self.bus.select_from_city(src_city)
        self.bus.select_dest_city(dest_city)
        self.bus.select_depart_date(next_2_days_date)
        self.bus.click_search_button()
        time.sleep(20)

