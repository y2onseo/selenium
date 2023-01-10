# 네이버 로그인 비밀번호 자동 완성
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.naver.com/")
e = driver.title

driver.find_element(By.CLASS_NAME, "link_login").click()

user = {'uid': 'leejisu2331', 'upw': 'rjawjd!0331'}

id1 = driver.find_element(By.ID, "id")
id1.click()
pyperclip.copy(user['uid'])
id1.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pw1 = driver.find_element(By.ID, "pw")
pw1.click()
pyperclip.copy(user['upw'])
pw1.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element(By.CLASS_NAME, "btn_login").click()

# nick = driver.find_element(By.CLASS_NAME, "link_set")

driver.close()
driver.quit()
print(e)
