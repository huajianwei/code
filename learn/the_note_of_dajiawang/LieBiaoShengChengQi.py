__author__ = 'Administrator'
#coding=utf-8

a = range(10)
print a


l=[]
for x in range(1,11):
	l.append(x*x)

print l

#使用列表生成式

l = [x*x for x in range(1,11)]
l = [x*x for x in range(1,11) if x % 2 == 0]
print l
ll = [m+n for m in 'abcd' for n in '1234']
print ll


# 列出当前目录下的所有文件和目录名
import os

print [d for d in os.listdir('.')]

# for循环其实可以同时使用两个甚至多个变量

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
	print k, '=', v


L = ['Hello', 'World', 'IBM', 'Apple']
ll = [s.lower() for s in L]
lll = [s.capitalize() for s in ll]
print ll
print lll



