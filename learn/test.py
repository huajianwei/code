__author__ = 'huajw'
# coding=utf-8
"""
目前尚不能使用
"""
from bs4 import BeautifulSoup
import os, sys, urllib2
# 创建文件夹，昨天刚学会
path = os.getcwd()  # 获取此脚本所在目录
new_path = os.path.join(path, u'tupian')
if not os.path.isdir(new_path):
    os.mkdir(new_path)


def page_loop(page=0):

    url = "http://image.baidu.com/" % page
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)
    my_girl = soup.find_all("img")
    # 加入结束检测，写的不好....
    if my_girl == []:
        print u'已经全部抓取完毕'
        sys.exit(0)
    print u'开始抓取'
    for girl in my_girl:
        link = girl.get('src')
        flink = "http://image.baidu.com/" + link

    print flink
    content2 = urllib2.urlopen(flink).read()
    with open(u'tupian' + '/' + flink[-11:], 'wb') as code:  #在OSC上现学的
        code.write(content2)
        page = int(page) + 1
        print u'开始抓取下一页'
    print 'the %s page' % page
    #page_loop(page)


if __name__ == 'main':
    print  'ok'
    page_loop()