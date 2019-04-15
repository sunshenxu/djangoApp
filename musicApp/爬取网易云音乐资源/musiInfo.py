#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
__data__ = '2019/4/13 10:18'
__author__ = 'shenxu'
import time
import pymysql
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing.pool import Pool
from selenium.webdriver.chrome.options import Options
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
# path = r'D:\Python\selenium-PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# browser = webdriver.PhantomJS(executable_path=path)   #打开phantomjs浏览器
wait = WebDriverWait(browser,10)

def save_mysql(data):
    db = pymysql.connect('localhost', 'root', '1525218978', 'musicdb')
    cursor = db.cursor()
    sql = "insert into music values(0,'%s','%s','%s','%s','%s','%s')" % (data['music_id'],data['music_name'],data['music_time'],data['music_outher'],data['lyric_content'],data['music_img'])
    print("正在保存数据库……",data['music_id'])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("保存数据库出错……",data['music_id'])
        db.rollback()
    cursor.close()
    db.close()


def get_words(music_list):
    for data in music_list:
        m_url= data['music_url']
        lyric_content,music_img = parse_words(m_url)
        data['lyric_content'] = lyric_content.replace('\n', '<br/>')
        data['music_img'] = music_img
        # print(music_img)
        # 保存进数据库
        save_mysql(data)
        time.sleep(2)

def parse_words(url):
    try:
        browser.get(url)
        browser.switch_to_frame('g_iframe')
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#lyric-content')))
        time.sleep(4)    #要等待一段时间，等js加载好了才能点击按钮
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cvrwrap')))
        music_img = browser.find_element(By.CSS_SELECTOR,'.cvrwrap .u-cover img').get_attribute('src')
        input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#flag_ctrl')))
        input.click()
        lyric_content = browser.find_element(By.CSS_SELECTOR, '#lyric-content').text
        return lyric_content,music_img
    except:
        return ' ',' '

def parse_info(url):
    try:
        browser.get(url)
        browser.switch_to_frame('g_iframe')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-table tbody')))
        info_list = browser.find_elements(By.CSS_SELECTOR, '.m-table tbody tr')
        music_list = []
        for info in info_list:
            m_url = info.find_element(By.CSS_SELECTOR,'.f-cb .tt .ttc .txt a').get_attribute('href')
            id = m_url.split('=')[-1]
            name = info.find_element(By.CSS_SELECTOR,'.f-cb .tt .ttc .txt a b').get_attribute('title')
            time = info.find_element(By.CSS_SELECTOR,'.s-fc3 span').text
            outher = info.find_element(By.CSS_SELECTOR,'td .text span').get_attribute('title')
            music = {
                'music_url':m_url,
                'music_id':id,
                'music_name':name,
                'music_time':time,
                'music_outher':outher
            }
            music_list.append(music)
        get_words(music_list)


            # print(music_id,music_name,music_time,music_outher,lyric_content)
            # browser.close()
            # exit()
    except:
        print("%s歌单响应超时爬取失败……" % url)

    # browser.close()
    # exit()


def parse_music(url):
    try:
        browser.get(url)
        browser.switch_to_frame('g_iframe')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#m-pl-container')))
        li_list = browser.find_elements(By.CSS_SELECTOR, '#m-pl-container li')
        music_list = []
        for li in li_list:
            music_list_url = li.find_element(By.CSS_SELECTOR,'.u-cover a').get_attribute('href')
            music_list.append(music_list_url)
        print(music_list)
        for music_url in music_list:
            parse_info(music_url)

    except:
        print("%s页响应超时爬取失败……" %url)


def main():
    url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset={}'
    for page in range(0,39):
        newUrl = url.format(page*35)
        # print(newUrl)
        print("爬取第%d页……" % page)
        try:
            parse_music(newUrl)
            print("第%d页爬取结束……" % page)
        except:
            print("出错")
    browser.close()

if __name__ == '__main__':
    main()
    #多进程爬取
    # pool = Pool(4)
    # groups = (x*35 for x in range(0,39))
    # pool.map(main,groups)
    # pool.close()
    # pool.join()


