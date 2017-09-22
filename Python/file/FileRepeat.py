#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os

print os.name
print os.uname()


#判断文件是否存在，不存在则创建，模拟过程 with codecs.open(fileName, 'wt','utf-8') 直接可以创建
def creatFile(filePath):
    if os.path.exists(filePath):
           return 1
    else:
           with codecs.open(filePath, 'wt','utf-8') as f:
                   return 0

def clearFile():
    with codecs.open('/Users/cd13337/Desktop/home.txt', 'w','utf-8') as f:
        f.truncate()
                
def writeFile(filePath,result):
    with codecs.open(filePath, 'a','utf-8') as f:
        f.writelines(result)
        
def readFile():
    with codecs.open('/Users/cd13337/Documents/Document/Python/file/debug.txt', 'r','utf-8') as f:
        for line in f.readlines():
             if searchFile(line) == -1:
                  writeFile('/Users/cd13337/Desktop/home.txt',line)


def searchFile(keyWord):
    with codecs.open('/Users/cd13337/Documents/Document/Python/file/release.txt', 'r','utf-8') as f:
        for line in f.readlines():
#             print(line.strip())
             if line == keyWord:
                        return 0
        return -1

def deleteDebugFile(filePath):
    with codecs.open(filePath, 'r','utf-8') as f:
        for line in f.readlines():
             if line.find('/Debug/') == -1:
                    fileName = os.path.join(os.path.abspath('.'),'testHome.txt')
                    writeFile(fileName,line)


clearFile()

readFile()

fileName = os.path.join(os.path.abspath('.'),'testHome.txt')
creatFile(fileName)


deleteDebugFile('/Users/cd13337/Desktop/home.txt')

#print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
#清理文件
#clearFile()

#readFile()
