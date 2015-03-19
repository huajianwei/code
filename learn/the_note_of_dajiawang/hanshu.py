__author__ = 'huajw'
#coding=utf-8

#部分函数
#abs(x) 求绝对值
print abs(3.45)
print abs(-3)
print abs(-78798)

#cmp(x,y)
print cmp(1,3)

#int() 函数可以把其他数据类型转换为整数
#函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

#定义一个函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
#添加了一下类型检查
def my_abs_type_check(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-12)
print  my_abs(-678687)
print  my_abs(87)

#定义一个空函数
def KongHanShu():
    pass

#函数可以返回多个值 其实是多个值得tuple

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x,y

