from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_obj = Service("C:\Program Files (x86)\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.current_url)
print(driver.title)
driver.minimize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
# driver.close()
