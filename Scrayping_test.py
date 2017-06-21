#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup

html=urllib.request.urlopen("http://gochiusa.com")
soup=BeautifulSoup(html,"lxml")
res=soup.find(id="nwu_001_t").find_all("a")
for i in res:
	print(i.text)