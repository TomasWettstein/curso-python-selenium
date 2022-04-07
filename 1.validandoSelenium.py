from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver_path = driver_path = Service("D:\\dchrome\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)
driver.get("http://python.org")
driver.close()