#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-10 下午3:00
# @Author  : ai-i-luru@interns.chuangxin.com
from django.conf.urls import url
from . import views
from . import api

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^news/$',views.new_detail,name='new_detail'),
    url(r'^login/$',views.login,name='login'),
    url(r'^topic/$',views.topic,name='topic'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^api/$',api.news, name='news'),
    url(r'^register/$',views.register,name='register'),
    url(r'^flush/$',views.flush,name='flush'),
    url(r'^api/news',api.allnews, name='allnews'),
    url(r'^api/time?',api.gettime, name='gettime'),

]