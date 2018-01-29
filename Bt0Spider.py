# encoding=utf-8
# 带有豆瓣评分的

import time
import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool, cpu_count

def get_urls():
    '''
    获取Bto下电影的所有url
    http://bt0.com/film-download/1-0-0-0-0-1.html
    http://bt0.com/film-download/1-0-0-0-0-1019.html
    '''
    page_urls = ['http://bt0.com/film-download/1-0-0-0-0-{cnt}.html'.format(cnt=cnt)
                for cnt in range(0, 1)]
    print("Please wait for second ...")

    movie_urls =[]
    for page_url in page_urls:                                      #在每个页面爬取所有电影的地址
        res = requests.get(page_url).content
        time.sleep(0.5)                   #休息一下
        soup = BeautifulSoup(res,'lxml')
        movies =soup.find("div", class_="masonry masonry-demos").find_all("div", class_="masonry__item")
        movies_urls =[]
        for movie in movies:
            try:
                movie_url = 'http://bt0.com'+ movie.find('a')['href']
                movie_urls.append(movie_url)    #将每部电影地址加入到movie_urls集合中
            except Exception:
                    pass
    return movie_urls    #用set()集合去重，并返回地址

def get_infos(url):
        '''
        爬取每个电影的名字和磁力链接
        '''
        res = requests.get(url).content
        time.sleep(0.5)                     #休息一下
        soup = BeautifulSoup(res,'lxml')
        m = []
        try:
            movie_infos =soup.find("div", class_="picture-container").find_all('a')
            #print(movie_infos)
            patten = re.compile('magnet:?[^\"]+',re.S)
            magnet = re.findall(patten,str(movie_infos))
        except:
            magnet = 'NULL'


        res = requests.get(url).content
        time.sleep(0.5)
        soup = BeautifulSoup(res,'lxml')
        infos = soup.find('div',style='margin-bottom:2em')

        name = soup.find('span',class_='info-title').text #获取电影名字
        try:
            '''
            获取电影评分
            '''
            scorers = soup.find('span',style='font-size: 2em;font-weight: 700;color:#fc9b35;').text
            s = re.findall(r"\d+\.?\d*",scorers)
            score = s[0]
        except:
            score = 'NULL'

        m.append(str(name) + ',' + str(score) + ',' + str(magnet[0]))
        print(m)


if __name__ == "__main__":
    urls = get_urls()
    pool = Pool(processes=cpu_count())
    pool.map(get_infos, urls)
