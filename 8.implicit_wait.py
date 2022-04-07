import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = driver_path = Service("D:\\dchrome\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = driver
    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #Para que cuando cargue la pagina le de una pausa de 5 segundos
        driver.get("http://www.google.com")
        myDynamicElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )#Un componente dinamico es aquel que tiene la posibilidad de cambiar lo que son sus identificadores en cualquier momento
        if myDynamicElement:
            driver.close()
if __name__ == '__main__':
    unittest.main()







#El implicit wait espera un cierto tiempo para que se cargue un componente y el tiempo se puede definir