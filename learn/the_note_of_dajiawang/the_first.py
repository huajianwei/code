__author__ = 'huajw'
#coding=utf-8
#jiajianchengchu

def  jia(x,y):
    return x+y
def  jian(x,y):
    return x-y
def  cheng(x,y):
    return x-y
def  chu(x,y):
    return x/y
def  jiecheng(x,y):
    return x**y
def  qiuyu(x,y):
    return x%y

def  main():
    print "哈哈，傻了吧"

a = 30
b = 10

if __name__ == "__main__":
    main()
    result = jia(a,b)
    print result
    result = jian(a,b)
    print result
    result = cheng(a,b)
    print result
    result = chu(a,b)
    print result
    result = jiecheng(a,b)
    print result
    result = qiuyu(a,b)
    print result


#got the user's input
#num = input("please input a number\n")
#print "the number you enter is ", num
#word = raw_input("please input a world\n")
#print "the word you input is " , word

import math
a = math.floor(34.7)
print
print a