import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
expected_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# div h4
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

time.sleep(2)
buttons = driver.find_elements(By.CSS_SELECTOR,".product-action button")
# buttonX = driver.find_elements(By.XPATH,"//div[@class='products']/div")
for button in buttons:
    button.click()
l=[]
res = driver.find_elements(By.XPATH,"//div[@class='products']/div//h4")
for r in res:
    l.append(r.text)
print(l)
assert l == expected_list



