from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions()) as driver:
    driver.get("https://news.naver.com/")

    xpath = '//*[@id="ct"]/div/section[1]/div[2]/div/div[1]/div[2]'
    eList = driver.find_elements(By.XPATH, value=xpath)

    for e in eList:
        print(e.text)