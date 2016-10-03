# -*- coding: utf-8 -*-
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    print username
    password = request.form['password']
    print password
    if username== '123' and password == '123':
        return render_template('signin_ok.html', username=username)
    else:
        return render_template('form.html', message = 'username or password error', username=username)

if __name__ == "__main__":
    app.run()

# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('home.html')
#     return '<h1>Hwllo World</h1>'
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return render_template('form.html')
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     #receive the data from submit
#     username = request.form['username']
#     password = request.form['password']
#     if username=='admin' and password=='password':
#         return render_template('signin-ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)
#
# if __name__ == '__main__':
#     app.run()