#-*- coding: UTF-8 -*-
# 原始版本
import time
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup



def get_urls():
    '''
    获取Bto下电影的所有url
    http://bt0.com/film-download/1-0-0-0-0-1.html
    http://bt0.com/film-download/1-0-0-0-0-1019.html
    '''
    page_urls = ['http://bt0.com/film-download/1-0-0-0-0-{cnt}.html'.format(cnt=cnt) for cnt in range(0, 1019)] #在这更改要爬取的页面
    print("Please wait for second ...")
    movie_urls =[]
    for page_url in page_urls:                                      #在每个页面爬取所有电影的地址
        res = requests.get(page_url)
        content = res.content
        time.sleep(0.5)                   #休息一下
        soup = BeautifulSoup(content,'lxml')
        movies =soup.find("div", class_="masonry masonry-demos").find_all("div", class_="masonry__item")
        #print(movies)
        movies_urls =[]
        for movie in movies:
            try:
                movie_url = 'http://bt0.com'+ movie.find('a')['href']
                #movie_url = [url.replace('"', "") for url in href]
                movie_urls.append(movie_url)    #将每部电影地址加入到movie_urls集合中
            except Exception:
                    pass
        #print(movie_urls)


    for url in movie_urls:
        '''
        爬取每个电影的名字和磁力链接
        '''
        res = requests.get(url)
        time.sleep(0.5)                     #休息一下
        content = res.content
        soup = BeautifulSoup(content,'lxml')
        m = []
        try:
            movie_infos =soup.find("div", class_="picture-container").find_all('a')
            #print(movie_infos)
            patten = re.compile('magnet:?[^\"]+',re.S)
            magnet = re.findall(patten,str(movie_infos))
            name = soup.find("a", class_="torrent-title").text
            n = name.strip()
        except:
             magnet = 'NULL'
             name ='NULL'

        # i={
        #     'movie_name' : n,
        #     'magnet': magnet[0]
        # }
        # m.append(i)
        # print(m)
        m.append(str(n) + ',' + str(magnet[0]))
        print(m)


get_urls()
