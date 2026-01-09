import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#настройки браузера Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #работа браузера в режиме headless

#установка актуального драйвера для хрома и запуск самого браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = "https://www.saucedemo.com" #адрес сайта
driver.get(base_url) #открываем адрес сайта в браузере
driver.maximize_window() #разворачиваем браузер в максимально возможном разрешении

#с помощью XPATH и командой send_keys ищем строку логина и вводим имя "standard_user"
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")
print("input login") #печатаем в вывод

#методом find_element с помощью XPATH и командой send_keys ищем строку пароля и вводим "secret_sauce"
password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
password.send_keys("secret_sauc")
print("input password") #печатаем в вывод

#ищем елемент "логин" и командой "сlick" нажимаем на елемент
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("click login button") #печатаем в вывод

warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']") #ищем нужный элемент
value_warning_text = warning_text.text
text_error = ('Epic sadface: Username and password do not match any user in this service') #текст ошибки
assert (value_warning_text == text_error) #сравниваем необходимый с фактическим


print('Cообщение корректно') #печатаем в вывод

time.sleep(3) #говорим браузеру ничего не делать в течении 3 секунд
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']") #ищем необходимый элемент
error_button.click() #нажимаем на элемент
print("click error button") #печатаем в вывод

time.sleep(3) #говорим браузеру ничего не делать в течении 3 секунд
driver.close() #закрываем браузер