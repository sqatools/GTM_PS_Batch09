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

    # NAME and ID Locator
    # Finding element with the help of find_element with NAME locator
    driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")

    # Finding element with the help of find_element with ID locator
    driver.find_element(By.ID, "pass").send_keys("User@12345")
    time.sleep(3)

    # Finding element with the help of find_element with NAME locator
    driver.find_element(By.NAME, "login").click()

    time.sleep(10)
    # close current open browser
    #driver.close()
#facebook()

def link_text_and_partial_linktext():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    time.sleep(5)

    # Identify the element with the help link text
    driver.find_element(By.LINK_TEXT, "Python 3 Tutorial").click()
    time.sleep(5)

    # Identify the element with the help partial link text
    driver.find_element(By.PARTIAL_LINK_TEXT, "Robot").click()
    time.sleep(5)

    driver.close()

#link_text_and_partial_linktext()

def get_element_with_tagname_classname():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    # Get element with TAG_NAME locator
    header = driver.find_element(By.TAG_NAME, "h1")
    print("website header :", header.text)

    time.sleep(5)

    # Get element with class name locator
    elem2 = driver.find_element(By.CLASS_NAME, "post-title")
    print(elem2.text)

    driver.close()


get_element_with_tagname_classname()

# check the uniqueness of element in developer tool
# 1. hash for id, e.g #id
# 2. dot for class, e.g  .clasname
# 3. double // for tagname e.g. //tagname
