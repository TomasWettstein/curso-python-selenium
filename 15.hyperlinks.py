from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

browser.get("https://www.w3schools.com/")
time.sleep(3)
encontrar_link = browser.find_element(by=By.LINK_TEXT, value = "Learn PHP") #Con esto vamos a encontrar texto en un link, la busca tal cual la ponemos en el valor, en este caso si agregamos un epacio al value ya daria error.
encontrar_link.click()