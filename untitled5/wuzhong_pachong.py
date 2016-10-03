# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import http.cookiejar as coolielib

session = requests.session()
session.cookies =coolielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load()
except:
    print('cookies未能得到加载')

html = session.get('http://www.hbswxzx.com/Alumni/My.asp?rel=VPer')
soup = BeautifulSoup(html.text, 'lxml')
names = soup.select('body > table > tbody > tr > td > div > table: > tbody > tr:nth-of-type(4) > td:nth-of-type(2)')
# name = names[0].get_text()
try:
    print(names)
except:
    print('未知错误')
with open('html.txt', 'w+') as f:
    f.write(str(html.text.encode('UTF-8')))
print(html.text.encode('GBK'), 'UTF-8')
print('李志席')

session.cookies.load()
'''body > table:nth-child(4) > tbody > tr > td:nth-child(2) > div > table:nth-child(2) > tbody > tr:nth-child(4) > td:nth-child(2)'''