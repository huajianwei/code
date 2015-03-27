__author__ = 'huajw'
# coding=utf-8
import os
print os.name

with open("G:\my\code\learn\environment.txt","w") as f:

    for key in os.environ:
        print key ," =" ,os.environ[key]
        f.write(key)
        f.write("=")
        f.write(os.environ[key])
        f.write("\n")


