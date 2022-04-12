import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains   #Para hacer accion del movimiento del mouse para posicionarlo donde queramos
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_hover(self):
        driver = self.driver
        driver.get("https://google.com")
        time.sleep(3)
        elemento = driver.find_element(by=By.LINK_TEXT, value = "Privacidad")
        hover = ActionChains(driver).move_to_element(elemento)  #Esto nos permie hacer el movimiento o la simulación
        hover.perform()
if __name__ == '__main__':
    unittest.main()

        
        
    
