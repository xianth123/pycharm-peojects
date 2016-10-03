# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy                            #导入数据库
from flask.ext.bootstrap import Bootstrap                               #导入 Bootstrap
from flask.ext.mail import Mail, Message                               #导入mail
from flask.ext.moment import Moment                                     #导入时间戳
from datetime import datetime

from config import config                                              #导入配置



bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)


    #附加路由和自定义的错误页面

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
