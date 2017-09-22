#!/usr/bin/python
# -*- coding: utf-8 -*-

#函数
print abs(100)

#比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1：
print cmp(1, 2)
print cmp(1, 1)
print cmp(3, 2)

#int()函数可以把其他数据类型转换为整数
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool('')

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
a(-1)

def nop():
	pass

#自定义函数 isinstance
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print my_abs(-1)		

import math

#返回多个值
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

#函数的参数 ,默认参数
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print power(5)
print power(5, 2)

#注册
def enroll(name, gender):
	print 'name:', name
	print 'gender:', gender
	
enroll('Sarah', 'F')


def enroll(name, gender, age=6, city='Beijing'):
	print 'name:', name
	print 'gender:', gender
	print 'age:', age
	print 'city:', city

#最后1个参数应用在参数age上
print enroll('Bob', 'M', 7)
print enroll('Adam', 'M',city ='Tianjin')
#最后1个参数应用在参数age上
print enroll('CCC', 'N','Tianjin')

#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

# 计算a2 + b2 + c2 +
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
	
print calc([1, 2, 3])
print calc((1, 3, 5, 7))

#可变参数
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去	
nums = [1, 2, 3]
calc2(*nums)
calc2(1, 2, 3)

#关键字参数 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw
	
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')

#参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
#用必选参数、默认参数、可变参数和关键字参数#
def func(a, b, c=0, *args, **kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
	
print func(1, 2, 3, 'a', 'b', x=99)

#*args是可变参数，args接收的是一个tuple；
#
#**kw是关键字参数，kw接收的是一个dict。
args = (1, 2, 3, 4)
kw = {'x': 99}
print func(*args, **kw)

#递归函数
def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)
	

