import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj =Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
print(count)
assert count == 3
assert count > 0
# //div[@class='products']/div/div/button--
for result in results:
    result.find_element(By.XPATH,"div/button").click()



driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()= 'PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#Sum validation
sum=0
results = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
for result in results:
    sum+=int(result.text)
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalAmount
discountAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print("DiscountAmount: ",discountAmount)
assert totalAmount > discountAmount
driver.find_element(By.XPATH,"//button[text() ='Place Order']").click()


