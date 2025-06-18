"""
Different types of waits in selenium.

1.  Implicit wait :  implicit wait applies on all the elements of the webpage by default.,
                     ->  This is maximum timeout to look for any element on the webpage
                     ->  IF we found element in few seconds, then it does not wait for complete timeout
                         it will jump on another element to find out.
2.  Explicit wait :  explicit wait that we have to apply explicitly on each of the element.
                    -> It does not work internally
                    -> We can use different conditions with explicit wait.

3.  Fluent wait : Fluent wait is part of explicit wait, where we can change polling frequency of any element.
                 ->  It works same as explicit wait.
                 ->  Default poll_frequency in explicit wait is 0.5 sec.

4.  Static Wait :  static wait is the hardcore sleep time, driver has to wait till specified time, in any
                   condition. e.g time.sleep(10)

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()

def implicit_wait_method():
    #driver.implicitly_wait(10)
    t1 = time.time()
    try :
        driver.find_element(By.NAME, "email123").send_keys("user1@gmail.com")
    except Exception as e:
        print(e)
        pass

    t2  = time.time()
    print("Total time taken :", t2 - t1)



#implicit_wait_method()

def selenium_explicit_wait():
    wait = WebDriverWait(driver, 15)
    t1 = time.time()
    try:
        element = wait.until(ec.presence_of_element_located((By.NAME, "email")))
        element.send_keys("user1@gmail.com")
    except Exception as e:
        print(e)

    t2 = time.time()
    print("total timeout :", t2-t1)


#selenium_explicit_wait()

def selenium_fluent_wait():
    wait = WebDriverWait(driver, 15, poll_frequency=3)
    t1 = time.time()
    try:
        element = wait.until(ec.presence_of_element_located((By.NAME, "email123")))
        element.send_keys("user1@gmail.com")
    except Exception as e:
        print(e)

    t2 = time.time()
    print("total timeout :", t2-t1)
