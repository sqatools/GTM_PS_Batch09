import time

from selenium.webdriver.common.by import By

def login(driver, username, password):
    driver.find_element(By.NAME, "email").send_keys(username)
    driver.find_element(By.NAME, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)


def test_facebook_login_cred1(get_driver):
    driver = get_driver
    user1 = 'fbuser1'
    pass1 = 'fb@1234'
    print("\n credentials :", user1, pass1)
    login(driver, user1, pass1)


def test_facebook_login_cred2(get_driver):
    driver = get_driver
    user2 = 'fbuser2'
    pass2 = 'admin@1234'
    print("\n credentials :", user2, pass2)
    login(driver, user2, pass2)

