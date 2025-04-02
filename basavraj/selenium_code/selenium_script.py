from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search bar and type in a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium on MacBook")

# Press Enter to search
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see results
time.sleep(3)

# Close the browser
driver.quit()
