#!/usr/bin/python
# -*- coding: utf-8 -*-

#try:
#	f = open('/path/to/file', 'r')
#	print f.read()
#finally:
#	print 'over'
import codecs
def readFile():
	with codecs.open('/Users/chendong/Desktop/home.txt', 'r','utf-8') as f:
	#	print f.read()	
		for line in f.readlines():
			print(line.strip()) # 把末尾的'\n'删掉
		
def writeFile():
	with codecs.open('/Users/chendong/Desktop/home.txt', 'w','utf-8') as f:
		f.writelines('Hello, world!')
	
writeFile()
readFile()

#操作文件和目录
import os
print os.name
print os.uname()

#环境变量
print os.environ
print os.getenv('PATH')

print os.path.abspath('.')
fileDir = os.path.join(os.path.abspath('.'),'testdir')
print fileDir

os.mkdir(fileDir)
os.rmdir(fileDir)
#删除文件
#os.remove(file)
#列出当前目录下所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
#列出所有文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#序列化
try:
	import cPickle as pickle
except ImportError:
	import pickle

#序列化
d = dict(name='Bob', age=20, score=88)	
with open('/Users/chendong/Desktop/home.txt','w') as f:
	pickle.dump(d, f)

#反序列化
with open('/Users/chendong/Desktop/home.txt','r') as f:
	print pickle.load(f)
	
	
import json
str = json.dumps(d)
print str
print json.loads(str)

class Student(object):
	    def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
	
	
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))