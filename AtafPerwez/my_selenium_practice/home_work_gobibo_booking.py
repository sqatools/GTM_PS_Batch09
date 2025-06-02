import random
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def goibibo_booking():
    driver.get("https://www.goibibo.com")
    wait= WebDriverWait(driver,10)
    # time.sleep(3)


    login_popup= wait.until(ec.presence_of_element_located((By.XPATH,'//span[@role="presentation"]')))
    time.sleep(2)
    login_popup.click()
    print('login/sighup window closed')

    close_ad = wait.until(ec.presence_of_element_located((By.XPATH,'//div[@data-id="dweb_pip_id"]/p[1]')))
    close_ad.click()
    print('bottom left ad is closed')
    time.sleep(1)

    flight_tab= wait.until(ec.element_to_be_clickable((By.XPATH,"//span[text()='Flights']")))
    time.sleep(2)
    flight_tab.click()
    print('clicked on FLight tab')

    # FROM city
    from_city = wait.until(ec.presence_of_element_located((By.XPATH,"//span[text()='From']//following-sibling::p")))
    time.sleep(2)
    from_city.click()
    print('clicked on from city')

    from_city_name= wait.until(ec.presence_of_element_located((By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']")))
    from_city_name.send_keys('Kolkata')
    print('from city name entered')

    from_city_name_select = wait.until(ec.element_to_be_clickable((By.XPATH,'//span[text()="Kolkata, India"]')))
    time.sleep(2)
    from_city_name_select.click()
    print('selected suggested city name from the list suggestion')


    # time.sleep(300)
    ### TO city ####
    # to_city = wait.until(ec.presence_of_element_located((By.XPATH,"//span[text()='To']//following-sibling::p")))
    # to_city.click()

    to_city_name= wait.until(ec.presence_of_element_located((By.XPATH,"//input[@type='text']")))
    time.sleep(2)
    to_city_name.send_keys('Dubai')
    print('To city name entered as Dubai')

    to_city_name_select = wait.until(ec.element_to_be_clickable((By.XPATH,'//span[text()="Dubai, United Arab Emirates"]')))
    time.sleep(2)
    to_city_name_select.click()
    print('selected DXB from the suggestion list')

    departure_date= wait.until(ec.element_to_be_clickable((By.XPATH,'(//div[@class="sc-12foipm-2 eTBlJr fswFld "])[3]')))
    time.sleep(2)
    departure_date.click()

    d_date= random.choice([5,6,7,8,9,10,11,12,13,14,15])
    departure_date_select= driver.find_element(By.XPATH,f'(//div[@class="DayPicker-Day"])[{d_date}]')
    time.sleep(2)
    departure_date_select.click()
    print('Departure date selected')

    return_date = wait.until(ec.element_to_be_clickable((By.XPATH, '(//div[@class="sc-12foipm-2 eTBlJr fswFld "])[4]')))
    time.sleep(2)
    return_date.click()

    r_date = random.choice([16,17,18,19,20,21,22,23,24,25])
    return_date_select = driver.find_element(By.XPATH, f'(//div[@class="DayPicker-Day"])[{r_date}]')
    time.sleep(2)
    return_date_select.click()
    print('return date selected successfully')

    search_button = wait.until(ec.element_to_be_clickable((By.XPATH,'//span[text()="SEARCH FLIGHTS"]')))
    time.sleep(2)
    search_button.click()
    time.sleep(5)
    print('clicked on the search flight button')

    view_fares_button = wait.until(ec.element_to_be_clickable((By.XPATH,'(//button[@type="button"])[3]')))
    time.sleep(3)
    view_fares_button.click()
    print('clicked on view fares button')

    book_now_button = wait.until(ec.element_to_be_clickable((By.XPATH,'//button[text()="CONTINUE" or text()="BOOK NOW" or text()="CONTINUE"]')))
    time.sleep(3)
    book_now_button.click()
    time.sleep(3)
    print('clicked on book now button')

    win_tab= driver.window_handles
    driver.switch_to.window(win_tab[1])
    time.sleep(3)
    print('switched to new tab successfully')


    # tnc_checkbox = wait.until(ec.element_to_be_clickable((By.XPATH,'//span[text()="I have read and understood all the above mentioned information"]//ancestor::span//input')))
    tnc_checkbox = wait.until(ec.element_to_be_clickable((By.XPATH,'(//input[@type="checkbox"])[1]')))
    time.sleep(3)

    tnc_checkbox.click()
    print('successfully selected the TnC checkbox')

    insurance_radio_button = wait.until(ec.element_to_be_clickable((By.XPATH,'(//input[@type="radio"])[4]')))
    time.sleep(3)
    insurance_radio_button.click()
    print('Clicked on the insurance radio button')

    ph_no = wait.until(ec.presence_of_element_located((By.XPATH,'(//input[@type="text"])[2]')))
    time.sleep(3)
    ph_no.send_keys('987654321')

    email_id = wait.until(ec.presence_of_element_located((By.XPATH,'(//input[@type="text"])[3]')))
    time.sleep(3)
    email_id.send_keys('Thanos@avengers.com')



    time.sleep(100)







goibibo_booking()
