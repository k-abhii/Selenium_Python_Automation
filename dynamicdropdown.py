import time

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(len(countries))
for country in countries:
    # print(country.text)
    if country.text == "India":
        country.click()
        break
# print(driver.find_element(By.ID,"autosuggest").text)---Text not work for dynamic
print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) # for Dynamic
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"