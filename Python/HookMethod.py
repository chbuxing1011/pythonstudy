#!/usr/bin/python
# -*- coding: utf-8 -*-
	

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]
print L[:3]
print L[-2:]
print L[-2:-1]

L = range(100)

print L[:10:2]
print L[::5]
print L[:]

print (0, 1, 2, 3, 4, 5)[:3]
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

#迭代 可以作用在其他可迭代对象上
from collections import Iterable

print isinstance('abc', Iterable)
print isinstance([1,2,3], Iterable)
print isinstance(123, Iterable)

#isinstance函数可以判断一个变量是不是字符串
x = 'abc'
isinstance(x, str)
#下标循环#
for i, value in enumerate(['A', 'B', 'C']):
	print i, value
	
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y
	
#列表生成式#
print range(1, 11)
print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0]

#两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']

import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

#dict的iteritems()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
	print k, '=', v
	
#列表生成式也可以使用两个变量来生成list
[k + '=' + v for k, v in d.iteritems()]
#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
 
#生成器 一边循环一边计算的机制，称为生成器（Generator）
#只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
for n in g:
	print n
	
#函数式编程
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a + b
		n = n + 1
		
print fib(6)

def fib1(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

#map/reduce
#map将传入的函数 依次 作用到序列的每个元素，并把结果作为新的list返回
def f(x):
	return x * x
map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#累积 reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def add(x, y):
	return x + y
reduce(add, [1, 3, 5, 7, 9])

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
	return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

reduce(fn, map(char2num, '13579'))

def is_odd(n):
	return n % 2 == 1

#filter filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

def not_empty(s):
	return s and s.strip()

filter(not_empty, ['A', '', 'B', None, 'C', '  '])

sorted([36, 5, 12, 9, 21])

def reversed_cmp(x, y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
	
sorted([36, 5, 12, 9, 21], reversed_cmp)

sorted(['bob', 'about', 'Zoo', 'Credit'])


def cmp_ignore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0

sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

#返回函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
	
f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2

#闭包
def count():
	fs = []
	for i in range(1, 4):
		def f():
			 return i*i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print f1()
print f2()
print f3()

#匿名函数
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def build(x, y):
	return lambda: x * x + y * y
	
f = lambda x: x * x
print f(5)

def build(x, y):
	return lambda: x * x + y * y
	
#装饰器
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def now():
	print '2013-12-25'
f = now

#函数对象有一个__name__属性，可以拿到函数的名字
print now.__name__
print f.__name__

def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper
	
@log
def now():
	print '2013-12-26'
	
print now()

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator
		
	
import functools

def log(text):
	print '4'
	def decorator(func):
		print '5'
		@functools.wraps(func)		
		def wrapper(*args, **kw):
			print '1 %s %s():' % (text, func.__name__)
			def wrapperInner():
				print('0')
				print '0 End %s %s():' % (text, func.__name__)
				return func(*args, **kw)
			print('111')
			return wrapperInner
		print '2 %s %s():' % (text, func.__name__)
		return wrapper
	print '3'
	return decorator
	
@log('execute')
def now():
	print '2013-12-27'
	
print now()

#偏函数 可以创建一个新的函数，这个新函数可以固定住原函数的部分参数
print int('12345')
print int('12345', base=8)

int2 = functools.partial(int, base=2)
print int2('100000')

max2 = functools.partial(max, 10)
max2(5, 6, 7)
