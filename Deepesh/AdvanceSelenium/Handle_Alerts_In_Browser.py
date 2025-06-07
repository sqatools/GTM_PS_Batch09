import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")

def handle_alert_box():
    alert_btn = driver.find_element(By.ID, "btnShowMsg")
    alert_btn.click()
    time.sleep(3)
    alert_obj = Alert(driver)
    print("alert msg :", alert_obj.text)
    alert_obj.accept()  # accept the alert
    time.sleep(3)

handle_alert_box()

def handle_confirm_box():
    # Accepting the alert
    alert_btn = driver.find_element(By.ID, "button")
    alert_btn.click()
    time.sleep(3)
    alert_obj = Alert(driver)
    print("alert msg :", alert_obj.text)
    alert_obj.accept()  # accept the alert
    time.sleep(3)
    ui_msg = driver.find_element(By.ID, "demo")
    print("message on UI:", ui_msg.text)

    # cancel the alert
    alert_btn = driver.find_element(By.ID, "button")
    alert_btn.click()
    time.sleep(3)
    alert_obj = Alert(driver)
    print("alert msg :", alert_obj.text)
    alert_obj.dismiss()  # accept the alert
    time.sleep(3)
    ui_msg = driver.find_element(By.ID, "demo")
    print("message on UI:", ui_msg.text)


handle_confirm_box()

def handle_prompt_box():
    # Accepting the alert
    alert_btn = driver.find_element(By.ID, "promptbtn")
    alert_btn.click()
    time.sleep(3)
    alert_obj = Alert(driver)
    print("alert msg :", alert_obj.text)
    # send value to alert
    alert_obj.send_keys("SQATools")

    alert_obj.accept()  # accept the alert
    time.sleep(3)
    ui_msg = driver.find_element(By.ID, "prompt")
    print("message on UI:", ui_msg.text)


    # Cancell the prompt alert
    alert_btn = driver.find_element(By.ID, "promptbtn")
    alert_btn.click()
    time.sleep(3)
    alert_obj = Alert(driver)
    print("alert msg :", alert_obj.text)

    alert_obj.dismiss()  # accept the alert
    time.sleep(3)
    ui_msg = driver.find_element(By.ID, "prompt")
    print("message on UI:", ui_msg.text)

handle_prompt_box()
