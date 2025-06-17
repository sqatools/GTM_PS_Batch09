from base.selenium_base import SeleniumBase
from .bus_booking_page_data import *
from .bus_booking_page_locator import *

class BusBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def goto_bus_booking_page(self):
        self.log.info(f"Open URL: {bus_booking_url}")
        self.driver.get(bus_booking_url)

    def select_from_city(self, src_city):
        self.log.info(f"select source city: {src_city}")
        self.enter_text(from_city_input_field, src_city)
        src_city_label = (By.XPATH, f"//span[text()='{src_city}']//parent::li")
        self.click_element(src_city_label)

    def select_dest_city(self, dest_city):
        self.log.info(f"select dest city: {dest_city}")
        self.enter_text(dest_city_input_field, dest_city)
        dest_city_label = (By.XPATH, f"//span[text()='{dest_city}']//parent::li")
        self.click_element(dest_city_label)

    def select_depart_date(self, depart_date):
        self.log.info(f"select depart date: {depart_date}")
        self.click_element(booking_date_loc)
        date_label = (By.XPATH, f"//span[text()='{depart_date}']//parent::li")
        self.click_element(date_label)

    def click_search_button(self):
        self.log.info(f"click to search button")
        self.click_element(search_btn)




