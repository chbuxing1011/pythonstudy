#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import json

def getRequest():

	url = "http://v.juhe.cn/laohuangli/d"
	para = {"key":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","date":"2017-3-22"}
	header ={}

	r = requests.get(url,params=para,headers= header)

	print('get请求获取的响应结果json类型',r.text)
	print("get请求获取响应状态码",r.status_code)
	print("get请求获取响应头",r.headers['Content-Type'])

	#响应的json数据转换为可被python识别的数据类型
	json_r = r.json()
	print(json_r)

getRequest()
