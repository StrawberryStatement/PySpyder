# -*- coding: utf-8 -*-
"""
@author: trick150

"""
import urllib
from urllib import request
from urllib import parse
from urllib.request import urlopen

def loadPage(url,filename):
	"""
	加载函数
	:param url:链接url
	:param filename: 下载至哪一文件
	:return: null
	"""
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3357.400 QQBrowser/9.6.11858.400"}
	#urllib库的代理在urllib.request下，接收一个字典值{protocol name : url proxy}
	url_proxy=request.ProxyHandler({"http":"http://127.0.0.1:8888"})
	opener=request.build_opener(url_proxy)
	html=request.Request(url,headers=headers)
	response=opener.open(html)
	filename="第"+str(filename)+"页"+".html"
	print("正在加载"+filename)
	#print(response.read())
	writePage(response.read(),filename)


def writePage(response,filename):
	"""
	写入函数
	:param url:链接url
	:param filename: 下载至哪一文件
	:return: null
	"""
	with open(filename,"wb+") as f:
		f.write(response)
	print("正在保存"+filename)
	print("-"*30)


def tiebaSpyder(url,startPage,endPage):
	'''
	调度函数
	:param url: 链接url
	:param startPage: 起始页
	:param endPage: 终止页
	:return:
	'''
	for page in range(startPage,endPage+1):
		pn=(page-1)*50
		url=url+"&pn="+str(pn)
		loadPage(url,page)



if __name__=="__main__":
	tieba_id=input("请输入贴吧名称:")
	begin=int(input("请输入起始页:"))
	end=int(input("请输入结束页:"))
	url="https://tieba.baidu.com/f?"
	#urlencode接收一个字典函数，字典值解析为等号左边，“：”解析为“=”，
	#字典值解析为等号右边的url编码值（中文）
	key= parse.urlencode({"kw":tieba_id})
	fullurl=url+key
	tiebaSpyder(fullurl,begin,end)
	print("操作完成")