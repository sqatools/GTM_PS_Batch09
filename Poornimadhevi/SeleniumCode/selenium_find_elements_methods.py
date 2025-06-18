import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://www.rediff.com/sports")
driver.maximize_window()
driver.implicitly_wait(20)

def get_all_blog_links():
    # get all the links for sports sections
    element_list = driver.find_elements(By.XPATH, "//h2/a")
    for element in element_list:
        print(element.get_attribute("href"))


#get_all_blog_links()

def select_all_checkboxes():
    driver.get("https://sqatools.in/dummy-booking-website/")
    checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkbox_list:
        print("is selected before click :", checkbox.is_selected())
        checkbox.click()
        print("is selected after click :", checkbox.is_selected())
        time.sleep(2)
        print("_"*50)


#select_all_checkboxes()

def select_specific_checkboxes():
    driver.get("https://sqatools.in/dummy-booking-website/")
    city_names = ['Mumbai', 'Kolkata']
    for city in city_names:
        element = driver.find_element(By.XPATH, f"//td[text()='{city}']//preceding-sibling::td/input")
        element.click()
        time.sleep(2)

#select_specific_checkboxes()

def search_child_element():
    driver.get("https://sqatools.in/dummy-booking-website/")
    row_element = driver.find_element(By.XPATH, "//table[@Id='cities']//tr[4]")
    colums_elments = row_element.find_elements(By.TAG_NAME, "td")
    for element  in colums_elments:
        #element.click()
        print(element.text)

#search_child_element()

def search_child_element_multiple_rows():
    driver.get("https://sqatools.in/dummy-booking-website/")
    tr_elements = driver.find_elements(By.XPATH, "//table[@Id='cities']//tr")
    print("row elems :", tr_elements)
    for row_element in tr_elements[1:]:
        colums_elments = row_element.find_elements(By.TAG_NAME, "td")
        print("colns elems :", colums_elments)
        for col_element in colums_elments:
            #element.click()
            print(col_element.text)
        print("_"*50)


search_child_element_multiple_rows()

