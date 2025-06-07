import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://sqatools.in/dummy-booking-website/")

title_name = driver.execute_script("return document.title;")
print("title name :", title_name)

website_url = driver.execute_script("return document.URL;")
print("document URL :", website_url)

from_city_elem = driver.execute_script("return document.getElementById('fromcity');" )
from_city_elem.send_keys("Mumbai")

dest_city_elem = driver.execute_script("return document.getElementById('destcity');" )
dest_city_elem.send_keys("Kolkata")

time.sleep(10)

document_height = driver.execute_script("return document.body.scrollHeight")
print("document height  :", document_height)

driver.execute_script(f"window.scrollBy(0, {document_height})")


time.sleep(10)

driver.execute_script("window.open('https://www.facebook.com')")

windows_list = driver.window_handles
driver.switch_to.window(windows_list[1])

time.sleep(10)
driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("user1@123")

time.sleep(5)
driver.close()


driver.switch_to.window(windows_list[0])
time.sleep(5)


driver.find_element(By.ID, "street_address1").send_keys("Mumbai, Boriwali")
time.sleep(5)

driver.close()

