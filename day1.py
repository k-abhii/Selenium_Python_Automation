from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# CHROME DRIVER
srevice_obj = Service()
driver = webdriver.Chrome(service=srevice_obj)
driver.get("https://rahulshettyacademy.com/")

