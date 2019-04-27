#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
__data__ = '2019/4/12 16:21'
__author__ = 'shenxu'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^index/(\d+)/$', views.info),
    url(r'^login/$',views.login,name='login'),
    url(r'^resign/$',views.resign,name='resign'),
    url(r'^logout/$',views.out,name='logout'),
    url(r'^checkuserid/$',views.checkuserid),
    url(r'^search/$',views.search),
    url(r'^userInfo/$',views.userInfo),
]
