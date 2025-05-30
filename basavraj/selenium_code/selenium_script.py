from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome browser
driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.find_element(By.ID,"oneway").click()
driver.find_element(By.ID,"roundtrip").click()


driver.find_element(By.NAME,"fromcity").send_keys("mumbai")
driver.find_element(By.NAME,"destcity").send_keys("benagaluru")

driver.close()
