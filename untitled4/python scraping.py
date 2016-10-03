# -*- coding=utf-8 -*-
import requests
from bs4 import  BeautifulSoup

# html = requests.get('http://baike.baidu.com/link?url=yyjuMH3OlZRm3zYox8vXbUsY_NzVFbgaoW82_A53Yn8HCUlACZt3JAv91whuBtt_r6imm2P2zGXyhzuU1Mb9w_')
# soup = BeautifulSoup(html.text, 'lxml')
#
# print(soup.find_all('a'))
#
# for link in soup.findAll('a'):
#     if 'title' in link.attrs:
#
#         print (type(link))
#         print (link.attrs['title'],type(link.attrs))

html = requests.get('http://www.dmoz.org/Computers/Programming/Languages/Python/Books/')
print (html)

        # '''//*[@id="content"]/h1
        # <h1>Darwin - The Evolution Of An Exhibition</h1>
        # <h1>Darwin - The Evolution Of An Exhibition</h1>
        # #content > h1'''
'''
#site-list-content > div:nth-child(1) > div.title-and-desc > a > div
'''