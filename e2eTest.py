from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
# Regular Expression XPATH--partial--<a class="nav-link" href="/angularpractice/shop" xpath="1">Shop</a>
# Regual Expression CSS_SELECTOR   a[href*='shop']
# driver.find_element(By.XPATH,"//a[contains(@href, 'shop')]").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
# //div[@class='card h-100']/div/h4/a
cards = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for card in cards:
    productName = card.find_element(By.XPATH,"div/h4/a").text
    if productName =="Blackberry":
        card.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"input[class*='validate']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successText = driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text
print(successText)
assert "Success! Thank you!" in successText

