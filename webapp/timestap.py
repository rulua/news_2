#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-22 上午10:03
# @Author  : ai-i-luru@interns.chuangxin.com

from bson.json_util import dumps,loads
import helper as db
import time
from time import gmtime, strftime

#print time.asctime()
pubDate = db.transtime()
result = dumps(pubDate)

for item in loads(result):
    try:
    #print item["pubDate"]
        n =""
        pubtime = item["pubDate"].strip()
        if "+0000" in pubtime:
            n = time.mktime(time.strptime(pubtime, '%a, %d %b %Y %H:%M:%S +0000'))
        elif "+0800" in pubtime:
            n = time.mktime(time.strptime(pubtime, '%a, %d %b %Y %H:%M:%S +0800'))
        elif "\u5e74".decode("utf-8") in pubtime:
            n = time.mktime(time.strptime(pubtime, '%Y年%m月%d日 %H:%M:%S'))
        elif "/" in pubtime:
            n = time.mktime(time.strptime(pubtime, '%Y/%m/%d %H:%M:%S'))
        elif "-" in pubtime:
            pubtime= pubtime+":02"
            n =time.mktime(time.strptime(pubtime, '%Y-%m-%d %H:%M:%S'))
            db.updatetime(pubtime,str(int(n)))
    except Exception as e:
        print(e)
#print result