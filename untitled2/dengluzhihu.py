# encoding=utf8
import cookielib
import urllib2
import urllib

url_start = r'https://www.zhihu.com/topic/19556498/questions?page='
filename = 'cookie.txt'
cj = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# opener.add_handler([('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0')])
opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0')]

def login():
    username = 'xianth123@qq.com'
    password = 'xianth123456'
    cap_url = 'https://www.zhihu.com/captcha.gif?r=1466595391805&type=login'
    # cap_content = urllib2.urlopen(cap_url).read()
    cap_content = opener.open(cap_url).read()
    cj.save(ignore_discard= True, ignore_expires= True)

    cap_file = open('C:/Users/jd/Desktop/cap.png','wb')
    cap_file.write(cap_content)
    cap_file.close()
    # 写入验证码
    captcha = raw_input('capture:')
    url = 'https://www.zhihu.com/login/phone_num'
    data = urllib.urlencode({"phone_num":username,"password":password,"captcha":captcha})
    print opener.open(url,data).read()

if __name__=="__main__":
    login()











