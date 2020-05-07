from django.shortcuts import render
from rest_framework import viewsets

from .serializer import NaverSportsSerializer
from .models import NaverSports
from . import task

class NaverSportsViewSet(viewsets.ModelViewSet):
    queryset = NaverSports.objects.all()
    serializer_class = NaverSportsSerializer

