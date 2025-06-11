import os
import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=False)
def setup():
    print("\n---- Common func fixture initiated -----")
    yield
    print("\n---- Common func fixture completed -----")


@pytest.fixture(scope='module')
def create_user_details():
    for i in range(1, 11):
        username= f'newuser{i}'
        password= f'password{i}'
        email = f'newuser{i}@gmail.com'
        with open('usersdetails.txt', 'a') as file:
            data = f"{username}, {password}, {email}\n"
            file.write(data)
    print("Users details added successfully \n")
    time.sleep(20)
    yield
    os.remove("usersdetails.txt")
    print("Users details removed successfully \n")



@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    yield driver
    driver.close()
