import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = driver_path = Service("D:\\dchrome\\chromedriver_win32\\chromedriver.exe")
#Declaramos una clase de tipo unittest.testcase
#Unittest va a buscar las funciones que empiezan con la variable test
class usando_unittest(unittest.TestCase):
    #Funcion para incializar el driver
    #Self hace referencia a la clase
    def setUp(self):
        self.driver = webdriver.Chrome(service=driver_path)
    def test_buscar(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title) #Para validar que en el titulo de la pagina este la palabra google
        elemento = driver.find_element(by=By.NAME, value = "q") #Busca el buscador de google por el NAME
        elemento.send_keys("Selenium")#Escribe en el buscador Selenium
        elemento.send_keys(Keys.RETURN) #Return es como ENTER
        time.sleep(5)#Le damos tiempo para que podamos verificar que todo este correcto
        assert "No se encontro el elemento: " not in driver.page_source #Mensaje en caso de que no se encuenre el elemento, "not in" es para verificar que no esta en el codigo de la pagina.
        def tearDown(self):
            self.driver.close()
#Para que corra las funciones de la clase hay que cerrar la clase
if __name__  == '__main__':
    unittest.main()