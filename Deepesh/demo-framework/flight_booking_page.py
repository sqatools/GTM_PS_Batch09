from selenium_base import SeleniumBase
from flight_booking_locators import *

class FlightBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_login_popup(self):
        self.click_element(close_popup_loc)

