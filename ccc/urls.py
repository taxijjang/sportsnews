from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from NaverSports import views

router = DefaultRouter()
router.register('naversports',views.NaverSportsViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
