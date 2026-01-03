import time

from selenium import webdriver
from selenium.webdriver.safari.service import Service

driver = webdriver.Safari()
driver.get ("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)
driver.close()