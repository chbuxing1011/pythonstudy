#!/usr/bin/python
# -*- coding: utf-8 -*-

#try:
#	f = open('/path/to/file', 'r')
#	print f.read()
#finally:
#	print 'over'
import codecs

def readFile():

	with codecs.open('/Users/cd13337/Documents/Document/Python/file/debug.txt', 'r','utf-8') as f:
	#	print f.read()	
		for line in f.readlines():
			print(line.strip()) # 把末尾的'\n'删掉
			if search(line.strip()) == 0:
				writeFile(line)
			
		
def writeFile(txt):
	with codecs.open('/Users/cd13337/Desktop/home.txt', 'w','utf-8') as f:
		f.writelines(txt)
	
def search(key):
	with codecs.open('/Users/cd13337/Documents/Document/Python/file/release.txt', 'r','utf-8') as f:
	#	print f.read()	
		for line in f.readlines():
			print(line.strip()) # 把末尾的'\n'删掉
			if line.strip() == key:
				return 1;
		return 0;


readFile()

#操作文件和目录
import os
print os.name
print os.uname()

