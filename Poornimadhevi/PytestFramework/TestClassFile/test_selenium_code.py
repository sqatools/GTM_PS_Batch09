import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver")
class TestSeleniumCode:
    def test_facebook_login(self, get_driver):
        self.driver = get_driver
        self.driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")

    def test_facebook_login2(self, get_driver):
        self.driver = get_driver
        self.driver.find_element(By.NAME, "pass").send_keys("user1@1234")
