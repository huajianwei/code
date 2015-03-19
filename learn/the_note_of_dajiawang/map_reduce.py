__author__ = 'huajw'
#coding=utf-8

#map 接受两个参数,前一个是函数,后一个是序列(元组,列表,等)
list_a = [x for x in range(1,21) if x%2 == 0]
print(list_a)

def ercifang(x):
    return x*x


result = map(ercifang,list_a)
print result

#or
#result = [x*x for x in range(1,21) if x%2 == 0]


#reduce 是将一个函数连续作用在一个序列上,例如

def jia(x,y):
    return x+y
def jiashi(x,y):
    return x*10 +y
def qiuji(x,y):
    return x*y
def prod(f,a=[]):
    return reduce(f,a)

re = prod(qiuji,list_a)
print "re=" ,re
b = reduce(jia,[x for x in range(101)])
c = reduce(jiashi,[x for x in range(10)])
print b
print c

print sum(result)

