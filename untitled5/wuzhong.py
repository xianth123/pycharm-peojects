import requests
from bs4 import BeautifulSoup
from PIL import Image
import http.cookiejar as coolielib

agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
headers ={'User-Agent': agent, 'Connection': 'keep-alive'}

session =requests.session()
session.cookies = coolielib.LWPCookieJar(filename= 'cookies')


url = 'http://www.hbswxzx.com/Alumni/Include/ShowCode.asp'
data = session.get(url, headers = headers)
session.cookies.save(ignore_discard=True)
with open('captcha.jpg', 'wb') as f:
    f.write(data.content)

im = Image.open('captcha.jpg')
im.show()
im.close()
yzm = input('请输入验证码\n')

data = { 'xm': 'xian', 'mima': 'xianth', 'yzm': yzm}
session.cookies.load()

post_url = 'http://www.hbswxzx.com/Alumni/Query.asp?act=LoginSave'

html = session.post(post_url,data=data, headers =headers)
session.cookies.save(ignore_discard=True)
# html = session.get('http://www.hbswxzx.com/Alumni/My.asp?rel=VPer')
# soup = BeautifulSoup(html.text, 'lxml')
print(html.text)

# user_name = soup.select('body > table:nth-of-type(4) > tbody > tr > td:nth-of-type(2) > div > table:nth-of-type(2) > tbody > tr:nth-of-type(4) > td:nth-of-type(2)').get_text()
# print(user_name)




'''获取验证码'''

# soup = BeautifulSoup(html.text, 'lxml')



'''
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36
Query String Parameters
view source
view URL encoded
body > table:nth-child(4) > tbody > tr > td > table > tbody > tr > td:nth-child(2) > table:nth-child(1) > tbody > tr > td > table > tbody > tr:nth-child(6) > td:nth-child(2) > img
'''