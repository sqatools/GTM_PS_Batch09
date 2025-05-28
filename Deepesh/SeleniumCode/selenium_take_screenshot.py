import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)


def get_screenshot():
    driver.get("https://sqatools.in/dummy-booking-website/")
    # take element element screenshot
    driver.find_element(By.XPATH, "//h1[@align='center']").screenshot("heading_element.png")
    # take entire page screenshot
    driver.save_screenshot("complete_page.png")

get_screenshot()
