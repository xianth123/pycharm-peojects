import requests
from bs4 import  BeautifulSoup
import json

html_url = "http://hg.58.com/sale.shtml"
url_host = 'http://hg.58.com'

def get_channel_url(url):
    wb_data = requests.get(html_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('ul > li > ul > li > b > a')
    for link in links:
        url = url_host + link.get('href')
        print url


#get_channel_url(html_url)

channel_list ='''
http://hg.58.com/tongxunyw/
http://hg.58.com/danche/
http://hg.58.com/fzixingche/
http://hg.58.com/diandongche/
http://hg.58.com/sanlunche/
http://hg.58.com/peijianzhuangbei/
http://hg.58.com/diannao/
http://hg.58.com/bijiben/
http://hg.58.com/pbdn/
http://hg.58.com/diannaopeijian/
http://hg.58.com/zhoubianshebei/
http://hg.58.com/shuma/
http://hg.58.com/shumaxiangji/
http://hg.58.com/mpsanmpsi/
http://hg.58.com/youxiji/
http://hg.58.com/jiadian/
http://hg.58.com/dianshiji/
http://hg.58.com/ershoukongtiao/
http://hg.58.com/xiyiji/
http://hg.58.com/bingxiang/
http://hg.58.com/binggui/
http://hg.58.com/chuang/
http://hg.58.com/ershoujiaju/
http://hg.58.com/bangongshebei/
http://hg.58.com/diannaohaocai/
http://hg.58.com/bangongjiaju/
http://hg.58.com/ershoushebei/
http://hg.58.com/yingyou/
http://hg.58.com/yingeryongpin/
http://hg.58.com/muyingweiyang/
http://hg.58.com/muyingtongchuang/
http://hg.58.com/yunfuyongpin/
http://hg.58.com/fushi/
http://hg.58.com/nanzhuang/
http://hg.58.com/fsxiemao/
http://hg.58.com/xiangbao/
http://hg.58.com/meirong/
http://hg.58.com/yishu/
http://hg.58.com/shufahuihua/
http://hg.58.com/zhubaoshipin/
http://hg.58.com/yuqi/
http://hg.58.com/tushu/
http://hg.58.com/tushubook/
http://hg.58.com/wenti/
http://hg.58.com/yundongfushi/
http://hg.58.com/jianshenqixie/
http://hg.58.com/huju/
http://hg.58.com/qiulei/
http://hg.58.com/yueqi/
http://hg.58.com/chengren/
http://hg.58.com/nvyongpin/
http://hg.58.com/qinglvqingqu/
http://hg.58.com/qingquneiyi/
http://hg.58.com/chengren/
http://hg.58.com/xiaoyuan/
http://hg.58.com/ershouqiugou/
http://hg.58.com/tiaozao/'''

channel_list2 = channel_list.split('\n')[1:]
