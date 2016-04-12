#!/usr/bin/env python
# coding=utf-8
import requests

r = requests.get('http://news.sina.com.cn/hotnews/')
# print r.text
print r.encoding
print r.content
print r.status_code
print r.headers
print r.history
