from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

instagram_username = ''
instagram_password = ''
the_page_of_your_followers = ''
path = 'C:/Users/Mohamad Ja/Desktop/chromedriver'
s = Service(path)
driver = webdriver.Chrome(service=s)

driver.get('https://www.instagram.com/')
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys(instagram_username)
password.send_keys(instagram_password)
sign_in = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
time.sleep(1)
sign_in.click()
time.sleep(10)
driver.get(f'{the_page_of_your_followers}followers/')
time.sleep(10)
follow_button = driver.find_elements(By.CLASS_NAME, '_acan')
for button in follow_button:
    try:
        button.click()
        time.sleep(0.5)
    except:
        pass

print("Done!")




