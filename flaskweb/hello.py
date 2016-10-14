#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, session, url_for, redirect, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment,datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
from threading import Thread

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#邮箱配置
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PROT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "xianth123@qq.com"
app.config['MAIL_PASSWORD'] = "qmozujeaouqdgadg"
app.config['MAIL_DEBUG'] = True
mail = Mail(app)

db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'lizhixi'
manger = Manager(app)

manger.add_command('db', MigrateCommand)

#发送邮件的函数
def send_emial(to, subject, template, **kwargs):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.html', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)



class Role(db.Model):
    '''定义角色的数据库模型'''
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role') #自身添加一个user属性，反过来给User添加一个role属性。属性可以赋值。

    def __repr__(self):
        '''打印角色名字'''
        return '<Role %r>' % self.name

class User(db.Model):
    '''定义使用者的数据库模型'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #为user表中添加添加一行外键，由该属性可以获得使用者的角色所对应的id值。

    def __repr__(self):
        '''打印使用者的名字'''
        return '<User %r>' % self.username





class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manger.add_command('shell', Shell(make_context=make_shell_context))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        print 'before query data'
        user =User.query.filter_by(username=form.name.data).first()
        print "after query data"
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            flash('Welcome to you ')
            send_emial('xianth123@qq.com', 'Nwe User', 'mail/new_user', user=form.name.data)
        else:
            session['known'] = True
            flash('See you again!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False),
                           current_time=datetime.utcnow())

if __name__ == "__main__":
    manger.run()




