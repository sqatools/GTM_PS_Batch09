import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)


def get_screenshot(image_path):
    driver.get("https://sqatools.in/dummy-booking-website/")
    # take element element screenshot
    driver.find_element(By.XPATH, "//h1[@align='center']").screenshot("heading_element.png")
    # take entire page screenshot
    file_path = os.path.join(image_path, 'complete_page.png')
    driver.save_screenshot(file_path)

get_screenshot(r"E:\Filesdata\batch09")
