from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
print(driver.current_url)
print(driver.title)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys("demo@gmail.com")
driver.find_element(By.XPATH, '//form/div[2]/input').send_keys("Hello@1234")
driver.find_element(By.XPATH, '//form/div[3]/input').send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[text() = 'Save New Password']").click()