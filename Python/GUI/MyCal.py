#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# 要求：

# 实现加减乘除及拓号优先级解析
# 用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
# 必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致
'''

import re
# import pdb
from tkinter import *

def main(strInput):
    # inputR = re.search(r'\(([^\d+\-*/\(\)]*)\)', str(strInput))
    # print inputR
    # if inputR is None:
    #     print "公式错误"
    #     return 0
    # strInput = input('请输入需要计算的算式')
    # print strInput
    a = ''.join(str(strInput).split())
    print a
    while True:
        if '(' in a:
            ct = re.search(r'\(([^()]+)\)', a)
            if ct is not None:
                print ct
                b = ct.groups()[0]
                print 'b: '
                print b
                c = count(b)
                print 'c: '
                print c
                a = re.sub(r'\(([^()]+)\)', str(c), a, 1)
                print 'a: '
                print a
                # pdb.set_trace()
        else:
            c = count(a)
            print(c)
            return c

def add_min(a):
    '''
    计算加减法
    '''

    if '--' in a:
        a = a.replace('--', '+')

    c = re.findall(r'-?\d+\.?\d*', a)
    print 'c: '
    print c
    ls = []
    for i in c:
        ls.append(float(i))
    print ls
    rest = sum(ls)
    print rest
    # pdb.set_trace()
    return rest


def mul(a):
    '''
    计算剩数
    '''


    b = re.search(r'\d+\.?\d*(\*-?\d+\.?\d*)+', a)
    if b is not None:
        b = b.group()
        rest = 1
        c = re.findall(r'-?\d+\.?\d*', b)
        print 'mul: '
        print c
        ls =[]
        for item in c:
            ls.append(float(item))
        print ls
        for i1 in range(len(ls)):
            rest = rest * ls[i1]
        print i1
        a = re.sub(r'\d+\.?\d*(\*-?\d+\.?\d*)+', str(rest), a, 1)
        print a
        # pdb.set_trace()
        return a



def div(a):
    '''
    计算除法
    '''

    b = re.search(r'\d+\.?\d*(\/-?\d+\.?\d*)+', a)
    if b is not None:
        b = b.group()
        c = re.findall(r'-?\d+\.?\d*', b)
        print "c: "
        print c
        ls =[]
        for i in c:
            ls.append(float(i))
        print ls
        rest = ls[0]
        for i1 in range(1,len(ls)):
            rest = rest / ls[i1]
        print rest
        a = re.sub(r'\d+\.?\d*(\/-?\d+\.?\d*)+', str(rest), a, 1)
        # pdb.set_trace()
        print a
        return a


def count(b):
    '''
    计算结果
    '''
    while True:
        if '*' in b:
            c = b.split('*')
            if '/' in c[0]:
                b = div(b)
            else:
                b = mul(b)
        elif '/' in b:
            b = div(b)

        elif '+' or '-' in b:
            b = add_min(b)
            return b
        else:
            return b


# main()
print '2*3' + str(count('2*3'))

reset=True
def buttonCallBack(event):
    global label
    global reset
    num=event.widget['text']
    print num
    if num=='C':
        label['text']="0"
        return
    if num in "=":
        label['text']=str(main(label['text']))
        reset=True
        return
    s=label['text']
    if s=='0' or reset==True:
        s=""
        reset=False
    label['text']=s+num

#主窗口
root=Tk()
root.wm_title("计算器")
#显示栏1
label=Label(root,text="0",background="white",anchor="e")
label['width']=35
label['height']=2
label.grid(row=1,columnspan=4,sticky=W)
#按钮
showText="789/456*123-0.C+"
for i in range(4):
    for j in range(4):
        b=Button(root,text=showText[i*4+j],width=7)
        b.grid(row=i+2,column=j)
        txt = '<'+ showText[i*4+j] + '>'
        print txt
        b.bind('<Button-1>',buttonCallBack)

print 'first '
showText="()"
for i in range(2):
    b=Button(root,text=showText[i],width=7)
    b.grid(row=6,column=2+i)
    txt = '<'+ showText[i] + '>'
    print txt
    b.bind('<Button-1>',buttonCallBack)

b=Button(root,text="=")
b.grid(row=6,columnspan=2,sticky="we")
b.bind('<Button-1>',buttonCallBack)
root.mainloop()
