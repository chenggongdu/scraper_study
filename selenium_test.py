from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
inputs = driver.find_element(By.CSS_SELECTOR, '#kw')
inputs.send_keys("优路教育图片")
button = driver.find_element(By.ID, 'su')
print(button)
print(driver.current_url)
print(driver.get_cookies())
print(driver.page_source)
print(inputs.text)
button.click()