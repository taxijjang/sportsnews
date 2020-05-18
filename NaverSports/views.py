from django.shortcuts import render
from rest_framework import viewsets

from .serializer import NaverSportsSerializer
from .models import NaverSports
from . import task

from rest_framework.decorators import api_view

class NaverSportsViewSet(viewsets.ModelViewSet):

    queryset = NaverSports.objects.all()
    serializer_class = NaverSportsSerializer

    #def get_queryset(self):
    #    task
    #    print("Asdf")