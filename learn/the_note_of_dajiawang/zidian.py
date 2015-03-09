__author__ = 'huajw'
#coding=utf-8
#init a dic
phonebook = {}
#print phonebook
phonebook = {"alice":13,"adam":26,"bill":27,"cell":13}
#print( phonebook)

#init a dic by dict function 通过映射来建立字典
name = ["jake","jack","alice","adam","bill"]
age = [12,2,4,56,0]
item = zip(name,age)
TheResult = dict(item)
print TheResult

#通过关键字来建立字典。dict 的key 是不可变对象，不能使用list作为key值
d = dict(name="jake",age=23)
print d

#字典的基本的操作
print len(d)
print d["name"]
print d["age"]

#新加一些key和value
d["heigh"]=178
print d

#更新原有key的value
d["heigh"] = 168
print d["heigh"]

#对于key的值不存在的情况，使用 in 会报错。
#可是使用key值的name来判断该key是否在字典中
#也可以使用dict提供的get方法来判断。推荐使用。
if "weight" in d:
    print d["weight"]
else:
    print "the key is not in dict"

d.get("weight")

a = d.get("weight","你要查找的key值不存在")
#print d.get("weight")
print a

#删除一个key值
d["weight"] = 34
print d
d.pop("weight")
print d
d["weight"] = 34

# set 和dict类似 是一组key的组合，没有value。
#初始化
s = set([1, 2, 3])
print s
#重复的元素在set中被过滤掉，，相当于是dict的key。

#添加元素
s.add(4)  #只可以添加一个值
print s

#删除元素

s.remove(3)
print s

#set类型可以做集合的交，& 并 |

