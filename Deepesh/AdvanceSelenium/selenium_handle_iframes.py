import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

iframe_element = driver.find_element(By.NAME, "globalSqa")
# switch to iframe
driver.switch_to.frame(iframe_element)

# heading in iframe
heading_in_frame = driver.find_element(By.XPATH, "//div[@class='page_heading']//h1")
print("heading in frame :", heading_in_frame.text)

menu_button = driver.find_element(By.ID, "mobile_menu_toggler")
menu_button.click()
time.sleep(5)

# get about menu option in iframe and click on it
about_elem = driver.find_element(By.XPATH, "//div[@id='mobile_menu']//a[text()='About']")
about_elem.click()
time.sleep(5)

# switch to default
driver.switch_to.default_content()

# heading in main page
heading_main_page = driver.find_element(By.XPATH, "//div[@class='page_heading']//h1")
print("heading main page :", heading_main_page.text)

time.sleep(5)
driver.close()



