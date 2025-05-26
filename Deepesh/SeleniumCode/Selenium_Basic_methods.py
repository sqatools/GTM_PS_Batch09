"""
List of Methods:

current_url
title
forward
back
refresh
send_keys
click
text
is_selected
is_displayed
get_attribute

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.rediff.com/cricket/ipl-2025")

def get_current_url():
    print("current URL", driver.current_url)

def get_title():
    print("current title", driver.title)

def back_forward_refresh():
    driver.find_element(By.XPATH, "//a[text()='Squads']").click()
    time.sleep(5)
    driver.back()  # it will navigate to initial page
    time.sleep(5)
    driver.forward() # # it will navigate to squad page
    time.sleep(10)
    driver.refresh() # it will refresh the current page.


get_title()
get_current_url()
back_forward_refresh()

