import time
#
from selenium import webdriver
from selenium.webdriver.common.by import By
#
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def booking_com():
    driver.get('https://www.booking.com/')
    time.sleep(1)
    destination_location = driver.find_element(By.XPATH,'//input[@class="b915b8dc0b"]')
    destination_location.click()
    time.sleep(1)
    destination_location.send_keys('Pune')
    time.sleep(1)
    
    check_in_date= driver.find_element(By.XPATH,'(//span[@class="be2db1c937 bcb41e7c40"])[1]').click()
    time.sleep(1)
    select_date= driver.find_element(By.XPATH,'//span[@data-date="2025-05-25"]').click()
    time.sleep(1)


    # check_out_date= driver.find_element(By.XPATH,'(//span[@class="be2db1c937 bcb41e7c40"])[2]').click()
    # time.sleep(1)
    # select_date = driver.find_element(By.XPATH, '//span[@data-date="2025-05-27"]').click()
    # time.sleep(1)

    search_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
    search_button.click()

    time.sleep(10)

booking_com()


def make_my_trip():
    driver.get('https://www.makemytrip.com')
    driver.execute_script("document.body.style.zoom='70%'")

    driver.find_element(By.LINK_TEXT,'Flights').click()
    time.sleep(2)







