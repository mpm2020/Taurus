import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestRequests(unittest.TestCase):

    def setUp(self):
        global driver
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.get('about:blank')
        driver.implicitly_wait(10.0)
        driver.maximize_window()

    def test_method(self):
        driver.get('http://www.blazedemo.com/')
        print("Headless Chrome Initialized")
        time.sleep(1.5)
        find_flights_button = "//input[@value='Find Flights']"
        driver.find_element(By.XPATH, find_flights_button).click()
        time.sleep(2.5)
        driver.save_screenshot("Test" + ".png")
        print("Test Finished")

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
