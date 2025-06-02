import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def mouse_hover_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(5)
    tester_hub = driver.find_element(By.XPATH, "//div[@id='menu']//a[contains(text(),'Tester')]")
    action = ActionChains(driver)

    action.move_to_element(tester_hub)
    action.perform()
    time.sleep(5)

    demo_site_testing = driver.find_element(By.XPATH, "//li//span[text()='Demo Testing Site']")
    action.move_to_element(demo_site_testing)
    action.perform()
    time.sleep(5)

    alert_box = driver.find_element(By.XPATH, "//li//span[text()='AlertBox']")
    action.click(alert_box)
    action.perform()
    time.sleep(5)
#mouse_hover_operation()

def perform_drag_drop_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(5)
    photo_iframe = driver.find_element(By.XPATH, "//iframe[contains(@data-src, 'photo')]")
    driver.switch_to.frame(photo_iframe)

    #src_image = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    tar_element = driver.find_element(By.ID, "trash")

    action = ActionChains(driver)
    # action.drag_and_drop(src_image, tar_element).perform()
    # time.sleep(5)

    images_elements = driver.find_elements(By.XPATH, "//h5[contains(text(), 'High Tatras')]//parent::li")
    for elem in images_elements:
        action.drag_and_drop(elem, tar_element).perform()
        time.sleep(5)

#perform_drag_drop_operation()

import pyautogui
# p

def context_click_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(5)
    about_element = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='About']")
    action = ActionChains(driver)
    action.context_click(about_element).perform()
    time.sleep(10)
    pyautogui.press('up')
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(5)


context_click_operation()
