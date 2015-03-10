__author__ = 'huajw'
#coding=utf-8
def digui(n):
    if n == 1:
        return 1
    else:
        return n + digui(n-1)

#递归 次数超过999次会报错。。在计算机中，
# 函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出

print digui(999)
#print digui(1000)
#尾递归的调用实现 http://code.activestate.com/recipes/474088-tail-call-optimization-decorator/