# encoding=utf8
import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import time
session = requests.session()
session.cookies = cookielib.MozillaCookieJar(filename= 'cookies')
for i in range(20):
    time.sleep(3)
    session.cookies.load('cookies', ignore_discard=True)
    agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    headers = {
        'User-Agent': agent
    }
    html = session.get('https://www.zhihu.com/people/xianth/followers', headers =headers)
    # with open('html.txt','wb') as f:
    #     f.write(str(html.text))
    # print(html.text)

    soup = BeautifulSoup(html.text, 'lxml')
    names = soup.select('#zh-profile-follows-list > div > div > div.zm-list-content-medium > h2 > span > a')
    for name in names:
        print('done')
        print(name['title'])
    session.cookies




# data = requests.get('https://www.zhihu.com/people/xianth/followers')
#
# soup = BeautifulSoup(data.text, 'lxml')
#
# print soup