# -*- coding: utf-8 -*-
import time, requests, random
from bs4 import BeautifulSoup
from get_ip import str_ip

def panduan_ip (url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'lxml')
    ip_data = soup.title

    i = 'ERROR' in ip_data.get_text()
    return i

headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}

'''
proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
    ]

    218.240.129.243:3128
'''

proxy_list = str_ip

# proxy_ip = random.choice(proxy_list)
# proxies = {'http': 'http://' + proxy_ip}

def get_yema_link(url, page = 100):
    yema_link_list = []
    for i in range(1, page+1):       # for 循环遍历数字要用range
        # 初始值变量不可以随便调用
        # http://huanggang.ganji.com/guizi/o2/
        # ip地址的获取也用该纳入循环中
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': 'http://' + proxy_ip}

        # while panduan_ip(proxies['http']):
        #     print proxies
        #     proxy_ip = random.choice(proxy_list)
        #     proxies = {'http': 'http://' + proxy_ip}


        page_url = '%s%s%s/'  % (url, 'o', str(i))
        print page_url
        yema_link_list.append(page_url)
        time.sleep(0.5)
        # 定位是哪个ip被限制了
        ip = proxies
        print ip
        data = requests.get(page_url, headers = headers)

        soup = BeautifulSoup(data.content, 'lxml')
        item_url = soup.select('#wrapper > div.leftBox > div.layoutlist > dl > dd > div > ul > li  a')
        # 使用列表解析式来取出item_url中的连接列表，并且去除‘javascript：’
        item_url_list = [i.get('href') for i in item_url if i.get('href') != 'javascript:']
        if item_url_list == []:
            continue
        print  item_url_list,'\n', len(item_url_list)
        xiayiye = soup.select('#wrapper > div.leftBox > div.pageBox > ul > li > a > span')
        # print type(xiayiye[-2].get_text())
        # 判断是否有下一页
        print xiayiye
        print [x.get_text() for x in xiayiye]
        if u'\u4e0b\u4e00\u9875' in [x.get_text() for x in xiayiye]:
            # u'\u4e0b\u4e00\u9875' 是中文‘下一页’的unicode的编码
            continue
        else:
            break
        # if len(xiayiye) < 2:
        #     break
        # elif xiayiye[-2].get_text() == str(i) :
        #     # 方法即使没有参数也要交括号
        #     break
        # else:
        #     continue
    return yema_link_list

print get_yema_link('http://huanggang.ganji.com/motuoche/')

# x = '下一页' in ['下一页', 'wewr',1233]
# print  x

'''
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(1) > dt > a > img
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(1) > dd.feature > div > ul > li > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(4) > dd.feature > div > ul > li > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(65) > dt
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(65) > dd.feature > div > ul > li > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(5) > dd.zzfeature > div > ul > li > div > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(4) > dd.feature > div > ul > li > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(10) > dd.feature > div > ul > li > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(8) > dd.zzfeature > div > ul > li > div > a
'''