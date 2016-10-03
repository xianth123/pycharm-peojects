# -*- coding: utf-8 -*-
'''这些代码实现了从表单中读取用户名，并且存入数据库。对应python flask web 第五章'''
from flask import Flask, render_template, session, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.bootstrap import Bootstrap                               #导入 Bootstrap

from flask.ext.wtf import Form                                          #导入表单
from wtforms import StringField, SubmitField, PasswordField
from  wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'xianth'

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')                   #使用join拼接路径  创建文件
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)                          #创建表中的行
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r' % self.username


class NameForm(Form):                                                   #表单类
    name = StringField("What is your name?", validators=[Required()])
    password = StringField("password")
    submit = SubmitField("Submit")

print 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = NameForm()
    name = 'lizhixi'
    known = False
    print 'mmmmmmmmmmmmmmmmmmmm'
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('home_page'))

    return render_template('hello.html', form=form, name=session.get('name'), known=session.get('known', False))


if __name__ == "__main__":
    app.run()