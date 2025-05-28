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
get_attribute
is_selected
is_displayed
is_enabled


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
    #time.sleep(5)
    driver.back()  # it will navigate to initial page
    #time.sleep(5)
    driver.forward() # # it will navigate to squad page
    time.sleep(2)
    driver.refresh() # it will refresh the current page.

def get_text_and_attribute_value_from_element():
    headline = driver.find_element(By.XPATH, "(//h2[@class='hdlines']/a)[1]")
    print(headline)
    print("First Headline :", headline.text)
    print("Link with headline :", headline.get_attribute("href"))


def check_displayed_enabled_selected():
    driver.get("https://www.facebook.com/r.php?entry_point=login")

    first_name_elem = driver.find_element(By.NAME, "firstname")
    print("Attribute value :", first_name_elem.get_attribute("aria-label"))

    radio_elem = driver.find_element(By.XPATH, "//input[@value='1']")
    print("radio is displayed :", radio_elem.is_displayed()) # True
    print("radio is enabled :", radio_elem.is_enabled()) # True
    print("radio is selected before click:", radio_elem.is_selected()) # False

    print("clicking on radio button")
    radio_elem.click()

    print("radio is selected after click:", radio_elem.is_selected()) # True



# get_title()
# get_current_url()
# get_text_and_attribute_value_from_element()
# check_displayed_enabled_selected()


#back_forward_refresh()


