# -*- coding: utf-8 -*-
from flask.ext.wtf import Form                                          #导入表单
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class NameForm(Form):                                                   #表单类
    name = StringField("What is your name?", validators=[Required()])
    password = StringField("password")
    submit = SubmitField("Submit")
