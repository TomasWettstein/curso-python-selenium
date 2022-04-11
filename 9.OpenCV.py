import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import cv2 
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = browser
    def test_usando_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot("img2.png")#Con esto tomamos una imagen a la pagina que tengamos abierta, toma unicamente la pagina.
        time.sleep(3)
    def test_comparando_imagenes(self):
        time.sleep(3)
        img1 = cv2.imread('img1.png')
        img2 = cv2.imread('img2.png')
        diferencia = cv2.absdiff(img1, img2)     #Con esto comparamos las imagenes.
        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)      #Con esto las convierto en gris, por que es complicado comparar imagenes a color
        contours,_ = cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Hacemos una coleccion de datos
        for c in contours:
            if cv2.contourArea(c) >= 20:    #Declaramos un for para recorrer la imagenes, el 20 indica la escalacion que va a hacer a nivel grises, entre menos rango mas fino se va a hacer pero es mas propenso a errores.
                posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c)    #boundingRect es las dimensiones que va a encontrar en toda la caja de la imagen y la va a asignar a las variables. Es decir encontramos la diferencia.
                cv2.rectangle(img1, (posicion_x, posicion_y),(posicion_x + ancho, posicion_y + alto), (0,0,255), 2) #Con esta linea dibujamos la diferencia
        while(1):
            cv2.imshow('Imagen1', img1)
            cv2.imshow('Imagen2', img2)
            cv2.imshow('Diferencias detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                cv2.destroyAllWindows() #Aca rompe
                break
if __name__ == '__main__':
    unittest.main()