import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unitttest(unittest.TestCase):
    
    def setUp(self): #Funcion para cargar el driver
        self.driver = browser
    def test_pagina_siguiente_o_anterior(self):
        driver = self.driver #Mandamos a llamar a driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.back() #Metodo de selenium para regresar a la pagina anterior
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward() #Metodo de selenium para ir a la pagina siguiente
        time.sleep(3)
        driver.quit() #Metodo para cerrar el driver
if __name__ == '__main__':
    unittest.main()