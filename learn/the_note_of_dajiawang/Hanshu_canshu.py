__author__ = 'huajw'
#coding=utf-8

def power(x):
    return x*x

print power(5)
print power(25)

#使用递归

def powern(x,n=1):
    if n == 0:
        return 1
    else:
        return x*powern(x,n-1)


print powern(3)
print powern(3,0)
print powern(3,1)
print powern(4,2)
print powern(4,4)

#使用while
def powern_while(x,n=1):
    s=1
    while n > 0:
        n -= 1
        s *= x
    return s

print powern_while(3)
print powern_while(3,0)
print powern_while(3,1)
print powern_while(3,2)
print powern_while(4,2)

#可变参数，参数是可以修改的
#sum = 1*1+2*2+3*3++++
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print "*"*20
print calc(1,2,4,7,9,20)

a=(1,2,3,4,5,6,7,8,9,10,12,13,11)

#list或tuple前面加一个*号,把list或tuple的元素变成可变参数传进去.
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自
# 动组装为一个tuple
#print calc(a)
print calc(*a)


print calc(11)

#关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw



person('Mike',18)
person('Bob', 35, city='Beijing')
person('Adam', 25, gender='M', job='Engineer')

#参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

print '*'*30
func(1, 2,)
func(1, 2, 3)
func(1, 2, 3, 'a')
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b','c', x=99)
func(1, 2,x=99)

