import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_usando_radio_button(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(5)
        radio_bt = driver.find_element(by=By.XPATH, value = "//*[@id='main']/div[3]/div[1]/input[4]")
        radio_bt.click()
        time.sleep(3)
        radio_bt =  driver. find_element(by=By.XPATH, value = "//*[@id='main']/div[3]/div[1]/input[3]")
        radio_bt.click()
        time.sleep(3)
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()