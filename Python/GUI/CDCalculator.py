#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import tkFont
import os
from functools import partial
from PIL import Image, ImageTk

reset=True

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.cal()

	def buttonCallBack(event):
	    global label
	    global reset
	    print '1'
	    num=event.widget['text']
	    print num
	    if num=='C':
	        label['text']="0"
	        return
	    if num in "=":
	        label['text']=str(eval(label['text']))
	        reset=True
	        return
	    s=label['text']
	    if s=='0' or reset==True:
	        s=""
	        reset=False
	    label['text']=s+num

	def cal():
	    self.resizable(0,0)
		label = Label(self,text="0",background="white",anchor="e")
		label['width']=35
		label['height']=2
		label.grid(row=1,columnspan=4,sticky=W)
		#按钮
		showText="789/456*123-0.C+"
		for i in range(4):
		    for j in range(4):
		        b=Button(self,text=showText[i*4+j],width=7)
		        b.grid(row=i+2,column=j)
		        txt = '<'+ showText[i*4+j] + '>'
		        print txt
		        b.bind('<Button-1>',buttonCallBack)

		print 'first '
		showText="()"
		for i in range(2):
		    b=Button(self,text=showText[i],width=7)
		    b.grid(row=6,column=2+i)
		    txt = '<'+ showText[i] + '>'
		    print txt
		    b.bind('<Button-1>',buttonCallBack)

		b=Button(self,text="=")
		b.grid(row=6,columnspan=2,sticky="we")
		b.bind('<Button-1>',buttonCallBack)

root = Application()
# 设置窗口标题:
root.master.title('计算器')
# 主消息循环:
root.mainloop()
