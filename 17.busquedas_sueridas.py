from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver_path = driver_path = Service("D:\\dchrome\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

palabra_busqueda = "sele"
driver.get("https://www.google.com")
time.sleep(3)
busqueda = driver.find_element(by=By.NAME, value = "q")
busqueda.send_keys(palabra_busqueda)
time.sleep(5)

for i in range(1,11):  #limitamos la busqueda a 11 elementos
    #En este caso sacamos el xpath de la primera busqueda relacionada y le cambiamos al XPATH el [1] (posición) por el valor de i en el for convertida a string, y que finalmente recupere el texto
    elementos = driver.find_element(by=By.XPATH, value = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
    print(elementos)
driver.close()