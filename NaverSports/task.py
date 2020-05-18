from .models import NaverSports
# Create your views here.
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#from threading import Thread
import time
def create_model(sport_lists):
    print("create model")
    for sport_list in sport_lists:
        NaverSports.objects.create(
            rank = int(sport_list[0]),
            url = sport_list[2],
            title=sport_list[1],
        )

def update_model(sport_list):
    print("update model")
    for sport_list in sport_list:
        obj = NaverSports.objects.get(rank = sport_list[0])
        obj.title = sport_list[1]
        obj.url = sport_list[2]
        obj.save()

def crwaling():
    url = "https://sports.news.naver.com/wfootball/index.nhn"
    source = urlopen(url).read()
    soup = BeautifulSoup(source,'html.parser')
    news = soup.find_all('ol', {'class' : 'news_list'})

    regex = ""

    #re_url = re.compile('href=..')
    #주소 찾기 위한 정규식
    re_url = re.compile('news[a-zA-Z0-9?=&;/.]+"')
  
    #tmp_news = str(news[0])
    news_url = re_url.findall(str(news[0]))
    
    for rank,news in enumerate(news):
        regex = str(news.get_text())
        regex = regex.split('\n')
        regex = regex[1:-1]

    sport_list = []
    for rank, r in enumerate(regex):
        rank_title = []
        if rank < 9:
            rank_title.append(r[:1])
            rank_title.append(r[1:])

        else:
            rank_title.append(r[:2])
            rank_title.append(r[2:])
        news_url[rank] = (news_url[rank])[:-1]
        news_url[rank] = news_url[rank].replace("amp;","")

        rank_title.append("https://sports.news.naver.com/"+(news_url[rank])[:])
       
        sport_list.append(rank_title)

    #print(NaverSports.objects.filter(rank=1))

    try:
        obj = NaverSports.objects.get(rank = 1)
        print(obj)
    except NaverSports.DoesNotExist:
        create_model(sport_list) 
    else :
        update_model(sport_list)
                
crwaling()