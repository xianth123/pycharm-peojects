# -*- coding: utf-8 -*-
from flask import Flask,redirect,render_template,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from  flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required           #导入表单模块

from datetime import datetime



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KRY'] = 'xianth'

class NameForm(Form):                                               #中的form类
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/',methods=['GET', 'POST'])           #最简单的flask模型   主页面
def hello_world():                                                  #最简单的flask模型   主页面
    return render_template('zhuyemian.html',
                            current_time=datetime.utcnow())

@app.route('/signin',methods=['GET'])                              #表单登录
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['GET', 'POST'])                              #表单登录
def signin():
    #receive the data from the forms
    username = request.form.get('username')
    print request.form.get('username')
    password = request.form.get('password')
    print request.form.get('password')
    if username=='lizhixi' and password == 'password':              #登录成功，返回成功页面
        return render_template('signin-ok.html', username=username)
    else:                                                            #登录失败，返回错误信息
        return render_template('zhuyemian.html', message='Bad username or password!', username=username)
                                                                     #render_template()函数可以向模版种传入参数

@app.route('/zhihu')         #重定向到知乎
def zhihu():                                                         #重定向到知乎
    return redirect('http://www.zhihu.com')

@app.route('/sanjiao')
def sanjiao():
    return render_template('sanjiaoxing.html')            #返回一个页面，把动态内容传入进去，嗯，nice！

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page500(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

