# -*- coding=utf-8 -*-
import urllib2
import cookielib


# 建立一个cj对象
filename = 'filecook.txt'
cookie = cookielib.MozillaCookieJar(filename)
# 把cookie带入到handler中,handler是一个实例
handler = urllib2.HTTPCookieProcessor(cookie)
# print type(handler)
# 利用该handler构建特殊的opener,该opener也是一个特殊的实例
opener = urllib2.build_opener(handler)
# 使用该opener，cookie会自动存储下来
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

for item in cookie:
    print 'name = '+ item.name
    print 'value ='+ item.value

# print cookie
# print type(opener)