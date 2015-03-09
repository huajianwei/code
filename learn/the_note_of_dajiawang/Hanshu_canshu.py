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

print calc(1,2,13)



