__author__ = 'huajw'
#coding=utf-8
#init a dic
phonebook = {}
#print phonebook
phonebook = {"alice":13,"adam":26,"bill":27,"cell":13}
#print( phonebook)

#init a dic by dict function 通过映射来建立字典
name = ["jake","jack","alice","adam","bill"]
age = [12,2,4,56,0]
item = zip(name,age)
TheResult = dict(item)
print TheResult

#通过关键字来建立字典。
d = dict(name="jake",age=23)
print d

#字典的基本的操作
print len(d)
item["jake"]
