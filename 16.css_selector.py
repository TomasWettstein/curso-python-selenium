from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

browser.get("https://www.w3schools.com/")
time.sleep(3)
content = browser.find_element(by=By.CSS_SELECTOR, value = "a.w3-button.tryit-button") #Guardamos dentro de una variable el elemento encontrado por medio de una clase.
content.click() #Click en el elemento