from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.minimize_window()
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
driver.close()
