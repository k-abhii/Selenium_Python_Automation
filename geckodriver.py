from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.service import Service


service_obj = Service("C:\Program Files (x86)\geckodriver.exe")


driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()