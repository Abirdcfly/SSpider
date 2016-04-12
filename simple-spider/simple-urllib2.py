#!/usr/bin/env python
# coding=utf-8
import urllib2

url = "http://news.sina.com.cn/hotnews/"
response = urllib2.urlopen(url)
headers = response.headers
response_status_code = response.getcode()
response_info = response.info()
response_get_url = response.geturl()  # 重定向后的真实地址.
content = urllib2.urlopen(url).read()

# print headers,  "\n\n", response_status_code, "\n\n", response_info, "\n\n", response_get_url
# print headers == response_info  # True
