__author__ = 'huajw'
#coding=utf-8

# 高级的特性

l = []
for x in range(100):
    if x%2 == 0:
        l.append(x)


#切片 取前三个元素
#one

a = [l[0], l[1], l[2]]
b = l[0:3]
c = l[:24:2]
d  = l[-5::2]
print a
print b
print c
print d

#dict迭代key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key ,d[key]
#dict 迭代value
for value in d.itervalues():
    print value
#dict 迭代key 和value。
for k, v in d.iteritems():
    print k,v

#判断一个对象是否是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(d, Iterable)

# 键值对的循环
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print (x,y)

