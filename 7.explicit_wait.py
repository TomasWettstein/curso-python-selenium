import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)


class usando_unitttest(unittest.TestCase):
    
    def setUp(self): #Funcion para cargar el driver
        self.driver = browser
    def test_usando_explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
        finally:
            driver.quit()
if __name__ == '__main__':
    unittest.main()
    #Esta funcion de selenium nos permite dar condiciones para cargar ciertos compnentes en un script. Espera que se cargue un componente para continuar con la automatización