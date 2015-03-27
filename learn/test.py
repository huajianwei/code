__author__ = 'huajw'
# coding=utf-8
import os
#返回目前的目录
print  os.path.abspath(".")
#新建一个目录 建议使用join函数拼接目录.拆分路径的时候用os.path.split()
#os.mkdir(os.path.join(os.path.abspath("."),"jincheng"))
#raw_input("ok")
#os.rmdir(os.path.join(os.path.abspath("."),"new"))
print os.path.split(os.path.abspath("."))[0]
print os.path.split(os.path.abspath("."))[1]
#列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') ]
