#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import current_app, render_template
from flask_mail import Message
from threading import Thread
from . import mail


def send_async_email(app, msg):
    #发送邮件
    with app.app_context():
        #调用上下文
        mail.send(msg)
#此处代码不懂


def send_emial(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    #使用工厂函数调用app
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.html', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr





