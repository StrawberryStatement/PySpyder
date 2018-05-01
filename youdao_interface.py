# -*- coding: utf-8 -*-
"""
@author: trick150

"""
import hashlib
import re
import random
from urllib import parse
import urllib.request
#有道应用ID
appKey = '06dca0450555376e'
#有道应用密钥
secretKey = 'cvI6ZVBjITjo6kRvp6CVF3tiEphtVmLt'
#html头
myurl = 'http://openapi.youdao.com/api'
#待翻译
q = input("请输入待翻译内容：")

fromLang = 'auto'
toLang = 'auto'
salt = random.randint(1, 65536)
#加密验证信息
sign = appKey + q + str(salt) + secretKey
m1 = hashlib.md5()
m1.update(sign.encode("utf-8"))
sign = m1.hexdigest()
#构造GET Url
myurl = myurl + '?appKey=' + appKey + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
	salt) + '&sign=' + sign

ua_header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#代理
#proxy_handler=urllib.request.ProxyHandler({'http':'http://127.0.0.1:8888/'})
#opener=urllib.request.build_opener(proxy_handler)

request=urllib.request.Request(myurl,headers=ua_header)
response=urllib.request.urlopen(request)
html=response.read().decode("utf-8")
unquote_html=urllib.parse.unquote(html)
#pattern
p1=r'q=([a-z]*)'
pattern = re.compile(p1)
#html必须从byte解码成str
m = re.search(pattern,unquote_html)
#print(type(html.decode("utf-8")))
#print(html.decode("utf-8"))
#验证格式
#print((m.group(0)))

print(m.group(0).split('=')[1])