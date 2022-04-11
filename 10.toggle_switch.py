import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp") #Pagina de w3schools para probar boton toggle
        time.sleep(3)
        toggle = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/label[3]/div"))
        )
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
