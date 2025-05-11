import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://feddev.seido.me/login")
driver.maximize_window()
time.sleep(5)