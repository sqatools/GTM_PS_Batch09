import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://sqatools.in/dummy-booking-website/")

def handle_dropdown_select_by_index():
    dd_element = driver.find_element(By.ID, "admorepass")
    select_obj = Select(dd_element)
    select_obj.select_by_index(2)
    time.sleep(5)

#handle_dropdown_select_by_index()

def handle_dropdown_select_by_value():
    dd_element = driver.find_element(By.ID, "admorepass")
    select_obj = Select(dd_element)
    select_obj.select_by_value("4")
    time.sleep(5)

#handle_dropdown_select_by_value()

def handle_dropdown_select_by_visible_text():
    dd_element = driver.find_element(By.ID, "billing_country")
    select_obj = Select(dd_element)
    select_obj.select_by_visible_text("India")
    time.sleep(5)

#handle_dropdown_select_by_visible_text()

def select_dropdown_value_without_select_tag():
    driver.get("https://www.goibibo.com/")

    driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()

    driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::p").click()

    driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::input").send_keys("Mumbai")
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='Mumbai, India']//ancestor::li").click()
    time.sleep(5)


select_dropdown_value_without_select_tag()
driver.close()

# Home work
# Automate goibibo flight booking search page.
# https://www.goibibo.com/
