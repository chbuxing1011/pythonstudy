#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1
print('hello, world!')

print "1","2","3"

print "100 + 200 =", 100+200

name = raw_input("please enter your name:")

print "hello,",name

# 2
a = 100
if a >= 0:
	print(a)
else:
	print(-a)
	
print "I\'m \"OK\"!"

print '\\\n\\'

print '\\\t\\'
#用r''表示''内部的字符串默认不转义
print r'\\\t\\'

#多行
print '''line1
line2
line3'''

True
False
print 3>2
print 3>5
#布尔值可以用and、or和not运算。

age = 15
if age >= 18:
	print 'adult'
else:
	print 'teenager'
	
#变量修改
a = 'ABC'
b = a
a = 'XYZ'
print b


PI = 3.14159265359

print 10/3
print 10.0/3
print 10%3

#空值是Python里一个特殊的值，用None表示

print ord('A')
print chr(65)

print u"中文"
print u'中'
print u"中文".encode('utf-8')
print u'\u4e2d'
print u'\u4e2d'.encode('utf-8')

print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print '拼接参数：'
print 'Hello, %s' % 'world'

print 'Hi, %s, you have $%d.' % ('Michael', 1000000)

print 'Age: %s. Gender: %s' % (25, True)

print 'growth rate: %d %%' % 7

print u'中文'.encode('gb2312')


