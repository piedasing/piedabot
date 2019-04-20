import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from selenium import webdriver

def weather(area):
    target_url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/' + area +'_City.htm'
    driver = webdriver.PhantomJS(executable_path=r'.\phantomjs.exe') # 導入PhantomJS路徑
    driver.get(target_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = ""
    for data in soup.select('#ftext'):
        title = str(data)
        content = title.split("<br/><br/>")[2]

    return content

# import requests
# from bs4 import BeautifulSoup

# # 下載 Yahoo 首頁內容
# r = requests.get('https://www.cwb.gov.tw/V8/C/')

# # 確認是否下載成功
# if r.status_code == requests.codes.ok:
#   # 以 BeautifulSoup 解析 HTML 程式碼
#   soup = BeautifulSoup(r.text, 'html.parser')

#   # 以 CSS 的 class 抓出各類頭條新聞
#   weather = soup.findAll('div', attrs={'class', 'cube_weather'})
#   print(weather)
#   # for s in stories:
#   #   # 新聞標題
#   #   print("標題：" + s.text)
#   #   # 新聞網址
#   #   print("網址：" + s.get('href'))
