import time

import pytest
from modules.bus_page.bus_booking_page_class import BusBooking
from modules.bus_page.bus_booking_page_data import *

@pytest.mark.usefixtures("get_driver")
class TestBusBooking():

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bus = BusBooking(self.driver)

    @pytest.mark.smoke
    def test_navigate_to_bus(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.goto_bus_booking_page()

    def test_select_src_city(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.select_from_city(src_city)

    def test_select_dest_city(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.select_dest_city(dest_city)

    def test_select_depart_date(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.select_depart_date(next_2_days_date)

    def test_click_to_search_button(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.click_search_button()
        time.sleep(20)

