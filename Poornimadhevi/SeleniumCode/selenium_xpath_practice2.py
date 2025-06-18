"""
Selenium Locators

    ID = "id" # DONE
    XPATH = "xpath"
    LINK_TEXT = "link text" # DONE
    PARTIAL_LINK_TEXT = "partial link text"  # DONE
    NAME = "name"  # DONE
    TAG_NAME = "tag name" # DONE
    CLASS_NAME = "class name"  # DONE
    CSS_SELECTOR = "css selector"
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initiate driver from webdriver class with chrome.
driver = webdriver.Chrome()
# Method to maximize the browser window
driver.maximize_window()
# Set wait for web element
driver.implicitly_wait(10)

def college_list():
    # Launch facebook website with get method
    driver.get("https://collegedunia.com/indore-colleges")

    college_fee = driver.find_element(By.XPATH, "//h3[contains(text(),'Institute of Engineering and Technology')]//ancestor::tr//a[@data-ga-event-category='courses-fees']/span[1]")
    print(college_fee.text)

    college_list = [
        'Acropolis Institute of Technology',
        'Indore Institute of Science and Technology',
        'IPS Academy',
        'Oriental University'
    ]

    for college in college_list:
        college_fee = driver.find_element(By.XPATH, f"//h3[contains(text(),'{college}')]//ancestor::tr//a[@data-ga-event-category='courses-fees']/span[1]")
        print(college, ":", college_fee.text)

    time.sleep(5)



college_list()
