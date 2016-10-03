import requests, time
from bs4 import BeautifulSoup

headers = {
   'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
   'Cookie' : 'ganji_xuuid=0c4a063d-0ac1-40ce-e752-ecaf30b844bb.1470646356471'

}
url = 'http://huanggang.ganji.com/wu/'
url_host = 'http://huanggang.ganji.com'
data = requests.get(url, headers=headers)
# print  data.content

soup = BeautifulSoup(data.content, 'lxml')
links = soup.select( 'div.content > div > div > dl > dd > a')

item_links = soup.select( 'div.content > div > div > dl > dt > a')
# print item_links
# print links

link_list = []
for link in links:
    link_list.append(url_host + link.get('href'))

for link in item_links:
    link_list.append(url_host + link.get('href'))


channel_list ='''http://huanggang.ganji.com/chuangdian/
http://huanggang.ganji.com/guizi/
http://huanggang.ganji.com/zhuoyi/
http://huanggang.ganji.com/shafachaji/
http://huanggang.ganji.com/zixingchemaimai/
http://huanggang.ganji.com/diandongche/
http://huanggang.ganji.com/motuoche/
http://huanggang.ganji.com/iphone/
http://huanggang.ganji.com/nokia/
http://huanggang.ganji.com/htc/
http://huanggang.ganji.com/sanxingshouji/
http://huanggang.ganji.com/motorola/
http://huanggang.ganji.com/shouji/_%E5%B0%8F%E7%B1%B3/
http://huanggang.ganji.com/shouji/_%E9%AD%85%E6%97%8F/
http://huanggang.ganji.com/tongxuntaocan/
http://huanggang.ganji.com/qqhao/
http://huanggang.ganji.com/bangongjiaju/
http://huanggang.ganji.com/jiguangyitiji/
http://huanggang.ganji.com/dayinji/z1/
http://huanggang.ganji.com/shipinjiagongshebei/
http://huanggang.ganji.com/shengchanjiamengshebei/
http://huanggang.ganji.com/jichuang/
http://huanggang.ganji.com/tuolaji/
http://huanggang.ganji.com/dianshi/
http://huanggang.ganji.com/bingxiang/
http://huanggang.ganji.com/kongtiao/
http://huanggang.ganji.com/reshuiqi/
http://huanggang.ganji.com/xiyiji/
http://huanggang.ganji.com/diancilu/
http://huanggang.ganji.com/weibolu/
http://huanggang.ganji.com/yueqiyinxiang/
http://huanggang.ganji.com/pingbandiannao/z1/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_%E8%8B%B9%E6%9E%9C/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_%E8%81%94%E6%83%B3/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_Thinkpad/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_%E7%B4%A2%E5%B0%BC/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_%E6%88%B4%E5%B0%94/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_%E5%8D%8E%E7%A1%95/
http://huanggang.ganji.com/ershoubijibendiannao/z1/_%E6%83%A0%E6%99%AE/
http://huanggang.ganji.com/yueqi/
http://huanggang.ganji.com/yinxiang/
http://huanggang.ganji.com/yundongqicai/
http://huanggang.ganji.com/tongche/
http://huanggang.ganji.com/tongzhuang/
http://huanggang.ganji.com/yingerche/
http://huanggang.ganji.com/yingerchuang/z1/
http://huanggang.ganji.com/niaobushi/
http://huanggang.ganji.com/wanju/
http://huanggang.ganji.com/naifen/
http://huanggang.ganji.com/taishidiannaozhengji/
http://huanggang.ganji.com/xianka/
http://huanggang.ganji.com/cpu/
http://huanggang.ganji.com/yingpan/
http://huanggang.ganji.com/luyouqi/
http://huanggang.ganji.com/3gwangka/
http://huanggang.ganji.com/shoucangpin/
http://huanggang.ganji.com/qitalipinzhuanrang/
http://huanggang.ganji.com/baojianpin/
http://huanggang.ganji.com/xiaofeika/
http://huanggang.ganji.com/fushi/
http://huanggang.ganji.com/xiangbao/
http://huanggang.ganji.com/xuemao/
http://huanggang.ganji.com/shoubiao/
http://huanggang.ganji.com/shipin/
http://huanggang.ganji.com/huazhuangpin/
http://huanggang.ganji.com/hufupin/
http://huanggang.ganji.com/shumaxiangji/
http://huanggang.ganji.com/shumashexiangji/
http://huanggang.ganji.com/youxiji/
http://huanggang.ganji.com/suishenting/
http://huanggang.ganji.com/yidongcunchu/
http://huanggang.ganji.com/zibubaojian/z2/
http://huanggang.ganji.com/anmobaojian/z1/
http://huanggang.ganji.com/bawanwujian/
http://huanggang.ganji.com/zhuanqu_anjia/all/
http://huanggang.ganji.com/zhuanqu_jiaren/all/
http://huanggang.ganji.com/zhuanqu_shenghuo/all/
http://huanggang.ganji.com/jiaju/
http://huanggang.ganji.com/rirongbaihuo/
http://huanggang.ganji.com/shouji/
http://huanggang.ganji.com/shoujihaoma/
http://huanggang.ganji.com/bangong/
http://huanggang.ganji.com/nongyongpin/
http://huanggang.ganji.com/jiadian/
http://huanggang.ganji.com/ershoubijibendiannao/
http://huanggang.ganji.com/ruanjiantushu/
http://huanggang.ganji.com/yingyouyunfu/
http://huanggang.ganji.com/diannao/
http://huanggang.ganji.com/xianzhilipin/
http://huanggang.ganji.com/fushixiaobaxuemao/
http://huanggang.ganji.com/meironghuazhuang/
http://huanggang.ganji.com/shuma/
http://huanggang.ganji.com/laonianyongpin/
http://huanggang.ganji.com/xuniwupin/
http://huanggang.ganji.com/qitawupin/
http://huanggang.ganji.com/ershoufree/
http://huanggang.ganji.com/wupinjiaohuan/'''

