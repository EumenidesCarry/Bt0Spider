#-*- coding: UTF-8 -*-
#测试


import re
import requests
from bs4 import BeautifulSoup
import os



BASE_PAGE_URL = 'http://bt0.com/film-download/1-0-0-3-0-'
PAGE_URL_LIST = []
for x in range(0,1):
	url = BASE_PAGE_URL + str(x) + '.html'
	PAGE_URL_LIST.append(url)


'''def download_name(name):
	n = name



def download_url(url):
	u = url'''



def get_page(page_url):
	res = requests.get(page_url)
	content = res.content
	soup = BeautifulSoup(content,'lxml')
	#获取电影名字
	name_list = soup.find_all('img',attrs={'lazy'})
	namelist = []
	for name in name_list:
		name = name['alt']
		namelist.append(name)#将名字加入到namelist集合
#	download_name(namelist)
	str_movie = str(namelist).replace('u\'','\'')
	print  str_movie.decode("unicode-escape")


	#获取每部电影地址
	url_list = soup.find_all('a',attrs={'block text-block'})
	urllist = []
	for url in url_list:
		url = 'http://bt0.com' +  url['href']
		urllist.append(url)  #将地址加入到urllist集合
#	download_url(urllist)

#	str_name =  zip(namelist,urllist)  #将namelist和urllist整合为dict
	#将unicode转换为中文 并打印
#	str_movie = str(str_name).replace('u\'','\'')
#	print str_movie.decode("unicode-escape")

	#获取磁力链接
	def get_movie(movie_url):
		res =requests.get(movie_url)
		content = res.content
		soup = BeautifulSoup(content,'lxml')

		magnet_list = soup.find('div',class_='tab__content')
		patten = re.compile('magnet:?[^\"]+',re.S)
		magnet_list = re.findall(patten,str(magnet_list))
		print '-'*100
#		print magnet_list[0]



	for movie_url in urllist:
		get_movie(movie_url)




def main():
	for page_url in PAGE_URL_LIST:
		get_page(page_url)



if __name__ == "__main__":
	main()



