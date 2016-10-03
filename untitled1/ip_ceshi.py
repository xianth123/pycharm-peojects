import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ip = client['ip']
ip_url = ip['ip_url']

ip_url.remove({'url':'121.33.226.167:3128'})
for i in  ip_url.find():
    print i['url']

print ip
def panduan_ip (url):
    print url
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'lxml')
    ip_data = soup.title

    i = 'ERROR' in ip_data.get_text()
    return i


# ip_url.remove({'url':'121.33.226.167:3128'})
for i in  ip_url.find():
    url = 'http://' + i['url']
    try:
        if panduan_ip(url):
            ip_url.remove({'url': i['url']})
    except:
        ip_url.remove({'url': i['url']})



# print panduan_ip('http://41.76.44.76:3128/')

'''
121.33.226.167:3128
'''