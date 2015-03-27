__author__ = 'huajw'
#coding = utf-8

import codecs

#文件读取尽量使用with.

with open('G:\my\code\learn\est.txt', 'w') as f:
    f.write("hello,world1")



with open('G:\my\code\learn\est.txt', "r") as f:
    print  f.read()
