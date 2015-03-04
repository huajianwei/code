__author__ = 'huajw'
#coding=utf-8
#分片操作

n=0

tag = "nishi wo de xiao a xiao pingguo"
a = tag[9:16]
print a

#索引
print  tag[3]

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

#序列相加和相乘


tag5 = tag1 + tag2
print tag5 ,"tag5"

#序列相乘
print tag4*3

#成员资格检查

for x in range(1,21,1):
    if x in tag4:
        print x ,"in tag4"

#长度，最大值，最小值。


a = len(tag4)
print a
print type(a)

a = max(tag4)
b = min(tag4)
print a
print b

# 列表元素赋值
print tag4
tag4[0] = 21
print tag4

print tag4
tag4[0:1] = [21,32,23,34,45]
print tag4

print tag4
tag4[:-1] = [21,32,23,34,45]
print tag4

print tag4
tag4[-3:-1] = [21,32,23,314,45]
print tag4

#删除元素
del tag4[4]
print tag4

#列表的方法
#append
tag4.append(4)
tag4.append("4")
print tag4
#count
a = tag4.count(4)
print a

a=tag4
#extend和+的区别是a.extend(b) 中的a已经改变
print  a+tag5
print a
tag4.extend(tag5)
print tag4


#index 需要事先检查元素是否在列表中
print  tag4.index(4)

#insert   添加列表的元素
tag4.insert(4,88)

print tag4
#pop 移除最后一个元素并返回
a = tag4.pop()
print a
print tag4
# 移除指定的项
a = tag4.pop(0)
print a
print tag4

#reverse
tag4.reverse()
print tag4
tag4.reverse()
print tag4

#sort and sorted
tag6 = tag4[:]
print tag6
tag6.sort()
print tag6

#sorted 已经排好序
tag3.reverse()
tag7 = sorted(tag3)
print tag7
print tag3
print "*"*20
#cmp
cmp(21,20)
tag7.sort(cmp)
print tag7 ,"tag7 cmp"

#tuple 将序列转化为元组。

a = tuple(tag3)
print a
