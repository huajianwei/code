__author__ = 'huajw'
#coding=utf-8
#变量也可以指向函数，即可以给函数些一个别名
print  abs(-10)
print  abs

a = abs
print a(-16)
print a
print abs


#高阶函数就是使用一个函数来接受另一个函数。
print "高阶函数"
def addd(x,y):
    return x + y

print addd(-20,-23)

#map map()函数接收两个参数，一个是函数，一个是序列，
#也可以是两个序列,不过序列的len必须一样.
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
print "map"

a = [x for x in range(1,10)]
print a
b = [x for x in range(-10,-1)]
print b

#c = map(abs,b)
c = map(lambda x, y : x * y , a, b)

print "c = " ,c

#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

xulieqiuhe = reduce(lambda x, y : x+y, [x  for x in range(1,10) ])
print xulieqiuhe


#将一个字符串"123456" 转化为数字 123456

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

print str2int("2344552")


a =  ['adam', 'LISA', 'barT']

b = "jake"
print  b.capitalize()


c = map(lambda x : x+1 , [x for x in range(1,10)] )
print c


def daxie(s):
    return s.capitalize()
print "b=", daxie(b)


b = map(daxie , [s for s in a])
print b

#filter
# 是为了筛选一个序列..
#
a = filter(lambda x: x%2==1,[x for x in range(1,19)])
print a

print '*'*30
def issushu(x):
    for y in range(2,int(x**0.5+1)):
        if x%y == 0:
#            print x
            return x

#for x in range(2,100):
#    issushu(x)


b = filter(issushu , [x for x in range(1,100)]  )
print b

