from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

browser.get("file:///D:/Programacion/curso-python-selenium/EJEMPLOS%20ALERT/alert_prompt.html")
time.sleep(3)
alert = browser.find_element(by=By.ID, value = "alert")
alert.click()
time.sleep(3)
alert = browser.switch_to.alert.send_keys("Tomas") #El switch_to_alert es para dirigirse a la alerta
time.sleep(2)
alert =  browser.switch_to.alert.accept()#En caso de querer cancelar, cambiar el accept por dismiss()
time.sleep(3)
browser.close()
