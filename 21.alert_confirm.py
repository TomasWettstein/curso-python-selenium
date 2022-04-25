from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

browser.get("file:///D:/Programacion/curso-python-selenium/EJEMPLOS%20ALERT/alert_confirm.html")
time.sleep(4)
confirm_alert = browser.find_element(by=By.ID, value = "alert")
confirm_alert.click()
time.sleep(3)
confirm_alert = browser.switch_to.alert.dismiss()#Cancelar alert confirm
time.sleep(3)
browser.close()