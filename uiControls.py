from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_url)
print(driver.title)
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
for radio in radiobuttons:
    if radio.get_attribute("value") =="radio2":
        radio.click()
        assert radio.is_selected()
        break

radiobuttons[2].click()
assert radiobuttons[2].is_selected()
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
print(driver.find_element(By.ID,"displayed-text").is_displayed())
assert  not driver.find_element(By.ID,"displayed-text").is_displayed()
for checkbox in checkboxes:
    if checkbox.get_attribute("value") =="option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

