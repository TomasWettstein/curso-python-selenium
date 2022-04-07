from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver_path = driver_path = Service("D:\\dchrome\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)
driver.get("https://mail.google.com/")

usuario = driver.find_element(by=By.ID, value = "identifierId")
usuario.send_keys("tmw@jphlions.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)
clave = driver.find_element(by=By.NAME, value = "password")
clave.send_keys("Contraseña") #Contraseña incorrecta, si pones la verdadera se hace el login correctamente
clave.send_keys(Keys.ENTER)
# driver.close()