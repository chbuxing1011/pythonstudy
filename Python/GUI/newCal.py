# -*- coding: utf-8 -*-


import re
import pdb

def main():
    strInput = input('请输入需要计算的算式')
    print strInput
    a = ''.join(str(strInput).split())

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
                pdb.set_trace()
        else:
            c = count(a)
            print(c)
            break

def add_min(a):
    '''
    计算加减法
    :param:
    :return:
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
    pdb.set_trace()
    return rest


def mul(a):
    '''
    计算剩数
    :param ct:
    :return:
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
        pdb.set_trace()
        return a



def div(a):
    '''
    计算出发
    :param a:
    :return:
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
        pdb.set_trace()
        print a
        return a


def count(b):
    '''
    计算结果
    :return:
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
print '2*3' + count('2*3')