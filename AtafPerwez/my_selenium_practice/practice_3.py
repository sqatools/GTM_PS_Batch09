import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initiate driver from webdriver class with chrome.
driver = webdriver.Chrome()
# Method to maximize the browser window
driver.maximize_window()
# Set wait for web element
driver.implicitly_wait(10)


def college_fees_details():
    driver.get("https://collegedunia.com/indore-colleges")
    course_fee = driver.find_element(By.XPATH,"//h3[contains(text(),'Institute of Engineering and Technology')]//ancestor::tr//a[@data-ga-event-category='courses-fees']/span[1]")
    print(course_fee.text)
    college_list = ['Acropolis Institute of Technology',
        'Indore Institute of Science and Technology',
        'IPS Academy',
        'Oriental University']
    for college in college_list:
        college_fee = driver.find_element(By.XPATH, f"//h3[contains(text(),'{college}')]//ancestor::tr//a[@data-ga-event-category='courses-fees']/span[1]")
        print(college,":", course_fee.text)

    time.sleep(5)

college_fees_details()


