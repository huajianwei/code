__author__ = 'huajw'
#coding=utf-8

a = [x for x in range(1,10)]
print type(a[0])
b = [x for x in range(-10,-1)]
print type(b[0])

#c = map(abs,b)
c = map(lambda x, y : x * y , a, b)

print "c = " ,c

print map(lambda x, y: x + y, [1, 3, 5, 7, 9], [-2, 4, 6, 8, 10])


