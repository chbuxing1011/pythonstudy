#!/usr/bin/python
# -*- coding: utf-8 -*-


import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = raw_input('Email: ')
password = raw_input('Password: ')
pop3_server = raw_input('POP3 server: ')

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome())
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = '\r\n'.join(lines)
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()

# indent用于缩进显示:
def print_info(msg, indent=0):
	if indent == 0:
		# 邮件的From, To, Subject存在于根对象上:
		for header in ['From', 'To', 'Subject']:
			value = msg.get(header, '')
			if value:
				if header=='Subject':
					# 需要解码Subject字符串:
					value = decode_str(value)
				else:
					# 需要解码Email地址:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' % (name, addr)
			print('%s%s: %s' % ('  ' * indent, header, value))
	if (msg.is_multipart()):
		# 如果邮件对象是一个MIMEMultipart,
		# get_payload()返回list，包含所有的子对象:
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print('%spart %s' % ('  ' * indent, n))
			print('%s--------------------' % ('  ' * indent))
			# 递归打印每一个子对象:
			print_info(part, indent + 1)
	else:
		# 邮件对象不是一个MIMEMultipart,
		# 就根据content_type判断:
		content_type = msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			# 纯文本或HTML内容:
			content = msg.get_payload(decode=True)
			# 要检测文本编码:
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sText: %s' % ('  ' * indent, content + '...'))
		else:
			# 不是文本,作为附件处理:
			print('%sAttachment: %s' % ('  ' * indent, content_type))