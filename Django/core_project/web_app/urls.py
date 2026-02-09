#
# from web_app import views
# path('', views., name='home')
from django.urls import path

from . import views
from django import urls




urlpatterns = [
path('', views.index, name='home')
]



