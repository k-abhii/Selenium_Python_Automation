from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME,"name").send_keys("Abhimanyu")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,".form-check-label").click()
driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success" in message
print(message)
