__author__ = 'huajw'
#coding=utf-8

import string

#所有的序列标准操作对字符串都适用，但是不能赋值。
a = 'www.baidu.com'
print a[0:3]
print a[-3:]
#a[-3:]  = "org"
print a
# 格式化输出

print "Hello,%s,do you %s enough?" %("big","clever")

#字符串常量
print  string.digits
print  string.letters
print  string.lowercase
print  string.lowercase
print  string.printable
print  string.punctuation
print  string.uppercase

#其他的字符串方法
a = string.lowercase

if a.find("ef"):
    print a.find("ef")
    print "find"


if a.find("cb"):
    print a.find("cb")
else:
    print "not find"
print a
#join
#是split的逆方法。只能连接字符串，不能连接数字。
sep = "+"
b = sep.join(a)
print b

#lower 返回字符串的小写字符 title 返回标题样式
a = 'www.baidu.com'
print  a.title()

b = a.title().lower()
print b


# replace p返回某字符串的所有匹配项均被替换之后的字符串 原来的字符串不变。

print  a.replace('com','org')

#split 分割字符串

print  b.split('.')

#strip 该方法返回去除两侧是空格的字符串







print '\n'*3
print  "%s"  % __file__

