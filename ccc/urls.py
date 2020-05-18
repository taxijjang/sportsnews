from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from NaverSports import views

from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('naversports',views.NaverSportsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
