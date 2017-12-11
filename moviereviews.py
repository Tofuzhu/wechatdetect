from urllib import request
from bs4 import BeautifulSoup as bs

def getNowPlayingMovie_list():
    resp=request.urlopen('http://movie.douban.com/nowplaying/nanjing/')
    html_data=resp.read().decode('utf-8')
    soup=bs(html_data,'html.parser')
    nowplaying_movie=soup.find_all('div',id='nowplaying')
    nowplaying_movie_list=nowplaying_movie[0].find_all('li',class_='list-item')


    nowplaying_list=[]
    for item in nowplaying_movie_list:
        nowplaying_dict={}
        nowplaying_dict['id']=item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name']=tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    return nowplaying_list

def getCommentsById(movieid,pageNum):
    requrl='https;//movie.douban.dom/subject/'+movieid[0]['id']+'/comments'+'?'+'start=0'+'&limit=20'
    resp=request.urlopen(requrl)
    html_data=resp.read().decode('utf-8')
    soup=bs(html_data,'html.parser')
    comment_div_lits=soup.find_all('div',class_='comment')

    print(comment_div_lits)
