__author__ = 'huajw'
#coding=utf-8
#分片操作

tag = "nishi wo de xiao a xiao pingguo"
a = tag[9:16]
print a
#生成数组
tag1=[]
for i in xrange(1,21,1):
    tag1.append(i)
print tag1
#序列分片和步长
tag2 = tag1[0:16:2]
print  tag2

tag3 = tag1[::3]
print  tag3

#步长为负数

tag4 = tag1[::-3]
print  tag4




