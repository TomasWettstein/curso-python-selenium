import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[3]/div[1]/select"))
        )
        opcion = select.find_elements(by=By.TAG_NAME, value="option") #Buscame todas las opciones del select y guardalas en la variable opcion
        time.sleep(3)
        for opcion in opcion:
            print("Los valores son: %s" % opcion.get_attribute("value"))
            opcion.click()
            time.sleep(2)
        seleccionar = Select( WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[3]/div[1]/select"))
        )) #Esto es una opcion de suport UI para volver a acceder al select
        seleccionar.select_by_value("10")
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()