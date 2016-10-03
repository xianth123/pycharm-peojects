# -*- coding: utf-8 -*-
''' 这些代码实现了程序请求的上下文'''

from flask import Flask, request
from flask.ext.script import Manager

app = Flask(__name__)

manger = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' %user_agent

if __name__ == '__main__':
    manger.run()

'''Your browser is Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'''

'''Your browser is Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'''