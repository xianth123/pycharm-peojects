# -*- coding: utf-8 -*-
# python 2

from bs4 import BeautifulSoup
import requests
import  os

url = 'https://mm.taobao.com/'

# data = requests.get(url)
# soup = BeautifulSoup(data.text, 'lxml')


def model_1(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'lxml')

    def zifu (a):
        s = a.split('\n')
        return s[1].strip() + '_' + s[2].strip()

    zhuye_links = soup.select('body > div.ladyRanking.J_LadyRanking > div.ladyRanking-items.J_huoyue.huoyue.clearfix > div > div > a')
    names = soup.select('body > div.ladyRanking.J_LadyRanking > div.ladyRanking-items.J_huoyue.huoyue.clearfix > div > div > div > p.ladyRanking-info')
    url_lists = []
    name_lists = []
    for i, j in zip(zhuye_links, names):
        url_lists.append('https:' + i.get('href'))
        name_lists.append(zifu(j.get_text()))
    # for m, n in zip(url_lists,name_lists):
    # print m, n

    return (url_lists,name_lists)


def built_file (m):
    for i in m[1]:
        os.mkdir(i)

def get_MM_photo(m):
    for u in m[0]:
        data = requests.get(u)
        soup = BeautifulSoup(data.text, 'lxml')
        photo_url = soup.select('')



def get_photo (u):
    data = requests.get(u)
    soup = BeautifulSoup(data.text, 'lxml')
    print data.text
    photo_url = soup.select('#J_ScaleImg > div:nth-of-type(10) > img')
    print photo_url








get_photo('https://mm.taobao.com/816580548.htm')

# 欠缺淘宝认证方法


# m =model_1(url)
# built_file(m)


'''
body > div.ladyRanking.J_LadyRanking > div.ladyRanking-items.J_huoyue.huoyue.clearfix > div:nth-child(1) > div > a  主页链接
body > div.ladyRanking.J_LadyRanking > div.ladyRanking-items.J_huoyue.huoyue.clearfix > div:nth-child(1) > div > a > img  封面图片连接
body > div.ladyRanking.J_LadyRanking > div.ladyRanking-items.J_huoyue.huoyue.clearfix > div:nth-child(1) > div > div > p.ladyRanking-info 模特名字
body > div.ladyRanking.J_LadyRanking > div.ladyRanking-items.J_huoyue.huoyue.clearfix > div:nth-child(1) > div > div > p.ladyRanking-info > span 模特地址
#J_ScaleImg > div:nth-child(10) > img:nth-child(1) 主页图片
#J_ScaleImg > div:nth-child(10) > img:nth-child(3)
'''