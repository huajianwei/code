__author__ = 'huajw'
#coding=utf-8

#利用系统自带的函数进行编程
print  sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)

#匿名函数
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])