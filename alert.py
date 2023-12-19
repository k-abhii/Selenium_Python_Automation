from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "Abhimanyu"

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
# alert.dismiss()
assert name in alertText
alert.accept()
