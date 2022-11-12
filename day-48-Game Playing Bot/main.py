from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = 'C:/Users/Mohamad Ja/Desktop/chromedriver'
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get(url='https://orteil.dashnet.org/cookieclicker/')
time.sleep(10)
lang = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang.click()
time.sleep(10)
button = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
while True:
    button.click()
