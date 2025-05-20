# """
# pip install selenium
# """
import time
#
from selenium import webdriver
from selenium.webdriver.common.by import By
#
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("User@12345")
# time.sleep(3)
driver.find_element(By.NAME, "login").click()

time.sleep(1)
# driver.close()
##################

### Amazon login ###
def amazon_login():
    driver.get("https://www.amazon.in/")

    driver.find_element(By.PARTIAL_LINK_TEXT, 'Hello, sign in').click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign i').click()

    # time.sleep(3)
    driver.find_element(By.ID, "ap_email_login").send_keys('abc@gmail.com')
    driver.find_element(By.XPATH,'//input[@type="submit"]').click()
    password= driver.find_element(By.XPATH,'//input[@type="password"]')
    password.send_keys('abc@1234567890')
    driver.find_element(By.ID,"signInSubmit").click()
    time.sleep(3)

    # time.sleep(10)
    # driver.close()
amazon_login()