#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-25 下午5:02
# @Author  : ai-i-luru@interns.chuangxin.com
from django import template
import time
import re


register = template.Library()
@register.filter
def news_data(timestamp):
    timeStamp = float(timestamp)
    timeArray = time.localtime(timeStamp)
    timestyle = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return timestyle

@register.filter
def news_content(content):
    con = re.sub(r'<(.+?)>',"",content)
    con = con[0:150]
    return con+"......"

@register.filter
def nclick(count):
    click = int(count)
    return click