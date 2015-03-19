__author__ = 'huajw'
#coding=utf-8

import sys
import copy



b = sys.path[:]

sys.path.append("G:\my\code")

a = sys.path[:]

print [x for x in a if x not in b]
print a
print b

