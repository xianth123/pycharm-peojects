#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm
from ..email import send_emial
from flask_login import current_user



@auth.before_app_request
def before_request():
    print request.endpoint
    if current_user.is_authenticated:
        current_user.ping()
        if current_user.is_authenticated \
                and not current_user.confirmed \
                and request.endpoint[:5] != 'auth.':
            return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')



@auth.route('/login', methods=['GET','POST'])
#登陆界面
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
#登出
@login_required
def logout():
    logout_user()
    flash('you had been logged out!')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['POST', 'GET'])
#注册界面。成功之后系统会发送确认邮件
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        print '--------------------------------------------------------------------------------------------------'
        token = user.generate_confirmation_token()
        print "***************************************************************************************************"
        send_emial(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
        print '####################################################################################################'
        flash('you can now login!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('you have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_emial(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user,token=token)
    flash('A new confirmation email has been sent to your email.')
    return redirect(url_for('main.index'))



















