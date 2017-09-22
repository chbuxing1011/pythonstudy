#!/usr/bin/python
# -*- coding: utf-8 -*-

#http://127.0.0.1:5000/

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
		return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
		print('get signin')
		return '''<form action="/signin" method="post">
							<p><input name="username"></p>
							<p><input name="password" type="password"></p>
							<p><button type="submit">Sign In</button></p>
							</form>'''

@app.route('/signin', methods=['POST'])
def signin():
		print('post signin')
		# 需要从request对象读取表单内容：
		if request.form['username']=='admin' and request.form['password']=='123456':
				return '<h3>Hello, admin!</h3>'
		return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
#	flask运行服务器后，会发现只有你自己的电脑可以使用服务，而网络中的其他电脑却不行。
#	缺省设置就是这样的，因为在调试模式下该应用的用户可以执行你电脑中的任意
#	Python 代码
		app.run(host='0.0.0.0', port=5000)
	
	