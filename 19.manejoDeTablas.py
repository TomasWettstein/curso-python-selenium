from idna import valid_contextj
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

driver_path = Service('D:\\dchrome\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=driver_path)

browser.get("https://www.htmlquick.com/es/tutorials/tables.html")
time.sleep(5)
valor = browser.find_element(by=By.XPATH, value = "//*[@id='the-scope-attribute']/div/div/table/tbody/tr").text#Con este XPATH obtenemos todos las columnas de la tabla y la convertimos en texto
print(valor)

rows = len(browser.find_elements(by=By.XPATH, value = "//*[@id='the-scope-attribute']/div/div/table/tbody/tr")) #El len sirve para traer el tamaño o la cantidad de elementos
columnas = len(browser.find_elements(by=By.XPATH, value = "//*[@id='the-scope-attribute']/div/div/table/tbody/tr[1]/th"))
print(rows)
print(columnas)

for n in range(2, rows + 1):
    for v in range(1, columnas):
        dato = browser.find_element(by=By.XPATH, value = "//*[@id='the-scope-attribute']/div/div/table/tbody/tr["+str(n)+"]/td["+str(v)+"]").text
        print(dato, end='                   ')
    print()
# //*[@id="header-cells"]/div/div/table/tbody/tr[2]/td[1]
# //*[@id="header-cells"]/div/div/table/tbody/tr[1]
# //*[@id="the-scope-attribute"]/div/div/table/tbody/tr[2]/th
# //*[@id="the-scope-attribute"]/div/div/table/tbody/tr[2]/td[1]