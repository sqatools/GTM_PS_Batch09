import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options



def execute_code(browser, headless=True):
    driver = None
    if browser == 'chrome':
        opt1 = chrome_options()
        if headless:
            opt1.add_argument("--headless")
        opt1.add_argument("--windows-size=1920*1080")
        opt1.add_argument("--disable-notifications")
        #opt1.add_argument("--incognito")
        prefs_dict = {"download.default_directory": "E:\\Filesdata\\DownloadFiles",
                      "download.prompt_for_download" : False,
                      "safebrowsing.enabled": True}

        # Keep browser in open state
        opt1.add_experimental_option("detach", True)
        opt1.add_experimental_option("prefs", prefs_dict)

        driver = webdriver.Chrome(options=opt1)



    elif browser == 'firefox':
        opt2 = firefox_options()
        if headless:
            opt2.add_argument("--headless")
        driver = webdriver.Firefox(options=opt2)

    elif browser == 'edge':
        opt3 = edge_options()
        if headless:
            opt3.add_argument("--headless")
        driver = webdriver.Edge(options=opt3)


    #driver.maximize_window()
    driver.implicitly_wait(10)

    """
    driver.get("https://www.facebook.com")
    time.sleep(5)
    driver.find_element(By.NAME, 'email').send_keys("user1@gmail.com")
    driver.find_element(By.NAME, 'pass').send_keys("user@12345")
    time.sleep(5)
    driver.save_screenshot(f"{headless}_facebook_page_{browser}.png")
    """

    driver.get("https://www.python.org/downloads/")
    time.sleep(10)
    download_link = driver.find_element(By.XPATH, "//div[@class='download-os-windows']//p[@class='download-buttons']/a")
    download_link.click()

    time.sleep(30)

    #driver.close()



# browsers_list = ['chrome', 'firefox', 'edge']
# for browser in browsers_list:
#     execute_code(browser, headless=False)

execute_code('chrome', headless=False)

