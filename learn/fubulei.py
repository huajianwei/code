__author__ = 'huajianwei2013'
#coding=utf-8
fibs=[1,1]
for i in range(4):
    fibs.append(fibs[-1]+fibs[-2])
print fibs
