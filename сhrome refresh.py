import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#настройки браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.saucedemo.com" #адрес сайта
driver.get(base_url) #открываем адрес сайта в браузере
driver.maximize_window() #разворачиваем браузер в максимально возможном разрешении

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #с помощью XPATH ищем элемент
user_name.send_keys("standard_user") #вводим логин
print ("ввод логина")

#с помощью XPATH ищем элемент
password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
password.send_keys("secret_sauc") #вводим неверный пароль
print("ввод пароля")

#ищем элемент "логин" и командой "сlick" нажимаем на элемент
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("click login button")

time.sleep(3) #говорим браузеру бездействовать в течении 3 секунд
driver.refresh() #обновить страницу

time.sleep(3) #говорим браузеру бездействовать в течении 3 секунд
driver.close() #закрыть браузер