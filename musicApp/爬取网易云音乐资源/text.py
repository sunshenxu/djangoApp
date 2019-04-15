#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
__data__ = '2019/4/13 20:36'
__author__ = 'shenxu'
import time
import pymysql
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

path = r'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
# path = r'D:\Python\selenium-PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# browser = webdriver.PhantomJS(executable_path=path)   #打开phantomjs浏览器
wait = WebDriverWait(browser,10)
try:
    url = 'https://music.163.com/#/song?id=1354477202'
    browser.get(url)
    browser.switch_to_frame('g_iframe')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#lyric-content')))
    # input = browser.find_element(By.CSS_SELECTOR, '#flag_ctrl')
    time.sleep(2)
    input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#flag_ctrl')))
    input.click()
    lyric_content = browser.find_element(By.CSS_SELECTOR, '#lyric-content').text
    print(lyric_content)

except TimeoutException:
    print("*******")