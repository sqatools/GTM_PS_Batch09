import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

# click on software testing link, it will open in new tab
driver.find_element(By.LINK_TEXT, "Software Testing Principles").click()

# Get window tabs list
windows_tabs = driver.window_handles
print(windows_tabs)

time.sleep(5)
# switch to new tab with the help list of windows
driver.switch_to.window(windows_tabs[1])

# get all the subheading text from software testing principles
topics_headings = driver.find_elements(By.XPATH, "//h3/span")
for topic in topics_headings:
    print(topic.text)

# get current url of testing principles
print("current url :", driver.current_url)

# close current active tab of testing principles
driver.close()

# switch to default tab
driver.switch_to.window(windows_tabs[0])

time.sleep(5)
# Navigate to API Testing Course
driver.find_element(By.LINK_TEXT, "API Testing").click()
print("current url :", driver.current_url)

time.sleep(5)
driver.close()




