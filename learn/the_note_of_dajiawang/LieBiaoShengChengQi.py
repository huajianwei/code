__author__ = 'huajw'
#coding=utf-8
# 列表生成器为了在循环的时候少占用内存空间
#要创建一个generator，有很多种方法。第一种方法很简单，
#只要把一个列表生成式的[]改成()，就创建了一个generator：

L = [x * x for x in range(10)]
print L


g = (x * x for x in range(10))


# 检查一个实例是否可以迭代。
import collections
print isinstance(g,collections.Iterable)

for n in g:
    print n


#使用yield的关键字进行运用生成一个生成器
#在执行过程中，遇到yield就中断，下次又继续执行
#
#
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for n in fib(6):
    print n


