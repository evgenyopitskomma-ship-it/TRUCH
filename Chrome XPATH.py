import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#настройки браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#установка актуального драйвера для хрома и запуск самого браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = "https://www.saucedemo.com" #адрес сайта
driver.get(base_url) #открываем адрес сайта в браузере
driver.maximize_window() #разворачиваем браузер в максимально возможном разрешении

#с помощью XPATH и командой send_keys ищем строку логина и вводим имя "standard_user"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")

#методом find_element с помощью XPATH и командой send_keys ищем строку пароля и вводим имя "secret_sauce"
password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
password.send_keys("secret_sauce")

#ищем елемент "логин" и командой "сlick" нажимаем на елемент
login_button = driver.find_element(By.ID, "login-button")
login_button.click()


#time.sleep(5) #говорим браузеру ничего не делать в течении 5 секунд
#driver.close() #закрываем браузер