#!/usr/bin/python
# -*- coding: utf-8 -*-


from PIL import Image

im = Image.open('test.png')

print im.format, im.size, im.mode

im.thumbnail((200, 100))

im.save('thumb.png', 'PNG')