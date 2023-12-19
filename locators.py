from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.current_url)
print(driver.title)
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
# driver.back()
# driver.refresh()
# driver.forward()
# driver.maximize_window()
# driver.minimize_window()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Abhimanyu")
assert "Success" in message
