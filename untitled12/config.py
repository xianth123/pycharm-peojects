# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'xianth'                                       #导入表单

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True                        #数据库配置

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'                     #邮件设置
    FLASKY_MAIL_SENDER = 'Flasky Admin <bgd131212@163.com>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False                      #书上没有的 自己添加
    @staticmethod                                               #静态方法
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # 通用配置
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'                                 #邮件配置
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'xianth123@qq.com'
    MIAL_PASSWORD = 'xianth19950926'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')   #数据库配置


class TestingConfig(Config):
    #测试配置
    TSETING =True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')   #数据库配置


class ProductionConfig(Config):
    #生产配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')   #数据库配置

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default':  DevelopmentConfig
}































