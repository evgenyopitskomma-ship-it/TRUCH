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
print("input login") #печатаем в вывод

#методом find_element с помощью XPATH и командой send_keys ищем строку пароля и вводим "secret_sauce"
password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
password.send_keys("secret_sauce")
print("input password") #печатаем в вывод

#ищем елемент "логин" и командой "сlick" нажимаем на елемент
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("click login button") #печатаем в вывод

print(driver.current_url) #печатаем верный сайт
get_url = driver.current_url
url = "https://www.saucedemo.com/inventory.html" #необходимый результат
assert url == get_url #сравниваем необходимый с фактическим
print("URL верный") #печатаем в вывод

#переменная для поиска элемента с помощью кастомного XPATH
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
print(text_products.text) #печатаем желаемый результат
assert text_products.text == 'Products' #сравниваем желаемый результат с необходимым
print('Заголовок верен') #печатаем в вывод


#time.sleep(5) #говорим браузеру ничего не делать в течении 5 секунд
#driver.close() #закрываем браузер