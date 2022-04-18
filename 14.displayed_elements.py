import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)
browser.get("https://www.google.com")
time.sleep(10)
displayed_element = browser.find_element(by=By.NAME, value = "btnI")
print(displayed_element.is_displayed()) #Regresa true o false si ya cargo el elemento. (Si lo mostro)
if displayed_element.is_enabled():
    print(displayed_element.is_enabled())#Regresa un true o false si el elemento esta disponible.(Si esta habilitado para hacer click o no.)
    
