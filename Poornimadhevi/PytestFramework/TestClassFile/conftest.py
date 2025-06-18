import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    yield driver
    driver.close()


@pytest.fixture(scope="class")
def get_driver_instance(request):
    driver1 = webdriver.Chrome()
    driver1.maximize_window()
    driver1.implicitly_wait(10)
    driver1.get("https://www.facebook.com")
    request.cls.driver = driver1
    yield
    driver1.close()




