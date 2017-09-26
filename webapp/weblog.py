# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse ,JsonResponse
import time
from bson.json_util import dumps
import codecs
'''
    arg[0] :timestamp
    arg[1] ：user_id
    arg[2] : data: news_id
'''
def log(user,data):
    with codecs.open("/home/luru/Desktop/36k/news/webapp/usedata/log.log","a","utf-8")as handle:
        handle.write(str(int(time.time())) + ","+user+","+data+"\n")

def online(user,data):
    with codecs.open("/home/luru/Desktop/36k/news/webapp/usedata/online.log","a","utf-8")as handle:
        handle.write(str(int(time.time())) + ","+user+","+data+"\n")