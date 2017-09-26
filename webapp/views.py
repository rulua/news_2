# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from bson.json_util import dumps,loads
import random
import time
import weblog
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
import helper as db
def index(request):
    template=loader.get_template('index.html')
    result = db.getnews(10)
    username =request.session['user']
    newslist=dumps(result)
    context = {"news_list": loads(newslist), "user":username,}
    ids = []
    for item in loads(newslist):
        ids.append(item["id"])
        #print item["id"]
    weblog.log(str(request.session['user_id']), str(ids))
    return HttpResponse(template.render(context, request))

def new_detail(request):
    if request.method == "GET":
        news_id = request.GET['id']
        template = loader.get_template('news.html')
        weblog.log(str(request.session['user_id']),news_id)
        db.addclick(news_id)
        result = db.newById(news_id)
        context={"new_detail": result}
        """
        文章点击数
        """


        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("error")

@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            user = request.POST['username']
            pwd = request.POST['pwd']

            '''
            用户登录验证
            '''
            result = db.login(user,pwd)
            if result == 1:
                request.session['user_id']="321443"
                request.session['user'] = user
                weblog.online(request.session['user_id'], "login")
                return HttpResponseRedirect("/webapp/")
            else:
                template = loader.get_template('login.html')
                context ={"msg":"用户名或密码错误！"}
                return HttpResponse(template.render(context, request))

        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render({}, request))
    except Exception as e:
        pass

@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':
            user_id =int(time.time())
            email = request.POST['email']
            password = request.POST['password']
            username =request.POST['username']
            request.session['user'] = username
            request.session['user_id'] = user_id
            data={"_id":user_id,"username":username,"password":password,"email":email}
            db.insert_user(data)
            '''
            添加用户的方法调用
            
            '''
            topics = ["电影", "体育", "技术", "杂志", "文学", "生活", "娱乐", "军事", "艺术", "海外"]
            context = {"topics": topics,}
            return render(request,'topic.html',context)

        else:
            template = loader.get_template('register.html')
            return HttpResponse(template.render({}, request))
    except Exception as e:
        pass


@csrf_exempt
def topic(request):
    try:
        if request.method == 'POST':
            vertor = request.POST.getlist('topic')
            weblog.online(str(request.session['user_id']),"register")
            weblog.online(str(request.session['user_id']),str(vertor))

            return HttpResponseRedirect("/webapp/")
        else:
            topics = ["电影", "体育", "技术", "杂志", "电影", "生活", "娱乐", "军事", "电影", "海外"]
            context = {"topics": topics, }
            template = loader.get_template('topic.html')
            return HttpResponse(template.render(context, request))
    except Exception as e:
        pass

def flush(request):

    num = random.randint(0,5000)
    #news_id=['934ecb6668a13f583ff555c28160af05','fbb865662f17bb172eff1dfdd836e7bd','e2c7376bc2e923855d039dbd5f10ee2b','e866c4af86d5467075f407ad6f424cfe','c1a1d8bb130b31c02c57caf73b6584dc',
     #        '49202abe03b92860a695b2cc6cd6babe'
      #       ]
    #result = db.getcommentnews(news_id)
    """
    返回推荐算法推荐的新闻ID列表，显示给用户
    """
    result = db.getcommentnews2(num)
    newslist = dumps(result)
    username=request.session["user"]
    context = {"news_list":loads(newslist),"user":username,}
    ids_log(str(request.session['user_id']),newslist)
    return render(request,"index.html",context)

def ids_log(useid,result):
    ids = []
    for item in loads(result):
        ids.append(item["id"])
        #print item["id"]
    weblog.log(useid, str(ids))

def logout(request):
    weblog.online(str(request.session["user_id"]),"logout")
    del request.session["user"]
    del request.session["user_id"]
    return HttpResponseRedirect("/webapp/login/")