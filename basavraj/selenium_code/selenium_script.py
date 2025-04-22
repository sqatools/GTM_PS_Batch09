from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for the page to load
time.sleep(2)

# Find the search box and type a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium automation tutorial")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait to see results
time.sleep(3)

# Close the browser
driver.quit()
