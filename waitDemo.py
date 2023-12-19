import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
