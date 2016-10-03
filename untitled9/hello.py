# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, url_for, redirect                    #导入flask

from flask.ext.bootstrap import Bootstrap                               #导入 Bootstrap

from flask.ext.wtf import Form                                          #导入表单
from wtforms import StringField, SubmitField, PasswordField
from  wtforms.validators import Required

from flask.ext.moment import Moment                                     #导入时间戳
from datetime import datetime

from flask.ext.mail import Mail, Message

import os



app = Flask(__name__)                                                     #导入flask
bootstrap = Bootstrap(app)                                                #导入 Bootstrap
moment = Moment(app)                                                      #导入时间戳
app.config['SECRET_KEY'] = 'xianth'                                       #导入表单

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'xianth123@qq.com'
app.config['MIAL_PASSWORD'] = 'xianth19950926'

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <bgd131212@163.com>'


mail = Mail(app)

def send_email (to, subject, template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender = app.config['FLASKY_MAIL_SENDER'], recipients = [to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)



class NameForm(Form):                                                   #表单类
    name = StringField("What is your name?", validators=[Required()])
    password = StringField("password")
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def home():
    name = 'Lizhixi'
    form = NameForm()
    if form.validate_on_submit():                                         #描述一个动作
        name = form.name.data
        bute = form.password.data
        password = form.password.data
        form.password.data = ''                                           #清空表单
        form.name.data = ''
    return render_template('home.html', form=form, name=name, current_time=datetime.utcnow())




if __name__ == "__main__":
    app.run()




