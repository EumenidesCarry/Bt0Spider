#-*- coding: UTF-8 -*-
import pymysql
import re
import os
import pandas as pd
import time
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup



def get_urls():
    '''
    获取Bto下电影的所有url
    http://bt0.com/film-download/1-0-0-0-0-1.html
    http://bt0.com/film-download/1-0-0-0-0-1018.html
    '''
    page_urls = ['http://bt0.com/film-download/1-0-0-0-0-{cnt}.html'.format(cnt=cnt) for cnt in range(0, 1)]
    print("Please wait for second ...")
    movie_urls =[]
    for page_url in page_urls:                                      #在每个页面爬取所有电影的地址
        res = requests.get(page_url)
        content = res.content
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

        i={
            'movie_name' : n,
            'magnet': magnet[0]
        }
        m.append(i)
        print(m)

        # dataframe = pd.DataFrame(columns=movies,data=list)
        # dataframe.to_csv("test.csv",index=True)






# # 打开数据库连接
# db = pymysql.connect("localhost","root","666666","TESTDB" )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('SAO', 'A', 25, 'M', 10000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()
#
# # 关闭数据库连接
# db.close()


# res = requests.get('http://bt0.com/mv/111.html')
# content = res.content
# soup = BeautifulSoup(content,'lxml')
# movie_infos =soup.find("div", class_="picture-container").find_all('a')
# #print(movie_infos)
# patten = re.compile('magnet:?[^\"]+',re.S)
# magnet = re.findall(patten,str(movie_infos))
# print(magnet[0])


get_urls()