cha_list = channel_list.split('\n')
# print cha_list

if __name__ == '__main__':
    print link_list
    for i in link_list:
        print i






'''
#wrapper > div.content > div:nth-child(3) > div:nth-child(1) > dl > dd > a:nth-child(1)
#wrapper > div.content > div:nth-child(2) > div:nth-child(2) > dl > dd > a:nth-child(2)
#wrapper > div.content > div:nth-child(5) > div:nth-child(1) > dl > dt > a:nth-child(1)
#wrapper > div.content > div:nth-child(2) > div:nth-child(1) > dl > dt > a
#wrapper > div.content > div:nth-child(6) > div > dl > dd > a:nth-child(1)
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36
Name
Cookie:ganji_xuuid=0c4a063d-0ac1-40ce-e752-ecaf30b844bb.1470646356471; ganji_uuid=5805657680927540348534; citydomain=huanggang; hotPriceTip=1; lg=1; crawler_uuid=147071464364269660454657; GANJISESSID=b56258f6fb60690f4ef78d800da98caa; __utmganji_v20110909=0xe00891dcdf7e4e861bbdb650cb2eb38; _gj_txz=MTQ3MDcxNTI1MDoOabJcXi3wT81SqJHHfvZOWNKotg==; __utmt=1; ganji_login_act=1470714866513; __utma=32156897.1628782060.1470646357.1470710719.1470714650.5; __utmb=32156897.5.10.1470714650; __utmc=32156897; __utmz=32156897.1470714650.5.5.utmcsr=wap.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/sorry/confirm.php; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22se%22%2C%22ca_kw%22%3A%22%25E8%25B5%25B6%25E9%259B%2586%25E7%25BD%2591%7Cutf8%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22sem_baidu%22%2C%22ca_n%22%3A%2234761383978%22%2C%22ca_i%22%3A%22ad%22%2C%22sid%22%3A36398638781%7D


'''

