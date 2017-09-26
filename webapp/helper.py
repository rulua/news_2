#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-10 下午3:05
# @Author  : ai-i-luru@interns.chuangxin.com

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db= client.news
news = db.newstable
user = db.user

def getnews(count):
    result=news.find({},{"_id":0,"id":1,"title":1,"content":1}).skip(30).limit(count)
    return result
#getnews(10)

def newByTitle(title):
    result=news.find_one({"title":title},{"title": 1, "id": 1,"content":1,"pubDate":1,"url":1})
    #print result
    return result

def newById(id):
    result=news.find_one({"id":id},{"title": 1, "id": 1,"content":1,"pubDate":1,"url":1,"click":1})
    #print result
    return result

#newByTitle("test")
def api_getnews(count):
    result=news.find({},{"_id":0}).limit(count)
    return result
#print api_getnews(10)

def pages():
    result=news.count()
    return result//15
#print pages()

def insert_user(data):
    user.insert_one(data)

def getcommentnews(list_id):
    data = list()
    for id in list_id:
        result = news.find_one({"id": id}, {"title": 1, "id": 1, "content": 1, "pubDate": 1, "url": 1})
        data.append(result)
    return data

def getid():
    result =news.find({},{"_id":0,"id":1})

def getcommentnews2(data):
    result = news.find().skip(data).limit(10)
    return result

def login(username, pwd):
    online = user.find({"username":username,"password":pwd},{"_id":0,"id":1}).count()
    return online

def transtime():
    dateset =news.find({},{"_id":0,"pubDate":1})
    return dateset

def updatetime(pubtime,stamtime):
    news.update({"pubDate":pubtime},{'$set':{"pubDate":stamtime}})

def allnews():
    result = news.find({}, {"_id": 0})
    return result

def gettime(starttime,endtime):
    result = news.find({"pubDate":{'$gt':starttime,'$lt':endtime}}, {"_id": 0})
    return result

def addclick(news_id):
    news.update({"id":news_id},{'$inc':{"click":1}})