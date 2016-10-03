# -*- coding: utf-8 -*-
import requests, time
from bs4 import BeautifulSoup
import pymongo
import json
from ganji_url import cha_list

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_lists = ganji['url_lists']
# 每个物品的主页链接
item_info = ganji['item_info']
# 每个物品的详细信息列表

link = cha_list   # 导入商品总目录连接
# print ganji_url.link_list

headers = {

}


# 输入主页链接列表， 输出单页所有商品连接的列表
def get_url (url):
    page_link_list = []
    for i in url:
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'lxml')
        page_url = soup.select('div.leftBox > div.layoutlist > dl > dd > div > ul > li > div > a')
        for link in page_url:
            page_link_list.append(link.get('href'))
            url_lists.insert_one({'url': link.get('href')})
    return  page_link_list

# 输入主页连接，得到商品的页数的连接列表
def get_yema_link (url, page = 100):
    yema_link_list = [url]
    '''
    #wrapper > div.leftBox > div.pageBox > ul > li:nth-child(6) > a > span
    #wrapper > div.leftBox > div.pageBox > ul > li:nth-child(2) > a > span
    #wrapper > div.leftBox > div.pageBox > ul > li:nth-child(1) > a > span
    #wrapper > div.leftBox > div.pageBox > ul > li:nth-child(5) > a > span
    '''

    for i in range(2, page+1):       # for 循环遍历数字要用range
        # 初始值变量不可以随便调用
        page_url = url + 'o%s/'  % (str(i))
        print page_url
        yema_link_list.append(page_url)
        time.sleep(0.5)
        data = requests.get(page_url)
        soup = BeautifulSoup(data.content, 'lxml')
        xiayiye = soup.select('#wrapper > div.leftBox > div.pageBox > ul > li > a > span')
        # print type(xiayiye[-2].get_text())
        # 判断是否有下一页
        print xiayiye
        if len(xiayiye) < 2:
            break
        elif xiayiye[-2].get_text() == str(i) :
            # 方法即使没有参数也要交括号
            break
        else:
            continue
    return yema_link_list

# 输入商品页链接列表，返回商品详细信息
def get_item_info(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')
    tits = soup.select('div.content.clearfix > div.leftBox > div.col-cont.title-box > h1')
    times = soup.select('div.content.clearfix > div.leftBox > div.col-cont.title-box > div > ul.title-info-l.clearfix > li:nth-of-type(1) > i')
    types = soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(3) > div > ul > li:nth-of-type(1) > span > a')
    prices = soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(3) > div > ul > li:nth-of-type(2) > i.f22.fc-orange.f-type')
    area = soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(3) > div > ul > li:nth-of-type(3) > a')
    miaoshu = soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(4) > div.det-summary > div > div')
    # print tits[0].get_text(), times[0].get_text().strip(),types[0].get_text().strip(), prices[0].get_text().strip()
    # print area, '\n', miaoshu[0].get_text()
    data_dict = {
        'title' : tits[0].get_text(),
        'time'  : times[0].get_text().strip(),
        'type'  : types[0].get_text().strip(),
        'price' : prices[0].get_text().strip(),
        'area'  : [i.get_text() for i in area],
        '描述信息' : miaoshu[0].get_text().strip()

    }
    item_info.insert_one(data_dict)
    print json.dumps(data_dict, ensure_ascii= False, encoding='UTF-8')
    # print data

# 一步到位，加载所有商品链接到数据库，无返回值
def inser_all_links ():
    print 'done'
    mulu_list = []
    print link
    for i in link:
        print i
        time.sleep(2)
        mulu_list.append(get_yema_link(i))
    print mulu_list
    return mulu_list




if __name__ == '__main__':
    # get_item_info('http://huanggang.ganji.com/shouji/2269849336x.htm')
    inser_all_links()


    print get_yema_link('http://huanggang.ganji.com/chuangdian/')





'''
body > div.box.wrapper.clearfix > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h3
body > div.box.wrapper.clearfix > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h3
#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1
#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1
#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > div > ul.title-info-l.clearfix > li:nth-child(1) > i
#wrapper > div.content.clearfix > div.leftBox > div:nth-child(3) > div > ul > li:nth-child(1) > span > a
#wrapper > div.content.clearfix > div.leftBox > div:nth-child(3) > div > ul > li:nth-child(2) > i.f22.fc-orange.f-type
#wrapper > div.content.clearfix > div.leftBox > div:nth-child(3) > div > ul > li:nth-child(3) > a:nth-child(2)
#wrapper > div.content.clearfix > div.leftBox > div:nth-child(3) > div > ul > li:nth-child(3) > a:nth-child(3)
#wrapper > div.content.clearfix > div.leftBox > div:nth-child(4) > div.det-summary > div > div
'''


# print get_yema_link('http://huanggang.ganji.com/chuangdian/')



# url = 'http://huanggang.ganji.com/chuangdian/o12/'
# data = requests.get(url)
# soup = BeautifulSoup(data.content, 'lxml')
# xiayiye = soup.select('div.leftBox > div.pageBox > ul > li > a > span')
# print xiayiye[-2].get_text()




'''
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(1) > dd.zzfeature > div > ul > li > div > a
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(8) > dt > a > img
#wrapper > div.leftBox > div.layoutlist > dl:nth-child(10) > dd.zzfeature > div > ul > li > div > a
#wrapper > div.leftBox > div.pageBox > ul > li:nth-child(8) > a > span
#wrapper > div.leftBox > div.pageBox > ul > li:nth-child(1) > a > span
'''