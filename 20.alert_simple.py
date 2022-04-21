from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

browser.get("file:///D:/Programacion/curso-python-selenium/EJEMPLOS%20ALERT/alert_simple.html")
time.sleep(5)
alerta = browser.find_element(by=By.ID, value = "alert")
alerta.click()
time.sleep(3)
alerta = browser.switch_to.alert.accept()#El Switch to alert, hace que se dirija a la ventana de la alerta y la acepte
time.sleep(3)
browser.close()