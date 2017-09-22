#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)
	
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
	def __call__(self):
		print('My name is %s.' % self.name)
		

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

print bart
print bart.score
print bart.get_grade()
bart.age = 18
print bart.age


#实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
print type(123)

import types
type('abc')==types.StringType
type(u'abc')==types.UnicodeType
type([])==types.ListType
type(str)==types.TypeType

#isinstance()
print dir('ABC')

print 'ABC'.__len__()


#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态



from types import MethodType
def set_score(self, score):
	self.score = score

#为了给所有实例都绑定方法，可以给class绑定方法

Student.set_score = MethodType(set_score, None, Student)

#定义一个特殊的__slots__变量，来限制该class能添加的属性

class StudentNew(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	
#	__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
	pass
	

class Student2(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2014 - self._birth
#定制类
class Chain(object):
	
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		if path =='users':
			def wrapper(text):
				return Chain('%s/%s/:%s' % (self._path, path, text))
			return wrapper
		return Chain('%s/%s' % (self._path, path))
		
	def __str__(self):
		return self._path

print Chain().status.user.timeline.list
print Chain().users('michael').repos

print callable(Student("CD", 18))
print callable(max)
print callable(None)
print callable('string')

#元类
class Hello(object):
    def hello(self, name='world'):
		print('Hello, %s.' % name)
		

h = Hello()
print h.hello()
print type(Hello)
print type(h)

#动态创建
#要创建一个class对象，type()函数依次传入3个参数：
#
#class的名称；
#继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self, name='world'): # 先定义函数
	print('Hello, %s.' % name)

Hello = type('Hello1', (object,), dict(hello1=fn)) # 创建Hello class
h = Hello()
print h.hello1()
print(type(Hello))
print(type(h))


# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类
	
L = MyList()
L.add(1)
print L

#错误处理
try:
	print 'try...'
	r = 10 / 0
	print 'result:', r
except ZeroDivisionError, e:
	print 'except:', e
finally:
	print 'finally...'
print 'END'

# err.py
import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)

main()
print 'END'


# err.py
class FooError(StandardError):
	pass

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n
	
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

