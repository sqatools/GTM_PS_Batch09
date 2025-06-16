from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def get_element(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, text_value):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text_value)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def select_dropdown_value(self, locator, dd_value):
        element = self.get_element(locator)
        sel = Select(element)
        sel.select_by_visible_text(dd_value)
