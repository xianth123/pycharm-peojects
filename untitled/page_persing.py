import requests, time, pymongo
from bs4 import  BeautifulSoup

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']
item_info = ceshi['item_info']

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.title.text
    price = soup.select('span.price_now > i')[0].text if soup.select('span.price_now > i') != [] else None
    data = soup.select('span.look_time')[0].text if soup.select('span.look_time')  != [] else None
    area = soup.select('div.palce_li > span > i')[0].text if soup.select('div.palce_li > span > i')  != [] else None
    return {'title': title, 'price': price, 'data': data, 'area': area}
    #item_info.insert_one({'title': title, 'price': price, 'data': data, 'area': area})

def get_link_from (channel, page):

    list_view = '%s/pn%s/' % (channel, str(page))
    wb_data = requests.get(list_view)
    time.sleep(2)
    soup =BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td','t'):
        print 'done'
        for link in soup.select('td.t a.t'):
            print link
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            info_data = get_item_info(item_link)
            item_info.insert_one(dict({'url': item_link}, **info_data))
            print item_link
    else:
        pass

if __name__ == '__main__':

    get_link_from('http://hg.58.com/pbdn/', 2)





    #get_item_info('http://zhuanzhuan.58.com/detail/760773199008694276z.shtml')




    #for item in url_list.find():
     #   print item



    #infolist > div.infocon > table > tbody > tr:nth-child(4) > td.t > a