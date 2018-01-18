#-*- coding: UTF-8 -*-
#爬取BT0上的电影资源

import re
import requests
from bs4 import BeautifulSoup
import os



BASE_PAGE_URL = 'http://bt0.com/film-download/1-0-0-0-0-'
PAGE_URL_LIST = []
for x in range(0,1):
	url = BASE_PAGE_URL + str(x) + '.html'
	PAGE_URL_LIST.append(url)


def download_name(name):
	print name





def download_url(url):
	print 'http://bt0.com' + url





def get_page(page_url):
	res = requests.get(page_url)
	content = res.content
	soup = BeautifulSoup(content,'lxml')
	name_list = soup.find_all('img',attrs={'lazy'})
	for name in name_list:
		name = name['alt']
		download_name(name)



	url_list = soup.find_all('a',attrs={'block text-block'})
	for url in url_list:
		url = url['href']
		download_url(url)

def main():
	for page_url in PAGE_URL_LIST:
		get_page(page_url)



if __name__ == "__main__":
	main()























'''for movie in movie_url_list:
	movie_url = 'http://bt0.com' + movie['href']'''




'''for movie in soup.select('.effect-sadie'):
	name = movie.select('h2')[0].text
	en_name = movie.select('p')[0].text
	print name,en_name
	print '--'*100

movie_url_list = soup.find_all('a',attrs={'block text-block'})
for movie in movie_url_list:
	movie_url = 'http://bt0.com' + movie['href']
	print movie_url
'''


'''name = soup.find('img',attrs={'class':'lazy'})
url = soup.find('a',attrs={'class':'block text-block'})
year = soup.find('span',attrs={'class':'type--fine-print'})
score = soup.find('span',attrs={'class':'tag-sm tag-picture2'})
print name['alt'],year.text,score.text,'http://bt0.com' + url['href']
'''









