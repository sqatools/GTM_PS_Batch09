from selenium.webdriver.common.by import By

from_city_input_field = (By.NAME, "autosuggestBusSRPSrcHomeName")
dest_city_input_field = (By.ID, "autosuggestBusSRPDestHome")
booking_date_loc = (By.XPATH, "//input[@placeholder='Pick a date']")
search_btn = (By.XPATH, "//button[@data-testid='searchBusBtn']")
