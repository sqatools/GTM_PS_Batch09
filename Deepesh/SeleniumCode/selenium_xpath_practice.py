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

def facebook():
    # Launch facebook website with get method
    driver.get("https://www.facebook.com")


    username_field = driver.find_element(By.XPATH, "//input[@data-testid='royal-email']")
    #print(username_field)
    username_field.send_keys("user1@gmail.com")

    password_field = driver.find_element(By.XPATH, "//input[@data-testid='royal-pass']")
    #print(password_field)
    password_field.send_keys("User@12345")
    time.sleep(3)

    # Finding element with the help of find_element with NAME locator
    driver.find_element(By.NAME, "login").click()

    time.sleep(10)
    # close current open browser
    #driver.close()
facebook()

