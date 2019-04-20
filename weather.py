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
