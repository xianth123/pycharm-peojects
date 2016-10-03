# -*- coding: utf-8 -*-
'''发送邮件的flask！'''
from flask.ext.mail import Mail, Message
from flask import Flask, render_template, session, url_for, redirect


app = Flask(__name__)



app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PROT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "xianth123@qq.com"
app.config['MAIL_PASSWORD'] = "qmozujeaouqdgadg"
app.config['MAIL_DEBUG'] = True

mail = Mail(app)

@app.route('/')
def index():

    msg = Message("Hi,This is a test", sender="xianth123@qq.com",
                  recipients=["15387190711@163.com"])
    print "wwwwwwwwwwww"
    msg.body = "this is a first mail."
    print "mmmmmmmmmmmm"
    mail.send(msg)
    print "mail send"
    return "<h1>Sent</h1>"


if __name__ == "__main__":
    app.run()