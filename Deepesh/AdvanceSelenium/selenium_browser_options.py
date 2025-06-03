import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options


opt1 = chrome_options()
opt1.add_argument("--headless")
driver = webdriver.Chrome(options=opt1)
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://www.facebook.com")
time.sleep(5)
driver.save_screenshot("facebook_page.png")

driver.close()





