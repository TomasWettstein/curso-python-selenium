import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")    #Esto es una instruccionde python para abrir una nueva ventana
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) #Las pestañas (ventanas) las cuenta desde el valor 0 entonces esta es la ventana 1.
        driver.get("http://stackoverflow.com") #Para que cargue en la nueva ventana otra pagina
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0]) #Vuelve a la primera pestaña
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()