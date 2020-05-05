from django.shortcuts import render

from rest_framework import viewsets
from .serializer import NaverSportsSerializer
from .models import NaverSports
# Create your views here.
from bs4 import BeautifulSoup
from urllib.request import urlopen

def model_reset(sport_lists):
    for sport_list in sport_lists:
        NaverSports(
            rank = int(sport_list[0]),
            url = sport_list[2],
            title=sport_list[1],
        ).save()


def crwaling():
 
    is_model = NaverSports.objects.all()

    if is_model.exists():   
        print("A")
    else:
        print('b')
        NaverSports.objects.all().delete()

    url = "https://sports.news.naver.com/wfootball/index.nhn"

    html = urlopen(url)
    source = html.read()
    html.close()

    soup = BeautifulSoup(source,'html.parser')

    news = soup.find_all('ol', {'class' : 'news_list'})

    import re

    regex = ""

    #re_url = re.compile('href=..')
    #주소 찾기 위한 정규식
    re_url = re.compile('news[a-zA-Z0-9?=&;/.]+"')

    tmp_news = str(news[0])
    news_url = re_url.findall(tmp_news)
    
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
    model_reset(sport_list)

class NaverSportsViewSet(viewsets.ModelViewSet):
    crwaling()
    queryset = NaverSports.objects.all()
    serializer_class = NaverSportsSerializer