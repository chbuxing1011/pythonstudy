#!/usr/bin/python
# -*- coding: utf-8 -*-
# 1

#list
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[-1]

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print classmates

classmates[1] = 'Sarah'
print classmates

L = ['Apple',123,True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)

aL = []
print len(aL)

#tuple一旦初始化就不能修改
classmates2 = ('Michael', 'Bob', 'Tracy')
print classmates2

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t1 = (1,)
print t1

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t


age = 3
if age >= 18:
	print 'adult'
elif age >= 6:
	print 'teenager'
else:
	print 'kid'
	
#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print name
	
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x
print sum

print range(5)

sum = 0
for x in range(101):
	sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print sum

birth = raw_input('birth: ')
if int(birth) < 2000:
	print '00前'
else:
	print '00后'
	
#数组
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
#通过in判断key是否存在
print 'Thomas' in d

#如果key不存在，可以返回None，或者自己指定的value
print d.get('Thomas')
print d.get('Thomas', -1)

#删除一个key
d.pop('Bob')

#set
s = set([1, 2, 3])
print s

s.add(4)
s.remove(4)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

#str是不变对象，而list是可变对象
a = ['c', 'b', 'a']
print a.sort()

a = 'abc'
b = a.replace('a', 'A')
print b


