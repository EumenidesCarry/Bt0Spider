#-*- coding: UTF-8 -*-
#爬取HTML上的磁力链接,正则表达式magnet:?[^\"]+

import re
import requests
from bs4 import BeautifulSoup

res =requests.get('http://bt0.com/subject/25322.html')
content = res.content
soup = BeautifulSoup(content,'lxml')

magnet_list = soup.find('div',class_='tab__content')
#print magnet_list
print '--'*100
patten = re.compile('magnet:?[^\"]+',re.S)
magnet = re.findall(patten,str(magnet_list))
print magnet[0]


#magnet = re.findall(r'magnet:?[^\"]+',)
#print magnet
