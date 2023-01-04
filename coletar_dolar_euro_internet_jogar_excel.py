from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import pyautogui as auto
from selenium.webdriver.common.by import By

print('pegando site')
nav =  web.Chrome()
nav.get('https://www.google.com.br/')

auto.sleep(4)
print('enviando procura de dolar hoje no site')
nav.find_element(By.NAME, 'q').send_keys('Dolar Hoje')  

auto.sleep(4)
print('pressionando enter')
nav.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
auto.sleep(2)