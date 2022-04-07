import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
driver_path = Service('C:\\Users\\tomas\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        buscar_por_xpath = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"))
        )   
        time.sleep(3)
        buscar_por_xpath.send_keys("Selenium", Keys.ARROW_DOWN)#ARROW_DOWN: Esto hace una tecla hacia abajo
        time.sleep(3)
    def tearDown(self):
        self.driver.close()
if(__name__ == '__main__'):
    unittest.main()
        
#XPATH: Es una estructura de objetos XML
#XPATH RELATIVO: En toda la estructura XML que tiene la pagina busca un modulo especifico. Se usa mas el XPATH relativo por que normalmente el codigo cambia de lugar y con esto nos soluciona ese problema.

#XPATH ABSOLUTO: Es la ruta XML completa, si cambia el codigo de lugar ya no la encuentra. Por este motivo no se suele usar, solo si tenemos la seguridad de que no va  cambiar el componente de ubicacion.
        