#!/usr/bin/python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Dong Chen'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello, world!'
	elif len(args)==2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many arguments!'

if __name__=='__main__':
	test()

import Module

Module.test()

#别名
try:
	import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
	import StringIO
	
try:
	import json # python >= 2.6
except ImportError:
	import simplejson as json # python <= 2.5

#作用域	
def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
		
import sys
print sys.path

