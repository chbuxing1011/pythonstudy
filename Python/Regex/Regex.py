#!/usr/bin/python
# -*- coding: utf-8 -*-

#re模块

import re

re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
	print 'ok'
else:
	print 'failed'
	
#切分字符串

print(re.split(r'\s+', 'a b   c'))

#分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.groups()
m.group(0)
m.group(1)

#贪婪匹配 正则匹配默认是贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()

#当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#
#编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#
#用编译后的正则表达式去匹配字符串。

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

re_telephone.match('010-12345').groups()